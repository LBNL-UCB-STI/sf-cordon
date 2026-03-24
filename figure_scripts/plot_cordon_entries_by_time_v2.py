"""
Figure 4: Number of vehicles entering cordon by time of day.
Journal-formatted version of DataProcessing_2.ipynb plot.
Reads from pre-aggregated cordon_entries_by_time.csv.
"""

import pandas as pd
import matplotlib.pyplot as plt

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

DATA_CSV = '../primary_outcomes/data/cordon_entries_by_time.csv'
SCENARIOS = ['baseline', 'flat', 'income-based']


def main():
    df = pd.read_csv(DATA_CSV)

    fig, ax = plt.subplots(figsize=(7.09, 3.2))

    for scenario in SCENARIOS:
        ax.plot(df['hour'], df[scenario], label=scenario, linewidth=2.0)

    # Shaded congestion pricing periods
    ax.axvspan(6, 9, alpha=0.1, color='red')
    ax.axvspan(15, 18, alpha=0.1, color='red')

    # Text annotations for pricing periods
    ax.text(7.5, ax.get_ylim()[1] * 0.07, 'Morning\nPricing Period',
            horizontalalignment='center', fontsize=8,
            color='darkred', fontweight='bold')
    ax.text(16.5, ax.get_ylim()[1] * 0.07, 'Afternoon\nPricing Period',
            horizontalalignment='center', fontsize=8,
            color='darkred', fontweight='bold')

    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Number of Vehicles')

    ax.legend(title='Scenario')

    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_facecolor('white')

    ax.set_xlim(5, 23)
    ax.set_xticks(range(5, 24, 2))

    plt.tight_layout()

    fig.savefig('Figure_4.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('Figure_4.tiff', dpi=300, bbox_inches='tight', facecolor='white')
    print('Saved: Figure_4.pdf')
    print('Saved: Figure_4.tiff')
    plt.close()


if __name__ == '__main__':
    main()
