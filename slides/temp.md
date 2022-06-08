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

##### 拉普拉斯平滑

---

在各取值的频数上赋予一个正数$\lambda$，通常取$\lambda=1$

<div class="top2"></div>

$$
\begin{align*}
    & \qquad \Pbb (y = k) = \frac{\text{第}k\text{类样本数} + \lambda ~~~~}{\text{总样本数} + c \lambda} \\[6pt]
    & \qquad \Pbb ( x_j = v_l^{(j)} | y=k) = \frac{\text{第}k\text{类样本中第}j\text{个特征取值}v_l^{(j)}\text{的样本数} + \lambda \qquad ~}{\text{第}k\text{类样本数} + n_j \lambda} \\[6pt]
    & \qquad \Pbb (x_j = 1 | y = k) = \frac{\text{第}k\text{类文本中包含词}v_j\text{的文本数} + \lambda \quad ~~~}{\text{第}k\text{类文本数} + d \lambda} \\[6pt]
    & \qquad \Pbb (\text{选取词}v_j | y = k) = \frac{\text{词}v_j\text{在第}k\text{类文本中出现总次数} + \lambda \quad~~~}{\text{第}k\text{类文本的总词数} + d \lambda}
\end{align*}
$$
