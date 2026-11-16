import pandas as pd

def verify_full_mass_hierarchy():
    print("--- §7.4.6.1 Generational Mass Hierarchy ---")
    
    # 1. Constants
    # Mass Constant (kappa_m) anchored to Electron
    # m_e = 0.511 MeV. Net Complexity N_e = 3. 
    KAPPA_M = 0.511 / 3.0 
    
    # Standard Model Reference Masses (in MeV; 2 GeV MS-bar values for light quarks)
    sm_masses = {
        "Electron": 0.511, "Muon": 105.66, "Tau": 1776.8,
        "Down": 4.7, "Strange": 95.0, "Bottom": 4180.0,
        "Up": 2.2, "Charm": 1275.0, "Top": 172900.0
    }

    # 2. Particle Topology Class Definitions
    def calc_lepton(w): 
        return 3 * (w**2)   # (-w, -w, -w) -> no color sharing
        
    def calc_d_type(w): 
        return w**2         # (-w, 0, 0) -> no sharing
        
    def calc_u_type(w): 
        return 2*(w**2) - w # (w, w, 0) -> w parallel sharing instances

    # 3. Assigned Benchmark Integer Writhes (First gen w=1; higher gens fixed to match spectrum)
    particles = [
        # First Generation (unit-writhe baseline inputs)
        {"name": "Electron", "type": "Lepton", "w": 1, "calc": calc_lepton},
        {"name": "Down", "type": "D-Type", "w": 1, "calc": calc_d_type},
        {"name": "Up", "type": "U-Type", "w": 1, "calc": calc_u_type},
        # Second Generation (assigned benchmark writhes)
        {"name": "Muon", "type": "Lepton", "w": 14, "calc": calc_lepton},
        {"name": "Strange", "type": "D-Type", "w": 24, "calc": calc_d_type},
        {"name": "Charm", "type": "U-Type", "w": 62, "calc": calc_u_type},
        # Third Generation (assigned benchmark writhes)
        {"name": "Tau", "type": "Lepton", "w": 59, "calc": calc_lepton},
        {"name": "Bottom", "type": "D-Type", "w": 157, "calc": calc_d_type},
        {"name": "Top", "type": "U-Type", "w": 712, "calc": calc_u_type}
    ]

    results = []
    for p in particles:
        w = p["w"]
        n_net = p["calc"](w)
        mass_mev = KAPPA_M * n_net
        empirical = sm_masses[p["name"]]
        
        # Calculate Delta (%)
        delta_pct = abs(mass_mev - empirical) / empirical * 100
        
        if p["type"] == "Lepton": config = f"(-{w}, -{w}, -{w})"
        elif p["type"] == "D-Type": config = f"(-{w}, 0, 0)"
        else: config = f"({w}, {w}, 0)"
        
        results.append({
            "Particle": p["name"],
            "Writhe Config": config,
            "Net N3": n_net,
            "Topo Mass (MeV)": f"{mass_mev:.3f}",
            "Observed (MeV)": f"{empirical:.3f}",
            "Δ (%)": f"{delta_pct:.2f}"
        })

    # 4. Output Table
    df = pd.DataFrame(results)
    print(df.to_string(index=False))

if __name__ == "__main__":
    verify_full_mass_hierarchy()
