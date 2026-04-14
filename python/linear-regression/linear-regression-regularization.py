import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(1)

plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 12,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})


n_samples = 20
x = np.random.rand(n_samples)
y = true_fun(x) + np.random.randn(n_samples) * 0.1
x_plot = np.linspace(0, 1, 100)

polynomial_features = PolynomialFeatures(degree=19, include_bias=True)
xx_plot = polynomial_features.fit_transform(x_plot[:, np.newaxis])
xx = polynomial_features.fit_transform(x[:, np.newaxis])

alpha = [0] + [10**i for i in range(-8, -2, 2)]  # 正则项
with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(1, len(alpha), sharey=True, figsize=(20, 5))

    for i, a in enumerate(alpha):
        sns.lineplot(x=x_plot, y=true_fun(x_plot), label=r"$\cos (3 \pi x  / 2)$", ax=ax[i])
        sns.scatterplot(x=x, y=y, s=20, label="样本", ax=ax[i])

        if a == 0:
            lr = LinearRegression()
        else:
            lr = Ridge(alpha=a)

        lr.fit(xx, y)
        ax[i].plot(x_plot, lr.predict(xx_plot), label="多项式回归")
        ax[i].set_title(rf'$\lambda = {a}$', fontsize=24, color="#d33682")
        ax[i].legend()
        leg = ax[i].get_legend()
        leg.texts[0].set_color("#d33682")

        ax[i].set_xlim((0, 1))
        ax[i].set_ylim((-2, 2))

    # plt.subplots_adjust(wspace=0.1, hspace=0.1)
    fig.savefig("linear-regression-regularization.svg")
