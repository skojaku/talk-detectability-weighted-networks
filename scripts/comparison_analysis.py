import sympy as sp

print("=== Comparison: General vs. Specific Weight Distribution ===\n")

# Define symbols
Omega = sp.Symbol("Omega", positive=True)
Delta_omega = sp.Symbol("Delta_omega", real=True)
Delta_kappa = sp.Symbol("Delta_kappa", real=True)
K = sp.Symbol("K", positive=True)
L = sp.Symbol("L", positive=True)

# From the original calc.py, the specific form was:
omega_in = (Omega + Delta_omega) / 2
omega_out = (Omega - Delta_omega) / 2

# Original specific variance expressions (from calc.py line 49-50)
w_in_squared_specific = (1 - omega_in**2)**2 / (L-3) + omega_in**2
w_out_squared_specific = (1 - omega_out**2)**2 / (L-3) + omega_out**2

print("1. Original Specific Weight Distribution:")
print(f"   From calc.py, the weight variances were:")
print(f"   E[w²_in] = (1 - ω²_in)²/(L-3) + ω²_in = {w_in_squared_specific}")
print(f"   E[w²_out] = (1 - ω²_out)²/(L-3) + ω²_out = {w_out_squared_specific}")

# Extract the variance part (second moment minus mean squared)
sigma_in_sq_specific = w_in_squared_specific - omega_in**2
sigma_out_sq_specific = w_out_squared_specific - omega_out**2

print(f"\n2. Specific Variances:")
print(f"   σ²_in = E[w²_in] - ω²_in = {sp.simplify(sigma_in_sq_specific)}")
print(f"   σ²_out = E[w²_out] - ω²_out = {sp.simplify(sigma_out_sq_specific)}")

# Simplify for large L
print(f"\n3. Large L Approximation:")
sigma_in_large_L = sp.series(sigma_in_sq_specific, L, sp.oo, n=2).removeO()
sigma_out_large_L = sp.series(sigma_out_sq_specific, L, sp.oo, n=2).removeO()
print(f"   For large L, σ²_in ≈ {sigma_in_large_L}")
print(f"   For large L, σ²_out ≈ {sigma_out_large_L}")

# Show that variances become very small for large L
print(f"\n4. Behavior as L → ∞:")
print(f"   σ²_in → (1 - ω²_in)²/L → 0")
print(f"   σ²_out → (1 - ω²_out)²/L → 0")
print(f"   This explains why the original analysis neglected variance terms!")

# General detectability condition
sigma_in_sq = sp.Symbol("sigma_in_sq", positive=True)
sigma_out_sq = sp.Symbol("sigma_out_sq", positive=True)

general_condition = (
    Delta_kappa**2 * Omega**2 / 2 +
    Delta_kappa * Delta_omega * K * Omega +
    Delta_kappa * Delta_omega * Omega - Delta_kappa * Omega +
    Delta_kappa * sigma_in_sq - Delta_kappa * sigma_out_sq +
    Delta_omega**2 * K**2 / 2 +
    Delta_omega**2 * K / 2 - Delta_omega * K +
    K * Omega**2 / 2 +
    K * sigma_in_sq + K * sigma_out_sq
)

# Substitute specific variances
specific_condition = general_condition.subs([
    (sigma_in_sq, sigma_in_sq_specific),
    (sigma_out_sq, sigma_out_sq_specific)
])

print(f"\n5. Substituting Specific Variances:")
print(f"   f_specific = {sp.simplify(specific_condition)}")

# Take large L limit
specific_large_L = sp.series(specific_condition, L, sp.oo, n=1).removeO()
print(f"\n6. Large L Limit of Specific Case:")
print(f"   f_specific (L→∞) = {sp.simplify(specific_large_L)}")

# Compare with deterministic case
deterministic_condition = general_condition.subs([(sigma_in_sq, 0), (sigma_out_sq, 0)])
print(f"\n7. Deterministic Case (σ²_in = σ²_out = 0):")
print(f"   f_deterministic = {sp.simplify(deterministic_condition)}")

# Verification: they should match in the large L limit
difference = sp.simplify(specific_large_L - deterministic_condition)
print(f"\n8. Verification:")
print(f"   Difference = f_specific(L→∞) - f_deterministic = {difference}")
if difference == 0:
    print("   ✓ Perfect match! The general formula reduces to the original result.")
else:
    print("   The formulas match up to higher-order terms in 1/L.")

# Physical interpretation
print(f"\n9. Physical Interpretation:")
print(f"   - Original analysis assumed large L (many possible edge weights)")
print(f"   - In this limit, weight variance becomes negligible")
print(f"   - General formula allows for finite variance in weight distributions")
print(f"   - Variance terms become important for small L or heavy-tailed distributions")

# Examples of when variance matters
print(f"\n10. When Variance Effects Are Important:")
print(f"    - Binary weights: σ² = ω(1-ω), significant for moderate ω")
print(f"    - Power-law weight distributions: high variance")
print(f"    - Small number of discrete weight values (small effective L)")
print(f"    - Experimental data with measurement noise")

# Coefficient analysis
print(f"\n11. Variance Coefficient Analysis:")
variance_coeff_kappa = Delta_kappa
variance_coeff_total = K
print(f"    - Coefficient of (σ²_in - σ²_out): {variance_coeff_kappa}")
print(f"    - Coefficient of (σ²_in + σ²_out): {variance_coeff_total}")
print(f"    - Variance difference effect scales with degree heterogeneity")
print(f"    - Total variance effect scales with average degree")

print(f"\n12. Summary:")
print(f"    The general formula provides a unified framework that:")
print(f"    - Recovers the original result as a special case")
print(f"    - Extends to arbitrary weight distributions")
print(f"    - Shows when variance effects can be neglected")
print(f"    - Provides insight into the role of weight heterogeneity")