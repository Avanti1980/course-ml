import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(1)

n_samples = 30
X = np.random.rand(n_samples)
y = true_fun(X) + np.random.randn(n_samples) * 0.1
X_test = np.arange(0, 1, 0.01)
degrees = [1, 4, 30]

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
        pipeline.fit(X.reshape(-1, 1), y)

        sns.lineplot(x=X_test, y=true_fun(X_test), label=r"$\cos (3 \pi x  / 2)$", ax=ax[i])
        sns.scatterplot(x=X, y=y, s=20, label="样本", ax=ax[i])
        sns.lineplot(x=X_test, y=pipeline.predict(X_test.reshape(-1, 1)), label="模型", ax=ax[i])

        ax[i].set(xlim=(0, 1), ylim=(-1.5, 1.5), title=f"{degree}阶多项式回归")
        ax[i].get_legend().texts[0].set_color("#d33682")

    fig.savefig("overfitting.svg")
