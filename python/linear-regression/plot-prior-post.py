import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st

np.random.seed(0)
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

w0_true, w1_true = 0, 0.5
a, b = 4, 100  # 超参数
mu, sigma = np.zeros(2), np.eye(2) / a  # w的先验高斯分布的均值、协方差
n_samples = 4
x, y = [], []  # 用来保存样本
Xy = np.zeros((2, 1))  # sum_i x_i y_i
x_plot = np.arange(-1, 1.01, 0.01)
xx, yy = np.meshgrid(x_plot, x_plot)
pos = np.dstack((np.meshgrid(x_plot, x_plot)))
lines = 5

with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(2, n_samples + 1, sharex=True, sharey=True, figsize=(15, 6))

    rv = st.multivariate_normal(mean=mu, cov=sigma)
    ax[0, 0].contourf(xx, yy, rv.pdf(pos), cmap='inferno')
    ax[0, 0].set_xlabel('$w_0$', fontsize=18)
    ax[0, 0].set_ylabel('$w_1$', fontsize=18)

    ax[0, 0].set_title("先验")

    W = rv.rvs(size=lines)
    for j in range(lines):
        sns.lineplot(x=x_plot, y=W[j, 0] + W[j, 1] * x_plot, ax=ax[1, 0])
    ax[1, 0].set_xlabel('$x$', fontsize=18)
    ax[1, 0].set_ylabel('$y$', fontsize=18)

    for i in range(n_samples):
        xi = st.uniform.rvs(loc=-1, scale=2)  # [-1,1]上均匀采样
        yi = w0_true + w1_true * xi + st.norm.rvs(loc=0, scale=np.sqrt(1 / b))
        x.append(xi)
        y.append(yi)
        ax[0, i + 1].set_title(f"$x = {xi:.2f}, y = {yi:.2f}$", color="#d33682")
        xi = np.array([[1], [xi]])
        Xy += xi * yi
        sigma = sigma - b * sigma @ xi @ xi.T @ sigma / (1 + b * xi.T @ sigma @ xi)  # Sherman-Morrison 公式
        mu = b * (sigma @ Xy).ravel()
        rv = st.multivariate_normal(mean=mu, cov=sigma)
        ax[0, i + 1].contourf(xx, yy, rv.pdf(pos), cmap='inferno')
        ax[0, i + 1].set_xlabel('$w_0$', fontsize=18)

        W = rv.rvs(size=lines)
        for j in range(lines):
            sns.lineplot(x=x_plot, y=W[j, 0] + W[j, 1] * x_plot, ax=ax[1, i + 1])
        # ax[1, i + 1].scatter(x, y)
        sns.scatterplot(x=x, y=y, s=50, ax=ax[1, i + 1])
        ax[1, i + 1].set_xlabel('$x$', fontsize=18)

    plt.setp(ax, xlim=(-1, 1), ylim=(-1, 1))
    # fig.subplots_adjust(wspace=0.15, hspace=0.15)
    fig.savefig("plot-prior-post.svg")
