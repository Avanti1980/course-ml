import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
from sklearn.linear_model import Perceptron

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
    'text.color': '#586e75',
})

X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y_and = np.array([1, 0, 0, 0])
y_or = np.array([1, 1, 1, 0])
y_not = np.array([0, 0, 1, 1])
h = .02
tasks = [
    (X, y_and, '与'),
    (X, y_or, '或'),
    (X, y_not, '非'),
]

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))

    for i, (X, y, name) in enumerate(tasks):

        x_min, x_max = -0.2, 1.2
        y_min, y_max = -0.2, 1.2
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        ax[i].set_xlim(xx.min(), xx.max())
        ax[i].set_ylim(yy.min(), yy.max())
        ax[i].set_xticks(())
        ax[i].set_yticks(())

        clf = Perceptron(tol=1e-3, random_state=0)
        clf.fit(X, y)  # 训练模型
        score = clf.score(X, y)  # 训练精度

        ax[i].set_title(f"{name}")

        if clf.intercept_[0] < 0:
            ax[i].set_xlabel(rf"${clf.coef_[0, 0]} \cdot x_1 + {clf.coef_[0, 1]} \cdot x_2 {clf.intercept_[0]}$", color="#d33682", fontsize='18')
        else:
            ax[i].set_xlabel(rf"${clf.coef_[0, 0]} \cdot x_1 + {clf.coef_[0, 1]} \cdot x_2 + {clf.intercept_[0]}$", color="#d33682", fontsize='18')

        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        # ax.contourf(xx, yy, Z, alpha=.8)
        contours = ax[i].contour(xx, yy, Z, 10, cmap="inferno", alpha=.8)
        ax[i].clabel(contours, fontsize=12, inline=True)
        sns.scatterplot(x=X[:, 0], y=X[:, 1], s=50, hue=y, palette="inferno", legend=False, ax=ax[i])

    plt.savefig("perceptron-logic.svg")
