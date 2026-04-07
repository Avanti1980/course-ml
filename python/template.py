import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('pgf')


# 如果中文、西文、公式分别用不同的字体，只能用下面的方案
plt.rcParams.update({
    "text.usetex": True,
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "pgf.preamble": (
        r"\usepackage{fontspec}"
        r"\usepackage{unicode-math}"
        r"\setsansfont{Ysabeau Office}"
        r"\usepackage{xeCJK}"
        r"\setCJKmainfont{LXGW Neo ZhiSong Screen Full}"
        r"\setmathfont{NewCMMath-Book.otf}"
    ),
    "axes.unicode_minus": True,
    "font.size": 10
})

fig, axs = plt.subplots(1, 2, figsize=(10, 8), sharex=True, sharey=True)
fig.suptitle('abcdefg这是全局标题$\\sin \\theta = a^2$', fontsize=16)

plt.savefig("template.pdf", transparent=True, bbox_inches="tight")
