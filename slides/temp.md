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

##### 再看线性回归

---

特征空间$\Xcal \subset \Rbb^d$，标记空间$\Ycal$，$\Xcal \times \Ycal$上的{==未知==}概率分布$\Dcal$

<div class="top-2"></div>

训练数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，其中$(\xv_i, y_i) \overset{\mathrm{iid}}{\sim} \Dcal$

假设数据的生成方式 (归纳偏好) 为

- 先在特征空间$\Xcal$中随机选取$\xv_i$
- 计算$y_i = \wv^\top \xv_i + \epsilon_i$，其中$\epsilon_i \sim \Ncal(0,\sigma^2)$

<div class="top2"></div>

目前待估计的参数是$\wv$和$\sigma^2$，似然为

$$
\begin{align*}
    \qquad \Pbb (D | \wv, \sigma^2) & = \prod_{i \in [m]} \Pbb (\xv_i, y_i | \wv, \sigma^2) = \prod_{i \in [m]} \Pbb (\xv_i) \Pbb (y_i | \xv_i, \wv, \sigma^2) \\
    & \propto \prod_{i \in [m]} \Pbb (y_i | \xv_i, \wv, \sigma^2) = \prod_{i \in [m]} \Ncal(\wv^\top \xv_i,\sigma^2)
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 线性回归 极大似然

---

对数似然为

$$
\begin{align*}
    \qquad \log \Pbb (D | \wv, \sigma^2) & = \const + \sum_{i \in [m]} \log \Ncal(\wv^\top \xv_i,\sigma^2) \\
    & = \const - \sum_{i \in [m]} \left( \frac{(y_i - \wv^\top \xv_i)^2}{2 \sigma^2} + \log \sigma \right)
\end{align*}
$$

极大似然估计$\wv$对应的优化问题为

$$
\begin{align*}
    \qquad \min_{\wv} ~ \sum_{i \in [m]} (y_i - \wv^\top \xv_i)^2 = \| \Xv \wv - \yv \|^2
\end{align*}
$$

我的批注 在上页的假设下，{==极大似然估计等价于最小二乘回归==}

<!-- slide vertical=true data-notes="" -->

##### 线性回归 贝叶斯视角

---

假设$\wv$的先验分布$\Pbb(\wv) = \Ncal(\wv | \mv_0, \Sv_0)$

根据贝叶斯公式，后验为

$$
\begin{align*}
    \quad \Pbb(\wv | D) & \propto \Pbb(\wv) \Pbb(D | \wv) \\
    & \propto \exp \left( -\frac{1}{2} (\wv - \mv_0)^\top \Sv_0^{-1} (\wv - \mv_0) \right) \prod_{i \in [m]} \exp \left( - \frac{(y_i - \wv^\top \xv_i)^2}{2 \sigma^2} \right) \\
    & = \exp \left( -\frac{1}{2} (\wv - \mv_0)^\top \Sv_0^{-1} (\wv - \mv_0) - \frac{\| \Xv \wv - \yv \|^2}{2 \sigma^2} \right)
\end{align*}
$$
