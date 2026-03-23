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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-ml.js"

<!-- slide vertical=true data-notes="" -->

##### 构建决策树

---

<p>
\begin{align}
    & a \left( \| \wv_{t-1} \| + \frac{\rho}{2} \right)^2 b \\
    & a \big( \| \wv_{t-1} \| + \frac{\rho}{2} \big)^2 b \\
    & a \bigg( \| \wv_{t-1} \| + \frac{\rho}{2} \bigg)^2 b
\end{align}
</p>

<p>
\begin{align}
    & \underbrace{a \left( \| \wv_{t-1} \| + \frac{\rho}{2} \right)^2 b}_{注释} \\
    & \underbrace{a ( \| \wv_{t-1} \| + \frac{\rho}{2} )^2 b}_{注释} \\
    & \underbrace{a \bigg( \| \wv_{t-1} \| + \frac{\rho}{2} \bigg)^2 b}_{注释}
\end{align}
</p>

