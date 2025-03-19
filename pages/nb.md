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

<div class="bottom20"></div>

# 机器学习

<hr class="width50 center">

## 朴素贝叶斯

<div class="bottom8"></div>

### 计算机学院 &nbsp;&nbsp; 张腾

#### _tengzhang@hust.edu.cn_

<!-- slide vertical=true data-notes="" -->

##### 大纲

---

@import "../vega/outline.json" {as="vega" .top-2}

<!-- slide data-notes="" -->

##### 贝叶斯决策论

---

- 样本空间$\Xcal$，类别标记集合$\Ycal$
- $\Dcal$是$\Xcal \times \Ycal$上的未知概率分布，概率密度函数为$p(\xv, y)$
- 损失函数$\ell: \Ycal \times \Ycal \mapsto \Rbb$

学习器$h: \Xcal \mapsto \Ycal$的泛化风险为

$$
\begin{align*}
    \quad R_{\Dcal} (h) & = \Ebb_{(\xv,y) \sim \Dcal} [\ell(y, h(\xv))] = \iint \ell(y, h(\xv)) p(\xv, y) \diff \xv \diff y \\
    & = \int \left( \int \ell(y, h(\xv)) p(y|\xv) \diff y \right) p(\xv) \diff \xv \\
    & = \Ebb_{\xv} \left[ \int \ell(y, h(\xv)) p(y|\xv) \diff y \right] = \Ebb_{\xv} [ \Ebb_y [\ell(y, h(\xv)) | \xv]]
\end{align*}
$$

<div class="top-4"></div>

最小泛化风险称为{==贝叶斯风险==}，对应的$h^\star$即{==贝叶斯最优学习器==}

$$
\begin{align*}
    \quad h^\star(\xv) = \mathop{\arg\min}_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 贝叶斯最优学习器

---

<div class="top2"></div>

$$
\begin{align*}
    \quad h^\star(\xv) = \mathop{\arg\min}_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align*}
$$

<div class="top-4"></div>

回归问题通常采用平方损失$\ell(y, h(\xv)) = (y - h(\xv))^2$

$$
\begin{align*}
    \quad \nabla_{h(\xv)} \left( \int (y - h(\xv))^2 p(y|\xv) \diff y \right) & = 2 \int (h(\xv) - y) p(y|\xv) \diff y \\
    & = 2 h(\xv) - 2 \int y p(y|\xv) \diff y \\
    & = 2 h(\xv) - 2 \Ebb[y|\xv]
\end{align*}
$$

<div class="top-4"></div>

即回归问题的贝叶斯最优模型$h^\star(\xv) = \Ebb[y|\xv]$

我的批注 在偏差方差分解中我们曾得到相同的结论

$$
\begin{align*}
    \quad \Ebb_{(\xv,y) \sim \Dcal} [(y - h(\xv))^2] = \Ebb_{\xv} [(h(\xv) - \Ebb [y|\xv])^2] + \text{噪声}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 贝叶斯最优学习器

---

<div class="top2"></div>

$$
\begin{align*}
    \quad h^\star(\xv) = \mathop{\mathrm{argmin}}_{h(\xv)} \int \ell(y, h(\xv)) p(y|\xv) \diff y
\end{align*}
$$

<div class="top-4"></div>

对分类问题，设$\Ycal = [c]$，$\ell(y, h(\xv)) = \Ibb(y \ne h(\xv))$，则

<div class="top1"></div>

$$
\begin{align*}
    \quad h^\star(\xv) & = \mathop{\mathrm{argmin}}_{\yhat \in [c]} \sum_{y \in [c]} \Ibb(y \ne \yhat) p(y|\xv) \\
    & = \mathop{\mathrm{argmin}}_{\yhat \in [c]} ~ (1 - p(\yhat|\xv)) \\
    & = \mathop{\mathrm{argmax}}_{\yhat \in [c]} ~ p(\yhat|\xv)
\end{align*}
$$

