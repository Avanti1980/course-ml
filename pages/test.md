---
presentation:
  margin: 0
  center: false
  transition: "none"
  enableSpeakerNotes: true
  slideNumber: "c/t"
  navigationMode: "linear"
---

@import "../css/font-awesome-4.7.0/css/font-awesome.css"
@import "../css/theme/solarized.css"
@import "../css/logo.css"
@import "../css/font.css"
@import "../css/color.css"
@import "../css/margin.css"
@import "../css/table.css"
@import "../css/main.css"
@import "../plugin/zoom/zoom.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/menu/menu.js"
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-ml.js"

<!-- slide data-notes="" -->

##### 模型选择

---

设假设空间$\Hcal$的$\text{VC}$维为$d$，至少以$1 - \delta$的概率有

$$
\begin{align*}
    \quad & R (h_D^{\text{ERM}}) \le R_D (h_D^{\text{ERM}}) + \sqrt{\frac{8 d \ln (2em/d) + 8 \ln (4/\delta)}{m}} \\
    & R(h_D^{\text{ERM}}) \le R(h^\star) + \sqrt{\frac{32 d \ln (2em/d) + 32 \ln (8/\delta)}{m}}
\end{align*}
$$

启示

- 右边第一项随$\Hcal$复杂度的增加而减小，第二项随$\Hcal$复杂度的增加而增大，因此选择假设空间时既不能太复杂、也不能太简单，要跟任务相适应
- 样本数$m$可以一定程度上制衡$\Hcal$的复杂度，因此当数据量很大时，可以选择较复杂的$\Hcal$，这也解释了为何深度神经网络在大数据集上表现更好

<!-- slide vertical=true data-notes="" -->

##### 欠拟合 过拟合

---

数据分布：$p(x) = \Ucal[0,1]$，$y = \cos (3 \pi x  / 2) + \Ncal(0, 1) / 10$

学习算法：{==$n$阶多项式回归==}

$$
\begin{align*}
    \min_{w_j} ~ F (w_j) = \frac{1}{2} \sum_{i \in [m]} \left( \sum_{j=0}^n w_j x_i^j - y_i \right)^2
\end{align*}
$$

<div class="top-3"></div>

其中$w_0, w_1, \ldots, w_n$为待求参数

假设空间

- 1 阶多项式
- 4 阶多项式
- 30 阶多项式

@import "../python/overfitting-sample.svg" {.lefta .right8 .width40 .top-43per title="训练集"}

<!-- slide vertical=true data-notes="" -->

##### 欠拟合 过拟合

---

@import "../python/overfitting.svg" {.center .width90 .bottom2 title="过拟合"}

左图：1 阶多项式{==欠拟合==} (underfitting)，经验均方误差很大

<div class="top-4"></div>

中图：4 阶多项式拟合地最好，最贴近真实模型

<div class="top-4"></div>

右图：30 阶多项式{==过拟合==} (overfitting)，经验均方误差很小

<div class="top-2"></div>

我的启示 选对假设空间至关重要！

<!-- slide vertical=true data-notes="" -->

##### 模型选择 验证

---

事先确定一组候选模型集合$\{ f_1, f_2, \ldots, f_n \}$，从中挑选最好的

从训练集中随机选择一部分样本作为{==验证集==} (validation set)

- 在剩余的训练集上依次训练$f_1, f_2, \ldots, f_n$
- 在验证集上依次评估$f_1, f_2, \ldots, f_n$

<div class="top4"></div>

{==交叉验证==} (cross validation)：将训练集平均分为$n$份，第$i$轮

- 在其中的第$[n] \setminus \{ i \}$份上依次训练$f_1, f_2, \ldots, f_n$
- 在第$i$份上依次评估$f_1, f_2, \ldots, f_n$

遍历$i \in [n]$取平均作为$f_1, f_2, \ldots, f_n$的性能，从中挑选最好的

<!-- slide data-notes="" -->

##### 偏差方差分解

---

以回归问题为例，对任意样本$(\xv,y) \sim \Dcal$，均方误差可分解为

<div class="top0"></div>

$$
\begin{align*}
    \quad (f (\xv) & - y)^2 = (f (\xv) - \Ebb [y|\xv] + \Ebb [y|\xv] - y)^2 \\
    & = (f (\xv) - \Ebb [y|\xv])^2 + (\Ebb [y|\xv] - y)^2 + 2 (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y)
\end{align*}
$$

<div class="top-3"></div>

其中{==条件期望$\Ebb [y|\xv]$与$y$无关==}，对交叉项有

