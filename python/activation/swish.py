import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": 'cm',
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'savefig.transparent': True,
    'text.color': '#586e75',
})

x = np.arange(-5, 5, 0.02)
beta = [0, 0.5, 1, 100]

swish0 = x / (1 + np.exp(- beta[0] * x))
swish1 = x / (1 + np.exp(- beta[1] * x))
swish2 = x / (1 + np.exp(- beta[2] * x))
swish3 = x / (1 + np.exp(- beta[3] * x))

gamma2 = 0.5
elu = np.maximum(0, x) + np.minimum(0, gamma2 * (np.exp(x) - 1))

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(8, 6))

    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')

    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    sns.lineplot(x=x, y=swish0, ls="-", lw=2, label=r'$\beta=0$', ax=ax)
    sns.lineplot(x=x, y=swish1, ls="dashed", lw=2, label=r'$\beta=0.5$', ax=ax)
    sns.lineplot(x=x, y=swish2, ls=":", lw=2, label=r'$\beta=1$', ax=ax)
    sns.lineplot(x=x, y=swish3, ls="-.", lw=2, label=r'$\beta=100$', ax=ax)

    ax.legend(loc='upper left', labelcolor='#d33682')
    ax.set_xlim([-5.1, 5.1])
    ax.set_ylim([-1.1, 5.1])

    plt.savefig("swish.svg")
