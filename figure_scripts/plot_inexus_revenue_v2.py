"""
Figure 10: INEXUS Impact vs Revenue Collected by income segment.
Two-panel figure (flat / income-based) for journal submission.
Based on INEXUS_SFFilter.ipynb (Cell 49).
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

DATA_DIR = '../primary_outcomes/data'

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

INCOME_ORDER = ['Very Low', 'Low', 'Moderate', 'Middle', 'High']
SCENARIOS = ['flat', 'income-based']
SCENARIO_LABELS = {'flat': 'Flat', 'income-based': 'Income-based'}
INEXUS_COLOR = '#9467bd'   # Purple
REVENUE_COLOR = '#E6BE8A'  # Amber


def millions_formatter(x, pos):
    return f'${x:.0f}M'


def main():
    # Load INEXUS impact data
    inexus_df = pd.read_csv(f'{DATA_DIR}/agg_diff_cache.csv')
    inexus_df = inexus_df[inexus_df['toll'] != 'baseline'].copy()
    inexus_df['aggregated_inexus'] = inexus_df['aggregated_inexus'].abs()

    # Load revenue data
    revenue_df = pd.read_csv(f'{DATA_DIR}/revenue_by_income_segment.csv')
    revenue_df = revenue_df.rename(columns={'scenario': 'toll'})
    revenue_df.loc[revenue_df['income_segment'] == 'Medium', 'income_segment'] = 'Middle'
    revenue_df = revenue_df[
        (revenue_df['toll'] != 'baseline') &
        (revenue_df['income_segment'] != 'Total')
    ]

    fig, axes = plt.subplots(1, 2, figsize=(7.09, 3.2), sharey=True,
                             gridspec_kw={'wspace': 0.08})

    bar_width = 0.35
    x = np.arange(len(INCOME_ORDER))

    for i, scenario in enumerate(SCENARIOS):
        ax = axes[i]
        sc_inexus = inexus_df[inexus_df['toll'] == scenario]
        sc_revenue = revenue_df[revenue_df['toll'] == scenario]

        inexus_vals = []
        revenue_vals = []
        for seg in INCOME_ORDER:
            row_i = sc_inexus[sc_inexus['income_segment'] == seg]
            inexus_vals.append(row_i['aggregated_inexus'].values[0] / 1e6 if not row_i.empty else 0)
            row_r = sc_revenue[sc_revenue['income_segment'] == seg]
            revenue_vals.append(row_r['annual_revenue'].values[0] / 1e6 if not row_r.empty else 0)

        ax.bar(x, inexus_vals, bar_width,
               label='INEXUS Impact (absolute)' if i == 0 else '', color=INEXUS_COLOR)
        ax.bar(x + bar_width, revenue_vals, bar_width,
               label='Revenue Collected' if i == 0 else '', color=REVENUE_COLOR)

        label = chr(ord('a') + i)
        ax.set_title(f'{label}) {SCENARIO_LABELS[scenario]}', loc='left', fontweight='bold')
        ax.set_xticks(x + bar_width / 2)
        ax.set_xticklabels(INCOME_ORDER, fontsize=9)
        ax.set_ylim(0, 220)
        ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        ax.set_facecolor('white')

    axes[0].set_ylabel('Dollars (Millions)')

    # Shared x-axis label
    fig.text(0.5, -0.02, 'Income Segment', ha='center', fontsize=10)

    # Shared legend below both panels
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=2,
               bbox_to_anchor=(0.5, -0.14))

    plt.tight_layout()

    for ext in ['pdf', 'tiff']:
        fig.savefig(f'Figure_10.{ext}', dpi=300, bbox_inches='tight', facecolor='white')
        print(f'Saved: Figure_10.{ext}')
    plt.close()


if __name__ == '__main__':
    main()
