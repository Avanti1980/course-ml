import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.neighbors import KernelDensity

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    "font.size": 16,
    'text.color': "#586e75",
})

X_plot = np.linspace(-6, 6, 1000)[:, None]
X_src = np.zeros((1, 1))

with plt.style.context('Solarize_Light2'):

    fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(10, 6))

    for i, kernel in enumerate(['tophat', 'linear', 'epanechnikov', 'cosine', 'gaussian', 'exponential']):
        ax = axs.ravel()[i]
        log_dens = KernelDensity(kernel=kernel).fit(X_src).score_samples(X_plot)
        ax.fill(X_plot[:, 0], np.exp(log_dens))
        ax.text(-1.8, 0.9, kernel)
        ax.xaxis.set_major_locator(plt.MultipleLocator(1))
        ax.yaxis.set_major_locator(plt.MultipleLocator(1))
        ax.set_xlim(-2, 2)
        ax.set_ylim(0, 1)

    plt.savefig('density-estimation-2.svg')
