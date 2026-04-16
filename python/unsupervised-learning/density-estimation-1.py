import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st


np.random.seed(1)
N, shift = 20, 0.6
X = np.concatenate((st.norm.rvs(0, 1, size=int(0.3 * N)), st.norm.rvs(5, 1, size=int(0.7 * N))))
bins = np.linspace(-4, 9, 14)

with plt.style.context('Solarize_Light2'):

    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "axes.unicode_minus": True,
        "savefig.bbox": "tight",
        "font.size": 16,
        'axes.labelsize': '20',
        'text.color': "#586e75",
    })

    fig, axs = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    x, y = -4.8, 6.8
    sns.histplot(X, bins=bins, stat="frequency", ax=axs[0])
    axs[0].text(x, y, "直方图")
    axs[0].set_ylabel("频率")
    sns.histplot(X, bins=bins + shift, stat="frequency", ax=axs[1])
    axs[1].text(x, y, f"直方图，bins 右移 {shift}")
    sns.histplot(X, bins=bins - shift, stat="frequency", ax=axs[2])
    axs[2].text(x, y, f"直方图，bins 左移 {shift}")

    for ax in axs:
        sns.scatterplot(x=X, y=np.full(len(X), -0.2), s=60, alpha=0.8, marker='.', ax=ax)
        ax.set_xlim(-5, 10)

    fig.savefig('density-estimation-1.svg')
