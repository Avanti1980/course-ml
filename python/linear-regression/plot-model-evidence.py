import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def true_fun(X):
    return np.sin(np.pi * X)


plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})


np.random.seed(1)
n_samples, degree = 30, 8
a, b = 0.05, 10  # 分布超参数
x = st.uniform.rvs(loc=-1, scale=2, size=n_samples)
y = true_fun(x) + st.norm.rvs(loc=0, scale=np.sqrt(1 / b), size=n_samples)
x_plot = np.arange(-1.2, 1.2, 0.01)
evidence = []

with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(2, int(degree / 2), figsize=(16, 8))
    ax = ax.ravel()

    for n in range(1, degree):
        polynomial_features = PolynomialFeatures(degree=n, include_bias=True)
        x_features = polynomial_features.fit_transform(x[:, np.newaxis])
        x_plot_features = polynomial_features.fit_transform(x_plot[:, np.newaxis])
        lr = LinearRegression()
        lr.fit(x_features, y)
        # ax[n].plot(x_plot, lr.predict(x_plot_features), label='degree = %d' % (n))

        sns.lineplot(x=x_plot, y=lr.predict(x_plot_features), label=f'{n}阶多项式', ax=ax[n])
        sns.scatterplot(x=x, y=y, s=20, ax=ax[n])

        # ax[n].scatter(x, y)
        ax[n].set_xlim(-1.2, 1.2)
        ax[n].set_ylim(-2, 2)

        if n == 1 or n == 4:
            ax[n].set_ylabel('$y$', fontsize=20, color="#d33682")
        if n >= 4:
            ax[n].set_xlabel('$x$', fontsize=20, color="#d33682")

        sigma = b * x_features.T @ x_features + a * np.eye(n + 1)
        mu = b * np.linalg.inv(sigma) @ x_features.T @ y[:, np.newaxis]

        evidence.append((np.log(a) * (n + 1) + np.log(b) * n_samples - b * np.linalg.norm(y[:, np.newaxis] - x_features @ mu)**2 - a * np.linalg.norm(mu)**2 - np.log(np.linalg.det(sigma)) - np.log(2 * np.pi) * n_samples) / 2)

    # ax[0].plot([i for i in range(1, degree)], evidence)

    sns.lineplot(x=[i for i in range(1, degree)], y=evidence, ax=ax[0])
    ax[0].set_xlim(0, degree)
    ax[0].set_ylim(-35, -10)
    ax[0].set_xlabel('多项式阶数', fontsize=18)
    ax[0].set_ylabel('对数模型证据', fontsize=18)

    fig.subplots_adjust(wspace=0.3, hspace=0.3)
    fig.savefig("plot-model-evidence.svg")
