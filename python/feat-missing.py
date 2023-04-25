import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

X = np.array([
    [1, '周六', '吃饭', '晴天', '轻松', '清零', '精彩', 25.2, 0.5],
    [6, '周六', '逛街', '晴天', '轻松', '平缓', '无聊', np.nan, 2.0],
    [10, '周六', '-', '雨天', '轻松', '严峻', '无聊', 32.6, 8.2],
    [13, '周六', '逛街', '晴天', '正常', '清零', '精彩', 36.4, 9.8],
])

imp_mean = SimpleImputer(strategy='mean')
print(imp_mean.fit_transform(X[:, [7]]))  # 用均值填充
# [[25.2]
#  [31.4]
#  [32.6]
#  [36.4]]

imp_median = SimpleImputer(strategy='median')
print(imp_median.fit_transform(X[:, [7]]))  # 用中位数填充
# [[25.2]
#  [32.6]
#  [32.6]
#  [36.4]]

imp_frequent = SimpleImputer(missing_values='-', strategy='most_frequent')
print(imp_frequent.fit_transform(X[:, [2]].astype('object')))  # 用众数填充
# [['吃饭']
#  ['逛街']
#  ['逛街']
#  ['逛街']]

# 回归器默认采用BayesianRidge
# 其它可选DecisionTreeRegressor ExtraTreesRegressor KNeighborsRegressor
imp_iter = IterativeImputer(estimator=KNeighborsRegressor(n_neighbors=2))
print(imp_iter.fit_transform(X[:, [0, 7, 8]]))
# [[ 1.  25.2  0.5]
#  [ 6.  28.9  2. ]
#  [10.  32.6  8.2]
#  [13.  36.4  9.8]]
