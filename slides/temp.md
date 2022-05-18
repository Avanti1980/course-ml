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
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-entropy.js"

<!-- slide data-notes="" -->

##### 更好的界

---

感知机最终得到的超平面{==不唯一==}，其

- 与$\wv$的初始化有关
- 与迭代过程中误分类点的顺序也有关

间隔也没有保证，可能会很小，而间隔与泛化性能是息息相关的

<div class="top2"></div>

现放宽感知机的更新条件：

$$
\begin{align*}
    \qquad y \wv^\top \xv \le 0 ~ \longrightarrow ~ \frac{y \wv^\top \xv}{\| \wv \|} < \frac{\rho}{2}
\end{align*}
$$

<div class="top-4"></div>

即原本是犯错才更新，现在改为只要间隔不够大就更新

当无法再更新时，停止算法就得到了间隔至少为$\frac{\rho}{2}$的超平面

<!-- slide vertical=true data-notes="" -->

##### 更好的界

---

下面证明经此改动后，更新次数$M$最多变成$16r^2 / \rho^2$

取学习率$\eta = 1$，同前面一样有

$$
\begin{align*}
    M \rho \le \sum_{t \in [M]} y_{i_t} \vv^\top \xv_{i_t} \le \|\vv\| \left\| \sum_{t \in [M]} y_{i_t} \xv_{i_t} \right\| = \left\| \sum_{t \in [M]} (\wv_t - \wv_{t-1}) \right\| = \| \wv_M \|
\end{align*}
$$

<div class="top-4"></div>

若$\| \wv_M \| < 4 r^2 / \rho$，则$M < 4 r^2 / \rho^2 < 16r^2 / \rho^2$，结论已证

故不妨设$\| \wv_M \| \ge 4 r^2 / \rho$，对$\forall t \in [M]$，由新的更新规则知

$$
\begin{align*}
    \| \wv_t \|^2 & = \| \wv_{t-1} + y_{i_t} \xv_{i_t} \|^2 = \| \wv_{t-1} \|^2 + 2 y_{i_t} \wv_{t-1}^\top \xv_{i_t} + \| \xv_{i_t} \|^2 \\
    & \le \| \wv_{t-1} \|^2 + \rho \| \wv_{t-1} \| + r^2 \le \left( \| \wv_{t-1} \| + \frac{\rho}{2} \right)^2 + r^2 \\
    & \Longrightarrow \| \wv_t \| - \| \wv_{t-1} \| - \frac{\rho}{2} \le \frac{r^2}{\| \wv_t \| + \| \wv_{t-1} \| + \frac{\rho}{2}}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 更好的界

---

$$
\begin{align*}
    \| \wv_t \| - \| \wv_{t-1} \| - \frac{\rho}{2} \le \frac{r^2}{\| \wv_t \| + \| \wv_{t-1} \| + \frac{\rho}{2}}
\end{align*}
$$

若$\| \wv_t \|$和$\| \wv_{t-1} \|$中至少有一个$\ge 4 r^2 / \rho$，则

$$
\begin{align*}
    \| \wv_t \| \le \| \wv_{t-1} \| + \frac{\rho}{2} + \frac{r^2}{\frac{4 r^2}{\rho} + \frac{\rho}{2}} \le \| \wv_{t-1} \| + \frac{\rho}{2} + \frac{\rho}{4} = \| \wv_{t-1} \| + \frac{3\rho}{4}
\end{align*}
$$

注意$\| \wv_1 \| = \| \wv_0 + y_{i_1} \xv_{i_1} \| \le r$，又$\rho \le y_{i_1} \vv^\top \xv_{i_1} \le \|y_{i_1} \xv_{i_1}\| \le r$，故$\|\wv_1\| \le r \le 4 r^2 / \rho$，但$\| \wv_M \| \ge 4 r^2 / \rho$

必存在一个最大的$t$使得$\|\wv_t\| < 4 r^2 / \rho$且$\|\wv_{t+1}\| \ge 4 r^2 / \rho$，这表明$t$次更新后，每次更新得到的新$\|\wv\|$均$\ge 4 r^2 / \rho$

<!-- slide vertical=true data-notes="" -->

##### 更好的界

---

故由上面的推导知

$$
\begin{align*}
    \| \wv_M \|  & \le \| \wv_{M-1} \| + \frac{3\rho}{4}  \\
                      & \vdots                                \\
    \qquad \| \wv_{t+1} \| & \le \| \wv_t \| + \frac{3\rho}{4}
\end{align*}
$$

上面的不等式个数不超过$M$个，故

$$
\begin{align*}
    \qquad M \rho \le \| \wv_M \| \le \| \wv_t \| + \frac{3 M \rho}{4} \le \frac{4 r^2}{\rho} + \frac{3 M \rho}{4} \Longrightarrow M \le \frac{16r^2}{\rho^2}
\end{align*}
$$

我的批注 可以更新次数扩大$16$倍为代价换取间隔$\ge \rho /2$的超平面
