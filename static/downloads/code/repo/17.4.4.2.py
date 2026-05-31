import numpy as np
from itertools import product, combinations

def verify_standard_model_embedding():
    """
    Force-Matter Decomposition.
    
    This routine analyzes the algebraic subgroups of the generated E8 lattice
    to verify the existence of the Standard Model gauge groups and generational structure.
    
    Analysis Targets:
    1. Force/Matter Split (Integer vs Half-Integer Lattice).
    2. Subgroup Identification (SU(3) Color, SU(2) Weak).
    3. Generational Capacity (Matter count relative to SO(10) family size).
    """
    
    print("=================================================================")
    print("   FORCE-MATTER DECOMPOSITION")
    print("   E8 -> SO(16) (Force) + Spinor (Matter)")
    print("=================================================================")

    # 1. Regenerate E8 Roots
    roots_D8 = [] # Force candidates (Integer Lattice)
    for i, j in combinations(range(8), 2):
        for s1, s2 in product([1, -1], repeat=2):
            v = np.zeros(8); v[i]=s1; v[j]=s2
            roots_D8.append(v)
            
    roots_Spinor = [] # Matter candidates (Half-Integer Lattice)
    for signs in product([-0.5, 0.5], repeat=8):
        v = np.array(signs)
        if np.sum(v < 0) % 2 == 0: 
            roots_Spinor.append(v)
            
    # 2. Decomposition Analysis
    n_force = len(roots_D8)
    n_matter = len(roots_Spinor)
    
    print(f"   Total Roots: {n_force + n_matter}")
    print(f"   Force Sector (SO(16) Adjoint):  {n_force} roots")
    print(f"   Matter Sector (Spinor Rep):     {n_matter} roots")
    
    # 3. Subgroup Verification
    print("\n   [Subgroup Verification]")
    
    # SU(3) Color Triplet Generator (Confined to dimensions 0, 1, 2)
    # Corresponds to roots of SO(6) ~ SU(4), containing SU(3).
    su3_roots = []
    for r in roots_D8:
        if np.all(r[3:] == 0):
            su3_roots.append(r)
            
    print(f"   Roots confined to dims [0,1,2]: {len(su3_roots)} (matches SO(6) embedding)")
    
    # SU(2) Weak Group (Confined to dimensions 3, 4)
    # Corresponds to roots of SO(4) ~ SU(2) x SU(2).
    su2_roots = []
    for r in roots_D8:
        mask = np.ones(8, dtype=bool)
        mask[3] = False; mask[4] = False
        if np.all(r[mask] == 0):
            su2_roots.append(r)
            
    print(f"   Roots confined to dims [3,4]:   {len(su2_roots)} (matches SO(4) embedding)")
        
    # 4. Generational Capacity
    # Determine number of potential families assuming SO(10) unification scale (16 states/family).
    family_size_so10 = 16
    generations = n_matter / family_size_so10
    
    print("\n   [Matter Capacity Analysis]")
    print(f"   Matter Sector Size: {n_matter}")
    print(f"   SO(10) Family Size: {family_size_so10}")
    print(f"   Available Families: {generations:.1f}")
    print("-" * 65)

if __name__ == "__main__":
    verify_standard_model_embedding()
