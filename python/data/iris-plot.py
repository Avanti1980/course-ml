import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

iris = sns.load_dataset("iris")
iris.columns = ["花萼长度", "花萼宽度", "花瓣长度", "花瓣宽度", "类别"]
kind_dict = {"setosa": "山鸢尾", "versicolor": "杂色鸢尾", "virginica": "维吉尼亚鸢尾"}
iris["类别"] = iris["类别"].map(kind_dict)

with plt.style.context('Solarize_Light2'):
    plt.rcParams.update({
        "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
        "savefig.bbox": "tight",
        # "font.size": 16,  # 同时修改刻度、图例的字体大小
        # 'figure.figsize': [6.4, 4.8],
        # 'figure.labelsize': '30',
        # 'figure.titlesize': 'large',
        'axes.labelsize': '20',
        # 'axes.titlesize': 'large',
        "xtick.labelsize": 16,  # x轴刻度字体大小
        "ytick.labelsize": 16,  # y轴刻度字体大小
        'legend.fontsize': '20',
        'legend.title_fontsize': "22",
        'legend.labelcolor': '#586e75',
        # 'lines.markersize': 6.0,
        # 'savefig.transparent': False,
    })

    g = sns.pairplot(iris, hue="类别", aspect=1, markers=["o", "s", "D"])
    for i, row in enumerate(g.axes):
        for j, ax in enumerate(row):
            ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    g._legend.get_title().set_color('#586e75')
    plt.savefig("iris-plot.svg")

    g = sns.pairplot(iris, hue="类别", aspect=1, diag_kind="hist", kind="kde")
    for i, row in enumerate(g.axes):
        for j, ax in enumerate(row):
            ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    g._legend.get_title().set_color('#586e75')
    plt.savefig("iris-plot2.svg")
