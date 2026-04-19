import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from sklearn.neighbors import KernelDensity
from sklearn.utils.fixes import parse_version

np.random.seed(1)

dim = [2, 3, 10, 100, 1000, 10000]
# dim = [2, 3, 10, 100]
m = 2000

with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(2, 3, constrained_layout=True)

    i = 0
    for axi in ax.ravel():
        d = dim[i]
        print(d)
        X = np.random.rand(m, d)
        Z = np.random.rand(m, d)
        X = np.linalg.norm(X-Z, ord=2, axis=1, keepdims=True)

        axi.hist(X, bins=50, density=True)
        axi.set_xlim(0, np.sqrt(d))
        axi.set_title(str(d) + ' dims', color='#586e75')

        i += 1

    for axi in ax[1, :]:
        axi.set_xlabel('distance')

    for axi in ax[:, 0]:
        axi.set_ylabel('frequency')

plt.show()
