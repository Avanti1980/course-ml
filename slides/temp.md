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

以回归问题为例，对任意样本$(\xv,y) \sim \Dcal$，均方误差可分解为

$$
\begin{align*}
    (f (\xv) & - y)^2 = (f (\xv) - \Ebb [y|\xv] + \Ebb [y|\xv] - y)^2 \\
    & = (f (\xv) - \Ebb [y|\xv])^2 + (\Ebb [y|\xv] - y)^2 + 2 (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y)
\end{align*}
$$

<div class="top-4"></div>

其中{==条件期望$\Ebb [y|\xv]$与$y$无关==}，对交叉项有

$$
\begin{align*}
    \Ebb_{(\xv,y)} & [(f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) ] \\
    & = \iint (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) \Pr(\xv, y) \diff \xv \diff y \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \left( \int (\Ebb [y|\xv] - y) \Pr(\xv, y) \diff y \right) \diff \xv \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \underbrace{ ( \Ebb [y|\xv] \Pr(\xv) - \Pr(\xv) \overbrace{ \class{yellow}{\int y \Pr(y|\xv) \diff y}}^{=~\Ebb [y|\xv]} )}_{=~0} \diff \xv = 0
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    \Ebb_{(\xv,y)} [(f (\xv) - y)^2] & = \Ebb_{(\xv,y)} [(\overbrace{f (\xv) - \Ebb [y|\xv]}^{\mathrm{independent~of~}y})^2] + \overbrace{\Ebb_{(\xv,y)} [(\Ebb [y|\xv] - y)^2]}^{\mathrm{noise~of~}y} \\
    & = \Ebb_{\xv} [(f (\xv) - \Ebb [y|\xv])^2] + \noise
\end{align*}
$$

<div class="top-4"></div>

第二项标记中的{==噪声==}是问题所固有的，{==与模型$f$的选择无关==}

根据第一项，使得泛化均方误差最小的$f^\star (\xv) = \Ebb [y|\xv]$

- 由于我们不知道$y$的分布，因此没法精确计算$\Ebb [y|\xv]$
- 如果数据足够多，也可以得到近乎准确的$\Ebb [y|\xv]$
- 但通常我们只有大小为$m$的数据集$D$
- 不同的$D$上训练得到不同的$f_D$，不同的$f_D$对$\xv$有不同的预测

<div class="top2"></div>

将数据集$D$的随机性也考虑进来，注意$\noise$与$D$无关，故

$$
\begin{align*}
    E = \Ebb_D \Ebb_{(\xv,y)} [(f_D (\xv) & - y)^2] = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \noise
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

泛化均方误差$E = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \noise$

引入$\xv$的{==期望预测==}$\Ebb_D [f_D (\xv)]$，易知有分解

$$
\begin{align*}
    & (f_D (\xv) - \Ebb [y|\xv])^2 = (f_D (\xv) - \Ebb_D [f_D (\xv)] + \Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \\
    & = (f_D (\xv) - \Ebb_D [f_D (\xv)])^2 + (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \\
    & \qquad + 2 (f_D (\xv) - \Ebb_D [f_D (\xv)]) (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])
\end{align*}
$$

{==注意$\Ebb_D [f_D (\xv)]$与$D$无关==}，对交叉项有

$$
\begin{align*}
    \Ebb_D & [(f_D (\xv) - \Ebb_D [f_D (\xv)]) (\overbrace{\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]}^{\mathrm{independent~of~}D})] \\
    & = (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]) \underbrace{\Ebb_D [f_D (\xv) - \Ebb_D [f_D (\xv)]]}_{=~0} = 0
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    E & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2] + \Ebb_{\xv} \Ebb_D [(\overbrace{\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]}^{\mathrm{independent~of~}D})^2] + \noise \\
    & = \underbrace{\Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]}_{\variance} + \underbrace{\Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2]}_{\bias^2} + \noise
\end{align*}
$$

<div class="top-2"></div>

综上，泛化均方误差的偏差方差分解为

$$
\begin{align*}
    \Ebb_{(\xv,y)} \Ebb_D [(f_D (\xv) - y)^2] = \bias^2 + \variance + \noise
\end{align*}
$$

- 偏差$\bias^2 = \Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2]$，{==学习算法的拟合能力==}
- 方差$\variance = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]$，{==对数据集扰动的敏感度==}
- 噪声$\noise = \Ebb_{(\xv,y)} [(\Ebb [y|\xv] - y)^2]$，问题固有，无法优化
