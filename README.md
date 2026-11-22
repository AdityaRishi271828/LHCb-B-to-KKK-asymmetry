# LHCb-B-to-KKK-asymmetry
Measuring the asymmetry between the decay rates of B+ and B- decays using LHCb data


Raw charge asymmetry: **A = (N⁻ − N⁺)/(N⁻ + N⁺) = −0.049 ± 0.012** (statistical uncertainty only), 4.3 standard deviations from zero, from 8 057 ± 92 background-subtracted signal decays (4 226 B⁺ and 3 831 B⁻).
 This is a raw asymmetry: it has not been corrected for the B± production asymmetry or the kaon detection asymmetry, so it is not a direct measurement of CP violation. 

The data is not included in this repository. Download B2HHH_MagnetDown.root and B2HHH_MagnetUp.root from https://opendata.cern.ch/record/4900 and place them in data/ 


Python 3.15.2 was used. From the top folder:
 
```
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```


Run the scripts in order from the top folder:
 
| Script | What it does | Outputs |
| --- | --- | --- |
| `python src/01_explore.py` | Plots the raw variables and unselected mass | `figures/01_*.pdf` |
| `python src/02_select.py` | Applies the kaon selection | `results/02_cutflow.txt`, `figures/02_mass_selected.pdf`, `data/selected.npz` |
| `python src/03_mass_peak.py` | Defines the signal window and sidebands | `results/03_regions.txt`, `figures/03_mass_regions.pdf` |
| `python src/04_asymmetry.py` | Measures the asymmetry and its significance | `results/04_asymmetry.txt`, `figures/04_mass_by_charge.pdf` |
| `python src/05_checks.py` | Polarity, sideband, selection and window checks | `results/05_checks.txt` |


All analysis choices (cuts, mass windows, significance level) are in `config.py`. They were fixed before the asymmetry was examined; see the `selection-fixed` tag.


Repository Layout:
```
config.py       analysis settings
src/            analysis scripts and shared functions (tools.py)
notebooks/      exploratory notebooks
figures/        plots produced by the scripts
results/        numerical results produced by the scripts
writeup/        working notes
```

Code released under the MIT licence. The LHCb data are provided by CERN under the terms stated on the Open Data portal.
 