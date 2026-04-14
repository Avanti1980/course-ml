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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-entropy.js"

<!-- slide data-notes="" -->

<div class="bottom20"></div>

# 机器学习

<hr class="width50 center">

## 朴素贝叶斯

<div class="bottom8"></div>

### 计算机学院&emsp;张腾

#### *tengzhang@hust.edu.cn*

<!-- slide vertical=true data-notes="" -->

##### 大纲

---

@import "../vega/outline.json" {as="vega" .top-2}

<!-- slide data-notes="" -->

##### 贝叶斯决策论

---

<div class="top2"></div>

- 样本空间$\xc$，标记集合$\yc$
- $\ds$是$\xc \times \yc$上的未知概率分布，概率密度函数为$p(\xv, y)$
- 损失函数$\ell: \yc \times \yc \mapsto \rb$

学习器$h: \xc \mapsto \yc$的泛化风险为

<p>
\begin{align}
    R_{\ds} (h) & = \eb_{(\xv,y) \sim \ds} [\ell(y, h(\xv))] = \iint \ell(y, h(\xv)) p(\xv, y) \diff \xv \diff y \\
    & = \int \left( \int \ell(y, h(\xv)) p(y|\xv) \diff y \right) p(\xv) \diff \xv \\
    & = \eb_{\xv} \left[ \int \ell(y, h(\xv)) p(y|\xv) \diff y \right] = \eb_{\xv} [ \eb_y [\ell(y, h(\xv)) | \xv]]
\end{align}
</p>

最小泛化风险称为<span class="blue">贝叶斯风险</span>，对应的$h^\star$即<span class="blue">贝叶斯最优学习器</span>

<p>
\begin{align}
    h^\star(\xv) = \argmin_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 贝叶斯最优学习器

---

<p>
\begin{align}
    h^\star(\xv) = \argmin_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align}
</p>

回归问题通常采用平方损失$\ell(y, h(\xv)) = (y - h(\xv))^2$

<p>
\begin{align}
    \nabla_{h(\xv)} \left( \int (y - h(\xv))^2 p(y|\xv) \diff y \right) & = 2 \int (h(\xv) - y) p(y|\xv) \diff y \\
    & = 2 h(\xv) - 2 \int y p(y|\xv) \diff y \\
    & = 2 h(\xv) - 2 \eb[y|\xv]
\end{align}
</p>

即回归问题的贝叶斯最优模型$h^\star(\xv) = \eb[y|\xv]$

在偏差方差分解中我们曾得到相同的结论

<p>
\begin{align}
    \eb_{(\xv,y) \sim \ds} [(y - h(\xv))^2] = \eb_{\xv} [(h(\xv) - \eb [y|\xv])^2] + 噪声
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 贝叶斯最优学习器

---

<p>
\begin{align}
    h^\star(\xv) = \argmin_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align}
</p>

对分类问题，设$\yc = [c]$，$\ell(y, h(\xv)) = \ib(y \ne h(\xv))$，则

<p>
\begin{align}
    h^\star(\xv) & = \argmin_{\yh \in [c]} \sum_{y \in [c]} \ib(y \ne \yh) p(y|\xv) \\
    & = \argmin_{\yh \in [c]} ~ (1 - p(\yh|\xv)) \\
    & = \argmax_{\yh \in [c]} ~ p(\yh|\xv)
\end{align}
</p>

即分类问题的贝叶斯最优模型$h^\star(\xv) = \argmax_{\yh \in [c]} p(\yh|\xv)$

<p class="fragment"> $\eb[y|\xv]$和$\argmax_{\yh \in [c]} p(\yh|\xv)$均依赖未知的$p$，无法直接得到</p>

<!-- slide data-notes="" -->

##### 判别式 _vs._ 生成式

---

利用训练集求$\argmax_{y \in [c]} p(y|\xv)$有两种思路

判别式方法：用线性判别式直接拟合$p(y|\xv)$，如对率回归

- 二分类：$p(1|\xv) = \sigma(\wv^\top \xv)$
- 多分类：$[p(1|\xv), \ldots, p(c|\xv)] = \softmax (\wv_1^\top \xv, \ldots, \wv_c^\top \xv)$

<div class="top2"></div>

生成式方法：迂回策略，用贝叶斯公式从数据的生成机制入手

