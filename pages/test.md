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

##### 概率

---

概率是用来刻画不确定性的工具

频率主义：{==独立重复试验==}中随机事件发生{==频率==}的极限

<div class="top4"></div>

局限：若随机事件非可重复怎么办？

下一轮学科评估，计算机得 A+ 的概率有多大？

这个月大 A 股上涨的概率有多大？

今年祖国统一的概率有多大？

<!-- slide vertical=true data-notes="" -->

##### 概率

---

我们有一些观测

- 近两年学院引进了很多高水平的青年教师
- 资深教授大项目接连不断
- 毕业生去向越来越好

<div class="top4"></div>

- 市场情绪低迷，成交量持续萎缩
- 宏观经济数据不好
- 公司年报业绩频繁爆雷

<div class="top4"></div>

- 解放军先进装备列装，频繁秀肌肉
- 美国实力衰退，战略收缩

<div class="top4"></div>

贝叶斯主义：概率是观测者对随机事件发生的主观信念

<!-- slide vertical=true data-notes="注意在这个例子中 我们已经在用信念来表示概率了" -->

##### 贝叶斯公式的理解

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \underbrace{p(\Theta|X)}_{\text{后验}} & = \frac{\overbrace{p(X|\Theta)}^{\text{似然}} \overbrace{p(\Theta)}^{\text{先验}}}{\underbrace{p(X)}_{\text{证据}}} = \frac{p(X|\Theta) p(\Theta) }{\int p(X|\Theta) p(\Theta) \diff \Theta}
\end{align*}
$$

- 先验：对随机事件发生的初始{==信念==}
- 似然：观测数据对随机事件发生的支持
- 证据：观测数据，它是贝叶斯主义者做推断的基础
- 后验：得到观测数据后，观测者对初始信念的修正
