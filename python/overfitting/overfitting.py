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
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})

n_samples = 30
degrees = [1, 4, 30]
X = np.random.rand(n_samples)
y = true_fun(X) + np.random.randn(n_samples) * 0.1
X_test = np.arange(0, 1, 0.01)

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(1, 3, figsize=(14, 5))

    for i, degree in enumerate(degrees):

        polynomial_features = PolynomialFeatures(degree=degree, include_bias=True)
        linear_regression = LinearRegression()
        pipeline = Pipeline(
            [
                ("polynomial_features", polynomial_features),
                ("linear_regression", linear_regression),
            ]
        )
        pipeline.fit(X[:, np.newaxis], y)

        sns.lineplot(x=X_test, y=true_fun(X_test), label=r"$\cos (3 \pi x  / 2)$", ax=ax[i])
        sns.scatterplot(x=X, y=y, s=20, label="样本", ax=ax[i])
        sns.lineplot(x=X_test, y=pipeline.predict(X_test[:, np.newaxis]), label="模型", ax=ax[i])

        ax[i].set_xlim((0, 1))
        ax[i].set_ylim((-1.5, 1.5))
        ax[i].legend()
        leg = ax[i].get_legend()
        leg.texts[0].set_color("#d33682")
        ax[i].set_title(f"{degree}阶多项式回归")

    plt.savefig("overfitting.svg")
