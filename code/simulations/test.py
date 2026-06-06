import sympy as sp

def validate_space_dilation():
    # Define symbols
    t, rho, c, T, R = sp.symbols('t rho c T R', real=True, positive=True)

    print("=== 1. Metric Tensor Specification ===")
    g00 = -c**2
    g11 = sp.exp(2 * t / T)
    g = sp.Matrix([[g00, 0], [0, g11]])
    g_inv = g.inv()
    print(f"g_mu_nu =\n{g}\n")
    print(f"g^mu_nu =\n{g_inv}\n")

    print("=== 2. Connection Coefficients (Christoffel Symbols) ===")
    coords = [t, rho]
    def get_christoffel(lam, mu, nu):
        gamma = 0
        for sigma in range(2):
            term1 = sp.diff(g[nu, sigma], coords[mu])
            term2 = sp.diff(g[mu, sigma], coords[nu])
            term3 = sp.diff(g[mu, nu], coords[sigma])
            gamma += 0.5 * g_inv[lam, sigma] * (term1 + term2 - term3)
        return sp.simplify(gamma)

    Gamma_t_rho_rho = get_christoffel(0, 1, 1)
    Gamma_rho_t_rho = get_christoffel(1, 0, 1)
    print(f"Gamma^t_rho_rho   = {Gamma_t_rho_rho}")
    print(f"Gamma^rho_t_rho   = {Gamma_rho_t_rho}\n")

    print("=== 3. Trajectory 1: The Comoving Observer (rho = constant) ===")
    u_comoving = [1 / c, 0]
    a_comoving = []
    for lam in range(2):
        a_comp = 0
        for mu in range(2):
            for nu in range(2):
                a_comp += get_christoffel(lam, mu, nu) * u_comoving[mu] * u_comoving[nu]
        a_comoving.append(sp.simplify(a_comp))
    print(f"Four-acceleration vector a^mu = {a_comoving}")
    mag = sp.sqrt(g[0,0] * a_comoving[0]**2 + g[1,1] * a_comoving[1]**2)
    print(f"Proper acceleration magnitude  = {sp.simplify(mag)}\n")

    print("=== 4. Trajectory 2: The Static Observer (r = R) ===")
    rho_t = R * sp.exp(-t / T)
    v_rho = sp.diff(rho_t, t)
    print(f"Required coordinate trajectory rho(t) = {rho_t}")
    print(f"Coordinate velocity d_rho/dt           = {v_rho}\n")

    print("=== 5. Path Proper Length Evaluation ===")
    d_ell = sp.sqrt(g11) * sp.Abs(v_rho)
    print(f"Evaluated d_ell             = {sp.simplify(d_ell)} * dt\n")

    print("=== 6. Static Observer Acceleration Verification ===")
    # Four-velocity components u^mu = dx^mu/dtau
    # dtau = dt * sqrt(1 - R^2/(c^2*T^2))
    # Normalized such that u^mu u_mu = -c^2
    gamma = 1 / sp.sqrt(1 - R**2 / (c**2 * T**2))
    u_static = [gamma, -gamma * R * sp.exp(-t/T) / T]
    
    a_static = []
    for lam in range(2):
        du_dtau = gamma * sp.diff(u_static[lam], t)
        gamma_term = 0
        for mu in range(2):
            for nu in range(2):
                gamma_term += get_christoffel(lam, mu, nu) * u_static[mu] * u_static[nu]
        a_static.append(sp.simplify(du_dtau + gamma_term))
        
    print(f"Static observer four-acceleration a^mu = {a_static}")
    mag_squared = g[0,0] * a_static[0]**2 + g[1,1] * a_static[1]**2
    mag_static_physical = sp.sqrt(sp.simplify(mag_squared))
    print(f"Proper acceleration magnitude |a|     = {sp.simplify(mag_static_physical)}")
    print(f"Leading PN order (c -> oo) |a|        = {sp.limit(mag_static_physical, c, sp.oo)}")

if __name__ == "__main__":
    # Ensure the square-root argument in proper acceleration magnitude is positive 
    # in the physical regime T^2 * c^2 > R^2, since T^2*c^2 - R^2 = R^2 * (c^2 / (GM/R) - 1) > 0.
    validate_space_dilation()