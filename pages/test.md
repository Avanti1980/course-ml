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

<!-- slide data-notes="" -->

##### 路线之争

---

```dot
digraph g {
    bgcolor=transparent
    graph [nodesep=0.2, ranksep=0.4]
    rankdir=LR
    node [shape=plaintext, color="#586e75", fontname="Ysabeau, LXGWSong", fontcolor="#b58900", fontsize=18]
    edge [arrowhead=vee, color="#586e75", fontname="Ysabeau, LXGWSong", fontcolor="#268bd2", fontsize=14, arrowsize=0.6]

    subgraph cluster_1 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="Ysabeau, LXGWSong"
        label="增强品质"

        图属性 时间属性 空间属性

        node [fontcolor="#268bd2"]

        灵材
    }

    subgraph cluster_2 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="Ysabeau, LXGWSong"
        label="设计灵阵"

        图类 循环类 卷积类

        node [fontcolor="#268bd2"]

        丹方
    }

    subgraph cluster_3 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="Ysabeau, LXGWSong"
        label="精通用法"

        JAX PyTorch TensorFlow

        node [fontcolor="#268bd2"]

        丹炉
    }

    subgraph cluster_4 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="Ysabeau, LXGWSong"
        label="氪金"

        "华为 昇腾" "谷歌 TPU" "英伟达 GPU"

        node [fontcolor="#268bd2"]

        真火
    }

    subgraph cluster_5 {
        color="#586e75"
        fontcolor="#586e75"
        style="dashed"
        fontname="Ysabeau, LXGWSong"
        label="控制调节"

        提早停止 随机丢弃 层归一化

        node [fontcolor="#268bd2"]

        炼制
    }

    灵材 -> 丹方 -> 丹炉 -> 真火 -> 炼制
}
```
