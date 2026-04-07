import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from sklearn.decomposition import PCA
import scipy.stats as st

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    "font.size": 10,
})

n_samples = 500
X = st.multivariate_normal.rvs(mean=[0, 0], cov=[[5, 3], [3, 4]], size=n_samples, random_state=1)
pca = PCA(n_components=2).fit(X)

with plt.style.context('Solarize_Light2'):
    ax = sns.scatterplot(x=X[:, 0], y=X[:, 1], label="样本", alpha=0.5, s=10)
    for i, (comp, var) in enumerate(zip(pca.components_, pca.explained_variance_)):
        comp = comp * var
        ax = sns.lineplot(x=[0, comp[0]], y=[0, comp[1]], label=f"成分{i + 1}", lw=2)
    ax.set_aspect('equal')
    ax.legend()
    plt.savefig("pca-plot.svg")
