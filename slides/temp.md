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