<p>
\begin{align}
    p(y|\xv) & = \frac{\class{yellow}{p(y)} \times \class{blue}{p(\xv|y)}}{p(\xv)}
    \Longrightarrow \begin{cases} p(y = 1 | \xv) \propto \class{yellow}{p(y=1)} \times \class{blue}{p(\xv|y=1)} \\
    \quad \quad \vdots \\
    p(y = c | \xv) \propto \class{yellow}{p(y=c)} \times \class{blue}{p(\xv|y=c)} \end{cases} \\[10pt]
    & \Longrightarrow \argmax_{y \in [c]} p(y|\xv) = \argmax_{y \in [c]} p(y) p(\xv | y)
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 朴素贝叶斯

---

<p>
\begin{align}
    \argmax_{y \in [c]} p(y|\xv) = \argmax_{y \in [c]} p(y) p(\xv | y)
\end{align}
</p>

注意$\xv = [x_1; x_2; \ldots; x_d]$，于是有分解

<p>
\begin{align}
    p(\xv | y) = p(x_1 | y) p(x_2 | x_1, y) \cdots p(x_d | x_{d-1}, \ldots, x_2, x_1, y)
\end{align}
</p>

上式很难算，要考虑所有特征的所有取值，指数爆炸！

<div class="top4"></div>

朴素贝叶斯 (<span class="blue">n</span>aïve <span class="blue">B</span>ayes, NB) 引入<span class="blue">条件独立性假设</span>：

<p>
\begin{align}
    p(\xv | y) = p(x_1 | y) p(x_2 | y) \cdots p(x_d | y) = \prod_{j \in [d]} p(x_j | y)
\end{align}
</p>

问题：如何用训练集估计$p(y), ~ p(x_1 | y), ~ p(x_2 | y), ~ \ldots, ~ p(x_d | y)$？

<!-- slide data-notes="" -->

##### 从数据中估计参数

---

<p>
\begin{align}
    p(y | \xv) = p(y) p(x_1 | y) p(x_2 | y) \cdots p(x_d | y)
\end{align}
</p>

对于$p(y)$，记参数$\alpha_k = p(y = k)$，于是

<p>
\begin{align}
    p(y | \alphav) = \prod_{k \in [c]} p(y = k)^{\ib(y=k)} = \prod_{k \in [c]} \alpha_k^{\ib(y=k)}, \quad \sum_{k \in [c]} \alpha_k = 1
\end{align}
</p>

对于$p(\xv | y)$，设第$j$个特征共有$n_j$种不同取值$v_1^{(j)}, \ldots, v_{n_j}^{(j)}$

记参数$\theta_{kjl} = p( x_j = v_l^{(j)} | y=k)$，于是对$\forall k \in [c]$和$\forall j \in [d]$有

<p>
\begin{align}
    & p(x_j | y = k, \thetav) = \prod_{l \in [n_j]} \theta_{kjl}^{\ib(x_j = v_l^{(j)})}, \quad \sum_{l \in [n_j]} \theta_{kjl} = 1
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 从数据中估计参数

---

设数据集$\dc = \{ (\xv^{(i)}, y^{(i)}) \}_{i \in [m]}$，对数似然函数：

<p>
\begin{align}
    \LL & = \ln p(\dc | \alphav, \thetav) = \sum_{i \in [m]} \ln p(\xv^{(i)}, y^{(i)} | \alphav, \thetav) \\
    & = \sum_{i \in [m]} \ln \prod_{k \in [c]} p(\xv^{(i)}, y^{(i)} = k | \alphav, \thetav)^{\ib(y^{(i)}=k)} \\
    & = \sum_{i \in [m]} \sum_{k \in [c]} \ib(y^{(i)}=k) \ln p(\xv^{(i)}, y^{(i)} = k | \alphav, \thetav) \\
    & = \sum_{i \in [m]} \sum_{k \in [c]} \ib(y^{(i)}=k) \ln p(y^{(i)} = k | \alphav) \\ & \qquad \qquad \qquad + \sum_{i \in [m]} \sum_{k \in [c]} \ib(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav) \\[4pt]
    & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln \alpha_k + \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav)
\end{align}
</p>

<!-- slide data-notes="" -->

##### 极大似然估计

---

记$A_k = \sum_{i \in [m]} \ib(y^{(i)} = k)$为训练集中第$k$类样本数

$\alphav$相关的项