<div class="top-2"></div>

即分类问题的贝叶斯最优模型$h^\star(\xv) = \mathop{\mathrm{argmax}}_{\yhat \in [c]} p(\yhat|\xv)$

我的批注 $\Ebb[y|\xv]$和$\mathop{\mathrm{argmax}}_{\yhat \in [c]} p(\yhat|\xv)$均依赖未知的$p$，无法直接得到

<!-- slide data-notes="" -->

##### 判别式 <span style="font-weight:900">_vs._</span> 生成式

---

利用训练集求$\mathop{\mathrm{argmax}}_{y \in [c]} p(y|\xv)$有两种思路

判别式方法：用线性判别式直接拟合$p(y|\xv)$，如对率回归

- 二分类：$p(1|\xv) = \sigma(\wv^\top \xv)$
- 多分类：$[p(1|\xv), \ldots, p(c|\xv)] = \softmax (\wv_1^\top \xv, \ldots, \wv_c^\top \xv)$

<div class="top3"></div>

生成式方法：迂回策略，用贝叶斯公式从数据的生成机制入手

$$
\begin{align*}
    \quad p(y|\xv) & = \frac{\class{yellow}{p(y)} \times \class{blue}{p(\xv|y)}}{p(\xv)}
    \Longrightarrow \begin{cases} p(y = 1 | \xv) \propto \class{yellow}{p(y=1)} \times \class{blue}{p(\xv|y=1)} \\
    \quad \quad \vdots \\
    p(y = c | \xv) \propto \class{yellow}{p(y=c)} \times \class{blue}{p(\xv|y=c)} \end{cases} \\[10pt]
    & \Longrightarrow \mathop{\mathrm{argmax}}_{y \in [c]} p(y|\xv) = \mathop{\mathrm{argmax}}_{y \in [c]} p(y) p(\xv | y)
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 朴素贝叶斯

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \mathop{\mathrm{argmax}}_{y \in [c]} p(y|\xv) = \mathop{\mathrm{argmax}}_{y \in [c]} p(y) p(\xv | y)
\end{align*}
$$

<div class="top-4"></div>

注意$\xv = [x_1; x_2; \ldots; x_d]$，于是有分解

$$
\begin{align*}
    \quad p(\xv | y) = p(x_1 | y) p(x_2 | x_1, y) \cdots p(x_d | x_{d-1}, \ldots, x_2, x_1, y)
\end{align*}
$$

<div class="top-3"></div>

上式很难算，要考虑所有特征的所有取值，指数爆炸！

<div class="top4"></div>

朴素贝叶斯 (<u>n</u>aïve <u>B</u>ayes, NB) 引入{==条件独立性假设==}：

$$
\begin{align*}
    \quad p(\xv | y) = p(x_1 | y) p(x_2 | y) \cdots p(x_d | y) = \prod_{j \in [d]} p(x_j | y)
\end{align*}
$$

<div class="top-2"></div>

问题：如何用训练集估计$p(y), ~ p(x_1 | y), ~ p(x_2 | y), ~ \ldots, ~ p(x_d | y)$？

<!-- slide data-notes="" -->

##### 从数据中估计参数

---

<div class="top2"></div>

$$
\begin{align*}
    \quad p(y | \xv) = p(y) p(x_1 | y) p(x_2 | y) \cdots p(x_d | y)
\end{align*}
$$

对于$p(y)$，记参数$\alpha_k = p(y = k)$，于是

$$
\begin{align*}
    \quad p(y | \alphav) = \prod_{k \in [c]} p(y = k)^{\Ibb(y=k)} = \prod_{k \in [c]} \alpha_k^{\Ibb(y=k)}, \quad \sum_{k \in [c]} \alpha_k = 1
\end{align*}
$$

对于$p(\xv | y)$，设第$j$个特征共有$n_j$种不同取值$v_1^{(j)}, \ldots, v_{n_j}^{(j)}$

<div class="top-2"></div>

