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

##### 查准率 查全率 <span style="font-weight:900;">F1</span>

---

只看准确率有时不够全面，比如对某种罕见病做预测，数据集中阳性占 1%、阴性占 99%，此时无脑预测阴性也有 99% 的准确率

二分类结果的{==混淆矩阵==} (confusion matrix)

<div class="threelines row4-border-top-solid column1-border-right-solid column1-bold tr-hover top-1 bottom1 left-20">

|             |  预测 正样本   |  预测 负样本   |
| :---------: | :------------: | :------------: |
| 真实 正样本 | $\TP$ (真正例) | $\FN$ (假反例) |
| 真实 负样本 | $\FP$ (假正例) | $\TN$ (真反例) |

</div>


- 准确率：$\frac{\TP + \TN}{\TP + \TN + \FP + \FN}$
- {==查准率==} (precision)：$\frac{\TP}{\TP + \FP}$，预测的正样本中有多少是正样本
- {==查全率==} (recall)：$\frac{\TP}{\TP + \FN}$，所有正样本中有多少被预测出来了

<p class="footnote book"> precision、recall 也有人译作精确率、召回率，个人觉得没有查准率、查全率好</p>

<!-- slide vertical=true data-notes="" -->

##### 查准率 查全率 <span style="font-weight:900;">F1</span>

---

二分类结果的{==混淆矩阵==} (confusion matrix)

<div class="threelines row4-border-top-solid column1-border-right-solid column1-bold tr-hover top-2 bottom-2 left-20">

|             |  预测 正样本   |  预测 负样本   |
| :---------: | :------------: | :------------: |
| 真实 正样本 | $\TP$ (真正例) | $\FN$ (假反例) |
| 真实 负样本 | $\FP$ (假正例) | $\TN$ (真反例) |

</div>

{==查准率==} (precision)：预测的约会中有多少比例真的约会了

{==查全率==} (recall)：所有的约会中有多少比例被预测出来了

<div class="top3"></div>

$$
\begin{align*}
    & \quad \mathrm{precision} = \frac{\TP}{\TP + \FP}, \quad \mathrm{recall} = \frac{\TP}{\TP + \FN} \\[4pt]
    & \quad \mathrm{F1} = \frac{2 \cdot \mathrm{precision} \cdot \mathrm{recall}}{\mathrm{precision} + \mathrm{recall}} = \frac{2 \cdot \TP}{\text{样本总数} + \TP - \TN \quad}
\end{align*}
$$

<!-- slide data-notes="" -->

##### 机器学习一般流程

---

@import "../dot/ml-old.dot" {.top2}

<div class="bottom0"></div>

原始数据：表格、图片、视频、文本、语音、……

模型学习：最核心的部分，学习一个用来预测的映射

<span class="invis">特征工程：</span>

<ul>
    <li class="invis">提取：选取、构造对目标任务有用的潜在特征</li>
    <li class="invis">处理：无序的离散类别特征 → 数值特征，缺失处理，标准化</li>
    <li class="invis">变换：对特征进行挑选或映射得到对目标任务更有效的特征</li>
</ul>

<!-- slide vertical=true data-notes="" -->

##### 二分类示例

---

@import "../python/cancer-info.py" {line_start=0 line_end=119 .line-numbers .top-1 .left4 highlight=[]}

@import "../python/binary-classif.svg" {.center .top4 .width92 title="3 行对应 3 个人工数据集，第一个半月形，第二个圆环型，第三个线性可分，两种颜色深色的为训练样本，稍浅些的为测试样本，每个数据集各有 20%的噪声；6 列分别对应 决策树、感知机、神经网络、朴素贝叶斯、k 近邻、支持向量机 在这些数据集上的分类结果，右下角是预测精度"}

<!-- slide vertical=true data-notes="" -->

##### 混淆矩阵

---

@import "../python/multi-classif-confusion-matrix.svg" {.center .top2 .width65 title="混淆矩阵统计最终的预测结果，第 i 行第 j 列的值就是第 i 类样本被预测为第 j 类的样本个数"}
