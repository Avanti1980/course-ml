import numpy as np
from sklearn.neural_network import MLPClassifier

X = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([0, 1, 1, 0])

mlp = MLPClassifier(
    hidden_layer_sizes=(3,),  # 隐藏层神经元个数
    activation='logistic',    # 激活函数
    max_iter=100,             # 最大迭代轮数
    solver='lbfgs',           # 求解器
    alpha=0,                  # 正则项系数
    verbose=False
)

clf = mlp.fit(X, y)
clf.score(X, y)
