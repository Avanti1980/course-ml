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

##### 优化

---

<div class="threelines head-highlight-1 tr-hover column3-border1-right-solid-head row1-border-bottom-dashed row3-border-bottom-dashed column2-border-left-solid column3-border-left-solid row1-column4-border1-left-solid row2-column4-border1-left-solid row3-column1-border1-left-solid row4-column4-border1-left-solid row5-column1-border1-left-solid">

|   模型   |    $\Ycal$    |                                 优化目标                                  |                        $\gv$                        |
| :------: | :-----------: | :-----------------------------------------------------------------------: | :-------------------------------------------------: |
| 线性回归 |    $\Rbb$     |               $\min_{\wv} \sum_i (\wv^\top \xv_i - y_i)^2$                |       $2 \sum_i (\wv^\top \xv_i - y_i) \xv_i$       |
|  感知机  | $\{ \pm 1 \}$ |          $\min_{\wv} \sum_i \max \{ 0, - y_i \wv^\top \xv_i \}$           | $-\sum_i \Ibb(y_i \wv^\top \xv_i \le 0) y_i \xv_i$  |
|    ^     |   $\{1,0\}$   |      $\min_{\wv} \sum_i (\sgn(\wv^\top \xv_i) - y_i) \wv^\top \xv_i$      |     $\sum_i (\sgn(\wv^\top \xv_i) - y_i) \xv_i$     |
| 对率回归 | $\{ \pm 1 \}$ |         $\min_{\wv} \sum_i \ln (1 + \exp(- y_i \wv^\top \xv_i))$          | $\sum_i (\sigma(y_i \wv^\top \xv_i) - 1) y_i \xv_i$ |
|    ^     |  $\{ 1,0 \}$  | $\min_{\wv} \sum_i (\ln (1 + \exp(\wv^\top \xv_i)) - y_i \wv^\top \xv_i)$ |    $\sum_i (\sigma(\wv^\top \xv_i) - y_i) \xv_i$    |

</div>

求极值通常来说只需令$\gv = \zerov$即可，但$\wv$可能会很难求

线性回归：$\sum_i \xv_i \xv_i^\top \wv = \sum_i y_i \xv_i \Longrightarrow \wv^\star = (\sum_i \xv_i \xv_i^\top)^{-1} (\sum_i y_i \xv_i)$

感知机和对率回归对应的$\gv = \zerov$是非线性方程，$\wv$更难求

<!-- slide vertical=true data-notes="" -->

##### 梯度下降

---

设优化目标函数为$F(\wv)$，用迭代法构造单调递减序列：

$$
\begin{align*}
    \qquad F(\wv_0) \ge F(\wv_1) \ge F(\wv_2) \ge F(\wv_3) \ge \cdots
\end{align*}
$$

<div class="top-3"></div>

我的启示 {==单调有界序列必收敛==}，若$F$有下界，序列就会收敛到$F(\wv^\star)$

问题：如何实现单调递减？根据泰勒展式及柯西不等式知

$$
\begin{align*}
    -\| \nabla F(\wv)\| ~ \|\uv\| \le \lim_{\eta \rightarrow 0} \frac{F(\wv + \eta \uv) - F(\wv)}{\eta} = \nabla F(\wv)^\top \uv \le \| \nabla F(\wv)\| ~ \|\uv\|
\end{align*}
$$

<div class="top-1"></div>

- 只要$\uv$与$\nabla F(\wv)$夹角为钝角，就可以使得目标函数值下降
- 左边取等号条件是$\uv = -k \cdot \nabla F(\wv)$，{==负梯度是瞬时下降最快的方向==}

<div class="top2"></div>

梯度下降 (<u>g</u>radient <u>d</u>escent, GD)：$\wv_{t+1} \leftarrow \wv_t - \eta_t \nabla F(\wv_t)$

<!-- slide vertical=true data-notes="" -->

##### 梯度下降解线性回归

---

@import "../python/gradient-descent.svg" {.center .top6 .width90 title="用梯度下降求解 R 上的最小二乘"}

<!-- slide data-notes="" -->

##### 随机梯度下降

---

许多机器学习模型的优化目标为最小化每个样本上的损失的和

$$
\begin{align*}
    \qquad \min_{\wv} F(\wv) = \frac{1}{m} \sum_{i \in [m]} \ell(y_i, f(\xv_i;\wv))
\end{align*}
$$

<div class="top-4"></div>

