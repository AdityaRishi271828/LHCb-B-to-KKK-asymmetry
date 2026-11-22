import numpy as np

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1])) 

import uproot
from scipy import stats

import config

TRACKS = (1, 2, 3)
TRACK_VARS = ("PX", "PY", "PZ", "Charge", "ProbK", "ProbPi", "isMuon")
BRANCHES = [f"H{i}_{v}" for i in TRACKS for v in TRACK_VARS]



# Output stuff
def save_text(filename, lines):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    text = "\n".join(lines) + "\n"
    (config.RESULTS_DIR / filename).write_text(text)
    print(text)

def mass_edges():
    lo, hi = config.MASS_RANGE
    return np.arange(lo, hi + config.MASS_BIN, config.MASS_BIN)

def _has_none(value):
    if value is None:
        return True
    if isinstance(value, dict):
        return any(_has_none(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return any(_has_none(v) for v in value)
    return False

def require(*names):
    missing = [name for name in names if _has_none(getattr(config, name))]
    if missing:
        raise SystemExit("Fill in these settings in config.py first: " + ", ".join(missing))

def shade_regions(ax):
    ax.axvspan(*config.SIGNAL_WINDOW, color="tab:green", alpha=0.15, label="Signal window")
    for k, sb in enumerate(config.SIDEBANDS):
        ax.axvspan(*sb, color="grey", alpha=0.2, label="Sidebands" if k == 0 else None)


# Reading Data
def load(polarity, entry_stop=None, branches=BRANCHES):
    with uproot.open(str(config.FILES[polarity])) as f:
        return f[config.TREE].arrays(branches, entry_stop=entry_stop, library="np")

def iterate(polarity, step_size="100 MB", branches=BRANCHES):
    path = str(config.FILES[polarity]) + ":" + config.TREE
    yield from uproot.iterate(path, branches, step_size=step_size, library="np")



# Energy
def energy(PX, PY, PZ, m):
    return np.sqrt(PX**2 + PY**2 + PZ**2 + m**2)

def three_body_mass(d, m=config.M_K):
    E = sum(energy(d[f"H{i}_PX"], d[f"H{i}_PY"], d[f"H{i}_PZ"], m) for i in TRACKS)
    px = sum(d[f"H{i}_PX"] for i in TRACKS)
    py = sum(d[f"H{i}_PY"] for i in TRACKS)
    pz = sum(d[f"H{i}_PZ"] for i in TRACKS)
    return np.sqrt(np.maximum(E**2 - px**2 - py**2 - pz**2, 0.0))

def b_charge(d):
    return d["H1_Charge"] + d["H2_Charge"] + d["H3_Charge"]


# Selecting
def cut_flow_masks(d, probk_min, probpi_max):
    keep = np.ones(len(d["H1_PX"]), dtype=bool)
    steps = {"All candidates": keep.copy()}
    keep &= np.abs(b_charge(d)) == 1
    steps["Total charge is +1 or -1"] = keep.copy()
    
    for i in TRACKS:
        keep &= d[f"H{i}_isMuon"] == 0
    steps["No track identified as a muon"] = keep.copy()

    for i in TRACKS:
        keep &= d[f"H{i}_ProbK"] > probk_min
    steps[f"All three ProbK > {probk_min}"] = keep.copy()
    
    for i in TRACKS:
        keep &= d[f"H{i}_ProbPi"] < probpi_max
    steps[f"All three ProbPi < {probpi_max}"] = keep.copy()
    return steps

def select(probk_min, probpi_max):
    masses, charges, pols = [], [], []
    flow = {}
    for pol_code, pol in ((-1, "down"), (+1, "up")):
        for chunk in iterate(pol):
            steps = cut_flow_masks(chunk, probk_min, probpi_max)
            for name, mask in steps.items():
                flow[name] = flow.get(name, 0) + int(mask.sum())
            keep = list(steps.values())[-1]
            sel = {k: v[keep] for k, v in chunk.items()}
            masses.append(three_body_mass(sel))
            charges.append(b_charge(sel))
            pols.append(np.full(int(keep.sum()), pol_code))
    return np.concatenate(masses), np.concatenate(charges), np.concatenate(pols), flow

def load_selected():
    s = np.load(config.SELECTED_FILE)
    return s["mass"], s["charge"], s["polarity"]