<p>
\begin{align}
    \max_{\alpha_k} ~ \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln \alpha_k = \sum_{k \in [c]} A_k \ln \alpha_k, \quad \st ~ \sum_{k \in [c]} \alpha_k = 1
\end{align}
</p>

拉格朗日函数$L = \sum_{k \in [c]} A_k \ln \alpha_k - \lambda ( \sum_{k \in [c]} \alpha_k - 1 )$

<p>
\begin{align}
    \nabla_{\alpha_k} L  = \frac{A_k}{\alpha_k} - \lambda = 0 & \Longrightarrow \sum_{k \in [c]} A_k = \lambda \sum_{k \in [c]} \alpha_k = \lambda \\
    & \Longrightarrow \alpha_k = \frac{A_k}{\sum_{j \in [c]} A_j} = \frac{第 k 类样本数}{总样本数}
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计

---

$\thetav$相关的项

<p>
\begin{align}
    \LL (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \sum_{j \in [d]} \ib(y^{(i)}=k) \ln p(x_j^{(i)} | y^{(i)} = k, \thetav) \quad \longleftarrow 特征独立性 \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \sum_{j \in [d]} \ib(y^{(i)}=k) \ln \prod_{l \in [n_j]} p( x_j^{(i)} = v_l^{(j)} | y^{(i)}=k)^{\ib(x_j^{(i)} = v_l^{(j)})} \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{l \in [n_j]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ib(x_j^{(i)} = v_l^{(j)}) \ln \theta_{kjl} \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl}
\end{align}
</p>

其中$B_{kjl} = \sum_{i \in [m]} \ib(y^{(i)}=k) \ib(x_j^{(i)} = v_l^{(j)})$为训练集中第$k$类样本中第$j$个特征取值$v_l^{(j)}$的样本数

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计

---

对任意给定的类别$k$和特征$j$，我们只需考虑

<p>
\begin{align}
    \max_{\theta_{kjl}} ~ \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl}, \quad \st ~ \sum_{l \in [n_j]} \theta_{kjl} = 1
\end{align}
</p>

拉格朗日函数$L = \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl} - \lambda ( \sum_{l \in [n_j]} \theta_{kjl} - 1 )$

<p>
\begin{align}
    & \nabla_{\theta_{kjl}} L = \frac{B_{kjl}}{\theta_{kjl}} - \lambda = 0 \Longrightarrow \sum_{l \in [n_j]} B_{kjl} = \lambda \sum_{l \in [n_j]} \theta_{kjl} = \lambda \\[4pt]
    & \Longrightarrow \theta_{kjl} = \frac{B_{kjl}}{\sum_{l \in [n_j]} B_{kjl}} = \frac{第 k 类样本中第j个特征取值v_l^{(j)}的样本数}{第 k 类样本数~~~}
\end{align}
</p>

<!-- slide data-notes="" -->

##### 朴素贝叶斯算法

---

根据贝叶斯公式和条件独立性假设

<p>
\begin{align}
    \argmax_{y \in [c]} p(y|\xv) & = \argmax_{y \in [c]} p(y) p(\xv | y) \\
    & = \argmax_{y \in [c]} p(y) p(x_1 | y) p(x_2 | y) \cdots p(x_d | y)
\end{align}
</p>

根据训练集求

<p>
\begin{align}
    & p(y = k) = \frac{第 k 类样本数~~~}{总样本数~~~} \\
    & p( x_j = v_l^{(j)} | y=k) = \frac{第 k 类样本中第j个特征取值v_l^{(j)}的样本数}{第 k 类样本数~~~~}
\end{align}
</p>

<p class="comments"> 朴素贝叶斯就是数数！</p>

<!-- slide vertical=true data-notes="" -->

##### 朴素贝叶斯预测约会

---

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row9-border-top-dashed row18-border-top-solid top-3 fs9 left4 righta">

