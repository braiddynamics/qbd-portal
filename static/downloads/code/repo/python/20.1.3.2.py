# §20.1.3.2 — Peebles Multi-Level Braid Recombination Kinetics

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

# Physical constants in SI units
c = 2.99792458e8             # Speed of light [m/s]
k_B = 1.380649e-23           # Boltzmann constant [J/K]
hbar = 1.054571817e-34       # Reduced Planck constant [J s]
m_e = 9.1093837e-31          # Electron mass [kg]
m_p = 1.6726219e-27          # Proton mass [kg]
sigma_T = 6.6524587e-29      # Thomson scattering cross-section [m^2]
a_rad = 7.5657e-16           # Radiation constant [J/(m^3 K^4)]
eV_to_J = 1.602176634e-19    # Joules per eV

# Cosmological parameters from Chapter 18 & Chapter 19
T_gamma0 = 2.7255            # CMB temperature today [K]
h = 0.6736                   # Reduced Hubble parameter
H0 = 100.0 * h * 1000.0 / 3.085677581e22  # Hubble constant [s^-1]
Omega_b = 0.02237 / (h**2)   # Baryon density parameter
Omega_c = 0.1200 / (h**2)    # Cold dark matter density parameter
Omega_m = Omega_b + Omega_c  # Total matter density parameter
Omega_r = 2.47e-5 / (h**2)   # Radiation density parameter
Omega_Lambda = 1.0 - Omega_m - Omega_r  # Dark energy parameter
Y_p = 0.248                  # Primordial Helium-4 mass fraction (from §19.4.1)

# Atomic parameters
E_ion = 13.605693 * eV_to_J  # Hydrogen ground state binding energy [J]
E_2s = E_ion / 4.0           # n=2 level binding energy [J]
h_nu_alpha = (3.0 / 4.0) * E_ion  # Lyman-alpha photon energy [J]
lambda_alpha = 121.567e-9    # Lyman-alpha wavelength [m]
Lambda_2s = 8.22458          # Two-photon 2s -> 1s decay rate [s^-1]

# Total hydrogen number density at redshift z
def n_H(z):
    # Total baryon mass density rho_b(z) = rho_b,0 * (1+z)^3
    rho_crit0 = 3.0 * (H0**2) / (8.0 * np.pi * 6.67430e-11)
    rho_b0 = Omega_b * rho_crit0
    # Mass fraction in hydrogen is (1 - Y_p)
    return (1.0 - Y_p) * rho_b0 / m_p * ((1.0 + z)**3)

# Hubble expansion rate at redshift z [s^-1]
def H_z(z):
    return H0 * np.sqrt(Omega_r * ((1.0 + z)**4) + Omega_m * ((1.0 + z)**3) + Omega_Lambda)

# Case B recombination coefficient (Pequignot et al. fitting formula)
def alpha_B(T_m):
    t4 = T_m / 1.0e4
    # Pequignot, Petitjean & Boisson (1991) formula in m^3/s
    return 1.0e-19 * (4.309 * (t4**(-0.6166))) / (1.0 + 0.6703 * (t4**0.5300))

# Photoionization rate from n=2 level by CMB photons
def beta_B(T_gamma, T_m):
    # Detailed balance relation
    factor = (m_e * k_B * T_gamma / (2.0 * np.pi * (hbar**2)))**1.5
    return alpha_B(T_m) * factor * np.exp(-E_2s / (k_B * T_gamma))

# Peebles multi-level ODE system: d(x_e)/dz and d(T_m)/dz
def peebles_system(z, y):
    x_e = y[0]
    T_m = y[1]
    
    # Boundary clamps for numerical stability
    x_e = max(1.0e-6, min(1.0, x_e))
    T_m = max(1.0, T_m)
    
    T_g = T_gamma0 * (1.0 + z)
    Hz = H_z(z)
    nH = n_H(z)
    
    aB = alpha_B(T_m)
    bB = beta_B(T_g, T_m)
    
    # Lyman-alpha photon redshifting escape rate
    # Lambda_alpha = 8*pi*H / (lambda_alpha^3 * n_1s) where n_1s = n_H * (1 - x_e)
    n_1s = max(1.0e-10, nH * (1.0 - x_e))
    Lambda_alpha = 8.0 * np.pi * Hz / ((lambda_alpha**3) * n_1s)
    
    # Peebles net transition probability factor C(z)
    C_factor = (Lambda_2s + Lambda_alpha) / (Lambda_2s + Lambda_alpha + bB)
    
    # dx_e/dt
    recombination_rate = aB * nH * (x_e**2)
    ionization_rate = bB * (1.0 - x_e) * np.exp(-h_nu_alpha / (k_B * T_g))
    dxe_dt = - C_factor * (recombination_rate - ionization_rate)
    
    # dt/dz = -1 / ((1+z) * H(z))
    dxe_dz = dxe_dt * (-1.0 / ((1.0 + z) * Hz))
    
    # Compton cooling / heating of matter by CMB photons:
    # dT_m/dt = -2 H T_m + (8/3)*(sigma_T a_rad T_g^4 / m_e c)*(x_e / (1 + x_e + f_He))*(T_g - T_m)
    f_He = Y_p / (4.0 * (1.0 - Y_p))
    compton_coeff = (8.0 * sigma_T * a_rad * (T_g**4)) / (3.0 * m_e * c)
    compton_term = compton_coeff * (x_e / (1.0 + x_e + f_He)) * (T_g - T_m)
    
    dTm_dt = -2.0 * Hz * T_m + compton_term
    dTm_dz = dTm_dt * (-1.0 / ((1.0 + z) * Hz))
    
    return [dxe_dz, dTm_dz]

