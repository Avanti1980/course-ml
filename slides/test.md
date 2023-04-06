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

##### 支持向量机 对偶问题

---

支持向量机原问题：

$$
\begin{align*}
    \quad \min_{\wv,b} ~ f(\wv) = \frac{1}{2} \|\wv\|_2^2, \quad \st ~ y_i (\wv^\top \xv_i + b) \ge 1, ~ \forall i \in [m]
\end{align*}
$$

引入拉格朗日乘子$\alphav \ge \zerov$，拉格朗日函数为

$$
\begin{align*}
    \quad L(\wv, b, \alphav) = \frac{1}{2} \|\wv\|_2^2 - \sum_{i \in [m]} \alpha_i (y_i (\wv^\top \xv_i + b) - 1)
\end{align*}
$$

<div class="top-2"></div>

定义对偶函数$g(\alphav) = \min_{\wv,b} L(\wv, b, \alphav)$，于是

$$
\begin{align*}
    \quad g(\alphav) = \min_{\wv,b} L(\wv, b, \alphav) \le L(\wv, b, \alphav) \le f(\wv)
\end{align*}
$$

<div class="top-2"></div>

- 上式对任意可行的$\wv$均成立
- 设原问题最优解为$\wv^\star$，则$g(\alphav) \le f(\wv^\star) \triangleq p^\star$

<!-- slide data-notes="" -->

##### 支持向量机 对偶问题

---

对$\forall \alphav \ge \zerov$，对偶函数$g(\alphav)$给出了原问题最优值$p^\star$的一个下界

所有下界中最好的下界有多好？即最紧的下界是啥？

$$
\begin{align*}
    \quad \max_{\alphav} ~ g(\alphav), \quad \st ~ \alphav \ge \zerov
\end{align*}
$$
