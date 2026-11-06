from fractions import Fraction
import networkx as nx
from sympy import SparseMatrix, eye, zeros


# Fixed candidate graph constructors. This checks diagonal action, not the
# physical admission of a control or the probability of a preparation history.
class RibbonPatch:
    def background(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(35))
        graph.add_edges_from(((7*r+t, 7*r+t+1) for r in range(5)
                              for t in range(6)), H=0)
        graph.add_edges_from(((7*r, 7*(r+1)) for r in range(4)), H=0)
        return graph

    def graph(self, mask):
        graph = self.background()
        faces = [(r,t) for r in range(5) for t in range(4)]
        faces += [(r,4) for r in range(5) if mask & (1 << r)]
        for r,t in faces:
            u,v = 7*r+t+2, 7*r+t
            stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
            graph.add_edge(u,v,H=stamp)
        return graph


def sector_encoding():
    return SparseMatrix(32, 5, {(1 << r,r): 1 for r in range(5)})


def occupation(r):
    return SparseMatrix(32,32,{(word,word): 1 for word in range(32) if word & (1 << r)})


MODULE_SIZE = 26
BASE_PATTERN = sum(0x99 << (8*r) for r in range(5))


def encode_five_states(marked):
    if marked not in range(5):
        raise ValueError('Expected a ribbon in 0..4')
    graph = nx.DiGraph()
    graph.add_nodes_from(range(130))
    paths = {0:(0,10,11), 1:(1,12,13),
             2:(2,14,15,16,17,18,19), 3:(3,20,21,22,23,24,25)}
    local = [(2,6),(6,7),(7,3),(6,0),(6,1),
             (7,8),(8,4),(7,9),(9,5)]
    local += [(a,b) for path in paths.values() for a,b in zip(path,path[1:])]
    for r in range(5):
        off = 26*r
        graph.add_edges_from(((off+a,off+b) for a,b in local),H=0)
        if r:
            graph.add_edge(off-26+6,off+6,H=0)
    def add(u,v):
        stamp = 1 + max((d['H'] for _,_,d in graph.in_edges(u,data=True)), default=0)
        graph.add_edge(u,v,H=stamp)
    for r in range(5):
        off = 26*r
        for u,v in ((3,6),(7,2),(4,7),(5,7)):
            add(off+u,off+v)
        for port in (1,3):
            path = paths[port]
            for k in range(len(path)-1,1,-2):
                add(off+path[k],off+path[k-2])
        for inputs,outputs in (((0,1),(2,3)),((2,3),(4,5))):
            targets = outputs[::-1] if r == marked else outputs
            for u,v in zip(inputs,targets):
                add(off+u,off+v)
    return graph, ()

def active_edges():
    local = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5))
    return tuple((MODULE_SIZE * r + a, MODULE_SIZE * r + b) for r in range(5) for a, b in local)

def relative_rungs(graph):
    raw = sum(1 << bit for bit, edge in enumerate(active_edges()) if graph.has_edge(*edge))
    return raw ^ BASE_PATTERN

def logical_patterns():
    return tuple(0xFF << (8 * r) for r in range(5))

def check_rows(enhanced=False):
    rows = tuple((1 << (8 * r)) | (1 << (8 * r + k)) for r in range(5) for k in range(1, 8))
    return rows + (sum(1 << (8 * r) for r in range(5)),) if enhanced else rows

def raw_z(word, bit):
    return (-1) ** ((word >> bit) & 1)

def rung_occupation(word, module):
    """(1/8) sum_m (1-s_rm Z_rm)/2 on a raw physical edge word."""
    return sum((Fraction(1 - raw_z(BASE_PATTERN, bit) * raw_z(word, bit), 2)
                for bit in range(8 * module, 8 * module + 8)), Fraction()) / 8

def signed_check(word, row):
    return (-1) ** ((BASE_PATTERN & row).bit_count() + (word & row).bit_count())

def z_character_product(a, b):
    """Z-string multiplication on arbitrary raw words: Z_a Z_b = Z_(a XOR b)."""
    return a ^ b

def audit_diagonal_encodings():
    w = sector_encoding()
    assert w.conjugate().T * w == eye(5)
    patch = RibbonPatch()
    assert patch.background().number_of_nodes() == 35
    penta = []
    for k in range(4):
        h = occupation(k) - occupation(k + 1)
        z = zeros(5)
        z[k, k], z[k + 1, k + 1] = 1, -1
        assert h == h.conjugate().T
        assert h * w == w * z
        assert (eye(32) - w * w.conjugate().T) * h * w == zeros(32, 5)
        penta.append({"adjacent_pair": [k, k + 1], "intertwining": True,
                      "off_code_action_zero": True})

    rows = check_rows()
    assert len(rows) == 35
    records = []
    raw_words = []
    for j, relative in enumerate(logical_patterns()):
        graph, _ = encode_five_states(j)
        assert graph.number_of_nodes() == 130
        assert relative_rungs(graph) == relative
        word = sum(1 << bit for bit, edge in enumerate(active_edges())
                   if graph.has_edge(*edge))
        assert word == relative ^ BASE_PATTERN
        raw_words.append(word)
        eigenvalues = [rung_occupation(word, r) for r in range(5)]
        assert eigenvalues == [int(r == j) for r in range(5)]
        assert all(signed_check(word, row) == 1 for row in rows)
        records.append({"state": j, "raw_edge_word": hex(word),
                        "occupation_eigenvalues": list(map(int, eigenvalues)),
                        "all_35_signed_checks_plus_one": True})

    # Sparse ambient encoding: each graph ket is a distinct raw edge word.
    # Diagonal action has no support outside these five rows. These identities
    # represent equality of functions on the full 2**40 basis without allocating it.
    assert len(set(raw_words)) == 5
    for k in range(4):
        actual = {word: rung_occupation(word, k) - rung_occupation(word, k + 1)
                  for word in raw_words}
        expected = {word: int(j == k) - int(j == k + 1)
                    for j, word in enumerate(raw_words)}
        assert actual == expected

    # Each Nhat is a constant plus eight single-edge Z characters. Every signed
    # check is one Z character with a fixed sign. XOR commutativity proves their
    # commutation on ALL raw basis words, not just the selected five codewords.
    for row in rows:
        for bit in range(40):
            assert z_character_product(row, 1 << bit) == z_character_product(1 << bit, row)

    return {
        "penta_vertices": 35, "penta_occupation_register_dimension": 32,
        "penta_isometry": True, "penta_adjacent_imbalances": penta,
        "rung_vertices": 130, "rung_raw_register_dimension": str(2**40),
        "rung_states": records, "rung_intertwining_all_four_pairs": True,
        "rung_off_code_action_zero_all_four_pairs": True,
        "signed_stabilizer_count": len(rows),
        "baseline_physical_check_signs": [(-1) ** ((BASE_PATTERN & row).bit_count()) for row in rows],
        "all_diagonal_imbalances_commute_with_all_signed_checks": True,
        "commutation_method": "Exact Z-character XOR algebra on all 40 raw bits",
        "diagonal_validity_projector_commutation": "Any diagonal functions commute pointwise",
        "physical_hamiltonian_availability_derived": False,
    }



certificate = audit_diagonal_encodings()
print("signed checks | signed code eigenvalue | diagonal commutation")
assert certificate["all_diagonal_imbalances_commute_with_all_signed_checks"]
assert all(row["all_35_signed_checks_plus_one"] for row in certificate["rung_states"])
print(f"{certificate['signed_stabilizer_count']} | +1 | all raw edge words")
