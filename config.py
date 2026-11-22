from pathlib import Path
ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
RESULTS_DIR = ROOT / "results"


FILES = {"down": DATA_DIR / "B2HHH_MagnetDown.root", "up": DATA_DIR / "B2HHH_MagnetUp.root"}
TREE = "DecayTree"
SELECTED_FILE = DATA_DIR / "selected.npz" 


M_K = 493.677 # MeVc^-2


MASS_RANGE = (4800, 6000)
MASS_BIN = 10

PROBK_MIN = 0.5
PROBPI_MAX = 0.2