记参数$\theta_{kjl} = p( x_j = v_l^{(j)} | y=k)$，于是对$\forall k \in [c]$和$\forall j \in [d]$有

$$
\begin{align*}
    \quad & p(x_j | y = k, \thetav) = \prod_{l \in [n_j]} \theta_{kjl}^{\Ibb(x_j = v_l^{(j)})}, \quad \sum_{l \in [n_j]} \theta_{kjl} = 1
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 从数据中估计参数

---

设数据集$D = \{ (\xv^{(i)}, y^{(i)}) \}_{i \in [m]}$，对数似然函数：

$$
\begin{align*}
    \quad \mathrm{LL} & = \ln p(D | \alphav, \thetav) = \sum_{i \in [m]} \ln p(\xv^{(i)}, y^{(i)} | \alphav, \thetav) \\
    & = \sum_{i \in [m]} \ln \prod_{k \in [c]} p(\xv^{(i)}, y^{(i)} = k | \alphav, \thetav)^{\Ibb(y^{(i)}=k)} \\
    & = \sum_{i \in [m]} \sum_{k \in [c]} \Ibb(y^{(i)}=k) \ln p(\xv^{(i)}, y^{(i)} = k | \alphav, \thetav) \\
    & = \sum_{i \in [m]} \sum_{k \in [c]} \Ibb(y^{(i)}=k) \ln p(y^{(i)} = k | \alphav) \\ & \qquad \qquad \qquad + \sum_{i \in [m]} \sum_{k \in [c]} \Ibb(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav) \\[4pt]
    & = \sum_{k \in [c]} \sum_{i \in [m]} \underbrace{\Ibb(y^{(i)}=k) \ln \alpha_k}_{\alphav~\text{相关的项}\qquad} + \sum_{k \in [c]} \sum_{i \in [m]} \underbrace{\Ibb(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav)}_{\thetav~\text{相关的项}\qquad}
\end{align*}
$$

<!-- slide data-notes="" -->

##### 极大似然估计

---

记$A_k = \sum_{i \in [m]} \Ibb(y^{(i)} = k)$为训练集中第$k$类样本数

$\alphav$相关的项

$$
\begin{align*}
    \quad \max_{\alpha_k} ~ \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \alpha_k = \sum_{k \in [c]} A_k \ln \alpha_k, \quad \st ~ \sum_{k \in [c]} \alpha_k = 1
\end{align*}
$$

<div class="top-2"></div>

拉格朗日函数$L = \sum_{k \in [c]} A_k \ln \alpha_k - \lambda ( \sum_{k \in [c]} \alpha_k - 1 )$

$$
\begin{align*}
    \quad \nabla_{\alpha_k} L  = \frac{A_k}{\alpha_k} - \lambda = 0 & \Longrightarrow \sum_{k \in [c]} A_k = \lambda \sum_{k \in [c]} \alpha_k = \lambda \\
    & \Longrightarrow \alpha_k = \frac{A_k}{\sum_{j \in [c]} A_j} = \frac{\text{第}k\text{类样本数}~~~}{\text{总样本数}}
\end{align*}
$$

<div class="top-2"></div>

我的批注 根据交叉熵的结论也可得到该结果

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计

---

$\thetav$相关的项

