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

##### 最大化模型证据 解释

---

极大似然 vs. 最大后验

$$
\begin{align*}
    \quad \min_\wv & \frac{1}{2} \| \yv - \Phiv \wv \|_2^2 \Longrightarrow \wv^{\text{ML}} = (\Phiv^\top \Phiv)^{-1} \Phiv^\top \yv \\
    \min_\wv & \left\{ \frac{\beta}{2} \| \yv - \Phiv \wv \|_2^2 + \frac{\alpha}{2} \|\wv\|_2^2 \right\} \Longrightarrow \wv^{\text{MAP}} = (\beta \Phiv^\top \Phiv + \alpha \Iv)^{-1} \beta \Phiv^\top \yv
\end{align*}
$$

设$\beta \Phiv^\top \Phiv$对应于$\lambda_i$的特征向量为$\uv_i$，且全部已标准正交化

$$
\begin{align*}
    \quad \beta \Phiv^\top \Phiv & \underbrace{\begin{bmatrix} \uv_1 & \cdots & \uv_n \end{bmatrix}}_{\Uv} = \underbrace{\begin{bmatrix} \uv_1 & \cdots & \uv_n \end{bmatrix}}_{\Uv} \underbrace{\begin{bmatrix} \lambda_1 \\ & \ddots \\ & & \lambda_n \end{bmatrix}}_{\Lambdav} \\[-4pt]
    \Longrightarrow ~ & \beta \Phiv^\top \Phiv = \Uv \Lambdav \Uv^\top \\
    & (\beta \Phiv^\top \Phiv)^{-1} = \Uv \Lambdav^{-1} \Uv^\top, ~ (\beta \Phiv^\top \Phiv + \alpha \Iv)^{-1} = \Uv (\Lambdav + \alpha \Iv)^{-1} \Uv^\top
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 最大化模型证据 解释

---

极大似然 vs. 最大后验

$$
\begin{align*}
    \quad \wv^{\text{ML}} & = (\Phiv^\top \Phiv)^{-1} \Phiv^\top \yv = \Uv \Lambdav^{-1} \Uv^\top \beta \Phiv^\top \yv \\
    & = \begin{bmatrix} \uv_1 & \cdots & \uv_n \end{bmatrix} \begin{bmatrix} \uv_1^\top / \lambda_1 \\ \vdots \\ \uv_n^\top / \lambda_n \end{bmatrix} \beta \Phiv^\top \yv = \sum_{i \in [n]} \uv_i \frac{\beta \uv_i^\top \Phiv^\top \yv}{\lambda_i} \\[4pt]
    \wv^{\text{MAP}} & = (\beta \Phiv^\top \Phiv + \alpha \Iv)^{-1} \beta \Phiv^\top \yv = \Uv (\Lambdav + \alpha \Iv)^{-1} \Uv^\top \beta \Phiv^\top \yv \\
    & = \begin{bmatrix} \uv_1 & \cdots & \uv_n \end{bmatrix} \begin{bmatrix} \uv_1^\top / (\lambda_1 + \alpha) \\ \vdots \\ \uv_n^\top / (\lambda_n + \alpha) \end{bmatrix} \beta \Phiv^\top \yv = \sum_{i \in [n]} \uv_i \frac{\beta \uv_i^\top \Phiv^\top \yv}{\lambda_i + \alpha}
\end{align*}
$$

<div class="top-2"></div>

以$\uv_1, \ldots, \uv_n$为坐标轴表示解空间，则$\wv^{\text{MAP}}$、$\wv^{\text{ML}}$在第$i$个轴上的坐标分别为$\frac{\beta \uv_i^\top \Phiv^\top \yv}{\lambda_i + \alpha}$、$\frac{\beta \uv_i^\top \Phiv^\top \yv}{\lambda_i}$，比值为$\frac{\lambda_i}{\lambda_i + \alpha}$

<!-- slide vertical=true data-notes="" -->

##### 最大化模型证据 解释

---

在第$i$个轴上，$\wv^{\text{MAP}}$与$\wv^{\text{ML}}$的坐标比值为$\frac{\lambda_i}{\lambda_i + \alpha}$

- 若$\lambda_i \gg \alpha$，则比值接近$1$，$\wv^{\text{MAP}}$很接近于$\wv^{\text{ML}}$，这个方向很重要
- 若$\lambda_i \ll \alpha$，则比值接近$0$，$\wv^{\text{MAP}}$很接近零，这个方向不重要
- $\gamma = \sum_{i \in [n]}$表示先验“筛选”出的有效变量个数

<div class="top6"></div>

$$
\begin{align*}
    \quad \frac{1}{\beta^{\text{ML}}} = \frac{1}{m} \| \yv - \Phiv \wv^{\text{ML}} \|_2^2, \quad \frac{1}{\beta} = \frac{1}{m - \gamma} \| \yv - \Phiv \wv^{\text{MAP}} \|_2^2
\end{align*}
$$

- 类似于极大似然估计高斯分布的方差除以$m$是有偏的，除以$m-1$无偏，因为有一个自由度被用于估计均值和校正极大似然的偏差
- 贝叶斯线性回归的先验决定用$\gamma$个自由度估计均值和校正极大似然的偏差，因此估计$\beta$除以$m - \gamma$

<!-- slide data-notes="" -->

##### 频率 <span style="font-weight:900">_vs._</span> 贝叶斯

---

在机器学习中的区别：是否考虑先验

当观测数据量很大时，先验 (伪数据) 就无足轻重了，两种做法不会有太大差别

当观测数据量不大时，先验对模型性能有显著影响 (归纳偏好)

- 先验是主观的，纯人为选取，没有标准
- 抛硬币问题选贝塔分布做先验就是图计算方便
- 利用共轭先验可以不用显式地积分求$p(X)$，肉眼就能看出结果

<div class="top2"></div>

先验需有适当的自由度，能通过调整参数灵活表示领域知识
