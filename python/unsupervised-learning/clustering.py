import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    "font.size": 10,
    'figure.figsize': [10, 5],
})

with plt.style.context('Solarize_Light2'):
    fig, axs = plt.subplots(1, 2)
    n_samples, n_clusters = 2000, 6
    for i, n_components in enumerate([1, 2]):
        X, _ = make_blobs(n_samples=n_samples, centers=n_components, cluster_std=1.00)
        k_means = KMeans(init='k-means++', n_clusters=n_clusters, n_init=10).fit(X)

        axs[i] = sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=k_means.labels_, legend=False, alpha=0.5, s=10, ax=axs[i])  # 样本
        axs[i] = sns.scatterplot(x=k_means.cluster_centers_[:, 0], y=k_means.cluster_centers_[:, 1], hue=range(n_clusters), s=30, legend=False, marker='D', ax=axs[i])  # 簇中心
        plt.savefig('clustering.svg')
