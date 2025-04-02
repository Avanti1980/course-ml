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

##### 模型选择

---

若有一组模型$\Mcal_1, \ldots, \Mcal_l$，如何选择

频率主义者：从训练数据集$\Dcal$中分出一部分作为验证集

贝叶斯主义者


<!-- slide data-notes="" -->

##### 模型选择

---

- 可以通过先验引入{==领域知识==}，避免做出极端推断
- 方便动态地处理数据，上一时刻的后验作为下一时刻的先验

<div class="top2"></div>

缺点：概率依赖于观测者，是观测者的主观信念，唯心主义？

{==全贝叶斯==} (fully Bayesian)：考虑所有的$\theta$，根据后验做加权平均
