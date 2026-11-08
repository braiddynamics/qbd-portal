from decimal import Decimal, localcontext


def verify_neutrino_seesaw():
    """Compare the unit Planck anchor and calibrated two-state seesaw."""
    with localcontext() as context:
        context.prec = 60
        v = Decimal("246")
        mu = Decimal("0.40")
        c_star = Decimal("2.76")
        planck_mass = Decimal("1.22e19")
        unit_mass = planck_mass * (-c_star / mu).exp()
        target_mass = Decimal("2.36e16")
        matched_prefactor = target_mass / unit_mass
        gev_to_ev = Decimal("1e9")
        atmospheric_split_ev2 = Decimal("2.4e-3")

        print("TWO-STATE SEESAW: HEAVY-SCALE AND UNITS CHECK")
        print(f"Unit anchor: A=1, M_R={unit_mass:.6E} GeV")
        print(f"Matched anchor: A={matched_prefactor:.6f}, M_R={target_mass:.6E} GeV")
        print("Yukawa  m_D (GeV)  m_light (GeV)  m_light (eV)  Relative error bound")
        for value in ("0.01", "0.10", "0.50", "1.00"):
            yukawa = Decimal(value)
            dirac_mass = yukawa * v
            dirac_squared = dirac_mass ** 2
            gap = (target_mass ** 2 + 4 * dirac_squared).sqrt()
            light_gev = 2 * dirac_squared / (gap + target_mass)
            light_ev = light_gev * gev_to_ev
            relative_bound = (dirac_mass / target_mass) ** 2
            print(
                f"{yukawa:6.2f}  {dirac_mass:9.2f}  "
                f"{light_gev:13.6E}  {light_ev:12.6E}  {relative_bound:.3E}"
            )

        print(f"Atmospheric comparison: |delta m^2|={atmospheric_split_ev2:.3E} eV^2")
        print(f"Square-root scale: {atmospheric_split_ev2.sqrt():.6E} eV")


if __name__ == "__main__":
    verify_neutrino_seesaw()
