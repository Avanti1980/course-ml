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

##### 特征变换

---

模型学习前的最后一步，亦有将该步与模型学习融合的做法

<div class="invis bottom2">

当部分特征冗余甚至有害时，挑选或生成有用的特征子集

- 去除低方差特征，特别是那些在所有样本上取值均不变的特征
- 先计算 F 检验值、卡方检验值、互信息、线性相关性等统计量，然后据此设立阈值选择特征
- 引入$\ell_1$等稀疏范数作为约束，将选择特征与模型学习合二为一
- 通过 PCA、随机投影等降维技术浓缩现有特征

</div>

当特征稀缺时，利用现有特征构造新的特征

- 凭经验显式构造：$[x_1; x_2] \xrightarrow{\Rbb^2 \mapsto \Rbb^6} [x_1^2; x_2^2; \sqrt{2} x_1 x_2; \sqrt{2} x_1; \sqrt{2} x_2; 1]$
- 利用核函数$\kappa(\xv, \zv) = \phi(\xv)^\top \phi(\zv)$隐式构造，代表性方法为支持向量机
- 利用非线性函数复合$f_n ( f_{n-1} ( \cdots f_2 (f_1 (\xv))))$，代表性方法为神经网络

<!-- slide vertical=true data-notes="" -->

##### 特征变换 构造新特征

---

凭经验显式构造映射$\phi$，如二次多项式特征：

$$
\begin{align*}
    \xv = [x_1; x_2] \xrightarrow{\phi: ~ \Rbb^2 \mapsto \Rbb^6} \xvt = [x_1^2; x_2^2; \sqrt{2} x_1 x_2; \sqrt{2} x_1; \sqrt{2} x_2; 1]
\end{align*}
$$

@import "../tikz/kernel.svg" {.center .top0 .bottom4 .width80}

- 圆内是一类样本，圆外是另一类样本，它们无法{==线性可分==}
- 令$[x_1; x_2] \mapsto [z_1 = x_1^2; z_2 = x_2^2]$，在新的$(z_1,z_2)$空间中就线性可分了

<div class="top3"></div>

$$
\begin{align*}
    \qquad \qquad \qquad x_1^2 + x_2^2 \le t ~ \longrightarrow ~ z_1 + z_2 \le t
\end{align*}
$$

<!-- slide data-notes="" -->

##### 特征变换 核技巧

---

显式构造映射$\phi$过于依赖使用者的姿势水平，若后续模型学习

- 不需要样本$\xv$的新特征的显式表示$\phi(\xv)$
- 只用到新特征空间的内积$\phi(\xv)^\top \phi(\zv)$

对映射$\phi([x_1;x_2]) = [x_1^2; x_2^2; \sqrt{2} x_1 x_2; \sqrt{2} x_1; \sqrt{2} x_2; 1]$和样本$\xv,\zv$有

$$
\begin{align*}
    \phi(\xv)^\top \phi(\zv) & = x_1^2 z_1^2 + x_2^2 z_2^2 + 2 x_1 x_2 z_1 z_2 + 2 x_1 z_1 + 2 x_2 z_2 + 1 \\
    & = (x_1 z_1 + x_2 z_2 + 1)^2 \\
    & = (\xv^\top \zv + 1)^2 \\
    & = \kappa (\xv, \zv)
\end{align*}
$$

<div class="top-2"></div>

换言之构造新特征有两套方案：

- 显式构造核映射$\phi([x_1;x_2]) = [x_1^2; x_2^2; \sqrt{2} x_1 x_2; \sqrt{2} x_1; \sqrt{2} x_2; 1]$
- 通过在原空间直接定义{==核函数==}$\kappa (\xv, \zv) = (\xv^\top \zv + 1)^2$隐式构造

<!-- slide data-notes="" -->

##### 特征变换 核函数

---

核函数$\kappa(\cdot, \cdot)$是双变量对称函数，常见的有：

- 线性核$\kappa (\xv, \zv) = \xv^\top \zv$，相当于用了恒等核映射$\phi(\xv) = \xv$
- 多项式核$\kappa (\xv, \zv) = (\xv^\top \zv + k)^d$，$k = 0$则为齐次多项式核，$d \in \Zbb_+$
- 高斯核$\kappa (\xv, \zv) = \exp (- \| \xv - \zv \|^2 / 2 \sigma^2)$，$\sigma > 0$为高斯核的带宽 (width)
- 拉普拉斯核$\kappa (\xv, \zv) = \exp (- \| \xv - \zv \| / \sigma)$，$\sigma > 0$

将 PCA 中的样本$\xv$用$\phi(\xv)$替代即核 PCA，先升维再降维

$\qquad \max \limits_{\|\wv\|_2^2 = 1} \wv^\top \Xv^\top \Xv \wv \overset{\phi}{\longrightarrow} \max \limits_{\|\wv\|_2^2 = 1} \wv^\top \phi(\Xv)^\top \phi(\Xv) \wv$

