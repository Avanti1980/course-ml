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

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row9-border-top-dashed top-3 fs10 left4 righta row1-column2-red row4-column2-red row6-column2-red row10-column2-red row13-column2-red row17-column2-red row2-column2-yellow row3-column2-yellow row7-column2-yellow row8-column2-yellow row9-column2-yellow row15-column2-yellow row5-column2-blue row11-column2-blue row12-column2-blue row14-column2-blue row16-column2-blue">

| 次序 | 时间 | 方式 | 天气 | 课业 | 疫情 | 电视 | 约会 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  2   | 周日 | 吃饭 | 阴天 | 轻松 | 清零 | 精彩 |  是  |
|  3   | 周日 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  4   | 周六 | 吃饭 | 阴天 | 轻松 | 清零 | 精彩 |  是  |
|  5   | 周间 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  6   | 周六 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  是  |
|  7   | 周日 | 逛街 | 晴天 | 适中 | 平缓 | 无聊 |  是  |
|  8   | 周日 | 逛街 | 晴天 | 轻松 | 平缓 | 精彩 |  是  |
|  9   | 周日 | 逛街 | 阴天 | 适中 | 平缓 | 精彩 |  否  |
|  10  | 周六 | 学习 | 雨天 | 轻松 | 严峻 | 无聊 |  否  |
|  11  | 周间 | 学习 | 雨天 | 繁重 | 严峻 | 精彩 |  否  |
|  12  | 周间 | 吃饭 | 晴天 | 繁重 | 严峻 | 无聊 |  否  |
|  13  | 周六 | 逛街 | 晴天 | 适中 | 清零 | 精彩 |  否  |
|  14  | 周间 | 逛街 | 阴天 | 适中 | 清零 | 精彩 |  否  |
|  15  | 周日 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  否  |
|  16  | 周间 | 吃饭 | 晴天 | 繁重 | 严峻 | 精彩 |  否  |
|  17  | 周六 | 吃饭 | 阴天 | 适中 | 平缓 | 精彩 |  否  |

</div>

<div class="left55per top-60per">

<p class="fs12">
\begin{align}
    H(\dc) & = - \frac{8}{17} \log \frac{8}{17} - \frac{9}{17} \log \frac{9}{17} \\
    & = \log 17 - \frac{18}{17} \log 3 - \frac{24}{17} = 0.998
\end{align}
</p>

<p class="fs12 top4">
\begin{align}
    \class{red}{\dc_1}-周六，\class{yellow}{\dc_2}-周日，\class{blue}{\dc_3}-周间
\end{align}
</p>

<p class="fs12 top4">
\begin{align}
    \class{red}{H(\dc_1)} & = - \frac{3}{6} \log \frac{3}{6} - \frac{3}{6} \log \frac{3}{6} = \log 2 = 1 \\[4pt]
    \class{yellow}{H(\dc_2)} & = - \frac{4}{6} \log \frac{4}{6} - \frac{2}{6} \log \frac{2}{6} \\
    & = \log 3 - \frac{2}{3} = 0.918 \\[4pt]
    \class{blue}{H(\dc_3)} & = - \frac{1}{5} \log \frac{1}{5} - \frac{4}{5} \log \frac{4}{5} \\
    & = \log 5 - \frac{8}{5} = 0.722
\end{align}
</p>

<p class="fs12 top4">
\begin{align}
    \gain & (\dc, 时间) = 0.998 - \frac{6}{17} \times 1 \\
    & - \frac{6}{17} \times 0.918 - \frac{5}{17} \times 0.722 = 0.108
\end{align}
</p>

</div>
