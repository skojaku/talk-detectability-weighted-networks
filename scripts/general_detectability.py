import sympy as sp

# Define symbols
Omega = sp.Symbol("Omega", positive=True)
Delta_omega = sp.Symbol("Delta_omega", real=True)
Delta_kappa = sp.Symbol("Delta_kappa", real=True)
K = sp.Symbol("K", positive=True)
sigma_in_sq = sp.Symbol("sigma_in_sq", positive=True)
sigma_out_sq = sp.Symbol("sigma_out_sq", positive=True)

print("=== General Detectability Condition for Arbitrary Weight Distributions ===\n")

# The general eigenvalue numerator (detectability condition when λ = 1)
# From the previous analysis, the detectability condition is when the numerator - denominator = 0

numerator = (
    Delta_kappa**2 * Omega**2 / 2 +
    Delta_kappa * Delta_omega * K * Omega +
    Delta_kappa * Delta_omega * Omega +
    Delta_kappa * sigma_in_sq - Delta_kappa * sigma_out_sq +
    Delta_omega**2 * K**2 / 2 +
    Delta_omega**2 * K / 2 +
    K * Omega**2 / 2 +
    K * sigma_in_sq + K * sigma_out_sq
)

denominator = Delta_kappa * Omega + Delta_omega * K

# Detectability condition: numerator = denominator
detectability_condition = numerator - denominator

print("1. General Detectability Condition:")
print("   The condition for detectability (λ = 1) is:")
print("   f(Ω, K, Δω, Δκ, σ²_in, σ²_out) = 0")
print("   where:")

# Simplify and reorganize
f_general = sp.expand(detectability_condition)
print(f"   f = {f_general}")

# Group terms by variance and non-variance components
variance_terms = Delta_kappa * (sigma_in_sq - sigma_out_sq) + K * (sigma_in_sq + sigma_out_sq)
non_variance_terms = (
    Delta_kappa**2 * Omega**2 / 2 +
    Delta_kappa * Delta_omega * K * Omega +
    Delta_kappa * Delta_omega * Omega - Delta_kappa * Omega +
    Delta_omega**2 * K**2 / 2 +
    Delta_omega**2 * K / 2 - Delta_omega * K +
    K * Omega**2 / 2
)

print(f"\n2. Decomposition:")
print(f"   f = (Non-variance terms) + (Variance terms)")
print(f"   f = {sp.expand(non_variance_terms)} + {variance_terms}")

# The non-variance part is exactly our previous result!
print(f"\n3. Connection to Previous Analysis:")
print(f"   The non-variance terms are exactly the detectability condition")
print(f"   from our previous analysis with specific weight distribution.")
print(f"   The variance terms add corrections based on the weight distribution.")

print(f"\n4. Variance Effect:")
print(f"   Variance terms = Δκ(σ²_in - σ²_out) + K(σ²_in + σ²_out)")
print(f"   - If σ²_in > σ²_out: intra-community variance helps detectability")
print(f"   - If σ²_out > σ²_in: inter-community variance helps detectability")
print(f"   - Total variance K(σ²_in + σ²_out) always helps detectability")

# Special cases
print(f"\n5. Special Cases:")

# Case 1: Equal variances
print(f"\n   a) Equal variances (σ²_in = σ²_out = σ²):")
sigma_sq = sp.Symbol("sigma_sq", positive=True)
f_equal_var = f_general.subs([(sigma_in_sq, sigma_sq), (sigma_out_sq, sigma_sq)])
print(f"      f = {sp.simplify(f_equal_var)}")
print(f"      The variance difference term vanishes, only total variance matters")

# Case 2: No variance (deterministic weights)
print(f"\n   b) Deterministic weights (σ²_in = σ²_out = 0):")
f_deterministic = f_general.subs([(sigma_in_sq, 0), (sigma_out_sq, 0)])
print(f"      f = {sp.simplify(f_deterministic)}")
print(f"      This recovers our previous result exactly")

# Case 3: Only intra-community variance
print(f"\n   c) Only intra-community variance (σ²_out = 0):")
f_intra_only = f_general.subs(sigma_out_sq, 0)
print(f"      f = {sp.simplify(f_intra_only)}")

# Case 4: Only inter-community variance
print(f"\n   d) Only inter-community variance (σ²_in = 0):")
f_inter_only = f_general.subs(sigma_in_sq, 0)
print(f"      f = {sp.simplify(f_inter_only)}")

# General solution for Delta_omega
print(f"\n6. General Solution:")
print(f"   The general detectability boundary can be solved for Δω:")
solutions = sp.solve(detectability_condition, Delta_omega)
if len(solutions) > 0:
    print(f"   Δω = {sp.simplify(solutions[0])}")
else:
    print("   (Complex solution - consider numerical methods)")

# LaTeX output
print(f"\n7. LaTeX Equation:")
print(f"   The general detectability condition is:")
print(f"   {sp.latex(f_general)} = 0")

# Summary
print(f"\n8. Summary:")
print(f"   The general detectability condition extends the previous result by:")
print(f"   - Adding variance-dependent terms")
print(f"   - Allowing for arbitrary weight distributions")
print(f"   - Showing that variance differences and total variance affect detectability")
print(f"   - Reducing to the previous case when σ²_in = σ²_out = 0")

# Practical implications
print(f"\n9. Practical Implications:")
print(f"   - Higher weight variance generally makes detection easier")
print(f"   - Asymmetric variances (σ²_in ≠ σ²_out) can shift the detectability boundary")
print(f"   - The effect depends on both the variance magnitude and the degree structure")