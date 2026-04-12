import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 10,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})

iteration = 30
a, b, lr = 1, 100, 0.009
gamma_list = [0.0, 0.4, 0.8]
T = len(gamma_list)

N = 1000
x_list = np.linspace(-2.5, 2.5, N)
y_list = np.linspace(-0.5, 0.5, N)
X, Y = np.meshgrid(x_list, y_list)
Z = a * (X ** 2) + b * (Y ** 2)  # 目标函数

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(nrows=1, ncols=T, figsize=(15, 5))
    fig.suptitle(rf"$\min ~ {a} \cdot w_1^2 + {b} \cdot w_2^2$", color='#d33682', fontproperties={'size': 20})
    for i in range(T):
        gamma = gamma_list[i]
        ax[i].clabel(ax[i].contour(X, Y, Z, 20, alpha=.8, linewidths=1, cmap='inferno'))

        ax[i].set_xlim(-2.5, 2.5)
        ax[i].set_ylim(-.3, .3)
        ax[i].set_xlabel(rf"$\gamma = {gamma}$", color='#d33682', fontsize=18)

        w_1, w_2, v_1, v_2 = -2.4, 0.25, 0, 0  # 初始值
        w_1_curve, w_2_curve, v_1_curve, v_2_curve = [], [], [], []
        w_1_curve.append(w_1)
        w_2_curve.append(w_2)
        v_1_curve.append(v_1)
        v_2_curve.append(v_2)

        for step in range(iteration):

            w_1 = w_1 - lr * 2 * a * w_1 + gamma * v_1_curve[step]
            w_1_curve.append(w_1)
            v_1_curve.append(w_1 - w_1_curve[step])

            w_2 = w_2 - lr * 2 * b * w_2 + gamma * v_2_curve[step]
            w_2_curve.append(w_2)
            v_2_curve.append(w_2 - w_2_curve[step])

        sns.lineplot(x=w_1_curve, y=w_2_curve, lw=1, ax=ax[i])

    plt.savefig("momentum.svg")
