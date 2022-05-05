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

以回归问题为例，对任意样本$(\xv,y)$，其均方误差可分解为

$$
\begin{align*}
    (f (\xv) & - y)^2 = (f (\xv) - \Ebb [y|\xv] + \Ebb [y|\xv] - y_)^2 \\
    & = (f (\xv) - \Ebb [y|\xv])^2 + (\Ebb [y|\xv] - y)^2 + 2 (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y)
\end{align*}
$$

<div class="top-2"></div>

{==注意$\Ebb [y|\xv] = \int y ~ \Pr (y | \xv) \diff y$与$y$无关==}，对交叉项有

$$
\begin{align*}
    \Ebb_{(\xv,y)} & [(f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) ] \\
    & = \iint (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) \Pr(\xv, y) \diff \xv \diff y \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \left( \int (\Ebb [y|\xv] - y) \Pr(\xv, y) \diff y \right) \diff \xv \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \underbrace{\left( \Ebb [y|\xv] \Pr(\xv) - \int y \Pr(y|\xv) \Pr(\xv) \diff y \right)}_{=~0} \diff \xv = 0
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    \Ebb_{(\xv,y)} [(f (\xv) - y)^2] & = \Ebb_{(\xv,y)} [(f (\xv) - \Ebb [y|\xv])^2] + \Ebb_{(\xv,y)} [(\Ebb [y|\xv] - y)^2] \\
    & = \Ebb_{\xv} [(f (\xv) - \Ebb [y|\xv])^2] + \underbrace{\Ebb_{(\xv,y)} [(\Ebb [y|\xv] - y)^2]}_{\mathrm{noise~of~}y}
\end{align*}
$$

<div class="top-4"></div>

第二项是标记中的{==噪声==}，问题所固有的，{==与模型$f$的选择无关==}

我们能做的就是选取模型$f$使得第一项尽可能小

- 如果数据足够多，可以得到精确的$\Ebb [y|\xv]$，令$f(\xv) = \Ebb [y|\xv]$即可
- 但通常我们只有大小为$m$的数据集$D$
- 不同的$D$上训练得到不同的$f_D$，不同的$f_D$对$\xv$有不同的预测

<div class="top2"></div>

注意$\noise$与$D$无关，故泛化均方误差$E$分解为

$$
\begin{align*}
    E = \Ebb_{(\xv,y)} \Ebb_D [(f_D (\xv) & - y)^2] = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \noise
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

泛化均方误差$E = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \noise$

引入$\xv$的期望预测$\Ebb_D [f_D (\xv)]$，易知有分解

$$
\begin{align*}
    & (f_D (\xv) - \Ebb [y|\xv])^2 = (f_D (\xv) \class{yellow}{- \Ebb_D [f_D (\xv)] + \Ebb_D [f_D (\xv)]} - \Ebb [y|\xv])^2 \\
    & = (f_D (\xv) - \Ebb_D [f_D (\xv)])^2 + (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \\
    & \qquad + 2 (f_D (\xv) - \Ebb_D [f_D (\xv)]) (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])
\end{align*}
$$

{==注意$\Ebb_D [f_D (\xv)]$与$D$无关==}，对交叉项有

$$
\begin{align*}
    \Ebb_D & [(f_D (\xv) - \Ebb_D [f_D (\xv)]) (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])] \\
    & = (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]) \underbrace{\Ebb_D [f_D (\xv) - \Ebb_D [f_D (\xv)]]}_{=~0} = 0 \\
    & \qquad \Downarrow \\
    E & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2] + \Ebb_{\xv} \Ebb_D [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2] + \noise \\
    & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2] + \Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2] + \noise
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

综上，泛化均方误差分解为

$$
\begin{align*}
    \Ebb_{(\xv,y)} \Ebb_D [(f_D (\xv) & - y)^2] = \bias^2 + \variance + \noise
\end{align*}
$$

<div class="top-4"></div>

其中

$$
\begin{align*}
    \bias^2 & = \Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2] = \int (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \Pr (\xv) \diff \xv \\
    \variance & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]
\end{align*}
$$


- 噪声为$\varepsilon^2 = \Ebb_D [(y_D - y)^2]$，并假定噪声期望为零，即$\Ebb_D [y_D - y] = 0$
- 期望预测为$\Ebb_D [f_D (\xv)] = \Ebb_D [f_D (\xv)]$
- 预测方差为$\var(\xv) = \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]$，{==数据扰动造成的影响==}
- 预测偏差为$\bias^2(\xv) = (\Ebb_D [f_D (\xv)] - y)^2$，{==学习算法本身的拟合能力==}

<div class="top2"></div>

下面考虑对{==泛化误差==}$\Ebb_D [(f_D (\xv) - y_D)^2]$进行分解

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    & \quad ~ \Ebb_D [(f_D (\xv) - y_D)^2] = \Ebb_D [(f_D (\xv) \class{yellow}{- \Ebb_D [f_D (\xv)] + \Ebb_D [f_D (\xv)]} - y_D)^2] \\
    & = \underbrace{\Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]}_{\var(\xv)} + \Ebb_D [(\Ebb_D [f_D (\xv)] - y_D)^2] \\
    & \qquad \qquad + 2 \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])(\Ebb_D [f_D (\xv)] - y_D)] \\
    & = \var(\xv) + \Ebb_D [(\Ebb_D [f_D (\xv)] \class{yellow}{- y + y} - y_D)^2] + 2 \overbrace{\underbrace{\Ebb_D [f_D (\xv) - \Ebb_D [f_D (\xv)]]}_{=~0} \Ebb_D [\Ebb_D [f_D (\xv)] - y_D]}^{\text{噪声不依赖于f}} \\
    & = \var(\xv) + \Ebb_D [(\Ebb_D [f_D (\xv)] - y)^2] + \underbrace{\Ebb_D [(y - y_D)^2]}_{\varepsilon^2} + 2 \Ebb_D [(\Ebb_D [f_D (\xv)] - y)(y - y_D)] \\
    & = \var(\xv) + \underbrace{(\Ebb_D [f_D (\xv)] - y)^2}_{\bias^2(\xv)} + \varepsilon^2 + 2 \Ebb_D [\Ebb_D [f_D (\xv)] - y] \underbrace{\Ebb_D [y - y_D]}_{=~0} \\
    & = \var(\xv) + \bias^2(\xv) + \varepsilon^2
\end{align*}
$$