$$
\begin{align*}
    \quad \mathrm{LL}(\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln p(\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \sum_{j \in [d]} \Ibb(y^{(i)}=k) \ln p(x_j^{(i)} | y^{(i)} = k, \thetav) \quad \longleftarrow \text{特征独立性} \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \sum_{j \in [d]} \Ibb(y^{(i)}=k) \ln \prod_{l \in [n_j]} p( x_j^{(i)} = v_l^{(j)} | y^{(i)}=k)^{\Ibb(x_j^{(i)} = v_l^{(j)})} \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{l \in [n_j]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \Ibb(x_j^{(i)} = v_l^{(j)}) \ln \theta_{kjl} \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl}
\end{align*}
$$

<div class="top-4"></div>

其中$B_{kjl} = \sum_{i \in [m]} \Ibb(y^{(i)}=k) \Ibb(x_j^{(i)} = v_l^{(j)})$为训练集中第$k$类样本中第$j$个特征取值$v_l^{(j)}$的样本数

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计

---

对任意给定的类别$k$和特征$j$，我们只需考虑

$$
\begin{align*}
    \quad \max_{\theta_{kjl}} ~ \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl}, \quad \st ~ \sum_{l \in [n_j]} \theta_{kjl} = 1
\end{align*}
$$

拉格朗日函数$L = \sum_{l \in [n_j]} B_{kjl} \ln \theta_{kjl} - \lambda ( \sum_{l \in [n_j]} \theta_{kjl} - 1 )$

$$
\begin{align*}
    \quad & \nabla_{\theta_{kjl}} L = \frac{B_{kjl}}{\theta_{kjl}} - \lambda = 0 \Longrightarrow \sum_{l \in [n_j]} B_{kjl} = \lambda \sum_{l \in [n_j]} \theta_{kjl} = \lambda \\[4pt]
    & \Longrightarrow \theta_{kjl} = \frac{B_{kjl}}{\sum_{l \in [n_j]} B_{kjl}} = \frac{\text{第}k\text{类样本中第}j\text{个特征取值}v_l^{(j)}\text{的样本数}\qquad}{\text{第}k\text{类样本数}~~~}
\end{align*}
$$

<!-- slide data-notes="" -->

##### 朴素贝叶斯算法

---

根据贝叶斯公式和条件独立性假设

$$
\begin{align*}
    \quad \mathop{\mathrm{argmax}}_{y \in [c]} p(y|\xv) & = \mathop{\mathrm{argmax}}_{y \in [c]} p(y) p(\xv | y) \\
    & = \mathop{\mathrm{argmax}}_{y \in [c]} p(y) p(x_1 | y) p(x_2 | y) \cdots p(x_d | y)
\end{align*}
$$

根据训练集求

$$
\begin{align*}
    & \quad p(y = k) = \frac{\text{第}k\text{类样本数}~~~}{\text{总样本数}~~~} \\
    & \quad p( x_j = v_l^{(j)} | y=k) = \frac{\text{第}k\text{类样本中第}j\text{个特征取值}v_l^{(j)}\text{的样本数}\qquad}{\text{第}k\text{类样本数}~~~~}
\end{align*}
$$

我的批注 朴素贝叶斯就是数数！

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
|  18  | 周六 | 逛街 | 阴天 | 适中 | 清零 | 无聊 |  ？  |

</div>

<div class="top-60per left56per fs16">

$p(\text{约会}=\text{是})=8/17$
$p(\text{时间}=\text{周六}|\text{约会}=\text{是})=3/8$
$p(\text{方式}=\text{逛街}|\text{约会}=\text{是})=3/8$
$p(\text{天气}=\text{阴天}|\text{约会}=\text{是})=2/8$
$p(\text{课业}=\text{适中}|\text{约会}=\text{是})=1/8$
$p(\text{疫情}=\text{清零}|\text{约会}=\text{是})=5/8$
$p(\text{电视}=\text{无聊}|\text{约会}=\text{是})=2/8$

$p(\text{约会}=\text{否})=9/17$
$p(\text{时间}=\text{周六}|\text{约会}=\text{否})=3/9$
$p(\text{方式}=\text{逛街}|\text{约会}=\text{否})=4/9$
$p(\text{天气}=\text{阴天}|\text{约会}=\text{否})=3/9$
$p(\text{课业}=\text{适中}|\text{约会}=\text{否})=4/9$
$p(\text{疫情}=\text{清零}|\text{约会}=\text{否})=2/9$
$p(\text{电视}=\text{无聊}|\text{约会}=\text{否})=3/9$

<div class="top4"></div>

$\Large \frac{8}{17} \frac{3}{8} \frac{3}{8} \frac{2}{8} \frac{1}{8} \frac{5}{8}  \frac{2}{8} < \frac{9}{17} \frac{3}{9} \frac{4}{9} \frac{3}{9} \frac{4}{9} \frac{2}{9} \frac{3}{9}$

预测结果为“约会=否”

</div>

<!-- slide data-notes="" -->

##### 数值型特征 

---

以文本分类为例

- 词汇表$\Vcal = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\Nbb$、$\Rbb$

<div class="top2"></div>

$x_j = \Ibb(v_j\text{出现在文本}\xv\text{中}) \in \{0,1\}$，$\theta_{kj} = p (x_j = 1 | y = k)$

<div class="top1"></div>

$$
\begin{align*}
    \quad p (\xv | y = k, \thetav) = \prod_{j \in [d]} p (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
\end{align*}
$$

<div class="top-4"></div>

这是$d$个独立的伯努利分布的乘积

<!-- slide vertical=true data-notes="" -->

##### 数值型特征 

---

以文本分类为例

- 词汇表$\Vcal = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\Nbb$、$\Rbb$

<div class="top2"></div>

$x_j = \text{词}v_j\text{在文本}\xv\text{中出现的次数} \in \Nbb$，文本总词数$x_1 + \cdots + x_d$

第$k$类文本的每个词从词汇表中依概率$[\theta_{k1}; \ldots; \theta_{kj}; \ldots; \theta_{kd}]$选取

<div class="top-2"></div>

$\theta_{kj}$为第$k$类文本选取词$v_j$的概率，$\sum_{j \in [d]} \theta_{kj} = 1$

<div class="top1"></div>

$$
\begin{align*}
    \quad p (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align*}
$$

<div class="top-4"></div>

这是{==多项式分布==}，特别的，$d=2$即为二项式分布

<!-- slide vertical=true data-notes="" -->

##### 数值型特征 

---

以文本分类为例

- 词汇表$\Vcal = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\Nbb$、$\Rbb$

<div class="top2"></div>

$x_j \sim \Ncal(\mu_j, \sigma_j^2) \in \Rbb$，假设实数特征 (e.g., tf - idf) 服从高斯分布

$$
\begin{align*}
    \quad p (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align*}
$$

<div class="top-2"></div>

这是$d$个独立的高斯分布的乘积

<!-- slide data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">1</span>

---

$x_j = \Ibb(v_j\text{出现在文本}\xv\text{中}) \in \{0,1\}$，$\theta_{kj} = p (x_j = 1 | y = k)$

<div class="top1"></div>

$$
\begin{align*}
    \quad p (\xv | y = k, \thetav) = \prod_{j \in [d]} p (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
\end{align*}
$$

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \prod_{j \in [d]} \theta_{kj}^{x_j^{(i)}} (1 - \theta_{kj})^{1 - x_j^{(i)}}        \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) (x_j^{(i)} \ln \theta_{kj} + (1 - x_j^{(i)}) \ln (1 - \theta_{kj}) ) \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) )
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">1</span>

