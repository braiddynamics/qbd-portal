import numpy as np
import matplotlib.pyplot as plt

def calculate_kagome_bands(k_path, t=1.0, lambda_soc=0.0):
    """
    Solves the Tight-Binding Hamiltonian for a 2D Kagome Lattice.
    
    t: Kinetic hopping energy (Computational friction of standard graph)
    lambda_soc: The "Hardware T-Gate" (Complex topological phase shift)
    """
    energies = []
    
    for kx, ky in k_path:
        # The fundamental geometric vectors of the Trivalent 2D lattice
        k1 = kx
        k2 = 0.5 * kx + (np.sqrt(3.0) / 2.0) * ky
        k3 = -0.5 * kx + (np.sqrt(3.0) / 2.0) * ky
        
        # 1. The Standard Graph Routing (Nearest Neighbor)
        # Represents standard hopping between the 3 nodes of the Kagome unit cell
        h12 = -t * (1.0 + np.exp(-1j * k1))
        h13 = -t * (1.0 + np.exp(-1j * k2))
        h23 = -t * (1.0 + np.exp(-1j * k3))
        
        H = np.array([
            [0,   h12, h13],
            [np.conj(h12), 0,   h23],
            [np.conj(h13), np.conj(h23), 0]
        ])
        
        # 2. The QBD Topological Phase (Next-Nearest Neighbor "T-Gate")
        # Breaks time-reversal symmetry, turning the lattice into a topological insulator
        if lambda_soc > 0.0:
            soc12 = 1j * lambda_soc * (np.exp(-1j * k1) - 1.0)
            soc13 = -1j * lambda_soc * (np.exp(-1j * k2) - 1.0)
            soc23 = 1j * lambda_soc * (np.exp(-1j * k3) - 1.0)
            
            H_SOC = np.array([
                [0,   soc12, soc13],
                [np.conj(soc12), 0,   soc23],
                [np.conj(soc13), np.conj(soc23), 0]
            ])
            H = H + H_SOC

        # Calculate the allowed energy levels for this momentum vector
        eigenvalues = np.linalg.eigvalsh(H)
        energies.append(np.sort(eigenvalues))
        
    return np.array(energies)

def run_smoke_test():
    print("=================================================================")
    print(" QBD SMOKE TEST: KAGOME LATTICE BAND STRUCTURE")
    print("=================================================================")
    
    # 1. Define the path through momentum space (The Brillouin Zone)
    # Gamma (Center) -> K (Corner) -> M (Edge) -> Gamma
    points = 100
    Gamma = np.array([0, 0])
    K = np.array([4.0 * np.pi / 3.0, 0])
    M = np.array([np.pi, np.pi / np.sqrt(3.0)])
    
    path_G_K = np.linspace(Gamma, K, points)
    path_K_M = np.linspace(K, M, points)
    path_M_G = np.linspace(M, Gamma, points)
    
    full_path = np.vstack((path_G_K, path_K_M, path_M_G))
    x_axis = np.arange(len(full_path))
    
    # 2. Simulate Standard Vacuum (No Topological Doping)
    print("Simulating standard trivalent graph...")
    bands_standard = calculate_kagome_bands(full_path, t=1.0, lambda_soc=0.0)
    
    # 3. Simulate Doped Vacuum (With "Hardware T-Gate" Phase)
    print("Simulating topological graph (Spin-Orbit Phase enabled)...")
    bands_topological = calculate_kagome_bands(full_path, t=1.0, lambda_soc=0.2)

    # 4. Plotting the Results
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Standard
    for i in range(3):
        ax1.plot(x_axis, bands_standard[:, i], color='cyan', lw=2)
    ax1.set_title("Standard Trivalent Graph\n(Notice the completely Flat Band at E=2)")
    ax1.set_ylabel("Energy")
    ax1.set_xticks([0, points, 2*points, 3*points-1])
    ax1.set_xticklabels(['$\Gamma$', 'K', 'M', '$\Gamma$'])
    ax1.grid(alpha=0.2)
    
    # Plot 2: Topological
    for i in range(3):
        ax2.plot(x_axis, bands_topological[:, i], color='magenta', lw=2)
    ax2.set_title("Topological Graph (QBD Phase Shift)\n(Gaps open -> Protected Condensate)")
    ax2.set_xticks([0, points, 2*points, 3*points-1])
    ax2.set_xticklabels(['$\Gamma$', 'K', 'M', '$\Gamma$'])
    ax2.grid(alpha=0.2)
    
    plt.suptitle("Emergence of Macroscopic Topological Condensates in 2D Lattices")
    plt.tight_layout()
    plt.savefig('qbd_flatband_smoketest.png')
    print("-> Simulation complete. Image saved as 'qbd_flatband_smoketest.png'.")
    plt.show()

if __name__ == "__main__":
    run_smoke_test()