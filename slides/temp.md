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

##### 感知机的对偶形式

---

引入特征映射$\phi$，感知机算法的更新变为$\wv \leftarrow \wv + \eta y_j \phi(\xv_j)$

由于初始$\wv = \zerov$，因此最终$\wv = \sum_{j \in [m]} \alpha_j \phi(\xv_j)$

原始形式维护$\wv$外，对偶形式维护$m$维向量$\alphav = [\alpha_1; \ldots; \alpha_m]$

输入：训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]} \in (\Rbb^d \times \{ \pm 1 \})^m$，学习率$\eta > 0$<br>输出：向量$\alphav$

1. 初始化$\alphav = \zerov$
2. {==while==} 训练集中存在误分类点 {==do==}
3. &emsp;&emsp;获取样本$(\xv_i, y_i)$
4. &emsp;&emsp;{==if==} $(\xv_i, y_i)$被误分类，即$y_i (\sum_{j \in [m]} \alpha_j y_j \phi(\xv_j))^\top \phi(\xv_i) \le 0$ {==then==}
5. &emsp;&emsp;&emsp;&emsp;$\alpha_i \leftarrow \alpha_i + \eta ~ y_i$

<!-- slide vertical=true data-notes="" -->

##### 核感知机

---

若通过核函数$\kappa(\cdot, \cdot)$隐式定义特征映射$\phi$，则得到核感知机

$$
\begin{align*}
    \qquad \phi(\xv)^\top \phi(\zv) & = x_1^2 z_1^2 + x_2^2 z_2^2 + 2 x_1 x_2 z_1 z_2 + 2 x_1 z_1 + 2 x_2 z_2 + 1 \\
    & = (x_1 z_1 + x_2 z_2 + 1)^2 = (\xv^\top \zv + 1)^2 = \kappa (\xv, \zv)
\end{align*}
$$

输入：训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]} \in (\Rbb^d \times \{ \pm 1 \})^m$，学习率$\eta > 0$<br>输出：向量$\alphav$

1. 初始化$\alphav = \zerov$
2. {==while==} 训练集中存在误分类点 {==do==}
3. &emsp;&emsp;获取样本$(\xv_i, y_i)$
4. &emsp;&emsp;{==if==} $(\xv_i, y_i)$被误分类，即$y_i \sum_{j \in [m]} \alpha_j y_j \kappa(\xv_j ,\xv_i) \le 0$ {==then==}
5. &emsp;&emsp;&emsp;&emsp;$\alpha_i \leftarrow \alpha_i + \eta$

学习模型为$f(\zv) = \wv^\top \zv = \sum_{j \in [m]} \alpha_j y_j \kappa(\xv_j, \zv)$
