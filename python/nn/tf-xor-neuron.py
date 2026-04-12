import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
import scipy.stats as st
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

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
    'savefig.transparent': True,
})

np.random.seed(1)

# 异或 四个样本
X_xor, y_xor = np.array([[1, 1], [1, 0], [0, 1], [0, 0]]), np.array([0, 1, 1, 0])

X, y, m = X_xor, y_xor, 255
cov = [[0.01, 0], [0, 0.01]]  # 高斯分布的协方差矩阵

X, y, m = X_xor, y_xor, 255
for (xx, yy) in zip(X_xor, y_xor):  # 以异或的4个点为中心 从2维高斯分布中各随机采样255个样本
    X = np.vstack((X, st.multivariate_normal.rvs(xx, [[0.01, 0], [0, 0.01]], size=m)))
    y = np.concatenate((y, np.ones(m) * yy))

x_min, x_max = -0.5, 1.5
y_min, y_max = -0.5, 1.5
inc = 0.01
xx, yy = np.meshgrid(np.arange(x_min, x_max, inc), np.arange(y_min, y_max, inc))
i = 0

h_array = [2, 3, 4, 5]
col = len(h_array)

with plt.style.context('Solarize_Light2'):

    plt.figure(figsize=(18, 10))

    for i, h in enumerate(h_array):

        model = Sequential()
        model.add(Dense(units=h, activation="sigmoid", input_shape=(2, )))
        model.add(Dense(units=1, activation='sigmoid'))
        model.summary()

        model.compile(
            optimizer=Adam(0.1),
            loss="binary_crossentropy",
            metrics=['accuracy']
        )

        model.fit(X, y, epochs=10, batch_size=32)
        loss, acc = model.evaluate(X, y, verbose=2)
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z[:, 0].reshape(xx.shape)

        ax = plt.subplot(2, col, i + 1)
        ax.set_aspect('equal')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())

        ax.contourf(xx, yy, Z, alpha=.8, cmap='inferno')
        sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette="inferno", legend=False, s=30, ax=ax)
        ax.set_title(f'{h} 个神经元，准确率 = {acc:.2f}', size=18)

        ax = plt.subplot(2, col, i + col + 1, projection='3d')
        ax.plot_surface(xx, yy, Z)
        inc = 0.5
        ax.set_xticks(np.arange(x_min, x_max + 0.1, inc))
        ax.set_yticks(np.arange(y_min, y_max + 0.1, inc))
        ax.set_xlabel(r'$x_1$', color='#d33682')
        ax.set_ylabel(r'$x_2$', color='#d33682')

    plt.subplots_adjust(wspace=0.08, hspace=-0.3)
    plt.savefig('tf-xor-neuron.svg')