| 次序 | 时间 | 方式 | 天气 | 课业 | 疫情 | 电视 | 约会 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  2   | 周日 | 吃饭 | 阴天 | 轻松 | 清零 | 精彩 |  是  |
|  3   | 周日 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  4   | 周六 | 吃饭 | 阴天 | 轻松 | 清零 | 精彩 |  是  |
|  5   | 周间 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  6   | 周六 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  是  |
|  7   | 周日 | 逛街 | 晴天 | 适中 | 平缓 | 无聊 |  是  |
|  8   | 周日 | 逛街 | 晴天 | 轻松 | 平缓 | 精彩 |  是  |
|  9   | 周日 | 逛街 | 阴天 | 适中 | 平缓 | 精彩 |  否  |
|  10  | 周六 | 学习 | 雨天 | 轻松 | 严峻 | 无聊 |  否  |
|  11  | 周间 | 学习 | 雨天 | 繁重 | 严峻 | 精彩 |  否  |
|  12  | 周间 | 吃饭 | 晴天 | 繁重 | 严峻 | 无聊 |  否  |
|  13  | 周六 | 逛街 | 晴天 | 适中 | 清零 | 精彩 |  否  |
|  14  | 周间 | 逛街 | 阴天 | 适中 | 清零 | 精彩 |  否  |
|  15  | 周日 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  否  |
|  16  | 周间 | 吃饭 | 晴天 | 繁重 | 严峻 | 精彩 |  否  |
|  17  | 周六 | 吃饭 | 阴天 | 适中 | 平缓 | 精彩 |  否  |
|  18  | 周六 | 逛街 | 阴天 | 适中 | 清零 | 无聊 |  ?   |

</div>

<div class="top-60per left55per">

<p class="fs14">
\begin{align}
    & p(约会 = 是) = 8/17 \\
    & p(时间 = 周六 | 约会 = 是) = 3/8 \\
    & p(方式 = 逛街 | 约会 = 是) = 3/8 \\
    & p(天气 = 阴天 | 约会 = 是) = 2/8 \\
    & p(课业 = 适中 | 约会 = 是) = 1/8 \\
    & p(疫情 = 清零 | 约会 = 是) = 5/8 \\
    & p(电视 = 无聊 | 约会 = 是) = 2/8 \\[5pt]
    & p(约会 = 否) = 9/17 \\
    & p(时间 = 周六 | 约会 = 否) = 3/9 \\
    & p(方式 = 逛街 | 约会 = 否) = 4/9 \\
    & p(天气 = 阴天 | 约会 = 否) = 3/9 \\
    & p(课业 = 适中 | 约会 = 否) = 4/9 \\
    & p(疫情 = 清零 | 约会 = 否) = 2/9 \\
    & p(电视 = 无聊 | 约会 = 否) = 3/9 \\[10pt]
    & \frac{8}{17} \frac{3}{8} \frac{3}{8} \frac{2}{8} \frac{1}{8} \frac{5}{8}  \frac{2}{8} < \frac{9}{17} \frac{3}{9} \frac{4}{9} \frac{3}{9} \frac{4}{9} \frac{2}{9} \frac{3}{9} \\[10pt]
    & 预测结果为“约会=否”
\end{align}
</p>

</div>

<!-- slide data-notes="" -->

##### 数值型特征

---

以文本分类为例

- 词汇表$\vc = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\nb$、$\rb$

<div class="top2"></div>

$x_j = \ib(v_j出现在文本\xv中) \in \{0,1\}$，$\theta_{kj} = p (x_j = 1 | y = k)$

<div class="top1"></div>

<p>
\begin{align}
    p (\xv | y = k, \thetav) = \prod_{j \in [d]} p (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
\end{align}
</p>

这是$d$个独立的伯努利分布的乘积

<!-- slide vertical=true data-notes="" -->

##### 数值型特征

---

以文本分类为例

- 词汇表$\vc = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\nb$、$\rb$

<div class="top2"></div>

$x_j = 词v_j在文本\xv\text中出现的次数 \in \nb$，文本总词数$x_1 + \cdots + x_d$

第$k$类文本的每个词从词汇表中依概率$[\theta_{k1}; \ldots; \theta_{kj}; \ldots; \theta_{kd}]$选取

其中$\theta_{kj}$为第$k$类文本选取词$v_j$的概率，$\sum_{j \in [d]} \theta_{kj} = 1$

<p>
\begin{align}
    p (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align}
</p>

这是<span class="blue">多项式分布</span>，特别的，$d=2$即为二项式分布

<!-- slide vertical=true data-notes="" -->

##### 数值型特征

---

以文本分类为例

- 词汇表$\vc = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\nb$、$\rb$

<div class="top2"></div>

$x_j \sim \nc(\mu_j, \sigma_j^2) \in \rb$，假设实数特征 (e.g., tf - idf) 服从高斯分布

<p>
\begin{align}
    p (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align}
</p>

这是$d$个独立的高斯分布的乘积

<!-- slide data-notes="" -->

##### 极大似然估计 情形 1

---

$x_j = \ib(v_j出现在文本\xv中) \in \{0,1\}$，$\theta_{kj} = p (x_j = 1 | y = k)$

<p>
\begin{align}
    p (\xv | y = k, \thetav) = \prod_{j \in [d]} p (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
\end{align}
</p>

对数似然函数中$\thetav$相关的项为

<p>
\begin{align}
    \LL (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln \prod_{j \in [d]} \theta_{kj}^{x_j^{(i)}} (1 - \theta_{kj})^{1 - x_j^{(i)}}        \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) (x_j^{(i)} \ln \theta_{kj} + (1 - x_j^{(i)}) \ln (1 - \theta_{kj}) ) \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) )
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 1