---

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) (x_j^{(i)} \ln \theta_{kj} + (1 - x_j^{(i)}) \ln (1 - \theta_{kj}) ) \\
    & = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) )
\end{align*}
$$

<div class="top-4"></div>

其中

$$
\begin{align*}
    \quad B_{kj} & = \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} = \text{第}k\text{类文本中包含词}v_j\text{的文本数} \\
    \Bbar_{kj} & = \sum_{i \in [m]} \Ibb(y^{(i)}=k) (1 - x_j^{(i)}) = \text{第}k\text{类文本中不包含词}v_j\text{的文本数}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">1</span>

---

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) ) \\
    B_{kj} & = \text{第}k\text{类文本中包含词}v_j\text{的文本数} \\
    \Bbar_{kj} & = \text{第}k\text{类文本中不包含词}v_j\text{的文本数}
\end{align*}
$$

对某个固定的$k$和$j$，估计$\theta_{kj}$只需求解优化问题

$$
\begin{align*}
    \quad \max_{\theta_{kj}} ~ \{ B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) \}
\end{align*}
$$

<div class="top-4"></div>

令关于$\theta_{kj}$的导数为零可得

$$
\begin{align*}
    \quad \theta_{kj} = \frac{B_{kj}}{B_{kj} + \Bbar_{kj}} = \frac{\text{第}k\text{类文本中包含词}v_j\text{的文本数}\quad ~~~}{\text{第}k\text{类文本数}}
