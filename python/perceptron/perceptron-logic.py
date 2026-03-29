import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.linear_model import Perceptron

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "font.size": 16
})

X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y_and = np.array([1, -1, -1, -1])
y_or = np.array([1, 1, 1, 0])
y_not = np.array([0, 0, 1, 1])

i = 1
h = .02

tasks = [
    (X, y_and, '与'),
    (X, y_or, '或'),
    (X, y_not, '非'),
]

figure = plt.figure(figsize=(12, 4))

with plt.style.context('Solarize_Light2'):
    for index, ds in enumerate(tasks):

        X, y, name = ds

        x_min, x_max = -0.2, 1.2
        y_min, y_max = -0.2, 1.2
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        ax = plt.subplot(1, len(tasks), i)

        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        i += 1

        clf = Perceptron(tol=1e-3, random_state=0)
        clf.fit(X, y)  # 训练模型
        score = clf.score(X, y)  # 训练精度

        if clf.intercept_[0] < 0:
            ax.set_title(rf"{name}: ${clf.coef_[0, 0]} \cdot x_1 + {clf.coef_[0, 1]} \cdot x_2 {clf.intercept_[0]}$", color="#586e75")
        else:
            ax.set_title(rf"{name}: ${clf.coef_[0, 0]} \cdot x_1 + {clf.coef_[0, 1]} \cdot x_2 + {clf.intercept_[0]}$", color="#586e75")

        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        # ax.contourf(xx, yy, Z, alpha=.8)
        contours = ax.contour(xx, yy, Z, 10, alpha=.8)
        ax.clabel(contours, fontsize=12, inline=True)
        ax.scatter(X[:, 0], X[:, 1], s=50, c=y, edgecolors='#002b36')
        # ax.text((xx.min()+xx.max())/2, yy.min()+0.05, ('acc = %.2f' % score).lstrip('0'), size=14, horizontalalignment='center')

plt.savefig("perceptron-logic.svg", transparent=True, bbox_inches="tight")
