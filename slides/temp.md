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

##### 感知机实现逻辑运算

---

<div class="threelines column1-border1-right-solid-head column2-border1-right-solid-head column3-border1-right-solid-head column3-border-right-solid column6-border-right-solid column9-border-right-solid head-highlight-1 tr-hover row8-border-top-dashed top-2 center">

|   >   |   >   | 与  |   >   |   >   | 或  |   >   |   >   | 非  | >     | >     | 异或 |
| :---: | :---: | :-: | :---: | :---: | :-: | :---: | :---: | --- | ----- | ----- | ---- |
| $x_1$ | $x_2$ | $y$ | $x_1$ | $x_2$ | $y$ | $x_1$ | $x_2$ | $y$ | $x_1$ | $x_2$ | $y$  |
|  $1$  |  $1$  | $1$ |  $1$  |  $1$  | $1$ |  $1$  |  $1$  | $0$ | $1$   | $1$   | $0$  |
|  $1$  |  $0$  | $0$ |  $1$  |  $0$  | $1$ |  $1$  |  $0$  | $0$ | $1$   | $0$   | $1$  |
|  $0$  |  $1$  | $0$ |  $0$  |  $1$  | $1$ |  $0$  |  $1$  | $1$ | $0$   | $1$   | $1$  |
|  $0$  |  $0$  | $0$ |  $0$  |  $0$  | $0$ |  $0$  |  $0$  | $1$ | $0$   | $0$   | $0$  |

</div>

将$y = 1$看作正类，$y = 0$看作负类，一旦感知机$\sign(\cdots)$可以正确分类，再$(\sign(\cdots) + 1) / 2$就可以得到$y$

<!-- slide vertical=true data-notes="" -->

##### 感知机实现逻辑运算

---

实现与、或、非运算，设$x_1,x_2$为布尔变量

- 与：$\sign(x_1 + x_2 - 1.5) = \begin{cases} 1, & x_1 = x_2 = 1 \\ -1, & \ow \end{cases}$
- 或：$\sign(x_1 + x_2 - 0.5) = \begin{cases} -1, & x_1 = x_2 = 0 \\ 1, & \ow \end{cases}$
- 非：$\sign(- x_1 + 0.5) = \begin{cases} -1, & x_1 = 1 \\ 1, & x_1 = -1 \end{cases}$

再$(\sign(\cdots) + 1) / 2$就
