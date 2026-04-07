import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import numpy as np
import scipy.stats as st

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    "font.size": 16,
    'text.color': "#586e75",
})

np.random.seed(1)
N, shift = 20, 0.6
X = np.concatenate((st.norm.rvs(0, 1, size=int(0.3 * N)), st.norm.rvs(5, 1, size=int(0.7 * N))))
bins = np.linspace(-4, 9, 14)

with plt.style.context('Solarize_Light2'):

    fig, axs = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    x, y = -4.8, 6.8
    sns.histplot(X, bins=bins, stat="frequency", ax=axs[0])
    axs[0].text(x, y, "直方图")
    axs[0].set_ylabel("频率", fontsize=20)
    sns.histplot(X, bins=bins + shift, stat="frequency", ax=axs[1])
    axs[1].text(x, y, f"直方图，bins 右移 {shift}")
    sns.histplot(X, bins=bins - shift, stat="frequency", ax=axs[2])
    axs[2].text(x, y, f"直方图，bins 左移 {shift}")

    for ax in axs:
        ax.plot(X, np.full(len(X), -0.2), '+')
        ax.set_xlim(-5, 10)

    plt.savefig('density-estimation-1.svg')
