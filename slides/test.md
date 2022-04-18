---
presentation:
  margin: 0
  transition: "convex"
  enableSpeakerNotes: true
  slideNumber: "c/t"
---

@import "../css/font-awesome-4.7.0/css/font-awesome.css"
@import "../css/solarized.css"
@import "../plugin/zoom/zoom.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"

<!-- slide data-notes="" -->

<img src="../img/qr.png" height=387px width=387px class="center top10">

<!-- slide vertical=true data-notes="" -->

@import "../dot/preliminary.dot" {class="top5 center"}

<!-- slide vertical=true data-notes="" -->

@import "../mermaid/nn.mermaid"

<!-- slide vertical=true data-notes="" -->

@import "../puml/ai.puml" {.center .top10}

<!-- slide data-notes="" -->

|   公式   |          $p \rightarrow q$           |
| :------: | :----------------------------------: |
| **条件** | $A \rightarrow \neg B \wedge \neg C$ |
|          |    $\neg A \rightarrow B \vee C$     |
|          | $B \rightarrow \neg A \wedge \neg C$ |
|          |    $\neg B \rightarrow A \vee C$     |

<!-- slide data-notes="" -->

<video data-autoplay src="https://rr3---sn-npoe7nek.googlevideo.com/videoplayback?expire=1649887671&ei=V_VWYsWnIYG6kwaMlYPIAw&ip=2001%3A470%3A1f04%3A726%3A%3A7&id=o-AOGA8fpYah6mcnJ-F7M0ftFpgosaONyYoXn9gs_LB4B4&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ratebypass=yes&dur=267.215&lmt=1616815581796458&fexp=24001373,24007246&c=ANDROID&txp=5432434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAJB2toZ39POsLuYB6akTFKKrBp2dMl9V9Vg0qm9KOE0lAiAtptEqD9my-adLhBukhnoLgatpl7MjmppDDAQXR-NvSg%3D%3D&redirect_counter=1&cm2rm=sn-axqzes&req_id=9e813d63edbca3ee&cms_redirect=yes&mh=Sp&mip=212.107.28.9&mm=34&mn=sn-npoe7nek&ms=ltu&mt=1649865652&mv=m&mvi=3&pl=24&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgNv5sba0ddDQ_Z7h78sq8IWaNKRa6wVAG2dyLRCCP9vECIQCgIzgRhvVu_2DIncPwVGTxR1EayNQgToNnjyQZtQid5g%3D%3D" width="100%"></video>

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
