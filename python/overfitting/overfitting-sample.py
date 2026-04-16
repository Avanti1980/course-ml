import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(1)

n_samples = 30
X = np.random.rand(n_samples)
y = true_fun(X) + np.random.randn(n_samples) * 0.1
X_test = np.arange(0, 1, 0.01)

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
    })

    fig, ax = plt.subplots(figsize=(4, 5))
    sns.lineplot(x=X_test, y=true_fun(X_test), label=r"$\cos (3 \pi x  / 2)$", ax=ax)
    sns.scatterplot(x=X, y=y, s=20, label="样本", ax=ax)
    ax.set(xlim=(0, 1), ylim=(-1.5, 1.5))
    ax.get_legend().texts[0].set_color("#d33682")
    fig.savefig("overfitting-sample.svg")
