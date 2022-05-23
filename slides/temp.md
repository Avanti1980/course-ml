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

##### 另一个视角

---

<div class="threelines row1-column2-border1-left-solid row2-column2-border1-left-solid row3-column1-border1-left-solid row4-column2-border1-left-solid row5-column1-border1-left-solid row6-column2-border1-left-solid row7-column2-border1-left-solid row3-column1-border1-right-dashed row5-column1-border1-right-dashed column3-border-left-dashed column1-border1-right-solid-head row1-border-bottom-dashed row3-border-bottom-dashed row5-border-bottom-dashed row6-border-bottom-dashed head-highlight-1 tr-hover">

|    &emsp;    |                                            >                                            |                                      对率回归                                      |
| :----------: | :-------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
|   $\Ycal$    |                                      $\{ \pm 1 \}$                                      |                                    $\{ 0,1 \}$                                     |
| 后验<br>概率 |                  $\Pr(y=+1 \big\arrowvert \xv) = \sigma(\wv^\top \xv)$                  |                $\Pr(y=1 \big\arrowvert \xv) = \sigma(\wv^\top \xv)$                |
|      ^       |                 $\Pr(y=-1 \big\arrowvert \xv) = \sigma(-\wv^\top \xv)$                  |               $\Pr(y=0 \big\arrowvert \xv) = \sigma(-\wv^\top \xv)$                |
| 优化<br>目标 |                $\min_{\wv} \sum_i \ln (1 + \exp(- y_i \wv^\top \xv_i))$                 |     $\min_{\wv} \sum_i (\ln (1 + \exp(\wv^\top \xv_i)) - y_i \wv^\top \xv_i)$      |
|      ^       |            $\min_{\wv} (- \sum_{i \in [m]} \ln \sigma(y_i \wv^\top \xv_i))$             | $\min_{\wv} \sum_{i \in [m]} (- \ln \sigma(-\wv^\top \xv_i) - y_i \wv^\top \xv_i)$ |
|    $\gv$     |                   $\sum_i (\sigma(y_i \wv^\top \xv_i) - 1) y_i \xv_i$                   |                   $\sum_i (\sigma(\wv^\top \xv_i) - y_i) \xv_i$                    |
|    $\Hv$     | $\sum_i (\sigma(y_i \wv^\top \xv_i)) (1 - \sigma(y_i \wv^\top \xv_i)) \xv_i \xv_i^\top$ |   $\sum_i \sigma(\wv^\top \xv_i) (1 - \sigma(\wv^\top \xv_i)) \xv_i \xv_i^\top$    |

</div>

以上是通过{==极大似然法==}导出的，用{==交叉熵==}可以导出同样的结果

<!-- slide vertical=true data-notes="" -->

##### 交叉熵

---

问题：给定分布$\qv$，如何度量分布$\pv$与它之间的差异？

定义交叉熵$H_{\qv} (\pv) \triangleq - \sum_i q_i \log p_i = \sum_i q_i \log (1/p_i)$

当$\pv = \qv$时交叉熵最小，此时交叉熵$H_{\qv} (\pv)$即为分布$\qv$的熵$H(\qv)$

<div class="top4"></div>

$$
\begin{align*}
    \qquad \min_{\pv} ~ H_{\qv} (\pv) = - \sum_i q_i \log p_i = \sum_i q_i \log (1/p_i), \quad \st ~ \sum_i p_i = 1
\end{align*}
$$

<div class="top-2"></div>

拉格朗日函数为$L = - \sum_i q_i \log p_i + \alpha (\sum_i p_i - 1)$，于是

$$
\begin{align*}
    \qquad \frac{\partial L}{\partial p_i} = - \frac{q_i}{p_i} + \alpha = 0 \Longrightarrow q_i = \alpha p_i \Longrightarrow \sum_i q_i = \alpha \sum_i p_i \Longrightarrow \alpha = 1
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 交叉熵损失

---

考虑将对率回归的预测结果和真实标记都写成分布的形式

