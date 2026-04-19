import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import scipy.stats as st


n_samples = 500
X = st.multivariate_normal.rvs(mean=[0, 0], cov=[[5, 3], [3, 4]], size=n_samples, random_state=1)
pca = PCA(n_components=2).fit(X)

with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        "legend.labelcolor": "#586e75",
    })

    fig, ax = plt.subplots(figsize=[5, 5])
    sns.scatterplot(x=X[:, 0], y=X[:, 1], label="样本", alpha=0.5, s=10, ax=ax)
    for i, (comp, var) in enumerate(zip(pca.components_, pca.explained_variance_)):
        comp = comp * var
        sns.lineplot(x=[0, comp[0]], y=[0, comp[1]], label=f"成分{i + 1}", ax=ax)
    ax.set_aspect('equal')
    fig.savefig("pca-plot.svg")
