# %%
import sympy as sp

# Define symbols
Omega = sp.Symbol("Omega", positive=True)
Delta_omega = sp.Symbol("Delta_omega", real=True)
Delta_kappa = sp.Symbol("Delta_kappa", real=True)
K = sp.Symbol("K", positive=True)

print("=== Detectability Limit for Weighted Networks ===\n")

# The detectability curve equation (derived from lambda = 1 condition)
# This is a quadratic form in Delta_omega and Delta_kappa
detectability_curve = (
    Delta_kappa**2 * Omega**2 / 4 +
    Delta_kappa * Delta_omega * K * Omega / 2 +
    Delta_kappa * Delta_omega * Omega / 2 -
    Delta_kappa * Omega / 2 +
    Delta_omega**2 * K**2 / 4 +
    Delta_omega**2 * K / 4 -
    Delta_omega * K / 2 +
    K * Omega**2 / 4
)

print("1. General Detectability Curve f(Ω, K, Δω, Δκ) = 0:")
print("   where the system is detectable when f > 0\n")

# Rewrite in a cleaner quadratic form
# f = a*Delta_omega^2 + b*Delta_omega*Delta_kappa + c*Delta_kappa^2 + d*Delta_omega + e*Delta_kappa + f
a = K**2/4 + K/4
b = K*Omega/2 + Omega/2
c = Omega**2/4
d = -K/2
e = -Omega/2
f = K*Omega**2/4

print("   The curve can be written as:")
print(f"   ({a})*Δω² + ({b})*Δω*Δκ + ({c})*Δκ² + ({d})*Δω + ({e})*Δκ + {f} = 0")
print("\n   Or in matrix form: [Δω, Δκ, 1] * A * [Δω, Δκ, 1]ᵀ = 0")

# For a given Omega and K, solve for Delta_omega as a function of Delta_kappa
print("\n2. Explicit Solution for Δω(Δκ):")
solutions = sp.solve(detectability_curve, Delta_omega)
sol = solutions[1]  # Take the positive branch
print("   Δω = " + str(sp.simplify(sol)))

# Special cases
print("\n3. Special Cases:")

# Case 1: Delta_kappa = 0 (uniform degree)
print("\n   a) When Δκ = 0 (uniform degree):")
curve_dk0 = detectability_curve.subs(Delta_kappa, 0)
sol_dk0 = sp.solve(curve_dk0, Delta_omega)
print("      Critical Δω = " + str(sp.simplify(sol_dk0[1])))
print("      This gives: Δω_c = (2 - Ω²) / (K + 1)")

# Case 2: Delta_omega = 0 (uniform weight)
print("\n   b) When Δω = 0 (uniform weight):")
curve_dw0 = detectability_curve.subs(Delta_omega, 0)
sol_dw0 = sp.solve(curve_dw0, Delta_kappa)
print("      Critical Δκ = " + str(sp.simplify(sol_dw0[1])))
print("      This gives: Δκ_c = 2(1 - K*Ω) / Ω")

# Asymptotic behavior
print("\n4. Asymptotic Behavior:")
print("\n   a) Large K limit:")
print("      The curve approaches: Δω ≈ (1 - Δκ*Ω) / K")
print("      This shows that larger average degree K makes detection easier")

print("\n   b) Small Ω limit:")
print("      The curve approaches: Δκ ≈ 2/Ω - K")
print("      As Ω → 0, we need larger Δκ for detection")

# Detectability region characterization
print("\n5. Detectability Region:")
print("   The detectable region is where f(Ω, K, Δω, Δκ) > 0")
print("   This forms an elliptical region in the (Δω, Δκ) plane")
print("   centered approximately at (Δω, Δκ) = (1/K, 2/Ω)")

# Generate the LaTeX equation for the paper
print("\n6. LaTeX Equation for Paper:")
print("   The detectability boundary is given by:")
latex_eq = sp.latex(detectability_curve) + " = 0"
print("   " + latex_eq)

print("\n   Or in simplified form:")
# Factor out common terms
simplified = sp.collect(detectability_curve, [Delta_omega, Delta_kappa])
print("   " + sp.latex(simplified) + " = 0")

# Create a normalized form
print("\n7. Normalized Form:")
print("   Define normalized variables:")
print("   δω = Δω * (K+1)/2  and  δκ = Δκ * Ω/2")
print("   Then the detectability condition becomes approximately:")
print("   δω² + δω*δκ + δκ² - δω - δκ + constant = 0")
