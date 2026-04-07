import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'savefig.transparent': True,
    'text.color': '#586e75',
})

x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))
tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(8, 6))

    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')

    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

    sns.lineplot(x=x, y=logistic, ls="-", lw=2, label="对率函数", ax=ax)
    sns.lineplot(x=x, y=tanh, ls="--", lw=2, label="双曲正切函数", ax=ax)

    ax.legend(loc='upper left')
    ax.set_xlim([-5.1, 5.1])
    ax.set_ylim([-1.1, 1.1])

    plt.savefig("sigmoid.svg")
