import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])) # lets the script find config.py

import matplotlib.pyplot as plt
import numpy as np

import config
import tools

N_SAMPLE = 500_000 # a sample is enough to see the shapes; raise it if you like

d = tools.load("down", entry_stop=N_SAMPLE)
config.FIG_DIR.mkdir(exist_ok=True)

# histogram
for var in tools.TRACK_VARS:
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.hist(d[f"H1_{var}"], bins=100)
    ax.set_xlabel(f"H1_{var}")
    ax.set_ylabel("Candidates")
    fig.tight_layout()
    fig.savefig(config.FIG_DIR / f"01_H1_{var}.pdf")
    plt.close(fig)


# 2. Three-kaon invariant mass with no selection at all
mass = tools.three_body_mass(d)
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(mass, bins=tools.mass_edges(), histtype="step")
ax.set_xlabel(r"$m(K^+K^-K^\pm)$ [MeV/$c^2$]")
ax.set_ylabel(f"Candidates per {config.MASS_BIN} MeV/$c^2$")
fig.tight_layout()
fig.savefig(config.FIG_DIR / "01_mass_no_selection.pdf")

charge_ok = np.mean(np.abs(tools.b_charge(d)) == 1)
print(f"Read {len(mass)} candidates; fraction with total charge +/-1: {charge_ok:.3f}")