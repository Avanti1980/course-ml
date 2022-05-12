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
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-entropy.js"

<!-- slide data-notes="" -->

##### 增益率 基尼指数

---

信息增益偏好取值数目多的属性，将“次序”加入属性集会如何？

{==C4.5 决策树==}：使用增益率选择最优划分属性

$$
\begin{align*}
    \qquad \mathrm{Gain\_ratio} = \frac{\gain(D,a)}{\mathrm{IV}(a)}, \quad \mathrm{IV}(a) = -\sum_{v \in [V]} \frac{|D_v|}{|D|} \log \frac{|D_v|}{|D|}
\end{align*}
$$

{==分类回归树==} (<u>c</u>lassification <u>a</u>nd <u>r</u>egression <u>t</u>ree, CART)

$$
\begin{align*}
    \qquad & \gini(D) = \sum_{k \in [C]} \sum_{k' \ne k} p_k p_{k'}, \quad \mathrm{Gini\_index} (D,a) = \sum_{v \in [V]} \frac{|D_v|}{|D|} \gini(D_v)
\end{align*}
$$

<div class="top-2"></div>

- 基尼值等于从$D$中随机抽两个样本，其标记不一致的概率，{==越小越纯==}
- 分类回归树：$a^\star = \argmin_{a \in A} ~ \mathrm{Gini\_index} (D,a)$
