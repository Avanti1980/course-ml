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

<div class="threelines column1-border-right-solid head-highlight-1 tr-hover">

| &emsp;  |                                            >                                            |                                   对率回归                                    |
| :-----: | :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------: |
| $\Ycal$ |                                      $\{ \pm 1 \}$                                      |                                  $\{ 0,1 \}$                                  |
|  _obj_  |                $\min_{\wv} \sum_i \ln (1 + \exp(- y_i \wv^\top \xv_i))$                 |   $\min_{\wv} \sum_i (\ln (1 + \exp(\wv^\top \xv_i)) - y_i \wv^\top \xv_i)$   |
|  $\gv$  |                   $\sum_i (\sigma(y_i \wv^\top \xv_i) - 1) y_i \xv_i$                   |                 $\sum_i (\sigma(\wv^\top \xv_i) - y_i) \xv_i$                 |
|  $\Hv$  | $\sum_i (\sigma(y_i \wv^\top \xv_i)) (1 - \sigma(y_i \wv^\top \xv_i)) \xv_i \xv_i^\top$ | $\sum_i \sigma(\wv^\top \xv_i) (1 - \sigma(\wv^\top \xv_i)) \xv_i \xv_i^\top$ |

</div>

<div class="threelines column1-border-right-solid head-highlight-1 tr-hover">

| &emsp;  |                           >                            |                             感知机                              |
| :-----: | :----------------------------------------------------: | :-------------------------------------------------------------: |
| $\Ycal$ |                     $\{ \pm 1 \}$                      |                           $\{ 0,1 \}$                           |
|  _obj_  | $\min_{\wv} \sum_i \max \{ 0, - y_i \wv^\top \xv_i \}$ | $\min_{\wv} \sum_i (\sgn(\wv^\top \xv_i) - y_i) \wv^\top \xv_i$ |
|  $\gv$  |   $-\sum_i \Ibb(y_i \wv^\top \xv_i \le 0) y_i \xv_i$   |           $\sum_i (\sgn(\wv^\top \xv_i) - y_i) \xv_i$           |

</div>

目标函数是关于样本的求和，每一项称为该样本上的{==损失==} (loss)

对于$\Ycal = \{ \pm 1 \}$，其损失为{==对率损失==}$\ln (1 + \exp(- y \wv^\top \xv))$

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