---

对数似然函数中$\thetav$相关的项为

<p>
\begin{align}
    \LL (\thetav) & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) (x_j^{(i)} \ln \theta_{kj} + (1 - x_j^{(i)}) \ln (1 - \theta_{kj}) ) \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) )
\end{align}
</p>

其中

<p>
\begin{align}
    B_{kj} & = \sum_{i \in [m]} \ib(y^{(i)}=k) x_j^{(i)} = 第 k 类文本中包含词v_j的文本数 \\
    \Bbar_{kj} & = \sum_{i \in [m]} \ib(y^{(i)}=k) (1 - x_j^{(i)}) = 第 k 类文本中不包含词v_j的文本数
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 1

---

对数似然函数中$\thetav$相关的项为

<p>
\begin{align}
    & \LL (\thetav) = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) ) \\
    & B_{kj} = 第 k 类文本中包含词v_j的文本数 \\
    & \Bbar_{kj} = 第 k 类文本中不包含词 v_j 的文本数
\end{align}
</p>

对某个固定的$k$和$j$，估计$\theta_{kj}$只需求解优化问题

<p>
\begin{align}
    \max_{\theta_{kj}} ~ \{ B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) \}
\end{align}
</p>

令关于$\theta_{kj}$的导数为零可得

<p>
\begin{align}
    \theta_{kj} = \frac{B_{kj}}{B_{kj} + \Bbar_{kj}} = \frac{第 k 类文本中包含词 v_j 的文本数}{第 k 类文本数}
\end{align}
</p>

<!-- slide data-notes="" -->

##### 极大似然估计 情形 2

---

$x_j = 词 v_j 在文本 \xv 中出现的次数 \in \nb$

$\theta_{kj}$为第$k$类文本选取词$v_j$的概率，$\sum_{j \in [d]} \theta_{kj} = 1$

<p>
\begin{align}
    p (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align}
</p>

对数似然函数中$\thetav$相关的项为

<p>
\begin{align}
    \LL (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln \left\{ \frac{(x_1^{(i)} + \cdots + x_d^{(i)})!}{x_1^{(i)}! \cdots x_d^{(i)}!} \prod_{j \in [d]} \theta_{kj}^{x_j^{(i)}} \right\} \\
    & = 常数 + \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) x_j^{(i)} \ln \theta_{kj}
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 2

---

对数似然函数中$\thetav$相关的项为

<p>
\begin{align}
    & \LL (\thetav) = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) x_j^{(i)} \ln \theta_{kj} = \sum_{k \in [c]} \sum_{j \in [d]} B_{kj} \ln \theta_{kj} \\
    & B_{kj} = \sum_{i \in [m]} \ib(y^{(i)}=k) x_j^{(i)} = 第 k 类文本中词 v_j 出现总次数
\end{align}
</p>

对某个固定的$k$，估计$\theta_{kj}$只需求解优化问题

<p>
\begin{align}
    \max_{\theta_{kj}} ~ \sum_{j \in [d]} B_{kj} \ln \theta_{kj}, \quad \st ~ \sum_{j \in [d]} \theta_{kj} = 1
\end{align}
</p>

拉格朗日函数$L = \sum_{j \in [d]} B_{kj} \ln \theta_{kj} - \lambda ( \sum_{j \in [d]} \theta_{kj} - 1 )$

<p>
\begin{align}
    \frac{\partial L}{\partial \theta_{kj}} = \frac{B_{kj}}{\theta_{kj}} - \lambda = 0 \Longrightarrow \theta_{kj} = \frac{第 k 类文本中词v_j出现总次数}{第 k 类文本的总词数}
