# Generated Figures for Weighted Community Detection Paper

This directory contains figures generated from the theoretical and numerical analysis of detectability thresholds in weighted networks.

## Main Figures (corresponding to paper figures)

### Figure 1: Detectability Thresholds vs Omega
- **figure1_thresholds.pdf**: Theoretical detectability thresholds as functions of average weight Ω
  - Panel (a): δₖ* thresholds for homogeneous weights scenario
  - Panel (b): δ_ω* thresholds for homogeneous topology scenario
  - Shows Dirac, Poisson, and Exponential distributions

### Figure 2: Homogeneous Weights Scenario (δₖ experiments)
- **figure2_delta_k_Omega1.pdf**: Results for Ω=1
- **figure2_delta_k_Omega10.pdf**: Results for Ω=10  
- **figure2_delta_k_Omega100.pdf**: Results for Ω=100
- Each plot shows:
  - Panel (a): Largest eigenvalue λ vs δₖ with theoretical curves and empirical data
  - Panel (b): Order parameter P vs δₖ showing detectability transition
  - Vertical dotted lines mark theoretical thresholds

### Figure 3: Homogeneous Topology Scenario (δ_ω experiments)
- **figure3_delta_w_Omega1.pdf**: Results for Ω=1
- **figure3_delta_w_Omega2.pdf**: Results for Ω=2
- **figure3_delta_w_Omega4.pdf**: Results for Ω=4
- Each plot shows:
  - Panel (a): Largest eigenvalue λ vs δ_ω with theoretical curves and empirical data
  - Panel (b): Order parameter P vs δ_ω showing detectability transition
  - Vertical dotted lines mark theoretical thresholds

## Additional Distribution Figures

### Geometric Distribution
- **figure_geometric_delta_k_Omega[2,4,10].pdf**: δₖ experiments for geometric weights
- **figure_geometric_delta_w_Omega[2,4].pdf**: δ_ω experiments for geometric weights
- Valid for Ω ≥ 2 (since geometric distribution requires w ≥ 1)

### Sign Distribution  
- **figure_sign_delta_k_Omega[0.5,1].pdf**: δₖ experiments for sign weights
- **figure_sign_delta_w_Omega[0.5,1].pdf**: δ_ω experiments for sign weights
- Valid for Ω ≤ 2 (since sign distribution requires w ∈ [-1,1])

## Summary Figure
- **summary_theoretical_predictions.pdf**: Comprehensive 2×3 panel overview showing:
  - Theoretical thresholds vs Ω for both scenarios
  - λ vs δₖ curves for representative Ω values
  - λ vs δ_ω curves for representative Ω values

## Color Coding
- **Red**: Dirac distribution (deterministic weights)
- **Black**: Poisson distribution (count-based weights)
- **Blue**: Exponential distribution (maximum entropy)
- **Green**: Geometric distribution (over-dispersed counts)
- **Purple**: Sign distribution (±1 weights)

## Key Theoretical Results Demonstrated

1. **Dirac distribution** provides the easiest detection (lowest thresholds)
2. **Exponential distribution** threshold is √2 times larger than Dirac
3. **Poisson distribution** threshold depends on Ω, approaching Dirac for large Ω
4. **Geometric distribution** threshold approaches exponential from below as Ω increases
5. **Sign distribution** shows unique behavior with threshold inversely related to sign imbalance

All figures validate the theoretical predictions from the paper equations, showing excellent agreement between theory (solid lines) and numerical simulations (data points with error bars).