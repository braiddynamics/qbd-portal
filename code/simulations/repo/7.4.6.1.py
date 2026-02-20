import pandas as pd
import numpy as np

def verify_mass_hierarchy():
    print("--- QBD Mass Hierarchy Verification ---")
    
    # 1. Constants
    # Mass Constant (kappa_m) anchored to Electron
    # m_e = 0.511 MeV. Net Complexity N_e = 3. 
    # kappa_m = 0.511 / 3 = 0.17033... MeV
    KAPPA_M = 0.511 / 3.0 
    K_SHARE = 1

    # 2. Particle Topology Data
    # Defined by Writhe Configuration (w1, w2, w3) based on Lemmas 7.3.5 & 7.3.6
    # Sharing is derived from parallel ribbon interactions (Lemma 7.4.5)
    particles = [
        {
            "name": "Neutrino (v_e)", 
            "writhe": (0, 0, 0),
            "sharing": 0, # Trivial topology
            "type": "Lepton" 
        },
        {
            "name": "Electron (e-)", 
            "writhe": (-1, -1, -1),
            "sharing": 0, # Singlet: Internal symmetry prevents color-binding efficiency
            "type": "Lepton"
        },
        {
            "name": "Down Quark (d)", 
            "writhe": (-1, 0, 0),
            "sharing": 0, # No parallel ribbons to share
            "type": "Quark"
        },
        {
            "name": "Up Quark (u)", 
            "writhe": (1, 1, 0),
            "sharing": 1, # Two parallel ribbons share 1 geometric quantum
            "type": "Quark"
        },
        {
            "name": "Strange (s)", 
            "writhe": (-1, -1, 1),
            "sharing": 0, # Anti-parallel structure prevents efficient sharing
            "type": "Quark"
        },
        {
            "name": "Top Quark (t)", 
            "writhe": (2, 2, 0), # Higher torsion generation
            "sharing": 2, # High tension parallel sharing
            "type": "Quark"
        }
    ]

    results = []

    for p in particles:
        w = p["writhe"]
        
        # 3. Calculate Isolated Complexity (Sum of Squares for Torsion)
        # Per Lemma 6.3.5: C_T ~ w^2
        n_iso = sum([val**2 for val in w])
        
        # 4. Apply Geometric Sharing
        sharing_reduction = K_SHARE * p["sharing"]
        
        # 5. Net Complexity
        n_net = n_iso - sharing_reduction
        
        # 6. Predicted Mass
        mass_mev = KAPPA_M * n_net
        
        results.append({
            "Particle": p["name"],
            "Writhe Config": str(w),
            "N_iso (Sum w^2)": n_iso,
            "Sharing Redux": sharing_reduction,
            "Net N3": n_net,
            "Mass (MeV)": round(mass_mev, 3)
        })

    # 7. Output Table
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    
    # 8. Verify Isospin Degeneracy
    m_u = df.loc[df['Particle'] == 'Up Quark (u)', 'Mass (MeV)'].values[0]
    m_d = df.loc[df['Particle'] == 'Down Quark (d)', 'Mass (MeV)'].values[0]
    
    print("\n--- Isospin Check ---")
    print(f"Mass Up:   {m_u} MeV")
    print(f"Mass Down: {m_d} MeV")
    
    if abs(m_u - m_d) < 1e-5:
        print("RESULT: Perfect zeroth-order degeneracy verified.")
        print("Note: Observed mass splitting (d > u) attributed to QED self-energy (Q_d^2 vs Q_u^2).")
    else:
        print("RESULT: Degeneracy failed.")

if __name__ == "__main__":
    verify_mass_hierarchy()