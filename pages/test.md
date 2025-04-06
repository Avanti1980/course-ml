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

##### 最大化模型证据

---

对数模型证据

$$
\begin{align*}
    \quad {\small \ln p(\yv | \alpha, \beta) = \frac{n}{2} \ln \alpha + \frac{m}{2} \ln \beta - \frac{1}{2} \ln |\Sigmav^{-1}| - \frac{\beta}{2} \| \yv - \Phiv \muv \|_2^2 - \frac{\alpha}{2} \muv^\top \muv - \frac{m}{2} \ln (2 \pi) }
\end{align*}
$$

$\Sigmav^{-1} = \beta \Phiv^\top \Phiv + \alpha \Iv_n$，设$\beta \Phiv^\top \Phiv$特征值为$\{ \lambda_i \}_{i \in [n]}$，$\Sigmav^{-1}$特征值为$\{ \alpha + \lambda_i \}_{i \in [n]}$，$\ln |\Sigmav^{-1}| = \ln \prod_{i \in [n]} (\alpha + \lambda_i) = \sum_{i \in [n]} \ln (\alpha + \lambda_i)$

$$
\begin{align*}
    \quad \frac{\diff \ln |\Sigmav^{-1}|}{\diff \alpha} & = \sum_{i \in [n]} \frac{\diff \ln (\alpha + \lambda_i)}{\diff \alpha} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \\
    \frac{\diff \ln |\Sigmav^{-1}|}{\diff \beta} & = \sum_{i \in [n]} \frac{\diff \ln (\alpha + \lambda_i)}{\diff \beta} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \frac{\diff \lambda_i}{\diff \beta} = \sum_{i \in [n]} \frac{1}{\alpha + \lambda_i} \frac{\lambda_i}{\beta}
\end{align*}
$$

<p class="footnote comments"> 注意$\beta \Phiv^\top \Phiv \vv_i = \lambda_i \vv_i$，两者呈线性关系，故$\diff \lambda_i / \diff \beta = \lambda_i / \beta$。</p>


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
