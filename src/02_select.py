import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])) 

import matplotlib.pyplot as plt
import numpy as np

import config
import tools

tools.require("PROBK_MIN", "PROBPI_MAX")

mass, charge, polarity, flow = tools.select(config.PROBK_MIN, config.PROBPI_MAX)
np.savez(config.SELECTED_FILE, mass=mass, charge=charge, polarity=polarity)

# Cut-flow table: how many candidates survive each requirement
total = next(iter(flow.values()))
lines = ["Cut flow, both magnet polarities", ""]
for name, n in flow.items():
    lines.append(f"{name:<32} {n:>10} ({100 * n / total:6.2f}%)")
tools.save_text("02_cutflow.txt", lines)

# Mass distribution after selection, both charges combined
config.FIG_DIR.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(mass, bins=tools.mass_edges(), histtype="step")
ax.set_xlabel(r"$m(K^+K^-K^\pm)$ [MeV/$c^2$]")
ax.set_ylabel(f"Candidates per {config.MASS_BIN} MeV/$c^2$")
fig.tight_layout()
fig.savefig(config.FIG_DIR / "02_mass_selected.pdf")