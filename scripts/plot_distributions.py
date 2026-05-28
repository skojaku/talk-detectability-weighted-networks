"""Plot weight distributions with the same mean W for the talk slide."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, expon, geom

W = 4  # common mean

fig, ax = plt.subplots(1, 1, figsize=(8, 8))

from scipy.special import gamma as gammafn

# Dirac delta at W
ax.axvline(W, color="#e74c3c", linewidth=3, label=f"Dirac ($w = {W}$)", zorder=5)

# Poisson (mean = W) — supported on [0, ∞)
x_poisson = np.linspace(0, 15, 500)
pdf_poisson = np.exp(x_poisson * np.log(W) - W - np.log(gammafn(x_poisson + 1)))
ax.plot(x_poisson, pdf_poisson, color="#2c3e50", linewidth=2.5, label=f"Poisson ($\\mu = {W}$)", zorder=3)

# Exponential (mean = W) — supported on [0, ∞)
x_exp = np.linspace(0, 15, 500)
pdf_exp = expon.pdf(x_exp, scale=W)
ax.plot(x_exp, pdf_exp, color="#2980b9", linewidth=2.5, label=f"Exponential ($\\mu = {W}$)", zorder=4)

# Geometric (mean = W) — supported on [1, ∞)
p_geom = 1.0 / W
x_geom = np.linspace(1, 15, 500)
pdf_geom = p_geom * (1 - p_geom) ** (x_geom - 1)
ax.plot(x_geom, pdf_geom, color="#e67e22", linewidth=2.5, label=f"Geometric ($\\mu = {W}$)", zorder=3)

# Signed Bernoulli: w ∈ {-1, +1} with P(+1) = (W+1)/2, P(-1) = (1-W)/2...
# Only works for |W| ≤ 1, so use W=0.5 variant or skip.
# For W=4, Signed Bernoulli doesn't apply naturally. Show it conceptually with
# w ∈ {-W, +W} each with prob 0.5 → mean 0, not W.
# Actually signed Bernoulli in paper: w ∈ {-1, +1}. Mean = p(+1) - p(-1).
# This only gives mean in [-1, 1]. Skip for this plot since W=4.

ax.axvline(W, color="gray", linewidth=0.8, linestyle="--", alpha=0.5, zorder=1)
ax.annotate(f"mean $= {W}$", xy=(W, 0.25),
            xytext=(W + 2, 0.28), fontsize=14, color="gray",
            arrowprops=dict(arrowstyle="->", color="gray", lw=1.2))

ax.set_xlabel("Weight $w$", fontsize=16)
ax.set_ylabel("Probability", fontsize=16)
ax.set_xlim(-0.5, 15)
ax.set_ylim(0, 0.38)
ax.legend(fontsize=13, loc="upper right", framealpha=0.9)
ax.tick_params(labelsize=13)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig("figs/distributions_same_mean.png", dpi=200, bbox_inches="tight", facecolor="white")
print("Saved figs/distributions_same_mean.png")