$$
\begin{align*}
    \quad \Ebb_{(\xv,y) \sim \Dcal} & [(f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) ] \\
    & = \iint (f (\xv) - \Ebb [y|\xv]) (\Ebb [y|\xv] - y) p(\xv, y) \diff \xv \diff y \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \left( \int (\Ebb [y|\xv] - y) p(\xv, y) \diff y \right) \diff \xv \\
    & = \int (f (\xv) - \Ebb [y|\xv]) \underbrace{ ( \Ebb [y|\xv] p(\xv) - p(\xv) \overbrace{ \class{yellow}{\int y \cdot p(y|\xv) \diff y}}^{=~\Ebb [y|\xv]} )}_{=~0} \diff \xv = 0
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    \quad \Ebb_{(\xv,y)} [(f (\xv) - y)^2] & = \Ebb_{(\xv,y)} [(\overbrace{f (\xv) - \Ebb [y|\xv]}^{\text{与}y\text{无关}})^2] + \overbrace{\Ebb_{(\xv,y)} [(\Ebb [y|\xv] - y)^2]}^{\text{与}f\text{无关}} \\
    & = \Ebb_{\xv} [(f (\xv) - \Ebb [y|\xv])^2] + \text{噪声}
\end{align*}
$$

- 根据第一项，使得泛化均方误差最小的$f^\star (\xv) = \Ebb [y|\xv]$，但由于真实分布$p(y|\xv)$未知，因此没法计算$\Ebb [y|\xv]$，$f^\star (\xv)$不可求
- 第二项{==噪声==}是不可知 (agnostic) 学习固有的，只和真实分布有关，{==与模型无关==}

<div class="top2"></div>

上面的式子是针对给定模型的，算法在不同数据集$D$上得到的模型$f_D$也不同，因此泛化均方误差

$$
\begin{align*}
    \quad E & = \Ebb_D \Ebb_{(\xv,y)} [(f_D (\xv) - y)^2] \\
    & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \text{噪声}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

泛化均方误差$E = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb [y|\xv])^2] + \text{噪声}$

引入$\xv$的{==期望预测==}$\Ebb_D [f_D (\xv)]$，易知有分解

<div class="top1"></div>

$$
\begin{align*}
    \quad (f_D (\xv) - \Ebb [y|\xv])^2 & = (f_D (\xv) - \Ebb_D [f_D (\xv)] + \Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \\
    & = (f_D (\xv) - \Ebb_D [f_D (\xv)])^2 + (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2 \\
    & \qquad + 2 (f_D (\xv) - \Ebb_D [f_D (\xv)]) (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])
\end{align*}
$$

{==注意$\Ebb_D [f_D (\xv)]$与$D$无关==}，对交叉项有

$$
\begin{align*}
    \quad \Ebb_D [(f_D (\xv) - \Ebb_D [& f_D (\xv)]) (\overbrace{\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]}^{\text{与}D\text{无关}})] \\
    & = (\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]) \underbrace{\Ebb_D [f_D (\xv) - \Ebb_D [f_D (\xv)]]}_{=~0} = 0
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 偏差方差分解

---

$$
\begin{align*}
    E & = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2] + \Ebb_{\xv} \Ebb_D [(\overbrace{\Ebb_D [f_D (\xv)] - \Ebb [y|\xv]}^{\text{与}D\text{无关}})^2] + \text{噪声} \\
    & = \underbrace{\Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]}_{\text{方差}} + \underbrace{\Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2]}_{\text{偏差 }^2} + \text{噪声}
\end{align*}
$$

<div class="top-3"></div>

综上，泛化均方误差可分解为$E = \text{偏差}^2 + \text{方差} + \text{噪声}$

- $\text{偏差}^2 = \Ebb_{\xv} [(\Ebb_D [f_D (\xv)] - \Ebb [y|\xv])^2]$，期望预测与最优模型预测的差别，体现{==学习算法的拟合能力==}，越小拟合能力越强
- $\text{方差} = \Ebb_{\xv} \Ebb_D [(f_D (\xv) - \Ebb_D [f_D (\xv)])^2]$，$D$上模型的预测与期望预测的差别，体现{==学习算法对数据集扰动的敏感度==}，越小越不敏感

<div class="top2"></div>

我的启示 我们要选择{==低偏差==}同时{==低方差==}的模型！

<!-- slide data-notes="" -->

##### 偏差方差分解

---

@import "../python/bias-var-dec.svg" {.center .width82 title="随机生成了 5 个数据集：1 阶多项式高偏差、低方差；30 阶多项式低偏差、高方差；4 阶多项式低偏差、低偏差，是最理想的模型"}

<!-- slide vertical=true data-notes="" -->

##### 偏差方差窘境

---

偏差、方差往往是两难选择，即便对于单模型亦存在

- 训练不足时，模型还很糙，拟合能力不强，偏差占主导
- 训练程度加深后，模型开始捕捉数据细节，方差占主导

@import "../tikz/bias-var-dec.svg" {.center .top5 .width45 title="很多学习算法都可控制训练程度，例如决策树可控制层数，神经网络可控制训练轮数，集成学习方法可控制基学习器个数"}
