import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
import scipy.stats as st
from sklearn.neighbors import KernelDensity

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': '12',
    'text.color': "#586e75",
})

N = 100
X = np.concatenate((st.norm.rvs(0, 1, size=int(0.3 * N)), st.norm.rvs(5, 1, size=int(0.7 * N))))[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
true_dens = (0.3 * st.norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * st.norm(5, 1).pdf(X_plot[:, 0]))

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.fill(X_plot[:, 0], true_dens, alpha=0.2, label='真实分布')

    for kernel in ['tophat', 'linear', 'epanechnikov', 'cosine', 'gaussian', 'exponential']:
        log_dens = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X).score_samples(X_plot)
        ax = sns.lineplot(x=X_plot[:, 0], y=np.exp(log_dens), lw=1, ls='-', alpha=0.5, label=f"核 = {kernel}")

    ax.legend(loc='upper left')
    ax.plot(X[:, 0], -0.005 - 0.01 * st.uniform.rvs(size=X.shape[0]), '+')
    ax.set_xlim(-4, 9)
    ax.set_ylim(-0.02, 0.4)

    plt.savefig('density-estimation-3.svg')
