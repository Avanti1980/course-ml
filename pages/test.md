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

##### 评估 多分类

---

多分类同样有错误率、准确率

$$
\begin{align*}
    \quad E_D (f) = \frac{1}{m} \sum_{i \in [m]} \Ibb (y_i \ne f(\xv_i)), \quad \text{Acc}_D (f) = 1 - E_D (f)
\end{align*}
$$

以及混淆矩阵

<div class="threelines column1-border-right-solid column2-border-right-dashed column3-border-right-dashed column4-border-right-dashed row2-border-top-dashed row3-border-top-dashed row4-border-top-dashed column1-bold top-1 bottom1 center">

|             | 预测第$1$类 | 预测第$2$类 | &emsp;&emsp; ... &emsp;&emsp; | 预测第$c$类 |
| :---------: | :---------: | :---------: | ----------------------------- | ----------- |
| 真实第$1$类 |   &emsp;    |   &emsp;    | &emsp;                        | &emsp;      |
| 真实第$2$类 |   &emsp;    |   &emsp;    | &emsp;                        | &emsp;      |
|     ...     |   &emsp;    |   &emsp;    | &emsp;                        | &emsp;      |
| 真实第$c$类 |   &emsp;    |   &emsp;    | &emsp;                        | &emsp;      |

</div>

<!-- slide vertical=true data-notes="" -->

##### 评估 交叉熵损失

---

错误率 (0-1 损失) 不连续、难优化，通常采用交叉熵损失

设$c$个类别的预测函数分别为$f_1, \ldots, f_c$，则样本$x$的预测结果为

$$
\begin{align*}
    \quad \pv = \left[ \frac{e^{f_1(x)}}{\sum_{j \in [c]} e^{f_i(x)}}, \frac{e^{f_2(x)}}{\sum_{j \in [c]} e^{f_i(x)}}, \ldots, \frac{e^{f_c(x)}}{\sum_{j \in [c]} e^{f_i(x)}} \right] \quad \longleftarrow \text{softmax}
\end{align*}
$$

<div class="bottom-4"></div>

这是一个$c$维向量，同时也是一个离散概率分布

类标记$y$可转化为独热编码$\ev_y$，这也是一个$c$维离散概率分布

替代损失的要求：关于$\pv$、$\ev_y$连续，且$\pv$、$\ev_y$越接近损失越小

问题：给定离散概率分布$\qv$，如何度量分布$\pv$与它的距离？

<!-- slide vertical=true data-notes="" -->

##### 评估 交叉熵损失

---

交叉熵 (cross-entropy) $H_{\qv} (\pv) \triangleq - \sum_i q_i \ln p_i$

当$\pv = \qv$时交叉熵最小，此时交叉熵$H_{\qv} (\pv)$即为分布$\qv$的熵$H(\qv)$

$$
\begin{align*}
    \quad \min_{\pv} H_{\qv} (\pv) = - \sum_i q_i \ln p_i, \quad \st ~ \sum_i p_i = 1
\end{align*}
$$

<div class="top-2"></div>

拉格朗日函数为$L(p_i, \alpha) = - \sum_i q_i \ln p_i + \alpha (\sum_i p_i - 1)$，于是

$$
\begin{align*}
    \quad \nabla_{p_i} L(p_i, \alpha) & = - \frac{q_i}{p_i} + \alpha = 0 \Longrightarrow q_i = \alpha p_i \\
    & \Longrightarrow \sum_i q_i = \alpha \sum_i p_i \Longrightarrow \alpha = 1 \Longrightarrow \pv = \qv
\end{align*}
$$

对$(x,y)$，$y \in [c]$，交叉熵损失为$- \ln \frac{e^{f_y(x)}}{\sum_{j \in [c]} e^{f_i(x)}}$

<!-- slide vertical=true data-notes="" -->

##### 评估 交叉熵损失

---

对$(x,y)$，$y \in \{1, -1\}$，$\qv = [(1+y)/2; (1-y)/2]$，交叉熵损失为

$$
\begin{align*}
    \quad \text{CE} & = - \frac{1+y}{2} \ln \frac{e^{f_1(x)}}{e^{f_1(x)}+e^{f_2(x)}} - \frac{1-y}{2} \ln \frac{e^{f_2(x)}}{e^{f_1(x)}+e^{f_2(x)}} \\
    & = - \frac{1+y}{2} \ln \frac{e^{f_1(x)-f_2(x)}}{e^{f_1(x)-f_2(x)}+1} - \frac{1-y}{2} \ln \frac{1}{e^{f_1(x)-f_2(x)}+1} \\
    & = - \frac{1+y}{2} \ln \frac{e^{w(x)}}{e^{w(x)}+1} - \frac{1-y}{2} \ln \frac{1}{e^{w(x)}+1} \quad \leftarrow w(x) \triangleq f_1(x)-f_2(x) \\
    & = \begin{cases}
        \ln (1 + e^{-w(x)}), & y = 1 \\
        \ln (1 + e^{-w(x)}), & y = -1
    \end{cases} \\
    & = \ln (1 + e^{- y w(x)})
\end{align*}
$$

由此可见，多分类的交叉熵损失就是二分类的对率损失的拓展

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
