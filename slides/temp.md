---
presentation:
  margin: 0
  center: false
  slideNumber: "c/t"
  navigationMode: "linear"
---

@import "../css/theme/solarized.css"
@import "../css/logo.css"
@import "../css/font.css"
@import "../css/color.css"
@import "../css/margin.css"
@import "../css/table.css"
@import "../css/main.css"

<!-- slide data-notes="" -->

##### 偏差方差分解

---

对回归问题，

$$
\begin{align*}
    \iint (f(\xv) - y)^2 \Pr(\xv, y) \diff \xv \diff y
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

对任意样本$\xv$，设

- $y$为其真实标记
- $y_D$为其在数据集$D$中的标记，可能不等于$y$，即存在噪声
- $f_D (\xv)$为数据集$D$上的训得的模型$f$对$\xv$的预测

<div class="top2"></div>

对回归任务，样本数相同的不同数据集$D \sim \Dcal^m$，学习算法的

- 噪声为$\varepsilon^2 = \Ebb_D [(y_D - y)^2]$，并假定噪声期望为零，即$\Ebb_D [y_D - y] = 0$
- 期望预测为$\bar{f}(\xv) = \Ebb_D [f_D (\xv)]$
- 预测方差为$\var(\xv) = \Ebb_D [(f_D (\xv) - \bar{f}(\xv))^2]$，{==数据扰动造成的影响==}
- 预测偏差为$\bias^2(\xv) = (\bar{f}(\xv) - y)^2$，{==学习算法本身的拟合能力==}

<div class="top2"></div>

下面考虑对{==泛化误差==}$\Ebb_D [(f_D (\xv) - y_D)^2]$进行分解

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    & \quad ~ \Ebb_D [(f_D (\xv) - y_D)^2] = \Ebb_D [(f_D (\xv) \class{yellow}{- \bar{f}(\xv) + \bar{f}(\xv)} - y_D)^2] \\
    & = \underbrace{\Ebb_D [(f_D (\xv) - \bar{f}(\xv))^2]}_{\var(\xv)} + \Ebb_D [(\bar{f}(\xv) - y_D)^2] \\
    & \qquad \qquad + 2 \Ebb_D [(f_D (\xv) - \bar{f}(\xv))(\bar{f}(\xv) - y_D)] \\
    & = \var(\xv) + \Ebb_D [(\bar{f}(\xv) \class{yellow}{- y + y} - y_D)^2] + 2 \overbrace{\underbrace{\Ebb_D [f_D (\xv) - \bar{f}(\xv)]}_{=~0} \Ebb_D [\bar{f}(\xv) - y_D]}^{\text{噪声不依赖于f}} \\
    & = \var(\xv) + \Ebb_D [(\bar{f}(\xv) - y)^2] + \underbrace{\Ebb_D [(y - y_D)^2]}_{\varepsilon^2} + 2 \Ebb_D [(\bar{f}(\xv) - y)(y - y_D)] \\
    & = \var(\xv) + \underbrace{(\bar{f}(\xv) - y)^2}_{\bias^2(\xv)} + \varepsilon^2 + 2 \Ebb_D [\bar{f}(\xv) - y] \underbrace{\Ebb_D [y - y_D]}_{=~0} \\
    & = \var(\xv) + \bias^2(\xv) + \varepsilon^2
\end{align*}
$$