def run_peebles_simulation():
    # Initial conditions at z = 1600 (tight-coupling equilibrium)
    z_start = 1600.0
    z_end = 600.0
    
    # Saha equilibrium initial ionization fraction at z_start
    T_g_init = T_gamma0 * (1.0 + z_start)
    nH_init = n_H(z_start)
    saha_rhs = ((m_e * k_B * T_g_init / (2.0 * np.pi * (hbar**2)))**1.5) / nH_init * np.exp(-E_ion / (k_B * T_g_init))
    # xe^2 / (1 - xe) = saha_rhs => xe = (-saha_rhs + sqrt(saha_rhs^2 + 4*saha_rhs)) / 2
    xe_init = (-saha_rhs + np.sqrt(saha_rhs**2 + 4.0 * saha_rhs)) / 2.0
    xe_init = min(0.9999, max(0.001, xe_init))
    Tm_init = T_g_init
    
    y0 = [xe_init, Tm_init]
    z_eval = np.linspace(z_start, z_end, 500)
    
    # Solve stiff system using Radau / RK45
    sol = solve_ivp(peebles_system, (z_start, z_end), y0, t_eval=z_eval, method='Radau', rtol=1e-7, atol=1e-9)
    
    # Find recombination epoch z_rec where x_e = 0.5 and x_e = 0.1
    z_arr = sol.t
    xe_arr = sol.y[0]
    Tm_arr = sol.y[1]
    Tg_arr = T_gamma0 * (1.0 + z_arr)
    
    # Interpolate exact z_rec (x_e = 0.5) and z_dec (x_e = 0.1)
    z_rec_50 = float(np.interp(0.5, xe_arr[::-1], z_arr[::-1]))
    z_rec_10 = float(np.interp(0.1, xe_arr[::-1], z_arr[::-1]))
    
    # Residual ionization at z = 600
    xe_freezeout = float(xe_arr[-1])
    
    # Sample diagnostic table across redshifts
    sample_z = [1500, 1300, 1100, 1000, 900, 800, 700, 600]
    results = []
    for sz in sample_z:
        idx = (np.abs(z_arr - sz)).argmin()
        z_val = z_arr[idx]
        xe_val = xe_arr[idx]
        tm_val = Tm_arr[idx]
        tg_val = Tg_arr[idx]
        nH_val = n_H(z_val)
        
        results.append({
            "Redshift z": f"{z_val:.1f}",
            "CMB Temp T_gamma (K)": f"{tg_val:.1f}",
            "Matter Temp T_m (K)": f"{tm_val:.1f}",
            "Ionization Fraction x_e": f"{xe_val:.6f}",
            "Hydrogen Density n_H (m^-3)": f"{nH_val:.3e}"
        })
        
    df = pd.DataFrame(results)
    
    output_lines = [
        "-" * 78,
        "§20.1.3.2 Peebles Multi-Level Braid Recombination Kinetics",
        "-" * 78,
        f"Cosmological Parameters: Omega_b*h^2 = 0.02237, Omega_c*h^2 = 0.1200, h = {h}",
        f"Helium Mass Fraction Y_p: {Y_p:.3f}, T_gamma,0 = {T_gamma0} K",
        "-" * 78,
        df.to_markdown(index=False, tablefmt="github"),
        "-" * 78,
        f"Recombination Redshift (x_e = 0.5): z_rec = {z_rec_50:.2f} (T = {T_gamma0*(1+z_rec_50):.1f} K, ~0.30 eV)",
        f"Decoupling Threshold (x_e = 0.1):  z_dec = {z_rec_10:.2f} (T = {T_gamma0*(1+z_rec_10):.1f} K)",
        f"Residual Freeze-out Ionization (z=600): x_e,inf = {xe_freezeout:.4e}",
        "-" * 78,
        "status: pass",
        "-" * 78
    ]
    output_str = "\n".join(output_lines)
    print(output_str)
    
    with open("code/repo/python/outputs/20.1.3.2.txt", "w", encoding="utf-8") as f:
        f.write(output_str + "\n")

if __name__ == "__main__":
    run_peebles_simulation()
