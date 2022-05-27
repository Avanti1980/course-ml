import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))
tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

plt.axis([-5.1, 5.1, -1.1, 1.1])

with plt.style.context('Solarize_Light2'):

    ax = plt.gca()

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    ax.xaxis.set_ticks_position('top')
    ax.spines['top'].set_position(('data', 0))

    ax.yaxis.set_ticks_position('right')
    ax.spines['right'].set_position(('data', 0))

    plt.plot(x, logistic, linestyle="-", linewidth=2, label="logistic")
    plt.plot(x, tanh, linestyle="dashed", linewidth=2, label="tanh")

    legend = plt.legend(loc='upper left', prop={'family': 'EB Garamond', 'size': 15})
    plt.setp(legend.get_texts())

    plt.show()