- 对率回归的预测结果是分布$\pv = [\sigma(\wv^\top \xv); \sigma(-\wv^\top \xv)]$
- 对$\Ycal = \{ \pm 1 \}$，真实标记分布$\qv_{\{ \pm 1 \}} = [(1+y)/2; (1-y)/2]$
- 对$\Ycal = \{ 0,1 \}$，真实标记分布$\qv_{\{ 0,1 \}} = [y; 1-y]$

<div class="top2"></div>

$$
\begin{align*}
    \qquad H_{\qv_{\{ \pm 1 \}}} (\pv) & = - \frac{1+y}{2} \log \sigma(\wv^\top \xv) - \frac{1-y}{2} \log \sigma(-\wv^\top \xv) \\
    & = \begin{cases}
        - \log \sigma(\wv^\top \xv), & y = 1 \\
        - \log \sigma(-\wv^\top \xv), & y = -1
    \end{cases} \\
    & = - \log \sigma(y \wv^\top \xv) = \log (1 + \exp (- y \wv^\top \xv)) \\[6pt]
    H_{\qv_{\{ 0,1 \}}} (\pv) & = - y \log \sigma(\wv^\top \xv) - (1-y) \log \sigma(-\wv^\top \xv) \\
    & = -y \log \frac{\sigma(\wv^\top \xv)}{1 - \sigma(\wv^\top \xv)} - \log \sigma(-\wv^\top \xv) \\
    & = \log (1 + \exp(\wv^\top \xv)) - y \wv^\top \xv
\end{align*}
$$

<!-- slide data-notes="" -->

##### 多类扩展

---

设共有$C$个类，预测函数$f(\xv) = \argmax_{c \in [C]} (\wv_c^\top \xv + b_c)$

引入$\Rbb^C \mapsto \Delta^C$的 Softmax 映射：

$$
\begin{align*}
    p(y = c | \xv) & = \frac{\exp (\wv_c^\top \xv + b_c)}{\sum_{c' \in [C]} \exp (\wv_{c'}^\top \xv + b_{c'})} \\
    & = \frac{\exp ((\wv_c - \wv_C)^\top \xv + b_c - b_C)}{\sum_{c' \in [C-1]} \exp ((\wv_{c'} - \wv_C)^\top \xv + b_{c'} - b_C) + 1}
\end{align*}
$$

令$\wv_c \leftarrow \wv_c - \wv_C$，$b_c \leftarrow b_c - b_C$，记$p_c = p(y = c | \xv)$，于是

$$
\begin{align*}
    p_c = \frac{\exp (\wv_c^\top \xv + b_c)}{\sum_{c' \in [C-1]} \exp (\wv_{c'}^\top \xv + b_{c'}) + 1}, \quad p_C = 1 - \sum_{c' \in [C-1]} p_c
\end{align*}
$$

<!-- slide data-notes="" -->

##### 损失函数

---

$$
\begin{align*}
    p_c = \frac{\exp (\wv_c^\top \xv + b_c)}{\sum_{c' \in [C-1]} \exp (\wv_{c'}^\top \xv + b_{c'}) + 1}, \quad p_C = 1 - \sum_{c' \in [C-1]} p_c
\end{align*}
$$

对于样本$(\xv_i, y_i)$，$\qv_i = [1_{y_i=1}, 1_{y_i=2}, \ldots, 1_{y_i=C}]$为$y_i$的独热编码

$$
\begin{align*}
    \pv_i & = [p_1, \ldots, p_{C-1}, p_C] = \frac{[ \exp (\wv_1^\top \xv_i + b_1), \ldots, \exp (\wv_{C-1}^\top \xv_i + b_{C-1}), 1 ]}{\sum_{c' \in [C-1]} \exp (\wv_{c'}^\top \xv_i + b_{c'}) + 1}
\end{align*}
$$

采用交叉熵$H_{\qv_i} (\pv_i)$作为替代损失可得多分类对数几率回归

$$
\begin{align*}
    \min_{\wv_c, b_c} & ~ \frac{1}{2} \sum_{c \in [C-1]} \| \wv_c \|_2^2 + \frac{\lambda}{m} \sum_{i \in [m]} \sum_{c \in [C]} [\qv_i]_c \log \frac{1}{[\pv_i]_c}
\end{align*}
$$
