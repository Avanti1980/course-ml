import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np


def sgn(x):
    return x >= 0


x1 = np.arange(-5, -0.02, 0.02)
x2 = np.arange(0, 5, 0.02)
y1 = sgn(x1)
y2 = sgn(x2)
x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))

with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        'legend.fontsize': 16,
        "xtick.labelsize": 16,
        "ytick.labelsize": 16,
        'text.color': '#586e75',
    })

    fig, ax = plt.subplots(figsize=(8, 6))

    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')

    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))

    sgn_color = "#dc322f"
    sns.lineplot(x=x1, y=y1, c=sgn_color, label="阶跃函数", ax=ax)
    sns.scatterplot(x=[0], y=[0], s=40, linewidth=2, edgecolor=sgn_color, ax=ax)
    sns.lineplot(x=x2, y=y2, c=sgn_color, ax=ax)
    sns.lineplot(x=x, y=logistic, label="对率函数", ax=ax)

    fig.savefig("sgn-logistic-func-plot.svg")