其中$\Xv = \begin{bmatrix} \xv_1^\top \\ \vdots \\ \xv_m^\top \end{bmatrix}$、$\phi(\Xv) = \begin{bmatrix} \phi(\xv_1)^\top \\ \vdots \\ \phi(\xv_m)^\top \end{bmatrix}$，注意$\wv$的维度不一样

<!-- slide vertical=true data-notes="" -->

##### 特征变换 核 <span style="font-weight:900">PCA</span>

---

问题：如何让模型中只出现内积$\phi(\xv_i)^\top \phi(\xv_j)$的形式？

对$\wv$做正交分解$\wv = \sum_{i \in [m]} \alpha_i \phi(\xv_i) + \vv = \phi(\Xv)^\top \alphav + \vv$，其中

$$
\begin{align*}
    \qquad \qquad \vv \perp \span \{ \phi(\xv_1), \ldots, \phi(\xv_m) \} ~ \Longrightarrow ~ \phi(\Xv) \vv = \zerov
\end{align*}
$$

<div class="top-4"></div>

于是

$$
\begin{align*}
    \qquad \|\wv\|_2^2 & = \alphav^\top \phi(\Xv) \phi(\Xv)^\top \alphav + \vv^\top \vv = \alphav^\top \Kv \alphav + \vv^\top \vv \\
    \qquad \phi(\Xv) \wv & = \phi(\Xv) (\phi(\Xv)^\top \alphav + \vv) = \phi(\Xv) \phi(\Xv)^\top \alphav = \Kv \alpha \\
    \qquad \Kv & = \phi(\Xv) \phi(\Xv)^\top = \begin{bmatrix} \phi(\xv_1)^\top \phi(\xv_1) & \cdots & \phi(\xv_1)^\top \phi(\xv_m) \\ \vdots & \ddots & \vdots \\ \phi(\xv_m)^\top \phi(\xv_1) & \cdots & \phi(\xv_m)^\top \phi(\xv_m) \end{bmatrix}
\end{align*}
$$

<div class="top-2"></div>

核 PCA 可重写为 $\max_{\alphav, \vv} ~ \alphav^\top \Kv \Kv \alphav, ~ \st ~ \alphav^\top \Kv \alphav + \vv^\top \vv = 1$

<!-- slide vertical=true data-notes="" -->

##### 特征变换 核 <span style="font-weight:900">PCA</span>

---

核 PCA：$\max_{\alphav, \vv} ~ \alphav^\top \Kv \Kv \alphav, ~ \st ~ \alphav^\top \Kv \alphav + \vv^\top \vv = 1$

设最优解为$(\alphav_\star, ~ \vv_\star)$，下面说明$\vv_\star = \zerov$

- 若$\vv_\star^\top \vv_\star = c > 0$，则$\alphav_\star^\top \Kv \alphav_\star = 1 - c < 1$
- $(\alphav_0 = 1 / \sqrt{1-c} ~ \alphav_\star, ~ \vv_0 = \zerov)$也是一组可行解
- 显然$\alphav_0^\top \Kv \Kv \alphav_0 = \alphav_\star^\top \Kv \Kv \alphav_\star / (1-c) > \alphav_\star^\top \Kv \Kv \alphav_\star$，这与$\alphav_\star$最优矛盾

<div class="top2"></div>

核 PCA 的最终形式为 $\max_\alphav ~ \alphav^\top \Kv \Kv \alphav, ~ \st ~ \alphav^\top \Kv \alphav = 1$

通过拉格朗日乘子法求得$\alphav$后，样本$\xv_j$在成分$\wv$上的投影为

$$
\begin{align*}
    \qquad \wv^\top \phi(\xv_j) = \sum_{i \in [m]} \alpha_i \phi(\xv_i)^\top \phi(\xv_j) = \sum_{i \in [m]} \alpha_i \kappa (\xv_i, \xv_j)
\end{align*}
$$

<div class="top-4"></div>

通过核 PCA 可以看出，全程我们都用不到$\phi(\cdot)$，只需要$\kappa(\cdot, \cdot)$

<!-- slide data-notes="" -->

##### 特征变换 非线性复合

---

设$\sigma_1, \ldots, \sigma_l$是一系列简单的非线性函数，如$[x]_+ = \max \{ x, 0 \}$

一个简单的$l$层神经网络：

$$
\begin{align*}
    \hv_1 & = \sigma_1(\Wv_1 \xv + \bv_1) \\
    \hv_2 & = \sigma_2(\Wv_2 \hv_1 + \bv_2) \\
    & \vdots \\
    \hv_{l-1} & = \sigma_{l-1}(\Wv_{l-1} \hv_{l-2} + \bv_{l-1}) \\
    f(\xv) & = \sigma_l (\Wv_l \hv_{l-1} + \bv_l)
\end{align*}
$$

<div class="top-4"></div>

前$l-1$层复合可视为特征变换，最后一层为模型学习

对比

- 核方法毕其功于一役，难点在于{==如何设计核函数==}
- 神经网络一步一个小目标，难点在于{==如何设计一系列非线性函数==}