\end{align}
</p>

<!-- slide data-notes="" -->

##### 极大似然估计 情形 3

---

$x_j \sim \nc(\mu_j, \sigma_j^2) \in \rb$，假设实数特征 (e.g., tf - idf) 服从高斯分布

<p>
\begin{align}
    p (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align}
</p>

对数似然函数中$\muv, \sigmav$相关的项为

<p>
\begin{align}
    \LL (\muv, \sigmav) & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \muv, \sigmav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \ib(y^{(i)}=k) \ln \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} \right) \\
    & = 常数 + \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 3

---

对数似然函数中$\muv, \sigmav$相关的项为

<p>
\begin{align}
    \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align}
</p>

对某个固定的$k$和$j$，估计$\mu_{kj}$只需求解优化问题

<p>
\begin{align}
    \min_{\mu_{kj}} ~ \sum_{i \in [m]} \ib(y^{(i)}=k) (x_j^{(i)} - \mu_{kj})^2
\end{align}
</p>

令关于$\mu_{kj}$的导数为零

<p>
\begin{align}
    \mu_{kj} & = \frac{\sum_{i \in [m]} \ib(y^{(i)}=k) x_j^{(i)}}{\sum_{i \in [m]} \ib(y^{(i)}=k)} = \frac{第 k 类文本第j个特征的和}{第 k 类文本数} \\[4pt]
    & = 第 k 类文本第j个特征的均值
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 3

---

对数似然函数中$\muv, \sigmav$相关的项为

<p>
\begin{align}
    \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \ib(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align}
</p>

对某个固定的$k$和$j$，估计$\sigma_{kj}$只需求解优化问题

<p>
\begin{align}
    \min_{\sigma_{kj}} ~ \sum_{i \in [m]} \ib(y^{(i)}=k) \left( \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} + \ln \sigma_{kj} \right)
\end{align}
</p>

令关于$\sigma_{kj}$的导数为零

<p>
\begin{align}
    \sigma_{kj}^2 & = \frac{\sum_{i \in [m]} \ib(y^{(i)}=k) (x_j^{(i)} - \mu_{kj})^2}{\sum_{i \in [m]} \ib(y^{(i)}=k)} \\
    & = 第 k 类文本第j个特征的方差
\end{align}
</p>

<!-- slide data-notes="" -->

##### 朴素贝叶斯预测约会

---

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row9-border-top-dashed row18-border-top-solid top-3 fs9 left4 righta">

| 次序 | 时间 | 方式 |    天气    | 课业 | 疫情 | 电视 | 约会 |
| :--: | :--: | :--: | :--------: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  2   | 周日 | 吃饭 |    阴天    | 轻松 | 清零 | 精彩 |  是  |
|  3   | 周日 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  4   | 周六 | 吃饭 |    阴天    | 轻松 | 清零 | 精彩 |  是  |
|  5   | 周间 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  6   | 周六 | 逛街 |    晴天    | 轻松 | 平缓 | 无聊 |  是  |
|  7   | 周日 | 逛街 |    晴天    | 适中 | 平缓 | 无聊 |  是  |
|  8   | 周日 | 逛街 |    晴天    | 轻松 | 平缓 | 精彩 |  是  |
|  9   | 周日 | 逛街 |    阴天    | 适中 | 平缓 | 精彩 |  是  |
|  10  | 周六 | 学习 |    雨天    | 轻松 | 严峻 | 无聊 |  是  |
|  11  | 周间 | 学习 |    雨天    | 繁重 | 严峻 | 精彩 |  是  |
|  12  | 周间 | 吃饭 |    晴天    | 繁重 | 严峻 | 无聊 |  是  |
|  13  | 周六 | 逛街 |    晴天    | 适中 | 清零 | 精彩 |  是  |
|  14  | 周间 | 逛街 |    阴天    | 适中 | 清零 | 精彩 |  是  |
|  15  | 周日 | 逛街 |    晴天    | 轻松 | 平缓 | 无聊 |  是  |
|  16  | 周间 | 吃饭 |    晴天    | 繁重 | 严峻 | 精彩 |  是  |
|  17  | 周六 | 吃饭 |    阴天    | 适中 | 平缓 | 精彩 |  是  |
|  18  | 周六 | 逛街 | <span class="blue">雨天</span> | 适中 | 清零 | 无聊 |  ？  |

</div>

<div class="top-60per left55per">

