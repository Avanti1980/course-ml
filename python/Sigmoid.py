import matplotlib.pyplot as plt
import numpy as np


def sgn(x):
    return np.array(x >= 0)


r = 10

x1 = np.arange(-r, -0.04, 0.02)
x2 = np.arange(0, r, 0.02)
y1 = sgn(x1).astype(np.int)
y2 = sgn(x2).astype(np.int)

x = np.arange(-r, r, 0.02)
logistic = 1 / (1 + np.exp(-x))

plt.axis([-5.1, 5.1, -1.1, 1.1])

with plt.style.context('Solarize_Light2'):

    # plt.figure(figsize = (10,5))
    ax = plt.gca()

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    ax.xaxis.set_ticks_position('top')
    ax.spines['top'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('right')
    ax.spines['right'].set_position(('data', 0))

    ax.tick_params(axis='x')
    ax.tick_params(axis='y')

    sgn_color, logistic_color = "#6c71c4", "#cb4b16"

    plt.plot(x1, y1, linestyle="-", linewidth=4, color=sgn_color, label="sgn")
    plt.scatter(0, 0, s=40, facecolors='none', linewidth=2, edgecolors=sgn_color)
    plt.plot(x2, y2, linestyle="-", linewidth=4, color=sgn_color)

    plt.plot(x, logistic, linestyle="dashed", linewidth=4, color=logistic_color, label="logistic")

    legend = plt.legend(loc='upper left', prop={'family': 'EB Garamond', 'size': 15})
    plt.setp(legend.get_texts())

    plt.show()
