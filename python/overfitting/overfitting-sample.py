import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(0)

plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": 'cm',
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})

n_samples = 30
X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
X_test = np.arange(0, 1, 0.01)

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(4, 5))
    sns.lineplot(x=X_test, y=true_fun(X_test), label=r"$\cos (3 \pi x  / 2)$", ax=ax)
    sns.scatterplot(x=X, y=y, s=20, label="样本", ax=ax)
    ax.set_xlim((0, 1))
    ax.set_ylim((-1.5, 1.5))

    ax.legend()
    leg = ax.get_legend()
    leg.texts[0].set_color("#d33682")
    fig.savefig("overfitting-sample.svg")
