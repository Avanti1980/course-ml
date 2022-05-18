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

##### 核感知机

---

若通过核函数$\kappa(\cdot, \cdot)$隐式定义核映射，则得到核感知机

<div class="top-2"></div>

根据感知机算法的更新$\wv \leftarrow \wv + \eta y_i \xv_i$，最终$\wv = \sum_{j \in [m]} \alpha_j y_j \xv_j$

<div class="top-2"></div>

故除了直接维护$\wv$外，也可以维护$m$维向量$\alphav = [\alpha_1; \ldots; \alpha_m]$

输入：训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]} \in (\Rbb^d \times \{ \pm 1 \})^m$，学习率$\eta > 0$<br>输出：$\alphav$

1. 初始化$\alphav = \zerov$，更新次数$t = 0$
2. {==while==} 训练集中存在误分类点 {==do==}
3. &emsp;&emsp;获取样本$(\xv_i, y_i)$
4. &emsp;&emsp;{==if==} $(\xv_i, y_i)$被误分类，即$y_i (\sum_{j \in [m]} \alpha_j y_j \xv_j)^\top \xv_i \le 0$ {==then==}
5. &emsp;&emsp;&emsp;&emsp;$\alpha_i \leftarrow \alpha_i + \eta$

将第 4 行的 if 条件换成$y_i \sum_{j \in [m]} \alpha_j y_j \kappa(\xv_i ,\xv_j) \le 0$即为核感知机

<!-- slide data-notes="" -->

##### 多层感知机

---



