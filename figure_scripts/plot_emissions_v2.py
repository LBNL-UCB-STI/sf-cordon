"""
Figure 11: Emission changes by geographic area.
Three-panel figure for journal submission.
Based on AQ_Analysis.ipynb (create_separate_emissions_plots).
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Journal formatting ---
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 10,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 8,
    'figure.dpi': 300,
})

GEO_LEVELS = ['Cordon', 'SF', 'Neither-Cordon-nor-SF']
GEO_LABELS = {
    'Cordon': 'Cordon',
    'SF': 'Rest of San Francisco',
    'Neither-Cordon-nor-SF': 'Rest of Bay Area',
}
EMISSIONS_COLS = [
    'tons_per_year_ROG', 'tons_per_year_NOx', 'tons_per_year_NH3',
    'tons_per_year_SOx', 'tons_per_year_PM2_5', 'tons_per_year_CO2',
]
EMISSIONS_NAMES = {
    'tons_per_year_ROG': 'ROG', 'tons_per_year_NOx': 'NOx',
    'tons_per_year_NH3': 'NH3', 'tons_per_year_SOx': 'SOx',
    'tons_per_year_PM2_5': 'PM2.5', 'tons_per_year_CO2': 'CO2',
}
FLAT_COLOR = '#ff7f0e'
INCOME_COLOR = '#2ca02c'


def main():
    income_pct_df = pd.read_csv('data/income_vs_baseline_pct_summary.csv', index_col=0)
    flat_pct_df = pd.read_csv('data/flat_vs_baseline_pct_summary.csv', index_col=0)

    pollutants = [EMISSIONS_NAMES[c] for c in EMISSIONS_COLS]
    x = np.arange(len(pollutants))
    bar_width = 0.35

    fig, axes = plt.subplots(1, 3, figsize=(7.09, 3.0), sharey=True)

    for i, geo_level in enumerate(GEO_LEVELS):
        ax = axes[i]
        flat_vals = [flat_pct_df.loc[geo_level, col] for col in EMISSIONS_COLS]
        income_vals = [income_pct_df.loc[geo_level, col] for col in EMISSIONS_COLS]

        ax.bar(x, flat_vals, bar_width, label='flat', color=FLAT_COLOR)
        ax.bar(x + bar_width, income_vals, bar_width, label='income-based',
               color=INCOME_COLOR)

        label = chr(ord('a') + i)
        ax.set_title(f'{label}) {GEO_LABELS[geo_level]}', loc='left',
                     fontweight='bold')
        ax.set_xticks(x + bar_width / 2)
        ax.set_xticklabels(pollutants, rotation=45, ha='right')
        ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        ax.set_facecolor('white')

    axes[0].set_ylabel('Change from Baseline (%)')

    # Shared legend in rightmost panel
    handles, labels = axes[0].get_legend_handles_labels()
    axes[2].legend(handles, labels, loc='lower left', title='Scenario')

    plt.tight_layout()

    for ext in ['pdf', 'tiff']:
        fig.savefig(f'Figure_11.{ext}', dpi=300, bbox_inches='tight', facecolor='white')
        print(f'Saved: Figure_11.{ext}')
    plt.close()


if __name__ == '__main__':
    main()
