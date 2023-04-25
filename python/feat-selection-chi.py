import numpy as np
from sklearn.feature_selection import SelectKBest, chi2

X = np.array([  # 已去掉方差为零的特征
    [1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
    [6., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0.],
    [10., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0.],
    [13., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1., 0., 1.],
])
y = [1, 1, 0, 0]

sk = SelectKBest(chi2)
sk.fit_transform(X, y)
print(sk.scores_)
# [8.53333333 1.         1.         0.         0.33333333 1.
#  1.         0.33333333 1.         1.         0.         0.
#  0.        ]
