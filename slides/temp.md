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

##### 再看对率回归

---

设训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，似然函数为

$$
\begin{align*}
    \quad \Pbb(D | \wv) \propto \prod_{i \in [m]} \Pbb(y_i | \xv_i, \wv) = \prod_{i \in [m]} \sigma(y_i \wv^\top \xv_i) = \prod_{i \in [m]} \frac{1}{1 + \exp(- y_i \wv^\top \xv_i)}
\end{align*}
$$

取先验分布$\Pbb(\wv) = \Ncal(\wv | \zerov, \alpha^{-1} \Iv)$，则

$$
\begin{align*}
    \quad \Pbb(\wv | D) & \propto \exp \left( -\frac{\alpha}{2} \wv^\top \wv \right) \prod_{i \in [m]} \frac{1}{1 + \exp(- y_i \wv^\top \xv_i)}
\end{align*}
$$

最大后验估计$\wv$只需求解优化问题

$$
\begin{align*}
    \quad \min_{\wv} ~ \sum_{i \in [m]} \ln (1 + \exp(- y_i \wv^\top \xv_i)) + \frac{\alpha}{2} \| \wv \|_2^2
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 再看对率回归

---

<div class="top2"></div>

目前待估计的参数是$\wv$和$\beta$，似然为

$$
\begin{align*}
    \qquad \Pbb (D | \wv, \beta) & = \prod_{i \in [m]} \Pbb (\xv_i, y_i | \wv, \beta) = \prod_{i \in [m]} \Pbb (\xv_i) \Pbb (y_i | \xv_i, \wv, \beta) \\
    & \propto \prod_{i \in [m]} \Pbb (y_i | \xv_i, \wv, \beta) = \prod_{i \in [m]} \Ncal(\wv^\top \xv_i,\beta^{-1})
\end{align*}
$$