\end{align*}
$$

<!-- slide data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">2</span>

---

$x_j = \text{词}v_j\text{在文本}\xv\text{中出现的次数} \in \Nbb$

<div class="top-2"></div>

$\theta_{kj}$为第$k$类文本选取词$v_j$的概率，$\sum_{j \in [d]} \theta_{kj} = 1$

<div class="top0"></div>

$$
\begin{align*}
    \quad p (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align*}
$$

<div class="top-4"></div>

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \thetav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \left\{ \frac{(x_1^{(i)} + \cdots + x_d^{(i)})!}{x_1^{(i)}! \cdots x_d^{(i)}!} \prod_{j \in [d]} \theta_{kj}^{x_j^{(i)}} \right\} \\
    & = \const + \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} \ln \theta_{kj}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">2</span>

---

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} \ln \theta_{kj} = \sum_{k \in [c]} \sum_{j \in [d]} B_{kj} \ln \theta_{kj} \\
    B_{kj} & = \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} = \text{第}k\text{类文本中词}v_j\text{出现总次数}
\end{align*}
$$

对某个固定的$k$，估计$\theta_{kj}$只需求解优化问题

$$
\begin{align*}
    \quad \max_{\theta_{kj}} ~ \sum_{j \in [d]} B_{kj} \ln \theta_{kj}, \quad \st ~ \sum_{j \in [d]} \theta_{kj} = 1
\end{align*}
$$

<div class="top-4"></div>

拉格朗日函数$L = \sum_{j \in [d]} B_{kj} \ln \theta_{kj} - \lambda ( \sum_{j \in [d]} \theta_{kj} - 1 )$

$$
\begin{align*}
    \quad \frac{\partial L}{\partial \theta_{kj}} = \frac{B_{kj}}{\theta_{kj}} - \lambda = 0 \Longrightarrow \theta_{kj} = \frac{\text{第}k\text{类文本中词}v_j\text{出现总次数}\quad~~~}{\text{第}k\text{类文本的总词数}}
\end{align*}
$$

<!-- slide data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">3</span>

---

$x_j \sim \Ncal(\mu_j, \sigma_j^2) \in \Rbb$，假设实数特征 (e.g., tf - idf) 服从高斯分布

$$
\begin{align*}
    \quad p (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align*}
$$

<div class="top-2"></div>

对数似然函数中$\muv, \sigmav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} & (\muv, \sigmav) = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln p (\xv^{(i)} | y^{(i)} = k, \muv, \sigmav) \\
    & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} \right) \\
    & = \const + \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">3</span>

---

对数似然函数中$\muv, \sigmav$相关的项为

$$
\begin{align*}
    \quad \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align*}
$$

<div class="top-3"></div>

对某个固定的$k$和$j$，估计$\mu_{kj}$只需求解优化问题

$$
\begin{align*}
    \quad \min_{\mu_{kj}} ~ \sum_{i \in [m]} \Ibb(y^{(i)}=k) (x_j^{(i)} - \mu_{kj})^2
\end{align*}
$$

<div class="top-5"></div>

令关于$\mu_{kj}$的导数为零

$$
\begin{align*}
    \quad \mu_{kj} & = \frac{\sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)}}{\sum_{i \in [m]} \Ibb(y^{(i)}=k)} = \frac{\text{第}k\text{类文本第}j\text{个特征的和}\quad~}{\text{第}k\text{类文本数}} \\[4pt]
    & = \text{第}k\text{类文本第}j\text{个特征的均值}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">3</span>

