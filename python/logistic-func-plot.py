import matplotlib.pyplot as plt
import numpy as np

r = 10

x = np.arange(-r, r, 0.02)
logistic = 1 / (1 + np.exp(-x))
y = np.sign(np.abs(x))

plt.axis([-5.1, 5.1, -0.1, 1.1])

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

    plt.plot(x, y, linestyle="dashed", linewidth=4, color=sgn_color)

    plt.plot(x, logistic, linestyle="-", linewidth=4, color=logistic_color, label="logistic")

    legend = plt.legend(loc='center left', prop={'family': 'EB Garamond', 'size': 15})
    plt.setp(legend.get_texts())

    plt.show()
