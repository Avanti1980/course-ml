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
    'text.color': '#586e75',
})


def sgn(x):
    return np.array(x >= 0)


x1 = np.arange(-5, -0.02, 0.02)
x2 = np.arange(0, 5, 0.02)
y1 = sgn(x1).astype(int)
y2 = sgn(x2).astype(int)
x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(8, 6))

    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')

    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

    sgn_color = "#dc322f"
    sns.lineplot(x=x1, y=y1, ls="-", lw=2, c=sgn_color, label="阶跃函数", ax=ax)
    sns.scatterplot(x=[0], y=[0], s=40, linewidth=2, edgecolor=sgn_color, ax=ax)
    sns.lineplot(x=x2, y=y2, ls="-", lw=2, c=sgn_color, ax=ax)
    sns.lineplot(x=x, y=logistic, ls="-", lw=2, label="对率函数")
    
    ax.legend()
    plt.savefig("sgn-logistic-func-plot.svg")
