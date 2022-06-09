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

##### 再看感知机

---

设训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]} \in (\Rbb^d \times \{ \pm 1 \})^m$，若

1. 存在$r > 0$对$\forall i \in [m]$有$\|\xv_i\| \le r$，即{==$D \subseteq B(\zerov, r)$==}
2. 存在$\rho>0$和$\|\vv\|=1$对$\forall i \in [m]$有$y_i \vv^\top \xv_i \ge \rho$，即以{==间隔==}$\rho$线性可分

则感知机更新次数$M \le r^2/\rho^2$

<div class="top2"></div>

间隔$\rho$刻画了问题的难度 (犯错次数)

- $\rho$越大，两类离得越远，问题越容易
- $\rho$越下，两类贴得越近，问题越困难

<div class="top2"></div>

如果多个超平面能将两类分开，选哪个？

- 感知机最终给出的超平面的间隔可能很小
- 直觉上越靠正中、离两类越远的超平面越好

@import "../tikz/Novikoff.svg" {.left60per .top-38per .width35}