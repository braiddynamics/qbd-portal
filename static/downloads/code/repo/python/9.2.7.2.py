# §9.2.7.2 — Diagonal action and intertwining on occupation and rung encodings
# Checks: N_r |G_j> = delta_{rj} |G_j> and Z_hat_k W = W Z_k on both encodings.
from fractions import Fraction
import networkx as nx
from sympy import SparseMatrix, zeros


class RibbonPatch:
    def background(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(35))
        graph.add_edges_from(
            ((7 * r + t, 7 * r + t + 1) for r in range(5) for t in range(6)), H=0
        )
        graph.add_edges_from(((7 * r, 7 * (r + 1)) for r in range(4)), H=0)
        return graph

    def graph(self, mask):
        graph = self.background()
        faces = [(r, t) for r in range(5) for t in range(4)]
        faces += [(r, 4) for r in range(5) if mask & (1 << r)]
        for r, t in faces:
            u, v = 7 * r + t + 2, 7 * r + t
            stamp = 1 + max((d["H"] for _, _, d in graph.in_edges(u, data=True)), default=0)
            graph.add_edge(u, v, H=stamp)
        return graph


def encode_five_states(marked):
    graph = nx.DiGraph()
    graph.add_nodes_from(range(130))
    paths = {
        0: (0, 10, 11),
        1: (1, 12, 13),
        2: (2, 14, 15, 16, 17, 18, 19),
        3: (3, 20, 21, 22, 23, 24, 25),
    }
    local = [(2, 6), (6, 7), (7, 3), (6, 0), (6, 1), (7, 8), (8, 4), (7, 9), (9, 5)]
    local += [(a, b) for path in paths.values() for a, b in zip(path, path[1:])]
    for r in range(5):
        off = 26 * r
        graph.add_edges_from(((off + a, off + b) for a, b in local), H=0)
        if r:
            graph.add_edge(off - 26 + 6, off + 6, H=0)

    def add(u, v):
        stamp = 1 + max((d["H"] for _, _, d in graph.in_edges(u, data=True)), default=0)
        graph.add_edge(u, v, H=stamp)

    for r in range(5):
        off = 26 * r
        for u, v in ((3, 6), (7, 2), (4, 7), (5, 7)):
            add(off + u, off + v)
        for port in (1, 3):
            path = paths[port]
            for k in range(len(path) - 1, 1, -2):
                add(off + path[k], off + path[k - 2])
        for inputs, outputs in (((0, 1), (2, 3)), ((2, 3), (4, 5))):
            targets = outputs[::-1] if r == marked else outputs
            for u, v in zip(inputs, targets):
                add(off + u, off + v)
    return graph


BASE_PATTERN = sum(0x99 << (8 * r) for r in range(5))
ACTIVE_EDGES = tuple(
    (26 * r + a, 26 * r + b)
    for r in range(5)
    for a, b in ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 5))
)


def rung_occupation(word, module):
    return sum(
        (
            Fraction(1 - ((-1) ** ((BASE_PATTERN >> bit) & 1)) * ((-1) ** ((word >> bit) & 1)), 2)
            for bit in range(8 * module, 8 * module + 8)
        ),
        Fraction(),
    ) / 8


patch = RibbonPatch()
w_occ = SparseMatrix(32, 5, {(1 << r, r): 1 for r in range(5)})
for j in range(5):
    g_occ = patch.graph(1 << j)
    assert g_occ.number_of_nodes() == 35
    occ_vec = [int(g_occ.has_edge(7 * r + 6, 7 * r + 4)) for r in range(5)]
    assert occ_vec == [int(r == j) for r in range(5)]

for k in range(4):
    nk = SparseMatrix(32, 32, {(w, w): 1 for w in range(32) if w & (1 << k)})
    nk1 = SparseMatrix(32, 32, {(w, w): 1 for w in range(32) if w & (1 << (k + 1))})
    z_mat = zeros(5)
    z_mat[k, k], z_mat[k + 1, k + 1] = 1, -1
    assert (nk - nk1) * w_occ == w_occ * z_mat

rung_words = []
for j in range(5):
    g_rung = encode_five_states(j)
    assert g_rung.number_of_nodes() == 130
    word = sum(1 << bit for bit, edge in enumerate(ACTIVE_EDGES) if g_rung.has_edge(*edge))
    assert (word ^ BASE_PATTERN) == (0xFF << (8 * j))
    rung_words.append(word)
    assert [rung_occupation(word, r) for r in range(5)] == [int(r == j) for r in range(5)]

for k in range(4):
    assert [rung_occupation(w, k) - rung_occupation(w, k + 1) for w in rung_words] == [
        int(j == k) - int(j == k + 1) for j in range(5)
    ]

print("encoding   | vertices | selected states | intertwining pairs")
print("occupation | 35       | 5               | 4")
print("rung       | 130      | 5               | 4")
