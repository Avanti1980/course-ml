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

<!-- slide vertical=true data-notes="" -->

##### 预测分布

---

数据：$x \sim \Ucal[-1,1]$，$y = \sin(\pi x) + \Ncal(0, 0.2)$

模型：四阶多项式，先验：$\wv \sim \Ncal(\zerov, \Iv_5)$

@import "../python/linear-regression/predictive-distribution.svg" {.center .width80}

<!-- slide data-notes="" -->

##### 频率 <span style="font-weight:900">_vs._</span> 贝叶斯

---

在机器学习中的区别：是否考虑先验

当观测数据量很大时，先验 (伪数据) 就无足轻重了，两种做法不会有太大差别

当观测数据量不大时，先验对模型性能有显著影响 (归纳偏好)

- 先验是主观的，纯人为选取，没有标准
- 抛硬币问题选贝塔分布做先验就是图计算方便
- 利用共轭先验可以不用显式地积分求$p(X)$，肉眼就能看出结果

<div class="top2"></div>

先验需有适当的自由度，能通过调整参数灵活表示领域知识
