import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))
y = np.sign(np.abs(x))

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
    sns.lineplot(x=x, y=logistic, label="对率函数", ax=ax)
    sns.lineplot(x=x, y=y, ls="--", ax=ax)
    ax.legend(loc="center right")

    fig.savefig("logistic-func-plot.svg", transparent=True)
