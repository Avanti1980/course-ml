import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import matplotlib.ticker as ticker
from sklearn.datasets import load_iris

zhisong = fm.FontEntry(fname="/home/avanti/Fonts/LXGW/LXGWNeoZhiSongScreenFull.ttf", name="LXGW Neo ZhiSong Screen Full")
fm.fontManager.ttflist.insert(0, zhisong)
plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    "font.size": 20,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
})

iris = sns.load_dataset("iris")
iris.columns = ["花萼长度", "花萼宽度", "花瓣长度", "花瓣宽度", "类别"]
kind_dict = {"setosa": "山鸢尾", "versicolor": "杂色鸢尾", "virginica": "维吉尼亚鸢尾"}
iris["类别"] = iris["类别"].map(kind_dict)

with plt.style.context('Solarize_Light2'):
    g = sns.pairplot(iris, hue="类别", aspect=1.4, markers=["o", "s", "D"])
    axes = g.axes
    for i, row in enumerate(axes):
        for j, ax in enumerate(row):
            ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.set_xlabel(g.x_vars[j], fontsize=20)
            ax.set_ylabel(g.y_vars[i], fontsize=20)
    plt.savefig("iris-plot.svg")
