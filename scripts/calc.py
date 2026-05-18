# %%
import sympy as sp
import numpy as np

# %% Lambda simple form
import sympy as sp

# The case of omega_in = omega_out = Omega / 2
Omega = sp.Symbol("Omega")
K = sp.Symbol("K")
Delta_omega =  0
Delta_kappa = sp.Symbol("Delta_kappa")

kappa_in = (K + Delta_kappa) / 2
kappa_out = (K - Delta_kappa) / 2
w_in = (Omega + Delta_omega) / 2
w_out = (Omega - Delta_omega) / 2
alpha_0 = sp.Symbol("alpha_0")
alpha_1 = sp.Symbol("alpha_1")
alpha_2 = sp.Symbol("alpha_2")

w_in_squared = alpha_0 + alpha_1 * w_in + alpha_2 * w_in * w_in

w_out_squared = alpha_0 + alpha_1 * w_out + alpha_2 * w_out * w_out

lam = kappa_in * w_in - kappa_out * w_out \
    + (kappa_in * w_in_squared + kappa_out * w_out_squared) \
    / (kappa_in * w_in - kappa_out * w_out)

sol_kappa = sp.solve(sp.diff(lam, Delta_kappa), Delta_kappa)


sp.print_latex(sp.simplify(sol_kappa[1]))

# %%
Delta_omega = sp.Symbol("Delta_omega")
Delta_kappa = 0

lam = kappa_in * w_in - kappa_out * w_out \
    + (kappa_in * w_in_squared + kappa_out * w_out_squared) \
    / (kappa_in * w_in - kappa_out * w_out)

sol_omega = sp.solve(sp.diff(lam, Delta_omega), Delta_omega)


sp.print_latex(sp.simplify(sol_omega[1]))