<p class="fs14">
\begin{align}
    & p(约会 = 否) = \class{blue}{0/17} \\[10pt]
    & 训练集中无负样本 \\[10pt]
    & 模型无脑预测“约会=是”
\end{align}
</p>

</div>

<!-- slide vertical=true data-notes="" -->

##### 朴素贝叶斯预测约会

---

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row9-border-top-dashed row18-border-top-solid top-3 fs9 left4 righta">

| 次序 | 时间 | 方式 |    天气    | 课业 | 疫情 | 电视 | 约会 |
| :--: | :--: | :--: | :--------: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  2   | 周日 | 吃饭 |    阴天    | 轻松 | 清零 | 精彩 |  是  |
|  3   | 周日 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  4   | 周六 | 吃饭 |    阴天    | 轻松 | 清零 | 精彩 |  是  |
|  5   | 周间 | 吃饭 |    晴天    | 轻松 | 清零 | 精彩 |  是  |
|  6   | 周六 | 逛街 |    晴天    | 轻松 | 平缓 | 无聊 |  是  |
|  7   | 周日 | 逛街 |    晴天    | 适中 | 平缓 | 无聊 |  是  |
|  8   | 周日 | 逛街 |    晴天    | 轻松 | 平缓 | 精彩 |  是  |
|  9   | 周日 | 逛街 |    阴天    | 适中 | 平缓 | 精彩 |  否  |
|  10  | 周六 | 学习 |    雨天    | 轻松 | 严峻 | 无聊 |  否  |
|  11  | 周间 | 学习 |    雨天    | 繁重 | 严峻 | 精彩 |  否  |
|  12  | 周间 | 吃饭 |    晴天    | 繁重 | 严峻 | 无聊 |  否  |
|  13  | 周六 | 逛街 |    晴天    | 适中 | 清零 | 精彩 |  否  |
|  14  | 周间 | 逛街 |    阴天    | 适中 | 清零 | 精彩 |  否  |
|  15  | 周日 | 逛街 |    晴天    | 轻松 | 平缓 | 无聊 |  否  |
|  16  | 周间 | 吃饭 |    晴天    | 繁重 | 严峻 | 精彩 |  否  |
|  17  | 周六 | 吃饭 |    阴天    | 适中 | 平缓 | 精彩 |  否  |
|  18  | 周六 | 逛街 | <span class="blue">雨天</span> | 适中 | 清零 | 无聊 |  ?   |

</div>

<div class="top-60per left55per">

<p class="fs14">
\begin{align}
    & p(约会 = 是) = 8/17 \\
    & p(时间 = 周六 | 约会 = 是) = 3/8 \\
    & p(方式 = 逛街 | 约会 = 是) = 3/8 \\
    & p(天气 = \class{blue}{雨天}| 约会 = 是)=\class{blue}{0/8} \\
    & p(课业 = 适中| 约会 = 是) = 1/8 \\
    & p(疫情 = 清零| 约会 = 是) = 5/8 \\
    & p(电视 = 无聊| 约会 = 是) = 2/8 \\[10pt]
    & \frac{8}{17} \frac{3}{8} \frac{3}{8} \class{blue}{\frac{0}{8}} \frac{1}{8} \frac{5}{8}  \frac{2}{8} = \class{blue}{0} \\[10pt]
    & 正样本中无“天气=雨天”的样本 \\[10pt]
    & 似然乘积为零，其它特征不起作用
\end{align}
</p>

</div>

<!-- slide vertical=true data-notes="" -->

##### 拉普拉斯平滑

---

在各取值的频数上赋予一个正数$\lambda$，通常取$\lambda=1$

<p>
\begin{align}
    & p (y = k) = \frac{第 k 类样本数 + \lambda}{总样本数 + c \lambda} \\[6pt]
    & p ( x_j = v_l^{(j)} | y=k) = \frac{第 k 类样本中第 j 个特征取值 v_l^{(j)} 的样本数 + \lambda}{第 k 类样本数 + n_j \lambda} \\[6pt]
    & p (x_j = 1 | y = k) = \frac{第 k 类文本中包含词v_j的文本数 + \lambda}{第 k 类文本数 + d \lambda} \\[6pt]
    & p (选取词v_j | y = k) = \frac{第 k 类文本中词v_j出现总次数 + \lambda}{第 k 类文本的总词数 + d \lambda}
\end{align}
</p>
