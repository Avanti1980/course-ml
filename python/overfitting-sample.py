import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

font_path = '/home/avanti/Slides/Courses/ML/fonts/Operator/OperatorMono-Book.otf'
font_name = fm.FontProperties(fname=font_path).get_name()


def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
X_test = np.arange(0, 1, 0.01)

with plt.style.context('Solarize_Light2'):

    plt.figure(figsize=(4, 5))
    plt.plot(X_test, true_fun(X_test), label="true func")
    plt.scatter(X, y, s=20, label="samples")
    plt.xlim((0, 1))
    plt.ylim((-1.5, 1.5))
    plt.legend(loc="best")
    plt.show()
