import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

n_samples, n_clusters = 2000, 6
with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "mathtext.fontset": "cm",
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        "font.size": 16,
        'figure.figsize': [10, 5],
    })
    fig, ax = plt.subplots(1, 2)

    for i, center in enumerate([[(0, 0)], [(2, 2), (-2, -2)]]):
        X, _ = make_blobs(n_samples=n_samples, centers=center, cluster_std=1.00, random_state=1)
        k_means = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10).fit(X)

        sns.scatterplot(x=X[:, 0], y=X[:, 1], c=k_means.labels_, cmap='inferno', legend=False, alpha=0.5, s=10, ax=ax[i])  # 样本
        sns.scatterplot(x=k_means.cluster_centers_[:, 0], y=k_means.cluster_centers_[:, 1], c=range(n_clusters), cmap='inferno', s=30, legend=False, marker='D', ax=ax[i])  # 簇中心

    fig.savefig('clustering.svg')
