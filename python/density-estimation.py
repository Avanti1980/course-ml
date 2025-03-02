import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

np.random.seed(1)
N = 20
X = np.concatenate((norm.rvs(0, 1, int(0.3 * N)), norm.rvs(5, 1, int(0.7 * N))))
X_plot = np.linspace(-5, 10, 1000)
bins = np.linspace(-5, 10, 10)

with plt.style.context('Solarize_Light2'):

    plt.figure(figsize=(16, 5))

    fig, ax = plt.subplots(1, 3, sharey=True)
    fig.subplots_adjust(hspace=0.05, wspace=0.05)

    # histogram 1
    ax[0].hist(X, bins=bins, density=True)
    ax[0].text(-3.5, 0.31, "Histogram")
    ax[0].set_ylabel('Density')

    # histogram 2
    ax[1].hist(X, bins=bins + 0.75, density=True)
    ax[1].text(-3.5, 0.31, "Bins right shifted 0.75")

    # histogram 2
    ax[2].hist(X, bins=bins - 0.75, density=True)
    ax[2].text(-3.5, 0.31, "Bins left shifted 0.75")

    for axi in ax.ravel():
        axi.plot(X, np.full(len(X), -0.01), '+k')
        axi.set_xlim(-4, 9)
        axi.set_ylim(-0.02, 0.34)
        axi.set_xlabel('x')

    plt.savefig('density-estimation-1.svg', transparent=True)
    plt.show()
