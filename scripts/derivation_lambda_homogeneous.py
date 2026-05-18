#!/usr/bin/env python3
"""
Detailed step-by-step symbolic derivation of eq:lambda_moment_homogeneous_weights
for the case where edge weights are homogeneous across communities.

This script derives the equation:
λ = (Δ_κ/2)Ω + (1/Δ_κ) · (KC)/(2Ω)

where:
- λ: largest eigenvalue of modularity matrix
- Δ_κ = κ_in - κ_out: difference in expected degrees
- Ω = ⟨w_in⟩ + ⟨w_out⟩: total average weight
- K = κ_in + κ_out: total expected degree
- C = 4α₀ + 2Ωα₁ + Ω²α₂: variance parameter
"""

import sympy as sp
from sympy import symbols, simplify, expand, collect, latex, pprint

def print_step(step_num, description, expr=None, latex_output=True):
    """Print a derivation step with clear formatting"""
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {description}")
    print('='*60)
    if expr is not None:
        if latex_output:
            print("LaTeX:")
            print(latex(expr))
            print("\nSymbolic:")
        pprint(expr)

def main():
    print("DETAILED DERIVATION OF λ FOR HOMOGENEOUS WEIGHTS")
    print("="*80)
    
    # Define all symbols
    print("\n1. SYMBOL DEFINITIONS:")
    print("-" * 40)
    
    # Basic parameters
    Omega = symbols('Omega', positive=True)  # Total average weight
    K = symbols('K', positive=True)          # Total expected degree
    Delta_kappa = symbols('Delta_kappa', real=True)  # Degree difference
    
    # Weight distribution parameters (second moment polynomial coefficients)
    alpha_0 = symbols('alpha_0', real=True)
    alpha_1 = symbols('alpha_1', real=True) 
    alpha_2 = symbols('alpha_2', real=True)
    
    # Derived quantities
    kappa_in = symbols('kappa_in', positive=True)
    kappa_out = symbols('kappa_out', positive=True)
    w_in = symbols('w_in', positive=True)
    w_out = symbols('w_out', positive=True)
    
    print(f"Ω = {Omega} (total average weight)")
    print(f"K = {K} (total expected degree)")
    print(f"Δ_κ = {Delta_kappa} (degree difference)")
    print(f"α₀, α₁, α₂ = {alpha_0}, {alpha_1}, {alpha_2} (weight distribution parameters)")
    
    # Step 1: Define the homogeneous weight condition
    print_step(1, "HOMOGENEOUS WEIGHT CONDITION")
    print("For homogeneous weights: ⟨w_in⟩ = ⟨w_out⟩ = Ω/2")
    print("This means community structure comes only from topology, not weight differences.")
    
    # Define the weight means
    w_in_mean = Omega / 2
    w_out_mean = Omega / 2
    Delta_omega = 0  # No weight difference
    
    print(f"⟨w_in⟩ = {w_in_mean}")
    print(f"⟨w_out⟩ = {w_out_mean}")
    print(f"Δ_ω = ⟨w_in⟩ - ⟨w_out⟩ = {Delta_omega}")
    
    # Step 2: Express degree parameters
    print_step(2, "DEGREE PARAMETERS")
    print("Express in-degree and out-degree in terms of total degree K and difference Δ_κ:")
    
    kappa_in_expr = (K + Delta_kappa) / 2
    kappa_out_expr = (K - Delta_kappa) / 2
    
    print(f"κ_in = (K + Δ_κ)/2 = {kappa_in_expr}")
    print(f"κ_out = (K - Δ_κ)/2 = {kappa_out_expr}")
    print(f"Verification: κ_in + κ_out = {simplify(kappa_in_expr + kappa_out_expr)} = K ✓")
    print(f"Verification: κ_in - κ_out = {simplify(kappa_in_expr - kappa_out_expr)} = Δ_κ ✓")
    
    # Step 3: Second moments of weights
    print_step(3, "SECOND MOMENTS OF WEIGHTS")
    print("For the second-order polynomial family, edge weight second moments are:")
    print("⟨w²⟩ = α₀ + α₁⟨w⟩ + α₂⟨w⟩²")
    
    w_in_squared = alpha_0 + alpha_1 * w_in_mean + alpha_2 * w_in_mean**2
    w_out_squared = alpha_0 + alpha_1 * w_out_mean + alpha_2 * w_out_mean**2
    
    print(f"⟨w²_in⟩ = α₀ + α₁(Ω/2) + α₂(Ω/2)² = {expand(w_in_squared)}")
    print(f"⟨w²_out⟩ = α₀ + α₁(Ω/2) + α₂(Ω/2)² = {expand(w_out_squared)}")
    
    # Since weights are homogeneous, both second moments are equal
    print(f"Since weights are homogeneous: ⟨w²_in⟩ = ⟨w²_out⟩ = {expand(w_in_squared)}")
    
    # Step 4: General eigenvalue formula
    print_step(4, "GENERAL EIGENVALUE FORMULA")
    print("Starting from the general formula (Eq. λ_dirac_moment in appendix):")
    print("λ = κ_in⟨w_in⟩ - κ_out⟨w_out⟩ + (κ_in⟨w²_in⟩ + κ_out⟨w²_out⟩)/(κ_in⟨w_in⟩ - κ_out⟨w_out⟩)")
    
    # Substitute our expressions
    numerator = kappa_in_expr * w_in_squared + kappa_out_expr * w_out_squared
    denominator = kappa_in_expr * w_in_mean - kappa_out_expr * w_out_mean
    
    lambda_general = denominator + numerator / denominator
    
    print_step(5, "SUBSTITUTE HOMOGENEOUS WEIGHT CONDITIONS")
    print("Substituting our expressions:")
    print(f"Numerator = κ_in⟨w²_in⟩ + κ_out⟨w²_out⟩")
    print(f"         = {kappa_in_expr} × {expand(w_in_squared)} + {kappa_out_expr} × {expand(w_out_squared)}")
    
    # Since w_in_squared = w_out_squared under homogeneous conditions
    common_second_moment = expand(w_in_squared)
    numerator_simplified = (kappa_in_expr + kappa_out_expr) * common_second_moment
    numerator_simplified = simplify(numerator_simplified)
    
    print(f"         = ({kappa_in_expr} + {kappa_out_expr}) × {common_second_moment}")
    print(f"         = K × {common_second_moment}")
    print(f"         = {expand(numerator_simplified)}")
    
    print(f"\nDenominator = κ_in⟨w_in⟩ - κ_out⟨w_out⟩")
    print(f"            = {kappa_in_expr} × {w_in_mean} - {kappa_out_expr} × {w_out_mean}")
    print(f"            = {simplify(denominator)}")
    
    # Step 6: Simplify the eigenvalue expression
    print_step(6, "SIMPLIFY EIGENVALUE EXPRESSION")
    
    # The denominator becomes
    denom_simplified = simplify(denominator)
    print(f"Denominator = {denom_simplified}")
    
    # The first term
    first_term = denom_simplified
    print(f"First term: {first_term}")
    
    # The second term (fraction)
    second_term = numerator_simplified / denom_simplified
    second_term_simplified = simplify(second_term)
    print(f"Second term: {numerator_simplified} / {denom_simplified}")
    print(f"           = {second_term_simplified}")
    
    # Complete expression
    lambda_expr = first_term + second_term_simplified
    lambda_final = simplify(lambda_expr)
    
    print_step(7, "EXPAND AND COLLECT TERMS")
    
    # Let's work with the second moment expression more carefully
    # ⟨w²⟩ = α₀ + α₁(Ω/2) + α₂(Ω²/4)
    second_moment_expanded = alpha_0 + alpha_1 * Omega/2 + alpha_2 * Omega**2/4
    
    # Numerator = K × (α₀ + α₁Ω/2 + α₂Ω²/4)
    num_expanded = K * second_moment_expanded
    num_expanded = expand(num_expanded)
    
    print(f"Numerator = K × [α₀ + α₁Ω/2 + α₂Ω²/4]")
    print(f"         = {num_expanded}")
    
    # Denominator = Δ_κ × Ω/2
    denom_final = Delta_kappa * Omega / 2
    
    print(f"Denominator = Δ_κ × Ω/2 = {denom_final}")
    
    # Second term = Numerator/Denominator
    second_term_final = num_expanded / denom_final
    second_term_final = simplify(second_term_final)
    
    print(f"Second term = {num_expanded} / {denom_final}")
    print(f"           = {second_term_final}")
    
    # Complete eigenvalue
    lambda_complete = denom_final + second_term_final
    lambda_complete = simplify(lambda_complete)
    
    print_step(8, "FINAL EIGENVALUE EXPRESSION")
    print(f"λ = {denom_final} + {second_term_final}")
    print(f"  = {lambda_complete}")
    
    # Step 9: Factor out and rearrange to target form
    print_step(9, "REARRANGE TO TARGET FORM")
    
    # Let's manually construct the target form
    # We want: λ = (Δ_κ/2)Ω + (1/Δ_κ) × (KC)/(2Ω)
    # where C = 4α₀ + 2Ωα₁ + Ω²α₂
    
    C = 4*alpha_0 + 2*Omega*alpha_1 + Omega**2*alpha_2
    print(f"Define C = 4α₀ + 2Ωα₁ + Ω²α₂ = {C}")
    
    # First term of target form
    term1_target = Delta_kappa * Omega / 2
    print(f"First term: (Δ_κ/2)Ω = {term1_target}")
    
    # Second term of target form  
    term2_target = (K * C) / (Delta_kappa * 2 * Omega)
    print(f"Second term: (1/Δ_κ) × (KC)/(2Ω) = {term2_target}")
    
    # Complete target form
    lambda_target = term1_target + term2_target
    lambda_target = simplify(lambda_target)
    
    print(f"Target form: λ = {lambda_target}")
    
    # Step 10: Verify equivalence
    print_step(10, "VERIFY EQUIVALENCE")
    
    # Let's expand C and substitute back
    C_expanded = expand(C)
    print(f"C = {C_expanded}")
    
    # Substitute C into the second term
    term2_with_C = (K * C_expanded) / (Delta_kappa * 2 * Omega)
    term2_with_C = expand(term2_with_C)
    
    print(f"Second term with C expanded:")
    print(f"(KC)/(2ΩΔ_κ) = K(4α₀ + 2Ωα₁ + Ω²α₂)/(2ΩΔ_κ)")
    print(f"              = (4Kα₀ + 2KΩα₁ + KΩ²α₂)/(2ΩΔ_κ)")
    print(f"              = (2Kα₀)/ΩΔ_κ + (Kα₁)/Δ_κ + (KΩα₂)/(2Δ_κ)")
    
    # This should match our derived expression
    our_second_term = second_term_final
    print(f"\nOur derived second term: {our_second_term}")
    
    # Simplify and compare
    difference = simplify(term2_with_C - our_second_term)
    print(f"Difference: {difference}")
    
    if difference == 0:
        print("✓ VERIFICATION SUCCESSFUL: Both forms are equivalent!")
    else:
        print("⚠ Need to check algebra...")
        
    # Final result
    print_step(11, "FINAL RESULT")
    print("The eigenvalue for homogeneous weights is:")
    print(f"λ = (Δ_κ/2)Ω + (1/Δ_κ) × (KC)/(2Ω)")
    print(f"where C = 4α₀ + 2Ωα₁ + Ω²α₂")
    
    print("\nThis is equation (eq:lambda_moment_homogeneous_weights) in the paper.")
    
    # Step 12: Physical interpretation
    print_step(12, "PHYSICAL INTERPRETATION")
    print("• First term (Δ_κ/2)Ω: Contribution from degree heterogeneity")
    print("  - Linear in degree difference Δ_κ")
    print("  - Proportional to total average weight Ω")
    print("• Second term (KC)/(2ΩΔ_κ): Contribution from weight variance")
    print("  - Inversely proportional to degree difference (1/Δ_κ)")
    print("  - Contains weight distribution information through C")
    print("• The non-monotonic behavior comes from the opposing trends of these terms")

if __name__ == "__main__":
    main()