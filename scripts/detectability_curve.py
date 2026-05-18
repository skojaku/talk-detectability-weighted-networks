# %%
import sympy as sp

# Define symbols
Omega = sp.Symbol("Omega", positive=True)
Delta_omega = sp.Symbol("Delta_omega", real=True)
Delta_kappa = sp.Symbol("Delta_kappa", real=True)
K = sp.Symbol("K", positive=True)
L = sp.Symbol("L", positive=True)

# Define parameters for the two groups
k_in = (K + Delta_kappa) / 2
k_out = (K - Delta_kappa) / 2
omega_in = (Omega + Delta_omega) / 2
omega_out = (Omega - Delta_omega) / 2

# For large L approximation, we use the simplified expression
# The detectability condition is lambda = 1
# From the calc.py file, the lambda for large L is approximately:
s_in = k_in * omega_in
s_out = k_out * omega_out
ds = s_in - s_out

# Simplified lambda for large L
lambda_simple = ds + (k_in * omega_in**2 + k_out * omega_out**2) / ds

# Detectability condition: lambda = 1
detectability_condition = lambda_simple - 1

# Expand and simplify
detectability_expanded = sp.expand(detectability_condition * ds)
detectability_simplified = sp.simplify(detectability_expanded)

print("Detectability condition (lambda = 1):")
print(sp.latex(detectability_simplified))

# Solve for the curve in terms of Delta_omega and Delta_kappa
# The curve is defined by f(Omega, K, Delta_omega, Delta_kappa) = 0
curve_equation = detectability_simplified

# Let's also derive a more explicit form
# Expand the equation to see the relationship between Delta_omega and Delta_kappa
curve_expanded = sp.expand(curve_equation)

print("\nExpanded curve equation:")
print(sp.latex(curve_expanded))

# Print the general form of the detectability curve
print("\nGeneral detectability curve f(Omega, K, Delta_omega, Delta_kappa) = 0:")
print("In LaTeX form:")
print(sp.latex(curve_equation))

# Let's also find a more explicit relationship
# Rearrange to show Delta_omega as a function of Delta_kappa
print("\n\nSolving for Delta_omega in terms of Delta_kappa:")
solutions_dw = sp.solve(curve_equation, Delta_omega)
for i, sol in enumerate(solutions_dw):
    print(f"\nSolution {i+1}:")
    print(sp.latex(sp.simplify(sol)))

# Derive special cases
print("\n\nSpecial Cases:")
print("1. When Delta_kappa = 0 (uniform degree):")
curve_dk0 = curve_equation.subs(Delta_kappa, 0)
print(sp.latex(sp.simplify(curve_dk0)))

print("\n2. When Delta_omega = 0 (uniform weight):")
curve_dw0 = curve_equation.subs(Delta_omega, 0)
print(sp.latex(sp.simplify(curve_dw0)))
# %%
