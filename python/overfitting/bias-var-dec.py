import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(0)

plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": 'cm',
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 12,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})

trial, n_samples = 5, 30
degrees = [1, 4, 10]
X = np.random.rand(trial, n_samples)
Y = true_fun(X) + np.random.randn(trial, n_samples) * 0.1
X_plot = np.linspace(0, 1, 100)

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(len(degrees) + 1, trial, sharex=True, sharey=True, figsize=(20, 12))

    # 每个子图画cos函数和样本点
    for t in range(trial):
        ax[0, t].set_title(f"样本集{t + 1}", fontsize='20')
        x, y = X[t, :], Y[t, :]
        for i in range(len(degrees) + 1):
            sns.lineplot(x=X_plot, y=true_fun(X_plot), label=r"$\cos (3 \pi x  / 2)$", ax=ax[i, t])
            sns.scatterplot(x=x, y=y, s=10, label="样本", ax=ax[i, t])

    # 按行来 每行对应一个degree
    for i, degree in enumerate(degrees):

        ax[i+1, 0].set_ylabel(f'{degree}阶多项式回归', fontsize='20')

        polynomial_features = PolynomialFeatures(degree=degree, include_bias=True)
        XX_plot = polynomial_features.fit_transform(X_plot[:, np.newaxis])

        # 前 trial-1 个样本集各训练一个回归模型 最后一个样本集测试平均模型
        lr = [LinearRegression()] * (trial - 1)
        pre_avg = np.zeros(len(X_plot))
        for t in range(trial - 1):
            x, y = X[t, :], Y[t, :]
            lr[t].fit(polynomial_features.fit_transform(x[:, np.newaxis]), y)
            sns.lineplot(x=X_plot, y=lr[t].predict(XX_plot), label="模型", ax=ax[i + 1, t])
            pre_avg += lr[t].predict(XX_plot)

        sns.lineplot(x=X_plot, y=pre_avg / 4, label="平均模型", ax=ax[i + 1, -1])

    for t in range(trial):
        for i in range(len(degrees) + 1):
            ax[i, t].set_xlim((0, 1))
            ax[i, t].set_ylim((-1.5, 1.5))
            ax[i, t].legend()
            leg = ax[i, t].get_legend()
            leg.texts[0].set_color("#d33682")

    plt.savefig("bias-var-dec.svg")
