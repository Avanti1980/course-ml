import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as st

plt.rcParams.update({
    "font.family": ["Ysabeau Office", "LXGW Neo ZhiSong Screen Full"],
    "mathtext.fontset": "cm",
    "axes.unicode_minus": True,
    "savefig.bbox": "tight",
    'legend.fontsize': 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    'text.color': '#586e75',
})

row, col = 5, 5
with plt.style.context('Solarize_Light2'):
    fig, ax = plt.subplots(row, col, figsize=(3 * row, 3 * col), sharex=True, sharey=True)
    for r in range(row):
        for c in range(col):
            x = np.linspace(0, 1, 100)
            a, b = r + 1, c + 1
            sns.lineplot(x=x, y=st.beta.pdf(x, a, b), label=rf'$\alpha = {a}, \beta = {b}$', ax=ax[r, c])
            ax[r, c].legend(labelcolor="#d33682")
    fig.subplots_adjust(wspace=0.05, hspace=0.05)
    fig.savefig("plot-beta-function.svg")