计算梯度$\nabla F(\wv) = \sum_{i \in [m]} \nabla \ell (y_i; f(\xv_i;\wv)) / m$需遍历所有训练样本，当样本数$m$很大时，梯度计算开销很大

批量梯度下降，随机采样一个下标子集$\Bcal_t \subseteq [m]$

$$
\begin{align*}
    \qquad \wv_{t+1} \leftarrow \wv_t - \eta_t \frac{1}{|\Bcal_t|} \sum_{i \in \Bcal_t} \nabla \ell(y_i, f(\xv_i;\wv))
\end{align*}
$$

<div class="top-4"></div>

若$|\Bcal_t| = 1$，则为常说的{==随机梯度下降==} (SGD)

<!-- slide vertical=true data-notes="" -->

##### GD vs. SGD

---

更新公式：

$$
\begin{align*}
    & \wv_{t+1} \leftarrow \wv_t - \eta_t \left( \frac{1}{m} \sum_{i \in [m]} \nabla l(y_i, f(\xv_i)) + \lambda \cdot \nabla \Omega(\wv) \right) \\
    & \wv_{t+1} \leftarrow \wv_t - \eta_t \left( \frac{1}{|\Bcal_t|} \sum_{i \in \Bcal_t} \nabla l(y_i, f(\xv_i)) + \lambda \cdot \nabla \Omega(\wv) \right)
\end{align*}
$$

- 当数据集中有冗余样本时，SGD 可以减少重复计算
- 迭代前期，SGD 更新频率快，较 GD 优势明显
- 迭代后期，GD 会停止于最优解处，SGD 则只能在最优解附近震荡
- 越靠近最优解，梯度越接近零，因此 GD 可以用恒定步长
- 最优解处随机梯度不一定为零，故 SGD 必须用衰减步长，否则算法不会停止
- SGD 因随机采样带来的噪声若能随着迭代而受到抑制，则可进一步加速，机器学习顶会有大量相关工作，包括 SAG，SAGA，SVRG 等及其衍生变种

<!-- slide data-notes="" -->

##### 加速梯度下降

---

当目标函数的变量尺度不同时，梯度下降效率很低

<img src="../python/momentum.svg" class="center width90 top2 bottom2">

动量法 (momentum)：$\wv_{t+1} = \wv_t - \eta_t \nabla F(\wv_t) + \gamma (\wv_t - \wv_{t-1})$

- 相对于梯度下降，多了第三项，上一轮的更新方向
- 参数$\gamma < 1$，通常取$0.9$

<!-- slide vertical=true data-notes="" -->

##### 动量法

---

$$
\begin{align*}
    \wv_{t+1} - \wv_t & = - \eta_t \nabla F(\wv_t) + \gamma (\wv_t - \wv_{t-1}) \\
    \gamma (\wv_t - \wv_{t-1}) & = - \eta_{t-1} \gamma \nabla F(\wv_{t-1}) + \gamma^2 (\wv_{t-1} - \wv_{t-2}) \\
    & \vdots \\
    \gamma^{t-1} (\wv_2 - \wv_1) & = - \eta_1 \gamma^{t-1} \nabla F(\wv_1) + \mathtip{\gamma^t (\wv_1 - \wv_0)}{因为\wv_1 = \wv_0，故该项等于零} \\
    \Longrightarrow ~ \wv_{t+1} - \wv_t & = - \sum_{i \in [t]} \eta_i \gamma^{t-i} \nabla F(\wv_i)
\end{align*}
$$

动量法每步更新是历史梯度的加权平均

- 若近期梯度方向不一致，则真实的更新幅度变小，减速，增加稳定性
- 若近期梯度方向较为一致，则真实的更新幅度变大，加速，加快收敛

Nesterov 加速梯度 (NAG)：改进动量法的第二步

$$
\begin{align*}
    \begin{cases} \widetilde{\wv} = \wv_t + \gamma (\wv_t - \wv_{t-1}) \\ \wv_{t+1} = \widetilde{\wv} - \eta_t \class{yellow}{\nabla F (\wv_t)} \end{cases} ~ \longrightarrow ~ \begin{cases} \widetilde{\wv} = \wv_t + \gamma (\wv_t - \wv_{t-1}) \\ \wv_{t+1} = \widetilde{\wv} - \eta_t \class{yellow}{\nabla F (\widetilde{\wv})} \end{cases}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 动量法 vs. NAG

---

第$t$轮迭代示意图：

@import "../tikz/mvsnag.svg" {.center .width90 .top6 .bottom2}
