import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

font_path = '/home/avanti/Slides/Courses/ML/fonts/Operator/OperatorMono-Book.otf'
#font_path = '/home/avanti/Slides/Courses/ML/fonts/Ysabeau/Ysabeau-Medium.otf'
font_name = fm.FontProperties(fname=font_path).get_name()
# plt.rcParams["font.family"] = font_name
# plt.rcParams["font.style"] = 'italic'
# plt.rcParams["font.weight"] = 'bold'

def true_fun(X):
    return np.cos(1.5 * np.pi * X)


np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1

with plt.style.context('Solarize_Light2'):
    plt.figure(figsize=(4, 5))

    X_test = np.arange(0, 1, 0.01)

    plt.plot(X_test, true_fun(X_test), label="true func")
    plt.scatter(X, y, s=20, label="samples")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best", labelcolor='#073642')

    plt.savefig('overfitting.svg', transparent=True)
    plt.show()
