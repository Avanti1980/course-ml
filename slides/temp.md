---
presentation:
  margin: 0
  center: false
  transition: "convex"
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

##### 频率 _vs._ 贝叶斯

---

在机器学习中体现出的区别：是否考虑先验

当观测数据量很大时，先验 (伪数据) 就无足轻重了，两种做法不会有太大差别

当观测数据量不大时，先验对模型性能有显著影响 (归纳偏好)

- 先验是主观的，纯人为选取，没有标准
- 抛硬币问题选贝塔分布做先验就是图计算方便
- 利用共轭先验可以不用积分显式地求$\Pbb(X)$，肉眼就能看出结果

<div class="top2"></div>

先验需有适当的自由度，通过调参数灵活表示领域知识

<!-- slide data-notes="" -->

##### 再看朴素贝叶斯

---

朴素贝叶斯引入{==条件独立性假设==}，将似然分解为

$$
\begin{align*}
    \qquad \Pbb(\xv | y) = \Pbb(x_1 | y) \Pbb(x_2 | y) \cdots \Pbb(x_d | y) = \prod_{j \in [d]} \Pbb(x_j | y)
\end{align*}
$$

<div class="top-4"></div>

通过极大似然估计$\Pbb(y), ~ \Pbb(x_1 | y), ~ \Pbb(x_2 | y), ~ \ldots, ~ \Pbb(x_d | y)$

根据贝叶斯公式有

$$
\begin{align*}
    \argmax_{\Theta} p(\Theta | \Scal) = \argmax_{\Theta} \frac{p(\Scal | \Theta) p(\Theta)}{p(\Scal)} = \argmax_{\Theta} p(\Scal | \Theta) p(\Theta)
\end{align*}
$$

因此相对于极大似然估计，最大后验概率估计就是将先验$p(\Theta)$也考虑了进来
