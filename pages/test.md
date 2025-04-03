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

##### 模型证据

---

将$\wv$积分掉，模型证据

$$
\begin{align*}
    \quad p(\yv | \alpha, \beta) = \frac{\beta^{m/2} \alpha^{n/2} |\Sigmav^{-1}|^{1/2}}{(2 \pi)^{m/2}} \exp \left( - \frac{\beta}{2} \yv^\top \yv + \frac{1}{2} \muv^\top \Sigmav \muv \right)
\end{align*}
$$

其中$\Sigmav = \beta \Phiv^\top \Phiv + \alpha \Iv_n$、$\muv = \Sigmav^{-1} (\beta \Phiv^\top \yv)$，代入

$$
\begin{align*}
    \quad - \frac{\beta}{2} \yv^\top & \yv + \frac{1}{2} \muv^\top \Sigmav \muv = - \frac{1}{2} (\beta \yv^\top \yv - 2 \muv^\top \Sigmav \class{blue}{\muv} + \muv^\top \class{green}{\Sigmav} \muv) \\
    & = - \frac{1}{2} (\beta \yv^\top \yv - 2 \muv^\top \Sigmav \class{blue}{\Sigmav^{-1} (\beta \Phiv^\top \yv)} + \muv^\top \class{green}{(\beta \Phiv^\top \Phiv + \alpha \Iv_n)} \muv) \\
    & = - \frac{1}{2} (\beta \yv^\top \yv - 2 \beta \muv^\top \Phiv^\top \yv + \beta \muv^\top \Phiv^\top \Phiv \muv + \alpha \muv^\top \muv) \\
    & = - \frac{\beta}{2} \| \yv - \Phiv \muv \|_2^2 - \frac{\alpha}{2} \muv^\top \muv
\end{align*}
$$

<!-- slide data-notes="" -->

##### 最大化模型证据

---

注意$|\Sigmav^{-1}|^{1/2} = |\Sigmav|^{-1/2}$，对数模型证据

$$
\begin{align*}
    \quad \ln p(\yv | \alpha, \beta) & = \frac{n}{2} \ln \alpha + \frac{m}{2} \ln \beta - \frac{\beta}{2} \| \yv - \Phiv \muv \|_2^2 - \frac{\alpha}{2} \muv^\top \muv \\
    & \qquad - \frac{1}{2} \ln |\Sigmav| - \frac{m}{2} \ln (2 \pi)
\end{align*}
$$

注意$\Sigmav = \beta \Phiv^\top \Phiv + \alpha \Iv_n$，设$\beta \Phiv^\top \Phiv$特征值为$\{ \lambda_i \}_{i \in [n]}$，则$\Sigmav$特征值为$\{ \alpha + \lambda_i \}_{i \in [n]}$，$\ln |\Sigmav| = \ln \prod_{i \in [n]} (\alpha + \lambda_i) = \sum_{i \in [n]} \ln (\alpha + \lambda_i)$

$$
\begin{align*}
    \quad \frac{\diff \ln |\Sigmav|}{\diff \alpha} & = \sum_{i \in [n]} \frac{\diff \ln (\alpha + \lambda_i)}{\diff \alpha} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \\
    \frac{\diff \ln |\Sigmav|}{\diff \beta} & = \sum_{i \in [n]} \frac{\diff \ln (\alpha + \lambda_i)}{\diff \beta} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \frac{\diff \lambda_i}{\diff \beta} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \frac{\lambda_i}{\beta}
\end{align*}
$$

<p class="footnote comments"> 注意$\beta \Phiv^\top \Phiv \vv_i = \lambda_i \vv_i$，两者呈线性关系，故$\diff \lambda_i / \diff \beta = \lambda_i / \beta$。</p>

<!-- slide vertical=true data-notes="" -->

##### 最大化模型证据

---

令对数模型证据关于$\alpha$的导数为零

$$
\begin{align*}
    \quad \frac{\diff \ln p(\yv | \alpha, \beta)}{\diff \alpha} & = \frac{n}{2\alpha} - \frac{1}{2} \muv^\top \muv - \frac{1}{2} \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} = 0 \\
    & \Longrightarrow \alpha \muv^\top \muv = n - \sum_{i \in [n]} \frac{\alpha}{\alpha + \lambda_i} = \sum_{i \in [n]} \frac{\lambda_i}{\alpha + \lambda_i} \triangleq \gamma \\
    & \Longrightarrow \alpha = \frac{\gamma}{\muv^\top \muv}
\end{align*}
$$

注意$\gamma$、$\muv = (\beta \Phiv^\top \Phiv + \alpha \Iv_n)^{-1} (\beta \Phiv^\top \yv)$都与$\alpha$相关，故交替求解

- 每轮先根据当前的$\alpha$计算$\gamma$、$\muv$，再根据最新的$\gamma$、$\muv$更新$\alpha$
- $\Phiv^\top \Phiv$的特征值可以事先算好，乘以$\beta$就是$\lambda_i$

<!-- slide vertical=true data-notes="" -->

##### 最大化模型证据

---

令对数模型证据关于$\beta$的导数为零

$$
\begin{align*}
    \quad \frac{\diff \ln p(\yv | \alpha, \beta)}{\diff \beta} & = \frac{m}{2\beta} - \frac{1}{2} \| \yv - \Phiv \muv \|_2^2 - \frac{1}{2} \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \frac{\lambda_i}{\beta} = 0 \\
    & \Longrightarrow \frac{m - \gamma}{\beta} = \| \yv - \Phiv \muv \|_2^2 \\
    & \Longrightarrow \frac{1}{\beta} = \frac{1}{m - \gamma} \| \yv - \Phiv \muv \|_2^2
\end{align*}
$$

注意$\muv = (\beta \Phiv^\top \Phiv + \alpha \Iv_n)^{-1} (\beta \Phiv^\top \yv)$与$\beta$相关，故交替求解

- $\alpha$、$\beta$可以一起更新
- 每轮先根据当前的$\alpha$、$\beta$计算$\gamma$、$\muv$，再根据最新的$\gamma$、$\muv$更新$\alpha$、$\beta$

<!-- slide data-notes="" -->

##### 频率 <span style="font-weight:900">_vs._</span> 贝叶斯

---

在机器学习中的区别：是否考虑先验

当观测数据量很大时，先验 (伪数据) 就无足轻重了，两种做法不会有太大差别

当观测数据量不大时，先验对模型性能有显著影响 (归纳偏好)

- 先验是主观的，纯人为选取，没有标准
- 抛硬币问题选贝塔分布做先验就是图计算方便
- 利用共轭先验可以不用显式地积分求$p(X)$，肉眼就能看出结果

<div class="top2"></div>

先验需有适当的自由度，能通过调整参数灵活表示领域知识
