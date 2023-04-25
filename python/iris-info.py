import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

# numpy格式 -> pandas格式
irisdf = pd.DataFrame(
    np.hstack((X, y[:, np.newaxis])),
    columns=['sepal-length', 'sepal-width',
             'petal-length', 'petal-width', 'class']
)
kind_dict = {0: "setosa", 1: "versicolor", 2: "virginica"}
irisdf["class"] = irisdf["class"].map(kind_dict)

print(irisdf.head())  # 前5个样本
#    sepal-length  sepal-width  petal-length  petal-width   class
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

print(irisdf.describe())  # 特征统计信息
#        sepal-length  sepal-width  petal-length  petal-width
# count    150.000000   150.000000    150.000000   150.000000
# mean       5.843333     3.057333      3.758000     1.199333
# std        0.828066     0.435866      1.765298     0.762238
# min        4.300000     2.000000      1.000000     0.100000
# 25%        5.100000     2.800000      1.600000     0.300000
# 50%        5.800000     3.000000      4.350000     1.300000
# 75%        6.400000     3.300000      5.100000     1.800000
# max        7.900000     4.400000      6.900000     2.500000
