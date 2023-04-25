import numpy as np
from scipy.spatial import distance
from sklearn import random_projection

np.random.seed(0)

X = np.random.rand(100, 10000)
D1 = distance.cdist(X, X, 'euclidean')  # 原样本的成对距离矩阵

transformer = random_projection.GaussianRandomProjection()  # 高斯随机矩阵
XX = transformer.fit_transform(X)
print(XX.shape)
# (100, 3947)

D2 = distance.cdist(XX, XX, 'euclidean')  # 投影后样本的成对距离矩阵
print(np.linalg.norm(D1 - D2, ord='fro'))  # 两个成对距离矩阵差的F范数
# 45.5042470391125

transformer = random_projection.SparseRandomProjection()  # 稀疏随机矩阵
XX = transformer.fit_transform(X)
print(XX.shape)
# (100, 3947)

D2 = distance.cdist(XX, XX, 'euclidean')  # 投影后样本的成对距离矩阵
print(np.linalg.norm(D1 - D2, ord='fro'))  # 两个成对距离矩阵差的F范数
# 45.20040904607192
