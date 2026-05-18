import sympy as sp

# Define symbols for the general case
Omega = sp.Symbol("Omega", positive=True)
Delta_omega = sp.Symbol("Delta_omega", real=True)
Delta_kappa = sp.Symbol("Delta_kappa", real=True)
K = sp.Symbol("K", positive=True)

# General variance symbols
sigma_in_squared = sp.Symbol("sigma_in_squared", positive=True)
sigma_out_squared = sp.Symbol("sigma_out_squared", positive=True)

# Define community parameters
k_in = (K + Delta_kappa) / 2
k_out = (K - Delta_kappa) / 2
omega_in = (Omega + Delta_omega) / 2
omega_out = (Omega - Delta_omega) / 2

print("=== General Eigenvalue Derivation for Arbitrary Weight Distributions ===\n")

print("Parameters:")
print(f"  k_in = {k_in}")
print(f"  k_out = {k_out}")
print(f"  ω_in = {omega_in}")
print(f"  ω_out = {omega_out}")
print(f"  σ²_in = {sigma_in_squared}")
print(f"  σ²_out = {sigma_out_squared}")

# Expected strength (first moment)
s_in = omega_in * k_in
s_out = omega_out * k_out

print(f"\nExpected strengths:")
print(f"  s_in = ω_in * k_in = {s_in}")
print(f"  s_out = ω_out * k_out = {s_out}")

# Second moment of edge weights: E[w²] = Var[w] + (E[w])²
w_in_squared = sigma_in_squared + omega_in**2
w_out_squared = sigma_out_squared + omega_out**2

print(f"\nSecond moments of edge weights:")
print(f"  E[w²_in] = σ²_in + ω²_in = {w_in_squared}")
print(f"  E[w²_out] = σ²_out + ω²_out = {w_out_squared}")

# Degree second moments
k_in_squared = k_in**2 + k_in  # E[k²] = E[k(k-1)] + E[k] for Poisson-like
k_out_squared = k_out**2 + k_out

# Expected squared strength
s_in_squared = w_in_squared * k_in + omega_in**2 * (k_in_squared - k_in)
s_out_squared = w_out_squared * k_out + omega_out**2 * (k_out_squared - k_out)

print(f"\nExpected squared strengths:")
print(f"  E[s²_in] = E[w²_in] * k_in + ω²_in * (E[k²_in] - k_in)")
print(f"          = {w_in_squared} * {k_in} + {omega_in**2} * ({k_in_squared} - {k_in})")
print(f"          = {sp.expand(s_in_squared)}")
print(f"  E[s²_out] = {sp.expand(s_out_squared)}")

# Variance of strength
s_in_var = s_in_squared - s_in**2
s_out_var = s_out_squared - s_out**2

print(f"\nVariances of strengths:")
print(f"  Var[s_in] = E[s²_in] - (E[s_in])² = {sp.expand(s_in_var)}")
print(f"  Var[s_out] = E[s²_out] - (E[s_out])² = {sp.expand(s_out_var)}")

# General eigenvalue formula
ds = s_in - s_out
ds_squared = s_in_squared + s_out_squared - 2 * s_in * s_out

print(f"\nDifference in expected strengths:")
print(f"  Δs = s_in - s_out = {sp.expand(ds)}")

print(f"\nExpected squared difference:")
print(f"  E[(s_in - s_out)²] = {sp.expand(ds_squared)}")

# The general eigenvalue
lambda_general = ds_squared / ds

print(f"\nGeneral eigenvalue:")
print(f"  λ = E[(s_in - s_out)²] / (s_in - s_out)")
print(f"    = {sp.simplify(lambda_general)}")

# Simplify the eigenvalue expression
lambda_simplified = sp.simplify(lambda_general)
print(f"\nSimplified eigenvalue:")
print(f"  λ = {lambda_simplified}")

# Expand to show the role of variances explicitly
lambda_expanded = sp.expand(lambda_general)
print(f"\nExpanded eigenvalue:")
print(f"  λ = {lambda_expanded}")

# Detectability condition: λ = 1
detectability_condition = lambda_general - 1

print(f"\nDetectability condition (λ = 1):")
print(f"  {sp.simplify(detectability_condition)} = 0")

# LaTeX output for the paper
print(f"\nLaTeX equation:")
print(f"  λ = {sp.latex(lambda_simplified)}")

print(f"\nDetectability condition in LaTeX:")
print(f"  {sp.latex(sp.simplify(detectability_condition))} = 0")

# Special case: when variances are equal (σ²_in = σ²_out = σ²)
print(f"\n=== Special Case: Equal Variances ===")
sigma_squared = sp.Symbol("sigma_squared", positive=True)
lambda_equal_var = lambda_general.subs([(sigma_in_squared, sigma_squared), 
                                       (sigma_out_squared, sigma_squared)])
print(f"When σ²_in = σ²_out = σ²:")
print(f"  λ = {sp.simplify(lambda_equal_var)}")

# Show how this relates to the original case
print(f"\n=== Connection to Original Case ===")
print("In the original analysis with specific weight distribution:")
print("  σ²_in was related to the weight distribution parameters")
print("  This general form allows for any weight distribution")
print("  by specifying the appropriate variance values")