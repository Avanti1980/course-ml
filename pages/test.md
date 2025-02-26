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

##### 评估 回归

---

给定模型$f$、数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$

- 均方误差 (<u>m</u>ean <u>s</u>quared <u>e</u>rror, MSE)：$\frac{1}{m} \sum_{i \in [m]} (f(\xv_i) - y_i)^2$
- 均方根误差 (<u>r</u>oot MSE, RMSE)：$\sqrt{\frac{1}{m} \sum_{i \in [m]} (f(\xv_i) - y_i)^2}$
- 平均绝对误差 (<u>m</u>ean <u>a</u>bsolute <u>e</u>rror, MAE)：$\frac{1}{m} \sum_{i \in [m]} |f(\xv_i) - y_i|$
- Huber 误差：$\frac{1}{m} \sum_{i \in [m]} \begin{cases} (f(\xv_i) - y_i)^2, & |(f(\xv_i) - y_i)^2| \le \delta \\ 2 \delta (|f(\xv_i) - y_i| - \delta), & |(f(\xv_i) - y_i)^2| > \delta \end{cases}$

@import "../python/model-evaluation-mse.py" {line_end=10 .line-numbers .top2 .left4 highlight=[7,10]}

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
