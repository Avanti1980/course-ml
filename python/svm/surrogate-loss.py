import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.arange(-5, 5, 0.02)
loss01 = [(1 - np.sign(xi)) / 2 for xi in x]
hinge = np.maximum(0, 1 - x)
square_hinge = np.maximum(0, 1 - x)**2
exp = np.exp(-x)
logistic = np.log2(1 + np.exp(-x))

with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "mathtext.fontset": 'cm',
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        'legend.fontsize': 16,
        "xtick.labelsize": 16,
        "ytick.labelsize": 16,
        'text.color': '#586e75',
        "axes.labelsize": 20,
        'axes.labelcolor': "#d33682",
        'savefig.transparent': True,
    })

    fig, ax = plt.subplots(figsize=(8, 5))
    for s in ['bottom', 'left']:
        ax.spines[s].set_position('zero')
        ax.spines[s].set_color('#586e75')
    for s in ['top', 'right']:
        ax.spines[s].set_color('none')

    sns.lineplot(x=x, y=loss01, ls="solid", label="0-1")
    sns.lineplot(x=x, y=hinge, ls="-", label="hinge")
    sns.lineplot(x=x, y=square_hinge, ls="dashed", label="square hinge")
    sns.lineplot(x=x, y=exp, ls=":", label="exp")
    sns.lineplot(x=x, y=logistic, ls="-.", label="logistic")

    ax.set(xlim=[-5.1, 5.1], ylim=[0, 5.05], xlabel="$y f(x)$")

    fig.savefig('surrogate-loss.svg')
