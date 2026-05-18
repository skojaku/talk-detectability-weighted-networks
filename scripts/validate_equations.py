

import sympy

def validate_equations():
    """
    Uses SymPy to validate the key equations in main.tex.
    """
    # Define symbolic variables
    # Moments of degree distributions
    k_in, k_out, k_in_sq, k_out_sq = sympy.symbols('k_in,k_out,k_in_sq,k_out_sq')
    # Moments of weight distributions
    w_in, w_out, w_in_sq, w_out_sq = sympy.symbols('w_in,w_out,w_in_sq,w_out_sq')
    # Moments of strength distributions
    s_in, s_out, s_in_sq, s_out_sq = sympy.symbols('s_in,s_out,s_in_sq,s_out_sq')
    # Strength difference
    Delta_s, Delta_s_sq = sympy.symbols('Delta_s,Delta_s_sq')
    # Parameters for specific cases
    K, Delta_k, W, Delta_w = sympy.symbols('K,Delta_k,W,Delta_w')
    alpha_0, alpha_1, alpha_2 = sympy.symbols('alpha_0,alpha_1,alpha_2')
    C = sympy.symbols('C')
    lambda_sym = sympy.symbols(r'\lambda')

    print("--- Validation Report ---")

    # --- Step 1: Validate moments of strength and strength-differential (Eqs. 9, 10, 11, 12) ---
    print("\n[Step 1] Validating moments of strength distributions...")

    # Theoretical expressions from the paper
    s_in_expr = w_in * k_in
    s_out_expr = w_out * k_out
    s_in_sq_expr = w_in_sq * k_in + w_in**2 * (k_in_sq - k_in)
    s_out_sq_expr = w_out_sq * k_out + w_out**2 * (k_out_sq - k_out)

    Delta_s_expr = s_in_expr - s_out_expr
    Delta_s_sq_expr = s_in_sq_expr - 2 * s_in_expr * s_out_expr + s_out_sq_expr

    # These are definitions, but we can print them to show the setup
    print(f"Eq. (11) <s_in>: {s_in_expr}")
    print(f"Eq. (12) <s_in^2>: {s_in_sq_expr}")
    print(f"Eq. (9) <Delta_s>: {Delta_s_expr}")
    print(f"Eq. (10) <Delta_s^2>: {Delta_s_sq_expr}")
    print("Step 1: Expressions match the paper's definitions.")

    # --- Step 2: Validate simplified strength moment for Poisson degrees (Eq. 15) ---
    print("\n[Step 2] Validating simplified second moment for Poisson degrees (Eq. 15)...")
    # For Poisson/Binomial degrees, var(k) = E[k], so k_in_sq = k_in**2 + k_in
    s_in_sq_poisson_expr = s_in_sq_expr.subs(k_in_sq, k_in**2 + k_in)
    s_in_sq_poisson_simplified = sympy.simplify(s_in_sq_poisson_expr)

    paper_s_in_sq_poisson = w_in_sq * k_in + w_in**2 * k_in**2
    print(f"Derived expression for <s_in^2> with Poisson degrees: {s_in_sq_poisson_simplified}")
    print(f"Paper's expression (Eq. 15): {paper_s_in_sq_poisson}")
    assert sympy.simplify(s_in_sq_poisson_simplified - paper_s_in_sq_poisson) == 0
    print("Step 2: Validation successful. The simplified expression is correct.")

    # --- Step 3: Validate main eigenvalue equation (Eq. 16) ---
    print("\n[Step 3] Validating main eigenvalue equation (Eq. 16)...")
    # The paper states lambda = <Delta_s^2> / <Delta_s>
    # Let's use the simplified Poisson-degree moments
    s_in_sq_poisson = w_in_sq * k_in + w_in**2 * k_in**2
    s_out_sq_poisson = w_out_sq * k_out + w_out**2 * k_out**2
    
    Delta_s_poisson_expr = s_in_expr - s_out_expr
    Delta_s_sq_poisson_expr = s_in_sq_poisson - 2 * s_in_expr * s_out_expr + s_out_sq_poisson
    
    lambda_derived_expr = Delta_s_sq_poisson_expr / Delta_s_poisson_expr
    lambda_derived_simplified = sympy.simplify(lambda_derived_expr)
    
    # The paper simplifies this as:
    # (s_in - s_out)^2 / (s_in - s_out) + (k_in*w_in_sq + k_out*w_out_sq) / (s_in - s_out)
    # = (s_in - s_out) + (k_in*w_in_sq + k_out*w_out_sq) / (s_in - s_out)
    paper_lambda_expr = (s_in_expr - s_out_expr) + (k_in * w_in_sq + k_out * w_out_sq) / (s_in_expr - s_out_expr)
    
    print(f"Derived lambda: {lambda_derived_simplified}")
    print(f"Paper's lambda (Eq. 16): {paper_lambda_expr.subs([(s_in, s_in_expr), (s_out, s_out_expr)])}")
    assert sympy.simplify(lambda_derived_simplified - paper_lambda_expr.subs([(s_in, s_in_expr), (s_out, s_out_expr)])) == 0
    print("Step 3: Validation successful. The main eigenvalue expression is correct.")

    # --- Step 4a: Homogeneous Weights (structure in topology) ---
    print("\n[Step 4a] Validating case with homogeneous weights (Eqs. 19, 22)...")
    # Conditions: w_in = w_out = W/2
    # k_in = (K+Delta_k)/2, k_out = (K-Delta_k)/2
    # w_in_sq = w_out_sq = alpha_0 + alpha_1*(W/2) + alpha_2*(W/2)**2
    
    w_in_hom = W/2
    w_out_hom = W/2
    k_in_hom = (K + Delta_k) / 2
    k_out_hom = (K - Delta_k) / 2
    
    # From Eq. (17), C = 4*alpha_0 + 2*W*alpha_1 + W**2*alpha_2
    # So, w_sq_hom = C / 4
    w_sq_hom = C / 4
    
    lambda_hom_w_derived = paper_lambda_expr.subs([
        (w_in, w_in_hom), (w_out, w_out_hom),
        (k_in, k_in_hom), (k_out, k_out_hom),
        (w_in_sq, w_sq_hom), (w_out_sq, w_sq_hom)
    ])
    lambda_hom_w_derived_simplified = sympy.simplify(lambda_hom_w_derived)

    paper_lambda_hom_w = (W/2)*Delta_k + (K*C)/(2*W*Delta_k)
    print(f"Derived lambda (homogeneous weights): {lambda_hom_w_derived_simplified}")
    print(f"Paper's lambda (Eq. 19): {paper_lambda_hom_w}")
    assert sympy.simplify(lambda_hom_w_derived_simplified - paper_lambda_hom_w) == 0
    print("Eq. (19) for lambda is correct.")

    # Validate detectability threshold
    deriv_lambda_hom_w = sympy.diff(paper_lambda_hom_w, Delta_k)
    threshold_sol = sympy.solve(deriv_lambda_hom_w, Delta_k)
    # solve returns two solutions, we take the positive one
    derived_threshold_k = threshold_sol[1] 

    paper_threshold_k = sympy.sqrt(K*C)/W
    print(f"Derived threshold Delta_k*: {derived_threshold_k}")
    print(f"Paper's threshold (Eq. 22): {paper_threshold_k}")
    assert sympy.simplify(derived_threshold_k - paper_threshold_k) == 0
    print("Eq. (22) for threshold Delta_k* is correct.")
    print("Step 4a: Validation successful.")

    # --- Step 4b: Homogeneous Topology (structure in weights) ---
    print("\n[Step 4b] Validating case with homogeneous topology (Eqs. 23, 24)...")
    # Conditions: k_in = k_out = K/2
    # w_in = (W+Delta_w)/2, w_out = (W-Delta_w)/2
    k_hom_t = K/2
    w_in_hom_t = (W + Delta_w) / 2
    w_out_hom_t = (W - Delta_w) / 2
    
    w_in_sq_hom_t = alpha_0 + alpha_1*w_in_hom_t + alpha_2*w_in_hom_t**2
    w_out_sq_hom_t = alpha_0 + alpha_1*w_out_hom_t + alpha_2*w_out_hom_t**2

    lambda_hom_t_derived = paper_lambda_expr.subs([
        (k_in, k_hom_t), (k_out, k_hom_t),
        (w_in, w_in_hom_t), (w_out, w_out_hom_t),
        (w_in_sq, w_in_sq_hom_t), (w_out_sq, w_out_sq_hom_t)
    ])
    lambda_hom_t_derived_simplified = sympy.simplify(lambda_hom_t_derived)

    # Paper's expression uses C = 4*alpha_0 + 2*W*alpha_1 + W**2*alpha_2
    paper_lambda_hom_t = (Delta_w/2)*(K + alpha_2) + C/(2*Delta_w)
    
    # To check equivalence, we must substitute C into the paper's expression
    paper_lambda_hom_t_expanded = paper_lambda_hom_t.subs(C, 4*alpha_0 + 2*W*alpha_1 + W**2*alpha_2)
    
    print(f"Derived lambda (homogeneous topology): {lambda_hom_t_derived_simplified}")
    print(f"Paper's lambda (Eq. 23, expanded): {sympy.simplify(paper_lambda_hom_t_expanded)}")
    assert sympy.simplify(lambda_hom_t_derived_simplified - paper_lambda_hom_t_expanded) == 0
    print("Eq. (23) for lambda is correct.")

    # Validate detectability threshold
    deriv_lambda_hom_t = sympy.diff(paper_lambda_hom_t, Delta_w)
    threshold_sol_w = sympy.solve(deriv_lambda_hom_t, Delta_w)
    derived_threshold_w = threshold_sol_w[1] # Positive solution

    paper_threshold_w = sympy.sqrt(C / (K + alpha_2))
    print(f"Derived threshold Delta_w*: {derived_threshold_w}")
    print(f"Paper's threshold (Eq. 24): {paper_threshold_w}")
    assert sympy.simplify(derived_threshold_w - paper_threshold_w) == 0
    print("Eq. (24) for threshold Delta_w* is correct.")
    print("Step 4b: Validation successful.")

    print("\n--- All validations completed successfully. ---")

if __name__ == '__main__':
    validate_equations()

