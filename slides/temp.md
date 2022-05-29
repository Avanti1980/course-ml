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

##### 从数据中估计概率

---

<div class="top2"></div>

$$
\begin{align*}
    \qquad \Pr(y | \xv) = \Pr(y) \cdot \Pr(x_1 | y) \cdot \Pr(x_2 | y) \cdots \Pr(x_d | y)
\end{align*}
$$

对于先验，记$\alpha_k = \Pr(y = k)$，$\Delta_K$是$K$维单纯形，于是

$$
\begin{align*}
    \qquad \Pr(y;\alphav) = \prod_{k \in [c]} \Pr(y = k)^{\Ibb(y=k)} = \prod_{k \in [c]} \alpha_k^{\Ibb(y=k)}
\end{align*}
$$

对于似然，记$\theta_{dk}$为第$k$类文本选取$v_d$的概率，$x_d$为$v_d$在文本$\xv$中出现的次数，于是

$$
\begin{align*}
    [\theta_{1k}; \theta_{2k}; \ldots; \theta_{Dk}] \in \Delta_D, \quad \Pr(\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_D)!}{x_1! \cdots x_D!} \prod_{d \in [D]} \theta_{dk}^{x_d}
\end{align*}
$$

显然这是一个多项式分布。
