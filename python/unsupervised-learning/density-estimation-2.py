import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity

X_plot = np.linspace(-6, 6, 1000)

with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        "font.size": 16,
        'text.color': "#586e75",
    })

    fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(10, 6))
    for ax, kernel in zip(axs.ravel(), ['tophat', 'linear', 'epanechnikov', 'cosine', 'gaussian', 'exponential']):
        log_dens = KernelDensity(kernel=kernel).fit([[0]]).score_samples(X_plot.reshape(-1, 1))
        ax.fill(X_plot, np.exp(log_dens))
        ax.text(-1.8, 0.88, kernel)
        ax.set(xlim=(-2, 2), ylim=(0, 1))

    fig.savefig('density-estimation-2.svg')
