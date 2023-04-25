import numpy as np
from sklearn.decomposition import PCA

X = np.array([
    [1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
    [6., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0.],
    [10., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0.],
    [13., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1., 0., 1.],
])

pca = PCA(n_components=3)
XX = pca.fit_transform(X)
print(XX)
# [[ 6.59008618 -0.65420003 -0.62672674]
#  [ 1.49765996  0.41345689  1.35501589]
#  [-2.55003899  1.68197454 -0.64673241]
#  [-5.53770716 -1.4412314  -0.08155674]]

print(np.linalg.norm(X - pca.inverse_transform(XX)))
# 3.1659611182970852e-15

pca = PCA(n_components=2)
XX = pca.fit_transform(X)
print(XX)
# [[ 6.59008618 -0.65420003]
#  [ 1.49765996  0.41345689]
#  [-2.55003899  1.68197454]
#  [-5.53770716 -1.4412314 ]]

print(np.linalg.norm(X - pca.inverse_transform(XX)))
# 1.6290392142641008
