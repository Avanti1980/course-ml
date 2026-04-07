import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
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
gamma = 0.2
relu = np.maximum(0, x)
lrelu = np.maximum(0, x) + gamma * np.minimum(0, x)
softplus = np.log(1 + np.exp(x))

gamma2 = 0.5
elu = np.maximum(0, x) + np.minimum(0, gamma2 * (np.exp(x) - 1))

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(8, 6))

    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')

    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    sns.lineplot(x=x, y=relu, ls="-", lw=2, alpha=0.8, label="ReLU", ax=ax)
    sns.lineplot(x=x, y=lrelu, ls="dashed", lw=2, alpha=0.8, label="LeakyReLU", ax=ax)
    sns.lineplot(x=x, y=elu, ls=":", lw=2, alpha=0.8, label="ELU", ax=ax)
    sns.lineplot(x=x, y=softplus, ls="-.", lw=2, alpha=0.8, label="Softplus", ax=ax)

    ax.legend(loc='upper left')
    ax.set_xlim([-5.1, 5.1])
    ax.set_ylim([-1.1, 5.1])

    plt.savefig("relu.svg")
