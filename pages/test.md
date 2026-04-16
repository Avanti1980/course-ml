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
@import "../js/anychart/venn-entropy.js"

<!-- slide vertical=true data-notes="" -->

##### 评估 交叉熵损失

---

<span class="blue">词频 - 逆文本频率</span>：对当前文本重要的单词必然

- 在当前文本中出现的频率高，即词频 (<span class="blue">t</span>erm <span class="blue">f</span>requency, tf) 高
- 在其他文本中出现的频率低，即逆文本频率 (<span class="blue">i</span>nverse <span class="blue">d</span>ocument <span class="blue">f</span>requency, idf) 高

<div class="top2"></div>

$\textrm{tf} = 单词在当前文本中出现的次数 / 当前文本的总词数$

<div class="top-2"></div>

$\textrm{idf} = \ln ((全部文本数 + C) / (包含该词的总文本数 + C)) + 1$

- $C = 0$，若词典包含从未在任何文本中出现的词，会有分母为零的问题
- $C = 1$，sklearn 默认的平滑版本，等于额外有一个包含所有词的文本

<div class="top2"></div>

tf - idf 特征：将 tf 和 idf 相乘后再标准化

- $\ell_1$标准化，线性变换成概率分布：$\textrm{tf} \otimes \textrm{idf} / \sum_i [\textrm{tf} \otimes \textrm{idf}]_i$
- $\ell_2$标准化，线性变换成单位向量：$\textrm{tf} \otimes \textrm{idf} / (\sum_i [\textrm{tf} \otimes \textrm{idf}]_i^2)^{1/2}$
