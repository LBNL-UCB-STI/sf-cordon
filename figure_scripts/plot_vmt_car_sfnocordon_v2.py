"""
Figure 6: VMT by passenger vehicle mode - SF outside cordon.
Journal-formatted broken y-axis bar chart (Car, Car HOV 2, Car HOV 3).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_DIR = '../primary_outcomes/data'
SCENARIOS = ['baseline', 'flat', 'income-based']
GEO = 'SF_nocordon'
COLORS = {'baseline': '#1f77b4', 'flat': '#ff7f0e', 'income-based': '#2ca02c'}

MODES_TO_DROP = ['bus_empty', 'cable_car', 'cable_car_empty', 'car_emer',
                 'car_hov2_emer', 'car_hov3_emer', 'ferry', 'ferry_empty',
                 'rail_empty', 'subway_empty', 'tram_empty']

MODE_MAPPING = {
    'car': 'Car', 'car_hov2': 'Car HOV 2', 'car_hov3': 'Car HOV 3',
    'car_RideHail': 'Ride-Hail', 'car_RideHail_Pool': 'Ride-Hail Pooled',
    'car_RideHail_empty': 'Ride-Hail Empty', 'walk': 'Walk', 'bike': 'Bike',
    'bus': 'Bus', 'tram': 'Tram', 'rail': 'Rail', 'subway': 'Subway',
}

METERS_TO_MILES = 1609.34


def main():
    dfs = []
    for scenario in SCENARIOS:
        df = pd.read_csv(f'{DATA_DIR}/vmt_mode_{scenario}_{GEO}.csv')
        df['scenario'] = scenario
        dfs.append(df)
    vmt_mode = pd.concat(dfs, ignore_index=True)

    vmt_mode = vmt_mode[~vmt_mode['mode'].isin(MODES_TO_DROP)]
    vmt_mode['mode'] = vmt_mode['mode'].replace(MODE_MAPPING)
    vmt_mode['length'] = vmt_mode['length'] / METERS_TO_MILES

    vmt_car = vmt_mode[vmt_mode['mode'].isin(['Car', 'Car HOV 2', 'Car HOV 3'])]

    plt.style.use('default')
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

    fig, (ax_top, ax_bottom) = plt.subplots(ncols=1, nrows=2, sharex=True,
                                             figsize=(5.0, 4.5))

    sns.barplot(x='mode', y='length', hue='scenario', hue_order=SCENARIOS,
                palette=COLORS, saturation=1.0, data=vmt_car, ax=ax_top)
    sns.barplot(x='mode', y='length', hue='scenario', hue_order=SCENARIOS,
                palette=COLORS, saturation=1.0, data=vmt_car, ax=ax_bottom)

    ax_top.set_ylim(bottom=300000, top=1000000)
    ax_bottom.set_ylim(0, 160000)

    ax_top.set_xlabel('')
    ax_bottom.set_xlabel('')
    ax_top.set_ylabel('')
    ax_bottom.set_ylabel('')

    def format_func(value, tick_number):
        return f'{value / 1000:.0f}'

    ax_top.yaxis.set_major_formatter(plt.FuncFormatter(format_func))
    ax_bottom.yaxis.set_major_formatter(plt.FuncFormatter(format_func))

    # Grid and background
    for ax in [ax_top, ax_bottom]:
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        ax.set_facecolor('white')

    # Break lines between subplots
    d = .02
    kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False, linewidth=0.8)
    ax_top.plot((-d, +d), (-d, +d), **kwargs)
    ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)
    kwargs.update(transform=ax_bottom.transAxes)
    ax_bottom.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax_bottom.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    # Y-axis label
    fig.text(0.02, 0.5, 'VMT (miles) (thousands)',
             va='center', rotation='vertical', fontsize=10)

    # Legend
    handles, labels = ax_top.get_legend_handles_labels()
    ax_top.legend(handles, labels, title='Scenario', loc='upper right')
    ax_bottom.legend_.remove()

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.08, left=0.12)

    fig.savefig('Figure_6.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('Figure_6.tiff', dpi=300, bbox_inches='tight', facecolor='white')
    print('Saved: Figure_6.pdf')
    print('Saved: Figure_6.tiff')
    plt.close()


if __name__ == '__main__':
    main()