---

对数似然函数中$\muv, \sigmav$相关的项为

$$
\begin{align*}
    \quad \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \left( - \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} - \ln \sigma_{kj} \right)
\end{align*}
$$

<div class="top-3"></div>

对某个固定的$k$和$j$，估计$\sigma_{kj}$只需求解优化问题

$$
\begin{align*}
    \quad \min_{\sigma_{kj}} ~ \sum_{i \in [m]} \Ibb(y^{(i)}=k) \left( \frac{(x_j^{(i)} - \mu_{kj})^2}{2 \sigma_{kj}^2} + \ln \sigma_{kj} \right)
\end{align*}
$$

<div class="top-4"></div>

令关于$\sigma_{kj}$的导数为零

$$
\begin{align*}
    \quad \sigma_{kj}^2 & = \frac{\sum_{i \in [m]} \Ibb(y^{(i)}=k) (x_j^{(i)} - \mu_{kj})^2}{\sum_{i \in [m]} \Ibb(y^{(i)}=k)} \\
    & = \text{第}k\text{类文本第}j\text{个特征的方差}
\end{align*}
$$

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
|  18  | 周六 | 逛街 | {==雨天==} | 适中 | 清零 | 无聊 |  ？  |

</div>

<div class="top-60per left56per fs16">

$p(\text{约会}=\text{否})=\class{blue}{0/17}$

<div class="top4"></div>

训练集中无负样本

模型无脑预测“约会=是”

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
|  18  | 周六 | 逛街 | {==雨天==} | 适中 | 清零 | 无聊 |  ？  |

</div>

<div class="top-60per left56per fs16">

$p(\text{约会}=\text{是})=8/17$
$p(\text{时间}=\text{周六}|\text{约会}=\text{是})=3/8$
$p(\text{方式}=\text{逛街}|\text{约会}=\text{是})=3/8$
$p(\text{天气}=\class{blue}{\text{雨天}}|\text{约会}=\text{是})=\class{blue}{0/8}$
$p(\text{课业}=\text{适中}|\text{约会}=\text{是})=1/8$
$p(\text{疫情}=\text{清零}|\text{约会}=\text{是})=5/8$
$p(\text{电视}=\text{无聊}|\text{约会}=\text{是})=2/8$

<div class="top4"></div>

$\Large \frac{8}{17} \frac{3}{8} \frac{3}{8} \class{blue}{\frac{0}{8}} \frac{1}{8} \frac{5}{8}  \frac{2}{8} = \class{blue}{0}$

正样本中无“天气=雨天”的样本

似然乘积为零，其它特征不起作用

</div>

<!-- slide vertical=true data-notes="" -->

##### 拉普拉斯平滑

---

在各取值的频数上赋予一个正数$\lambda$，通常取$\lambda=1$

<div class="top2"></div>

$$
\begin{align*}
    & \quad p (y = k) = \frac{\text{第}k\text{类样本数} + \lambda ~~~~}{\text{总样本数} + c \lambda} \\[6pt]
    & \quad p ( x_j = v_l^{(j)} | y=k) = \frac{\text{第}k\text{类样本中第}j\text{个特征取值}v_l^{(j)}\text{的样本数} + \lambda \qquad ~}{\text{第}k\text{类样本数} + n_j \lambda} \\[6pt]
    & \quad p (x_j = 1 | y = k) = \frac{\text{第}k\text{类文本中包含词}v_j\text{的文本数} + \lambda \quad ~~~}{\text{第}k\text{类文本数} + d \lambda} \\[6pt]
    & \quad p (\text{选取词}v_j | y = k) = \frac{\text{第}k\text{类文本中词}v_j\text{出现总次数} + \lambda \quad~~~}{\text{第}k\text{类文本的总词数} + d \lambda}
\end{align*}
$$
