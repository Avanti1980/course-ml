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

##### 结构预测 向量

---

多分类，标量类别标记经独热编码 (one-hot encoding) 后变成向量

<p>
\begin{align}
    0 & \to \ldots 0001 \\
    1 & \to \ldots 0010 \\
    2 & \to \ldots 0100 \\
    3 & \to \ldots 1000 \\
    \vdots & \to \ldots \ldots
\end{align}
</p>

<div class="bottom2"></div>

多标记学习 (multi-label learning)，用于图片中的多物体识别任务

<p>
\begin{align}
    \{ 🐶, 🐱 \} & \to \ldots 00011 \\
    \{ 🐶, 🐔 \} & \to \ldots 00101 \\
    \{ 🐱, 🪿 \} & \to \ldots 01010 \\
    \{ 🐖, 🐔, 🪿 \} & \to \ldots 11100 \\
    \vdots & \to \ldots \ldots
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 结构预测 序列

---

机器翻译：平行语料库

<div class="center threelines column1-border-right-solid head-highlight-1 tr-hover width90 top-2 chn2eng">

| 中                               | 英                                                                                                       |
| :------------------------------- | :------------------------------------------------------------------------------------------------------- |
| 苟利国家生死以，岂因祸福避趋之。 | Were it to benefit my country, I would lay down my life; What have I to fear when fortune comes or goes? |
| 我跟他谈笑风生。                 | I was chatting with him in a lively and pleasant manner.                                                 |
| 撸起袖子加油干。                 | Roll up our sleeves to work harder.                                                                      |
| 不忘初心，方得始终。             | Never forget why you started, and you can accomplish your mission.                                       |

</div>

<!-- slide vertical=true data-notes="" -->

##### 结构预测 序列

---

问答系统：阅读理解、知识竞赛

<div class="center threelines column1-border-right-solid head-highlight-1 tr-hover width90 top-2 chn2eng">

| 问                                                                                                       | 答                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 《周鼎传》：公讳鼎，字实甫，自为童子时即以言动自持...自是豪强屏息...，文中“自是豪强屏息”中“屏”的意思是？ | 收敛行迹                                                                                                                                                                                                                                           |
| 什么是基金定投？有什么优缺点？                                                                           | 基金定投是定期定额投资基金的方式。优点包括摊平成本、强制储蓄、享受复利、操作便捷、门槛低；缺点主要是收益慢、可能短期亏损、流动性受限。适合有长期理财需求、不想花太多时间研究市场的投资者，建议选择历史业绩稳健的指数基金或主动管理型基金进行定投。 |

</div>

<!-- slide vertical=true data-notes="" -->

##### 结构预测 句法树

---

用于对自然语言的句法分析

- {==S==}：句子
- {==NP==}：名词短语 (Noun Phrase)
- {==VP==}：动词短语 (Verb Phrase)
- {==PP==}：介词短语 (Prepositional Phrase)
- {==N==}：名词
- {==V==}：动词
- {==P==}：介词
- {==U==}：体标记

<img src="../tikz/syntax-tree/syntax-tree.svg" class="top-40 width40 bottom-10 right6 lefta">

<!-- slide data-notes="" -->

##### 小结

---

<div class="threelines column1-border-right-solid head-highlight-1 tr-hover top-2">

| 演绎推理 符号主义 | 归纳学习 连结主义 |
| ----------------: | :---------------- |
|        一般到具体 | 具体到一般        |
|    逻辑编程、搜索 | 神经网络          |
|        可解释性强 | 无可解释性        |
|                 4 | 会飞              |
|                 5 | 哺乳动物          |
|                 6 | 哺乳动物          |
|                 7 | 食肉动物          |
|                 8 | 食肉动物          |

</div>
