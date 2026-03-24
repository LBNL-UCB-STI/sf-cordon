"""
Figure 8: Mode shares by income level - 5 rows x 2 columns
Left: Trips to the cordon. Right: Trips outside the cordon.
Based on plot_mode_shares_by_income_vertical_clean.py (original version).
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

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

COLORS = {'baseline': '#1f77b4', 'flat': '#ff7f0e', 'income-based': '#2ca02c'}
SCENARIOS = ['baseline', 'flat', 'income-based']
MODES = ['Car', 'Transit', 'Ridehail', 'Active']
INCOME_LEVELS = ['Very Low Income', 'Low Income', 'Moderate Income',
                 'Medium Income', 'High Income']


def load_mode_shares(csv_file):
    """Load CSV and convert to 0-1 scale."""
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip()
    df = df.rename(columns={
        'Car %': 'Car', 'Transit %': 'Transit',
        'RideHail %': 'Ridehail', 'Active %': 'Active'
    })
    for col in MODES:
        df[col] = pd.to_numeric(df[col]) / 100.0
    return df


def plot_panel(ax, data, income_level, panel_label=''):
    """Plot a single income-level panel."""
    x = np.arange(len(MODES))
    width = 0.25
    income_data = data[data['Income Level'] == income_level]

    for j, scenario in enumerate(SCENARIOS):
        row = income_data[income_data['Scenario'] == scenario]
        values = row[MODES].values[0]
        ax.bar(x + (j - 1) * width, values, width,
               label=scenario, color=COLORS[scenario])

    ax.set_xticks(x)
    ax.set_xticklabels(MODES)
    ax.set_ylim(0, 0.70)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0, decimals=0))
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_facecolor('white')

    # Panel letter label with white background box
    if panel_label:
        ax.text(0.02, 0.95, panel_label, transform=ax.transAxes,
                fontsize=9, fontweight='bold', va='top', ha='left',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor='none', alpha=0.8))


def main():
    data_cordon = load_mode_shares('rest_of_sf_to_cordon_by_income.csv')
    data_outside = load_mode_shares('within_sf_outside_cordon_by_income.csv')

    # 5 rows x 2 columns, double-column width, tall
    fig, axes = plt.subplots(5, 2, figsize=(7.09, 9.5), sharey=True)

    # Panel labels: a-j, left to right, top to bottom
    LABELS = list('abcdefghij')

    for i, income_level in enumerate(INCOME_LEVELS):
        ax_left = axes[i, 0]
        ax_right = axes[i, 1]

        left_label = f'{LABELS[i * 2]})'
        right_label = f'{LABELS[i * 2 + 1]})'

        plot_panel(ax_left, data_cordon, income_level, panel_label=left_label)
        plot_panel(ax_right, data_outside, income_level, panel_label=right_label)

        # Remove x-tick labels except bottom row
        if i < 4:
            ax_left.set_xticklabels([])
            ax_right.set_xticklabels([])

        # Column headers on top row
        if i == 0:
            ax_left.set_title('Trips to Cordon', fontweight='bold')
            ax_right.set_title('Trips to zones outside Cordon', fontweight='bold')
            # Legend in top-right panel
            handles, labels = ax_right.get_legend_handles_labels()
            ax_right.legend(handles, labels, loc='upper right', title='Scenario')

    # Adjust layout first so positions are final
    fig.subplots_adjust(left=0.15, hspace=0.15, wspace=0.08, bottom=0.05, top=0.95)

    # Income level row labels in the left margin (after layout adjustment)
    for i, income_level in enumerate(INCOME_LEVELS):
        row_center = axes[i, 0].get_position()
        y_center = (row_center.y0 + row_center.y1) / 2
        fig.text(0.01, y_center, income_level, va='center', rotation='vertical',
                 fontsize=9, fontweight='bold')

    # Single centered y-axis label
    fig.text(0.055, 0.5, 'Mode Share (%)', va='center', rotation='vertical', fontsize=10)

    # Single centered x-axis label
    fig.text(0.55, 0.01, 'Mode', ha='center', fontsize=10)

    fig.savefig('Figure_8.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('Figure_8.tiff', dpi=300, bbox_inches='tight', facecolor='white')
    print('Saved: Figure_8.pdf')
    print('Saved: Figure_8.tiff')
    plt.close()


if __name__ == '__main__':
    main()
