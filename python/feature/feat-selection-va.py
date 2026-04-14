import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif

X = np.array([  # 已去掉方差为零的特征
    [1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
    [6., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0.],
    [10., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0.],
    [13., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1., 0., 1.],
])
y = [1, 1, 0, 0]

sk = SelectKBest(f_classif)
sk.fit_transform(X, y)
print(sk.scores_)
# [7.52941176 1.         1.         0.         1.         1.
#  1.         1.         1.         1.         0.         0.
#  0.        ]
