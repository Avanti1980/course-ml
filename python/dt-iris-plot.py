import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

irisdf = pd.DataFrame(
    np.hstack((X, y[:, np.newaxis])),
    columns=["花萼长度", "花萼宽度",
             "花瓣长度", "花瓣宽度", "类别"]
)
kind_dict = {0: "山鸢尾", 1: "杂色鸢尾", 2: "维吉尼亚鸢尾"}
irisdf["类别"] = irisdf["类别"].map(kind_dict)

plt.rcParams["font.sans-serif"] = ["SimHei"]
with plt.style.context('Solarize_Light2'):
    plt.subplot()
    g = sns.pairplot(irisdf, diag_kind="kde", kind="scatter", hue="类别", aspect=1.4, markers=["o", "s", "D"])
    plt.show()
