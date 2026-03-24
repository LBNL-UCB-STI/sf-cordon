"""
Figure 9: Potential INEXUS ($) relative to Baseline by income segment.
Journal-formatted grouped bar chart.
Based on INEXUS_CordonFilter.ipynb.
"""

import pandas as pd
import matplotlib.pyplot as plt

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

COLORS = {'flat': '#ff7f0e', 'income-based': '#2ca02c'}
INCOME_ORDER = ['Very Low', 'Low', 'Moderate', 'Middle', 'High']


def main():
    lorenz = pd.read_csv(f'{DATA_DIR}/lorenz_data_3_cordonfilter.csv')
    lorenz = lorenz[lorenz['toll'] != 'baseline']

    plot_data = lorenz.pivot(
        index='income_segment', columns='toll',
        values='potential_in_dollar_2023_relative_to_baseline'
    ).reindex(INCOME_ORDER)

    fig, ax = plt.subplots(figsize=(5.0, 3.5))

    bar_width = 0.35
    import numpy as np
    x = np.arange(len(INCOME_ORDER))

    ax.bar(x - bar_width / 2, plot_data['flat'], bar_width,
           label='flat', color=COLORS['flat'])
    ax.bar(x + bar_width / 2, plot_data['income-based'], bar_width,
           label='income-based', color=COLORS['income-based'])

    ax.set_xticks(x)
    ax.set_xticklabels(INCOME_ORDER)
    ax.set_xlabel('Income Segment')
    ax.set_ylabel('Potential INEXUS ($)\nrelative to Baseline')

    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_facecolor('white')

    ax.legend(title='Scenario', loc='lower right')

    plt.tight_layout()

    for ext in ['pdf', 'tiff']:
        fig.savefig(f'Figure_9.{ext}', dpi=300, bbox_inches='tight',
                    facecolor='white')
        print(f'Saved: Figure_9.{ext}')
    plt.close()


if __name__ == '__main__':
    main()
