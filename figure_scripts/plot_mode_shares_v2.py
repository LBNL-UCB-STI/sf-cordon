"""
Figure 7: Mode share comparison - trips to cordon vs trips outside cordon
Two-panel figure (side by side) for journal submission.
Based on plot_mode_shares.py (original version).
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
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

# Keep original color scheme (default seaborn/matplotlib blue, orange, green)
COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c']
SCENARIO_ORDER = ['baseline', 'flat', 'income-based']
MODE_ORDER = ['Car', 'Transit', 'Ridehail', 'Active']


def load_and_prepare(csv_file):
    """Load CSV and reshape for plotting."""
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip()
    for col in ['Car %', 'Transit %', 'RideHail %', 'Active %']:
        df[col] = pd.to_numeric(df[col]) / 100.0

    df_plot = df.melt(
        id_vars=['Scenario'],
        value_vars=['Car %', 'Transit %', 'RideHail %', 'Active %'],
        var_name='Mode',
        value_name='Share'
    )
    df_plot['Mode'] = df_plot['Mode'].str.replace(' %', '')
    df_plot['Mode'] = df_plot['Mode'].str.replace('RideHail', 'Ridehail')
    return df_plot


def plot_panel(ax, df_plot, title):
    """Plot a single mode share panel."""
    bar_width = 0.25
    x = np.arange(len(MODE_ORDER))

    for i, scenario in enumerate(SCENARIO_ORDER):
        subset = df_plot[df_plot['Scenario'] == scenario]
        # Ensure mode order
        values = []
        for mode in MODE_ORDER:
            val = subset[subset['Mode'] == mode]['Share'].values
            values.append(val[0] if len(val) > 0 else 0)
        ax.bar(x + i * bar_width, values, bar_width,
               label=scenario, color=COLORS[i])

    ax.set_xticks(x + bar_width)
    ax.set_xticklabels(MODE_ORDER)
    ax.set_xlabel('')
    ax.set_ylabel('Mode Share (%)')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0, decimals=0))
    ax.set_ylim(0, 0.70)
    ax.set_title(title, loc='left', fontweight='bold')
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_facecolor('white')


def main():
    # Load data
    df_cordon = load_and_prepare('sf_to_cordon_mode_share.csv')
    df_nocordon = load_and_prepare('SFNocordon_mode_share_by_scenario.csv')

    # Create two-panel figure
    # Double-column width: ~180mm = 7.09 inches; height ~3.2 inches
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.09, 3.2), sharey=True)

    plot_panel(ax1, df_cordon, 'a) Trips to the cordon')
    plot_panel(ax2, df_nocordon, 'b) Trips outside the cordon')

    # Only show y-label on left panel
    ax2.set_ylabel('')

    # Shared x-axis label centered below both panels
    fig.text(0.5, 0.01, 'Mode', ha='center', fontsize=10)

    # Legend inside panel b) (upper right, where there's space)
    handles, labels = ax1.get_legend_handles_labels()
    ax2.legend(handles, labels, loc='upper right', title='Scenario')

    plt.tight_layout(rect=[0, 0.05, 1, 1])

    # Save as PDF (vector) and TIFF (raster backup)
    fig.savefig('Figure_7.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('Figure_7.tiff', dpi=300, bbox_inches='tight', facecolor='white')
    print('Saved: Figure_7.pdf')
    print('Saved: Figure_7.tiff')

    plt.close()


if __name__ == '__main__':
    main()
