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

<!-- slide data-notes="" -->

##### 模型选择 验证

---

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row9-border-top-dashed top-3 fs10 right10">

| 次序 | 约会时间 | 约会方式 | 当天天气 | 课业任务 | 疫情形势 | 当天电视 | 答应约会 |
| :--: | :------: | :------: | :------: | :------: | :------: | :------: | -------- |
|  1   |   周六   |   吃饭   |   晴天   |   轻松   |   清零   |   好看   | 是       |
|  2   |   周日   |   吃饭   |   阴天   |   轻松   |   清零   |   好看   | 是       |
|  3   |   周日   |   吃饭   |   晴天   |   轻松   |   清零   |   好看   | 是       |
|  4   |   周六   |   吃饭   |   阴天   |   轻松   |   清零   |   好看   | 是       |
|  5   |  工作日  |   吃饭   |   晴天   |   轻松   |   清零   |   好看   | 是       |
|  6   |   周六   |   逛街   |   晴天   |   轻松   |   平缓   |  不好看  | 是       |
|  7   |   周日   |   逛街   |   晴天   |   繁重   |   平缓   |  不好看  | 是       |
|  8   |   周日   |   逛街   |   晴天   |   轻松   |   平缓   |   好看   | 是       |
|  9   |   周日   |   逛街   |   阴天   |   繁重   |   平缓   |   好看   | 否       |
|  10  |   周六   |   学习   |   雨天   |   轻松   |   严峻   |  不好看  | 否       |
|  11  |  工作日  |   学习   |   雨天   |   备考   |   严峻   |   好看   | 否       |
|  12  |  工作日  |   吃饭   |   晴天   |   备考   |   严峻   |  不好看  | 否       |
|  13  |   周六   |   逛街   |   晴天   |   繁重   |   清零   |   好看   | 否       |
|  14  |  工作日  |   逛街   |   阴天   |   繁重   |   清零   |   好看   | 否       |
|  15  |   周日   |   逛街   |   晴天   |   轻松   |   平缓   |  不好看  | 否       |
|  16  |  工作日  |   吃饭   |   晴天   |   备考   |   严峻   |   好看   | 否       |
|  17  |   周六   |   吃饭   |   阴天   |   繁重   |   平缓   |   好看   | 否       |

</div>

<!-- slide data-notes="" -->

##### 模型选择 验证

---

事先选定合适的模型 (归纳偏倚) 很重要！

从训练集中随机选择一部分样本作为{==验证集==} (validation set)

- 在剩余的训练集上训练一个学习模型
- 在验证集上计算模型的误差

据此比较多个候选模型的性能

```dot
digraph g {
    graph [nodesep=0.3, ranksep=0.2]
    bgcolor="transparent"
    node [shape=box color="#586e75" fontcolor="#b58900" fontsize=16 fontname="Ysabeau,LXGWWenKai"]
    edge [arrowhead=vee color="#586e75" fontcolor="#dc322f" fontsize=16 fontname="Ysabeau,LXGWWenKai" arrowsize=0.6]

    subgraph cluster_1 {
        color="#586e75"
        fontcolor="#dc322f"
        fontname="Ysabeau,LXGWWenKai"
        style="invis"

        D; 输出;

        node [shape=record fontcolor="#b58900"];

        subgraph cluster_11 {
            style="dashed"
            fontsize=18
            label="传统计算机算法"
            struct1 [label="训练集|验证集"];
        }

        D -> struct1:s1;
        struct1:sn -> 输出;
    }
}
```

<!-- slide vertical=true data-notes="" -->

##### 模型选择 交叉验证

---

{==交叉验证==} (cross validation)：将训练集平均分为$n$份，每轮

- 在其中$n-1$份上训练一个学习模型
- 在剩余的$1$份上计算模型的误差

迭代$n$轮取平均，据此比较多个候选模型的性能

```dot
digraph g {
    graph [nodesep=0.3, ranksep=0.2]
    rankdir=TB
    bgcolor="transparent"
    node [shape=box color="#586e75" fontcolor="#b58900" fontsize=16 fontname="Ysabeau,LXGWWenKai"]
    edge [arrowhead=vee color="#586e75" fontcolor="#dc322f" fontsize=16 fontname="Ysabeau,LXGWWenKai" arrowsize=0.6]

    subgraph cluster_0 {
        color="#586e75"
        fontcolor="#dc322f"
        fontname="Ysabeau,LXGWWenKai"
        style="invis"

        训练集D

        node [shape=record fontcolor="#b58900"];

        struct0 [label="D1|D2|D3|D4|D5"];

        训练集D -> struct0;
    }

    subgraph cluster_1 {
        style="invis"

        node [shape=record fontcolor="#b58900"];
        struct1 [label="D1|D2|D3|D4"];
        struct2 [label="D1|D2|D3|D5"];
        struct3 [label="D1|D2|D4|D5"];
        struct4 [label="D1|D3|D4|D5"];
        struct5 [label="D2|D3|D4|D5"];

        struct1 -> struct2 [style=invis];
        struct2 -> struct3 [style=invis];
        struct3 -> struct4 [style=invis];
        struct4 -> struct5 [style=invis];
    }

    subgraph cluster_2 {
        style="invis"

        node [shape=record fontcolor="#b58900"];
        D5 -> D4 -> D3 -> D2 -> D1 [style=invis];

        struct1 -> struct2 [style=invis];
        struct2 -> struct3 [style=invis];
        struct3 -> struct4 [style=invis];
        struct4 -> struct5 [style=invis];
    }





}
```
