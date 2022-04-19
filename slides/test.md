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
@import "../css/main.css"
@import "../plugin/zoom/zoom.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/menu/menu.js"

<!-- slide data-notes="" -->

##### 不忘初心 _Staying_

---

不忘初心 牢记使命 Staying True to Our Original Aspiration and Founding Mission 不忘初心 牢记使命 Staying True to Our Original Aspiration and Founding Mission

<!-- slide data-notes="" -->

##### 标题 title

<img src="../img/qr.png" height=387px width=387px class="center top10">

<!-- slide vertical=true data-notes="" -->

##### 前导课程

---

@import "../dot/preliminary.dot" {.center}

<!-- slide vertical=true data-notes="" -->

@import "../mermaid/nn.mermaid"

<!-- slide vertical=true data-notes="" -->

@import "../puml/ai.puml" {.center .top10}

<!-- slide data-notes="" -->

|   公式   | $\|\av\|^2 + \|\bv\|^2 = \|\cv\|^2$  |
| :------: | :----------------------------------: |
| **条件** | $A \rightarrow \neg B \wedge \neg C$ |
|          |    $\neg A \rightarrow B \vee C$     |
|          | $B \rightarrow \neg A \wedge \neg C$ |
|          |    $\neg B \rightarrow A \vee C$     |

<!-- slide data-background-iframe="https://www.bilibili.com/video/BV19E411576i?t=0.0" data-background-interactive data-notes="" -->

<!-- slide data-notes="" -->

```python {.line-numbers highlight=[1-9,14,21-22]}
import numpy as np
from scipy.spatial import distance

X = np.random.rand(100, 10000)
D1 = distance.cdist(X, X, 'euclidean') # 原样本的成对距离矩阵

transformer = random_projection.GaussianRandomProjection() # 高斯随机矩阵
XX = transformer.fit_transform(X)
D2 = distance.cdist(XX, XX, 'euclidean') # 投影后样本的成对距离矩阵

XX.shape
(100, 3947)

np.linalg.norm(D1 - D2, ord='fro') # 两个成对距离矩阵差的F范数
46.74573519884732

transformer = random_projection.GaussianRandomProjection() # 稀疏随机矩阵
XX = transformer.fit_transform(X)
D2 = distance.cdist(XX, XX, 'euclidean') # 投影后样本的成对距离矩阵

np.linalg.norm(D1 - D2, ord='fro') # 两个成对距离矩阵差的F范数
43.819210159457796
```

<!-- slide vertical=true data-notes="" -->

<pre><code data-line-numbers="3-5|8-10|13-15"><table>
    <tr>
        <td>Apples</td>
        <td>$1</td>
        <td>7</td>
    </tr>
    <tr>
        <td>Oranges</td>
        <td>$2</td>
        <td>18</td>
    </tr>
    <tr>
        <td>Kiwi</td>
        <td>$3</td>
        <td>1</td>
    </tr>
</table></code></pre>

<!-- slide data-notes="" -->

<p class="fragment">Fade in</p>
<p class="fragment fade-out">Fade out</p>
<p class="fragment highlight-red">Highlight red</p>
<p class="fragment fade-in-then-out">Fade in, then out</p>
<p class="fragment fade-up">Slide up while fading in</p>

<!-- slide vertical=true data-notes="" -->

<div class="r-stack">
    <img class="fragment" src="https://i1.read01.com/Dwq8pZQAzFoYeUDIYFsEuRo/0.jpg">
    <img class="fragment" src="http://img.takungpao.com/2017/0829/20170829031612361.jpg">
    <img class="fragment" src="https://i1.read01.com/e16hmLBdeEB0YnOyw-mjcGs/0.jpg">
</div>

<!-- slide data-notes="" -->

<div class="width80 center">
<h3 class="r-fit-text">FIT TEXT</h3>
</div>

<div class="width80 center">
<h3 class="r-fit-text">CAN BE USED FOR MULTIPLE HEADLINES</h3>
</div>

<!-- slide data-auto-animate data-notes="" -->

<div data-id="box" style="height: 50px; background: salmon;"></div>

<!-- slide data-auto-animate data-notes="" -->

<div data-id="box" style="height: 200px; background: blue;"></div>

<!-- slide data-auto-animate data-notes="" -->

- 赵
- 孙
- 周

<!-- slide data-auto-animate vertical=true data-notes="" -->

- 赵
- 钱
- 孙
- 李
- 周

<!-- slide data-notes="" -->

{++添加++}

{--删除--}

{~~替~>换~~}

{>>注释<<}

高亮{==高亮==}高亮
