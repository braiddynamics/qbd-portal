import sys
import numpy as np
import matplotlib.pyplot as plt

print("[1/5] Initializing simulation constants...", flush=True)

# ==========================================
# 1. Physical Constants & Astronomical Data
# ==========================================
G = 6.67430e-11          # m^3 kg^-1 s^-2
c = 2.99792458e8         # m/s
M_sun = 1.98847e30       # kg
day_in_sec = 86400.0

# Double Pulsar (PSR J0737-3039A/B) Parameters
m1 = 1.3381 * M_sun      # Mass Pulsar A
m2 = 1.2489 * M_sun      # Mass Pulsar B
M_tot = m1 + m2
mu = (m1 * m2) / M_tot   # Reduced mass
P_b = 0.1022515624 * day_in_sec  # Orbital period (2.4 hours in seconds)
e = 0.087777             # Eccentricity

# Semi-major axis and orbital frequency
a = (G * M_tot * (P_b / (2 * np.pi))**2)**(1/3)
Omega = 2 * np.pi / P_b

# GR Quadrupole Radiation (Peters & Mathews)
f_e_quad = (1 + (73/24)*e**2 + (37/96)*e**4) / (1 - e**2)**(3.5)
P_dot_GR = - (192 * np.pi / 5) * (G * M_tot * Omega / c**3)**(5/3) * (mu / M_tot) * f_e_quad

def P_dot_scalar_dipole(delta_alpha, P_b, m1, m2, a, e):
    """Calculates orbital decay rate due to scalar dipole radiation."""
    g_e_dip = (1 + 0.5*e**2) / (1 - e**2)**2.5
    E_dot_dipole = (G / (3 * c**3)) * (mu**2) * (Omega**4) * (a**2) * (delta_alpha**2) * g_e_dip
    E_orbit = G * m1 * m2 / (2 * a)
    return - (3 / 2) * P_b * (E_dot_dipole / E_orbit)

print("[2/5] Scanning parameter space across 500 evaluation points...", flush=True)
delta_alpha_range = np.logspace(-6, -2, 500)

P_dot_total = []
gamma_PPN_vals = []

for da in delta_alpha_range:
    p_dip = P_dot_scalar_dipole(da, P_b, m1, m2, a, e)
    p_tot = P_dot_GR + p_dip
    P_dot_total.append(p_tot)
    gamma_PPN_vals.append(1 - 2 * (da**2))

P_dot_total = np.array(P_dot_total)
gamma_PPN_vals = np.array(gamma_PPN_vals)
decay_ratio = P_dot_total / P_dot_GR

print("[3/5] Calculating critical breakdown thresholds...", flush=True)
kill_idx_pulsar = np.where(decay_ratio > 1.0001)[0][0]
kill_alpha_pulsar = delta_alpha_range[kill_idx_pulsar]

kill_idx_cassini = np.where(gamma_PPN_vals < (1.0 - 2.3e-5))[0][0]
kill_alpha_cassini = delta_alpha_range[kill_idx_cassini]

print("\n==================================================", flush=True)
print("=== BSU MODEL BREAKDOWN THRESHOLDS ===", flush=True)
print("==================================================", flush=True)
print(fr"1. Binary Pulsar Kill Limit : \Delta\alpha_C > {kill_alpha_pulsar:.3e}", flush=True)
print("   (Beyond this, scalar dipole radiation causes PSR J0737-3039 to decay faster than observed).", flush=True)
print(fr"2. Cassini Solar System Limit: \Delta\alpha_C > {kill_alpha_cassini:.3e}", flush=True)
print("   (Beyond this, gamma_PPN slip violates light deflection and radar time-delay data).", flush=True)
print("==================================================\n", flush=True)

print("[4/5] Rendering plot...", flush=True)
fig, ax1 = plt.subplots(figsize=(9, 6))

color = 'tab:red'
ax1.set_xlabel(r'Surviving Scalar Charge Difference $\Delta\alpha_C = |\alpha_1 - \alpha_2|$', fontsize=12)
ax1.set_ylabel(r'Orbital Decay Ratio ($\dot{P}_{\mathrm{BSU}} / \dot{P}_{\mathrm{GR}}$)', color=color, fontsize=12)
ax1.semilogx(delta_alpha_range, decay_ratio, color=color, linewidth=2.5, label='BSU Period Decay Ratio')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, which="both", ls="--", alpha=0.5)

ax1.axhline(1.0001, color='black', linestyle=':', label='PSR J0737-3039 Observational Ceiling (+0.01%)')
ax1.axhline(1.0, color='gray', linestyle='-')

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel(r'Post-Newtonian Parameter $\gamma_{\mathrm{PPN}}$', color=color, fontsize=12)
ax2.semilogx(delta_alpha_range, gamma_PPN_vals, color=color, linewidth=2, linestyle='--', label=r'$\gamma_{\mathrm{PPN}}$ Slip')
ax2.tick_params(axis='y', labelcolor=color)

ax2.axhline(1.0 - 2.3e-5, color='purple', linestyle='-.', label='Cassini Solar System Limit')

plt.title(r'Breakdown of BSU Model via Surviving Memory Scalar $C$', fontsize=13, pad=15)
fig.tight_layout()

# Save plot to file so it exists immediately
plt.savefig('bsu_breakdown.png', dpi=300)
print("[5/5] Plot saved to 'bsu_breakdown.png'. Opening window (close window to exit script)...", flush=True)

plt.show()
print("Execution complete.", flush=True)