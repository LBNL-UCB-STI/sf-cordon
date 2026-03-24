# Simulating Protective Cordon Pricing to Balance Congestion Management and Affordability in San Francisco

**Authors:** [TO BE ADDED UPON PUBLICATION]

**Contact:** [TO BE ADDED UPON PUBLICATION]

************************************************

**Description:**

This repository contains the data analysis and visualization code for the manuscript "Simulating Protective Cordon Pricing to Balance Congestion Management and Affordability in San Francisco". The study evaluates three pricing scenarios (baseline, flat-rate, and income-based) and their impacts on travel behavior, accessibility, air quality, and other transportation-related outcomes in San Francisco using an agent-based simulation framework coupling ActivitySim and BEAM.

************************************************

**Repository Content:**

- `/primary_outcomes` - Data processing, analysis, and visualization of key metrics (VMT, mode shift, trip counts, cordon entries by time of day)
- `/inexus` - INEXUS (consumer surplus) accessibility analysis and revenue comparison by income segment
- `/air_quality` - Air quality impact analysis (PM2.5, NOx, SOx, emissions by geographic area)
- `/figures` - Final publication figures (Figures 4–12) in PDF format
- `/figure_scripts` - Standalone Python scripts that generate each figure from the processed data

************************************************

**System Requirements & Dependencies:**

- Programming Language: Python 3.10
- Operating System: macOS
- Key libraries/packages:

| Library | Version | License |
|---------|---------|---------|
| pandas | 2.2.3 | BSD 3-Clause |
| NumPy | 1.26.4 | BSD 3-Clause |
| Matplotlib | 3.9.2 | PSF-based (BSD-compatible) |
| seaborn | 0.13.2 | BSD 3-Clause |
| GeoPandas | 1.1.2 | BSD 3-Clause |

************************************************

**Installation:**

- Clone the repository to a local computer with Python installed
- Navigate to the `papers/sf-cordon/` directory
- Install dependencies: `pip install pandas numpy matplotlib seaborn geopandas`
- Ensure the repository's directory structure is maintained, as the analysis scripts rely on relative paths

************************************************

**Notebooks and Their Outputs:**

*Primary Outcomes Analysis*

- **DataProcessing_1.ipynb**: Reads in events and person-to-vehicles files, adds links travelled, time, and passenger data. Adds population characteristics from person and household info, labels scenario, and exports to CSV.
- **DataProcessing_2.ipynb**: Combines data from all scenarios into a unified dataset, calculates income segments, and models revenue generation from cordon pricing schemes.
- **Plots_Cordon.ipynb**: Produces visualizations specific to the cordon area, including mode share comparisons, VMT changes by mode and scenario, trip count differences, and energy use differences with respect to baseline.
- **Plots_SF.ipynb**: Similar to the cordon plots, but focused on impacts across the entire San Francisco area.
- **Plots_SFNoCordon.ipynb**: Analyzes impacts on San Francisco areas outside the cordon.

*INEXUS Analysis*

- **INEXUS_CordonFilter.ipynb**: Analyzes consumer surplus (INEXUS) metrics for trips into and out of the cordon area, including welfare impacts by income segment, revenue generation by scenario, and mode share changes.
- **INEXUS_SFFilter.ipynb**: Similar INEXUS analysis but for trips within the entire San Francisco area.

*Air Quality Analysis*

- **AQ_Analysis.ipynb**: Processes air quality metrics for different scenarios, including particle levels (PM2.5, SOA, NOx, NH3, etc.) and comparison of air quality changes across scenarios and geographic areas.

*Figure Scripts*

Standalone Python scripts that generate the publication figures from processed data:

| Script | Figure |
|--------|--------|
| `plot_cordon_entries_by_time_v2.py` | Figure 4 — Vehicles entering cordon by time of day |
| `plot_vmt_car_cordon_v2.py` | Figure 5 — VMT by car mode (cordon trips) |
| `plot_vmt_car_sfnocordon_v2.py` | Figure 6 — VMT by car mode (outside cordon) |
| `plot_mode_shares_v2.py` | Figure 7 — Mode share by scenario and geography |
| `plot_mode_shares_by_income_vertical_clean_v2.py` | Figure 8 — Mode share by income and geography |
| `plot_inexus_income_segment_v2.py` | Figure 9 — INEXUS impact by income segment |
| `plot_inexus_revenue_v2.py` | Figure 10 — INEXUS losses vs. revenue by income |
| `plot_emissions_v2.py` | Figure 11 — Emission changes by geographic area |
| `add_labels_fig12.py` | Figure 12 — PM2.5 concentration map labels |

Note: Figures 1–3 (cordon zone map, model framework diagram, BEAM architecture) are not code-generated.

************************************************

**Data Description & Availability:**

While the code in this repository can be used to understand the analysis methodology, the full dataset from scenario runs is not included due to size constraints. Key data files available in the repository include:

- Trip counts by mode, scenario, and geographic area
- Vehicle miles traveled (VMT) by mode and scenario
- Vehicle hours traveled (VHT) by mode and scenario
- Air quality impacts (PM2.5, NOx, SOx, etc.)
- INEXUS (consumer surplus) metrics by income segment

For access to the complete dataset, please contact the authors.

************************************************

**How to Cite:**

If you use the data or code from this repository in your research, please cite the following manuscript:

[FULL CITATION TO BE ADDED UPON PUBLICATION]

************************************************

**Other Essential Information and Files:**

*Copyright Notice*

San Francisco Cordon Pricing Study (sf-cordon) Copyright (c) 2026,
The Regents of the University of California, through Lawrence Berkeley
National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software,
please contact Berkeley Lab's Intellectual Property Office at
IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department
of Energy and the U.S. Government consequently retains certain rights.  As
such, the U.S. Government has been granted for itself and others acting on
its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
Software to reproduce, distribute copies to the public, prepare derivative
works, and perform publicly and display publicly, and to permit others to do so.

*License Agreement*

- See the full [LICENSE](LICENSE.md) file.

*Citation*

- CITATION.cff: [TO BE ADDED ONCE CITATION IS AVAILABLE]
