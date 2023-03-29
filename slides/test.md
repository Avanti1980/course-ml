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

##### 数值型特征 

---

以文本分类为例

- 词汇表$\Vcal = \{ v_j \}_{j \in [d]}$，文本$\xv$，$d$维特征$[x_1; x_2; \ldots; x_d]$
- 特征$x_j$对应词$v_j$，取值的三种情形：$\{0,1\}$、$\Nbb$、$\Rbb$

<div class="top2"></div>

$x_j = \Ibb(v_j\text{出现在文本}\xv\text{中}) \in \{0,1\}$，$\theta_{kj} = \Pbb (x_j = 1 | y = k)$

<div class="top1"></div>

$$
\begin{align*}
    \quad \Pbb (\xv | y = k, \thetav) = \prod_{j \in [d]} \Pbb (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
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

$x_j = \text{词}v_j\text{在文本}\xv\text{中出现的次数} \in \Nbb$

<div class="top-2"></div>

$\theta_{kj}$为第$k$类文本选取词$v_j$的概率


$\Fbb = \Nbb$，词袋模型，文本的每个词依次从词汇表中随机选取生成

- $x_j$为词$v_j$在文本$\xv$中出现的次数
- $\theta_{kj}$为第$k$类文本选取词$v_j$的概率

<div class="top1"></div>

$$
\begin{align*}
    \quad [\theta_{k1}; \ldots; \theta_{kj}; \ldots; \theta_{kd}] \in \Delta_d, ~ \Pbb (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align*}
$$

<div class="top-7"></div>

注意这是{==多项式分布==}

<!-- slide vertical=true data-notes="" -->

##### 其它特征种类

---

$\Fbb = \Rbb$，tf - idf 模型，第$k$类样本的第$j$个特征$\sim \Ncal(\mu_{kj}, \sigma_{kj}^2)$

$$
\begin{align*}
    \quad \Pbb (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align*}
$$

<div class="top-2"></div>

注意这是$d$个独立的高斯分布的乘积

剩下只需用极大似然估计$\thetav, \muv, \sigmav$

<!-- slide data-notes="" -->

##### 极大似然估计 情形 <span style="font-weight:900">1</span>

---

$\Fbb = \{0,1\}$，$x_j = \Ibb(v_j\text{出现在文本}\xv\text{中})$，$\theta_{kj} = \Pbb (x_j = 1 | y = k)$

<div class="top1"></div>

$$
\begin{align*}
    \quad \Pbb (\xv | y = k, \thetav) = \prod_{j \in [d]} \Pbb (x_j | y = k, \thetav) = \prod_{j \in [d]} \theta_{kj}^{x_j} (1 - \theta_{kj})^{1 - x_j}
\end{align*}
$$

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \Pbb (\xv^{(i)} | y^{(i)} = k, \thetav) \\
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
    \quad & \mathrm{LL} (\thetav) = \sum_{k \in [c]} \sum_{j \in [d]} (B_{kj} \ln \theta_{kj} + \Bbar_{kj} \ln (1 - \theta_{kj}) ) \\
    & B_{kj} = \text{第}k\text{类文本中包含词}v_j\text{的文本数} \\
    & \Bbar_{kj} = \text{第}k\text{类文本中不包含词}v_j\text{的文本数}
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

$\Fbb = \Nbb$，词袋模型，文本的每个词依次从词汇表中随机选取生成

- $x_j$为词$v_j$在文本$\xv$中出现的次数
- $\theta_{kj}$为第$k$类文本选取词$v_j$的概率

<div class="top1"></div>

$$
\begin{align*}
    \quad [\theta_{k1}; \ldots; \theta_{kj}; \ldots; \theta_{kd}] \in \Delta_d, ~ \Pbb (\xv | y = k, \thetav) = \frac{(x_1 + \cdots + x_d)!}{x_1! \cdots x_d!} \prod_{j \in [d]} \theta_{kj}^{x_j}
\end{align*}
$$

<div class="top-4"></div>

对数似然函数中$\thetav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} (\thetav) & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \Pbb (\xv^{(i)} | y^{(i)} = k, \thetav) \\
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
    \quad & \sum_{k \in [c]} \sum_{j \in [d]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} \ln \theta_{kj} = \sum_{k \in [c]} \sum_{j \in [d]} B_{kj} \ln \theta_{kj} \\
    & B_{kj} = \sum_{i \in [m]} \Ibb(y^{(i)}=k) x_j^{(i)} = \text{第}k\text{类文本中词}v_j\text{出现总次数}
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

$\Fbb = \Rbb$，tf - idf 模型，第$k$类样本的第$j$个特征$\sim \Ncal(\mu_{kj}, \sigma_{kj}^2)$

$$
\begin{align*}
    \quad \Pbb (\xv | y = k, \muv, \sigmav) = \prod_{j \in [d]} \frac{1}{\sqrt{2\pi \sigma_{kj}^2}} \exp \left( - \frac{(x_j - \mu_{kj})^2}{2 \sigma_{kj}^2} \right)
\end{align*}
$$

<div class="top-2"></div>

对数似然函数中$\muv, \sigmav$相关的项为

$$
\begin{align*}
    \quad \mathrm{LL} & (\muv, \sigmav) = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \ln \Pbb (\xv^{(i)} | y^{(i)} = k, \muv, \sigmav) \\
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

<div class="top-5"></div>

令关于$\sigma_{kj}$的导数为零

$$
\begin{align*}
    \quad \sigma_{kj} & = \sqrt{\frac{\sum_{i \in [m]} \Ibb(y^{(i)}=k) (x_j^{(i)} - \mu_{kj})^2}{\sum_{i \in [m]} \Ibb(y^{(i)}=k)}} \\
    & = \text{第}k\text{类文本第}j\text{个特征的标准差}
\end{align*}
$$