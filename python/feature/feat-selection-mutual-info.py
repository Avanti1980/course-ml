import numpy as np
from sklearn.feature_selection import SelectKBest, mutual_info_classif

np.random.seed(0)

X = np.array([  # 已去掉方差为零的特征
    [1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
    [6., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0.],
    [10., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0.],
    [13., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1., 0., 1.],
])
y = [1, 1, 0, 0]

sk = SelectKBest(mutual_info_classif)
sk.fit_transform(X, y)
print(sk.scores_)
# [0.58333333 0.20833333 0.08333333 0.         0.08333333 0.
#  0.         0.         0.20833333 0.         0.         0.
#  0.        ]
