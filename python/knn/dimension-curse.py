import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
from scipy.spatial.distance import pdist

np.random.seed(1)

m, dim = 2000, [1, 4, 16, 100, 225, 400]
with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        "font.size": 12,
        'axes.labelsize': '20',
        'text.color': "#586e75",
    })

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))

    for ax, d in zip(axs.ravel(), dim):

        X = np.random.rand(m, d)
        dist = pdist(X, metric='euclidean')
        sns.histplot(dist, bins=50, stat="density", ax=ax)
        ax.set_xlim(0, np.sqrt(d))
        ax.set_title(f"{d}维")
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

    for axi in axs[0, :]:
        axi.set_xlabel('')

    for axi in axs[1, :]:
        axi.set_xlabel('距离')

    for axi in axs[:, 0]:
        axi.set_ylabel('频率')

    for axi in axs[:, 1]:
        axi.set_ylabel('')

    for axi in axs[:, 2]:
        axi.set_ylabel('')

    fig.savefig("dimension-curse.svg")
