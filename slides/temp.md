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

##### 感知机

---

实现与、或、非运算，设$x_1,x_2$为布尔变量

- 与：$\sign(x_1 + x_2 - 1.5) = \begin{cases} 1, & x_1 = x_2 = 1 \\ -1, & \ow \end{cases}$
- 或：$\sign(x_1 + x_2 - 0.5) = \begin{cases} -1, & x_1 = x_2 = 0 \\ 1, & \ow \end{cases}$
- 非：$\sign(- x_1 + 0.5) = \begin{cases} -1, & x_1 = 1 \\ 1, & x_1 = -1 \end{cases}$

再$(\sign(\cdots) + 1) / 2$就
