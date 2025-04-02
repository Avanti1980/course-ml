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

## 贝叶斯概率

<div class="bottom8"></div>

### 计算机学院 &nbsp;&nbsp; 张腾

#### _tengzhang@hust.edu.cn_

<!-- slide vertical=true data-notes="" -->

##### 大纲

---

@import "../vega/outline.json" {as="vega" .top-2}

<!-- slide data-notes="" -->

##### 概率

---

概率是用来刻画不确定性的工具

频率主义：{==独立重复试验==}中随机事件发生{==频率==}的极限

<div class="top4"></div>

局限：若随机事件非可重复怎么办？

下一轮学科评估，华科计算机得 A+ 的概率有多大？

这个月大 A 股上涨的概率有多大？

今年祖国统一的概率有多大？

<!-- slide vertical=true data-notes="" -->

##### 概率

---

我们有一些观测

- 近两年学院引进了很多高水平的青年教师
- 资深教授大项目接连不断
- 毕业生去向越来越好

<div class="top4"></div>

- 市场情绪低迷，成交量持续萎缩
- 宏观经济数据不好
- 公司年报业绩频繁爆雷

<div class="top4"></div>

- 解放军展示先进装备，频繁秀肌肉
- 美国实力衰退，在亚太地区影响力减弱

<div class="top4"></div>

根据这些观测，我们对上页问题的概率会有自己的判断

<!-- slide data-notes="注意在这个例子中 我们已经在用信念来表示概率了" -->

##### 贝叶斯公式

---

贝叶斯主义：概率是观测者对随机事件发生的主观信念 (belief)

<div class="top2"></div>

$$
\begin{align*}
    \quad \underbrace{p(\Theta|X)}_{\text{后验}} & = \frac{\overbrace{p(X|\Theta)}^{\text{似然}} \overbrace{p(\Theta)}^{\text{先验}}}{\underbrace{p(X)}_{\text{证据}}} = \frac{p(X|\Theta) p(\Theta) }{\int p(X|\Theta) p(\Theta) \diff \Theta}
\end{align*}
$$

- {==先验==} (prior) ：对随机事件$\Theta$发生 (评上 A+) 的初始信念
- {==似然==} (likelihood) ：观测$X$对信念的支持，上轮评上 A+ 的学校有多少大力引才、项目不断
- {==证据==} (evidence) ：观测$X$，它是贝叶斯主义者做推断的基础
- {==后验==} (posterior) ：得到观测$X$后，观测者对初始信念的修正

<!-- slide vertical=true data-notes="" -->

##### 应用到机器学习

---

$\Theta$为参数或模型，$X$为训练数据

<div class="top2"></div>

$$
\begin{align*}
    \quad \underbrace{p(\Theta|X)}_{\text{后验}} & = \frac{\overbrace{p(X|\Theta)}^{\text{似然}} \overbrace{p(\Theta)}^{\text{先验}}}{\underbrace{p(X)}_{\text{证据}}} = \frac{p(X|\Theta) p(\Theta) }{\int p(X|\Theta) p(\Theta) \diff \Theta}
\end{align*}
$$

根据是否利用先验，有两种估计$\Theta$的方式：

- 极大似然 (<u>m</u>aximum <u>l</u>ikelihood, ML)，$\Theta^{\text{ML}} = \argmax_\Theta ~ p(X|\Theta)$
- 最大后验 (<u>m</u>aximum <u>a</u> <u>p</u>osterior, MAP)，$\Theta^{\text{MAP}} = \argmax_\Theta ~ p(\Theta|X)$

<div class="top2"></div>

前者为频率主义者的做法，后者为贝叶斯主义者的做法

<!-- slide data-notes="" -->

##### 频率 <span style="font-weight:900">_vs._</span> 贝叶斯

---

以抛硬币为例，记$\theta = p(\text{正面})$，观测$X$：$t$次抛掷中有$k$次正面

频率主义：

- $\theta$是{==固定的==}未知参数，有了观测后，通过{==极大似然==}估计$\theta$
- $\theta$的{==不确定性==}来自观测，不同观测会估计出不同的$\theta$
- 估计的评估：如果有多个观测，在每个观测上做极大似然，看结果的方差，如果只有一个观测，先通过{==自举法==} (bootstrap) 构造多个不同的观测，在分别做极大似然

<div class="top2"></div>

贝叶斯主义：

- $\theta$不是固定的数，而是$[0,1]$上的随机变量 (硬币空间上的分布)
- 观测只有一个，是确定的，$\theta$的{==不确定性==}来自观测者，观测者的信息越完全/不完全，不确定性越小/越大，$\theta$的分布越窄/宽

<!-- slide vertical=true data-notes="" -->

##### 频率主义

---

观测$X$：$t$次抛掷中有$k$次正面，似然是{==二项式分布==}

$$
\begin{align*}
    \quad p(X | \theta) = \binom{t}{k} \theta^k (1 - \theta)^{t-k}
\end{align*}
$$

假设某次观测抛了$10$次全正，根据极大似然有$\theta^{\text{ML}} = 1$

预测：该硬币抛掷$100\%$都是正面

<!-- slide data-notes="" -->

##### 贝叶斯主义

---

观测$X$：$t$次抛掷中有$k$次正面，似然$p(X | \theta) = \binom{t}{k} \theta^k (1 - \theta)^{t-k}$

先验取参数为$(\alpha,\beta)$的{==贝塔分布==}：

$$
\begin{align*}
    \quad p(\theta) & = \BetaDist(\theta|\alpha,\beta) \\
    & = \frac{\theta^{\alpha - 1} (1-\theta)^{\beta - 1}}{\int_0^1 \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \diff \theta} \\
    & = \frac{\theta^{\alpha - 1} (1-\theta)^{\beta - 1}}{\BetaFunc(\alpha,\beta)}
\end{align*}
$$

- $\alpha+\beta-2$次多项式函数
- 在$[0,1]$上单峰值
- $\alpha$、$\beta$控制峰值位置

@import "../python/plot-beta-function.svg" {.top-48 .right4 .lefta .width45 .height45}

<p class="footnote book"> 分母$\BetaFunc(\alpha,\beta) = \int_0^1 \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \diff \theta$是第一类欧拉积分，归一化用</p>

<!-- slide vertical=true data-notes="" -->

##### 共轭先验

---

证据和后验分别为

$$
\begin{align*}
    \quad p(X) & = \int_0^1 p(\theta) p(X|\theta) \diff \theta = \binom{t}{k} \frac{1}{\BetaFunc(\alpha,\beta)} \int_0^1  \theta^{\alpha + k - 1} (1 - \theta)^{\beta + t-k-1} \diff \theta \\
    & = \binom{t}{k} \frac{\BetaFunc(\alpha+k,\beta+t-k)}{\BetaFunc(\alpha,\beta)} \\[4pt]
    p(\theta|X) & = \frac{p(\theta) p(X|\theta)}{p(X)} = \frac{\theta^{\alpha + k - 1} (1-\theta)^{\beta + t - k - 1}}{\BetaFunc(\alpha+k,\beta+t-k)} = \BetaDist(\theta|\alpha+k,\beta+t-k)
\end{align*}
$$

- 似然$p(X | \theta) = \binom{t}{k} \theta^k (1 - \theta)^{t-k}$，先验也{==呈型==}$\theta^\spadesuit (1-\theta)^\heartsuit$，{==选==}贝塔分布
- 若先验的选择使得后验与先验同属一个分布族，仅参数有变化，则该先验称为该似然的{==共轭先验==} (conjugate prior)，贝塔分布是{伯努利分布|二项式分布|几何分布|负二项式分布}的共轭先验
- 先验分布的参数$(\alpha,\beta)$由观测者自己选，可视为观测者的领域知识；也可视为{==伪数据==}：在$X$前还观测过$\alpha+\beta$次抛掷，其中$\alpha$次正面

<!-- slide vertical=true data-notes="" -->

##### 最大后验 预测分布

---

后验

$$
\begin{align*}
    \quad p(\theta|X) = \frac{\theta^{\alpha + k - 1} (1-\theta)^{\beta + t - k - 1}}{\BetaFunc(\alpha+k,\beta+t-k)} = \BetaDist(\theta|\alpha+k,\beta+t-k)
\end{align*}
$$

<div class="top-2"></div>

若目标就是估计$\theta$，采用 MAP 估计：$\theta^{\text{MAP}} = \argmax_\theta ~ p(\theta|X)$

- 由于先验 (伪数据) 的存在，不会出现频率主义中$\theta^{\text{ML}} = 1$的情况

<div class="top2"></div>

若目标是对下次抛硬币的结果$\xhat$做预测，有两种做法：

- 先估计$\theta^{\text{MAP}}$再计算$p(\xhat|\theta^{\text{MAP}})$，这样做忽略了$\theta$的随机性，尤其当后验$p(\theta|X)$是个{==平坦==}的分布时，只取一个点来做决策风险很大
- {==预测分布==} (predictive distribution)：根据$\theta$的后验做加权平均

<div class="top2"></div>

$$
\begin{align*}
    \quad p(\xhat|X) = \int p(\xhat|\theta) p(\theta|X) \diff \theta
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

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

<!-- slide data-notes="" -->

##### 再看朴素贝叶斯

---

朴素贝叶斯通过极大似然估计$p(y), ~ p(x_1 | y), ~ \ldots, ~ p(x_d | y)$

<div class="top-2"></div>

记$\alpha_k = p(y = k)$，于是$\sum_{k \in [c]} \alpha_k = 1$且

$$
\begin{align*}
    \quad p(y | \alpha_k) = \prod_{k \in [c]} p(y = k)^{\Ibb(y=k)} = \prod_{k \in [c]} \alpha_k^{\Ibb(y=k)}
\end{align*}
$$

<div class="top-5"></div>

是{==分类分布==}，伯努利分布的多元扩展，$c=2$即为伯努利分布

<div class="top1"></div>

伯努利分布呈$\theta^\spadesuit (1-\theta)^\heartsuit$的形式，共轭先验是贝塔分布

<div class="top1"></div>

$$
\begin{align*}
    \quad \BetaDist(\theta|\alpha,\beta) = \frac{\theta^{\alpha - 1} (1-\theta)^{\beta - 1}}{\int_0^1 \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \diff \theta} = \frac{\theta^{\alpha - 1} (1-\theta)^{\beta - 1}}{\BetaFunc(\alpha,\beta)}
\end{align*}
$$

分类分布的共轭先验是贝塔分布的多元扩展？

<!-- slide vertical=true data-notes="" -->

##### 狄利克雷分布

---

伽玛函数 (第二类欧拉积分) 和贝塔函数 (第一类欧拉积分)：

$$
\begin{align*}
    \quad \Gamma(m) & = \int_0^\infty \theta^{m - 1} \exp(- \theta) \diff \theta \\
    \BetaFunc(\alpha,\beta) & = \int_0^1 \theta^{\alpha - 1} (1-\theta)^{\beta - 1} \diff \theta = \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha+\beta)}
\end{align*}
$$

<div class="top-2"></div>

由贝塔函数可导出贝塔分布

$$
\begin{align*}
    \quad \BetaDist(\theta|\alpha,\beta) = \frac{\theta^{\alpha - 1} (1-\theta)^{\beta - 1}}{\BetaFunc(\alpha,\beta)} = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} \theta^{\alpha - 1} (1-\theta)^{\beta - 1}
\end{align*}
$$

<div class="top-2"></div>

贝塔分布的多元扩展为狄利克雷分布

$$
\begin{align*}
    \quad \Dir(\alphav | \mv) = \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{m_k - 1}, \quad \sum_{k \in [c]} \alpha_k = 1
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 狄利克雷分布先验

---

@import "../dot/conjugate-prior.dot" {.left10per}

<div class="top1"></div>

记$\alpha_k = p(y = k)$，于是

$$
\begin{align*}
    \quad p(y | \alphav) = \prod_{k \in [c]} p(y = k)^{\Ibb(y=k)} = \prod_{k \in [c]} \alpha_k^{\Ibb(y=k)}, \quad \sum_{k \in [c]} \alpha_k = 1
\end{align*}
$$

<div class="top-2"></div>

设$\alphav$服从参数为$\mv$的狄利克雷分布：

$$
\begin{align*}
    \quad p(\alphav) = \Dir(\alphav | \mv) = \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{m_k - 1}, \quad \sum_{k \in [c]} \alpha_k = 1
\end{align*}
$$

<!-- slide data-notes="" -->

##### 狄利克雷分布后验

---

根据贝叶斯公式，后验

$$
\begin{align*}
    \quad p(\alphav | \yv) & \propto p(\alphav) p(\yv|\alphav) \\
    & = \left( \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{m_k - 1} \right) \left( \prod_{i \in [m]} \prod_{k \in [c]} \alpha_k^{\Ibb(y^{(i)}=k)} \right) \\
    & = \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{m_k - 1} \alpha_k^{\sum_{i \in [m]} \Ibb(y^{(i)}=k)}                                                  \\
    & = \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{A_k + m_k - 1}                                                                                        \\
    & \propto \Dir(\alphav | A_1 + m_1, \ldots, A_c + m_c)
\end{align*}
$$

<div class="top-3"></div>

其中$A_k = \sum_{i \in [m]} \Ibb(y^{(i)} = k)$为第$k$类样本数

这就验证了狄利克雷分布是分类分布的共轭先验

<!-- slide vertical=true data-notes="" -->

##### 最大后验估计

---

记$A_k = \sum_{i \in [m]} \Ibb(y^{(i)} = k)$为第$k$类样本数，后验

$$
\begin{align*}
    \quad p(\alphav | \yv) \propto \frac{\Gamma(m_1 + \cdots + m_c)}{\Gamma(m_1) \cdots \Gamma(m_c)} \prod_{k \in [c]} \alpha_k^{A_k + m_k - 1}
\end{align*}
$$

<div class="top-2"></div>

最大后验估计$\alpha_k$只需求解优化问题

$$
\begin{align*}
    \quad & \max_{\alpha_k} ~ \sum_{k \in [c]} (A_k + m_k - 1) \ln \alpha_k, \quad \st ~ \sum_{k \in [c]} \alpha_k = 1 \\[4pt]
    & \alpha_k^{\text{MAP}} = \frac{A_k + m_k - 1}{\lambda} = \frac{A_k + m_k - 1}{\lambda \sum_{j \in [c]} \alpha_j} = \frac{A_k + m_k - 1}{\sum_{j \in [c]} (A_j + m_j - 1)}
\end{align*}
$$

- 取$\mv = \onev$，则$\alpha_k^{\text{MAP}} = \alpha_k^{\text{ML}}$，此时狄利克雷分布退化为均匀分布，先验不包含观测者的任何偏好，最大后验估计退化为极大似然估计
- 取$\mv = \boldsymbol{2}$得到拉普拉斯平滑，此时的朴素贝叶斯才是真·贝叶斯

<!-- slide vertical=true data-notes="" -->

##### 真·朴素贝叶斯 小结

---

<div class="threelines column1-border-right-solid">

|  类别  |                         似然                         |                      共轭先验                       |                                     后验                                     |
| :----: | :--------------------------------------------------: | :-------------------------------------------------: | :--------------------------------------------------------------------------: |
| 枚举型 | $\left. \mathrm{Cate}(\yv \right\arrowvert \alphav)$ | $\left. \mathrm{Dir}(\alphav \right\arrowvert \mv)$ | $\left. \mathrm{Dir}(\alphav \right\arrowvert m_1 + A_1, \ldots, m_c + A_c)$ |

</div>

<div class="threelines column1-border-right-solid">

|    特征     |                              似然                               |                       共轭先验                       |                                     后验                                     |
| :---------: | :-------------------------------------------------------------: | :--------------------------------------------------: | :--------------------------------------------------------------------------: |
|   枚举型    |      $\left. \mathrm{Cate}(\xv \right\arrowvert \thetav)$       | $\left. \mathrm{Dir}(\thetav \right\arrowvert \mv)$  | $\left. \mathrm{Dir}(\thetav \right\arrowvert m_1 + A_1, \ldots, m_c + A_c)$ |
| $\{ 0,1 \}$ |    $\left. \mathrm{Bern}(x_j \right\arrowvert \theta_{kj})$     | $\left. \BetaDist(\theta_{kj} \right\arrowvert m,n)$ |  $\left. \BetaDist(\theta_{kj} \right\arrowvert m + B_{kj},n+\bar{B}_{kj})$  |
|   $\Nbb$    |      $\left. \mathrm{Mult}(\xv \right\arrowvert \thetav)$       | $\left. \mathrm{Dir}(\thetav \right\arrowvert \mv)$  | $\left. \mathrm{Dir}(\thetav \right\arrowvert m_1 + A_1, \ldots, m_c + A_c)$ |
|   $\Rbb$    | $\left. \Ncal(x_{kj} \right\arrowvert \mu_{kj}, \sigma_{kj}^2)$ |          均值不固定、精度固定时，为高斯分布          |
|      -      |                                -                                |         均值固定、精度不固定时，为威沙特分布         |
|      -      |                                -                                |       均值、精度都不固定时，为高斯-威沙特分布        |

</div>

共轭先验的参数就是拉普拉斯平滑中的系数

<!-- slide data-notes="" -->

##### 再看线性回归

---

特征空间$\Xcal \subseteq \Rbb^d$，标记空间$\Ycal$，$\Xcal \times \Ycal$上的{==未知==}概率分布$\Dcal$

<div class="top-2"></div>

训练数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，其中$(\xv_i, y_i) \overset{\mathrm{iid}}{\sim} \Dcal$

假设数据的生成方式为

- 先在特征空间$\Xcal$中随机选取$\xv_i$
- 计算$y_i = \wv^\top \xv_i + \epsilon_i$，其中$\epsilon_i \sim \Ncal(0,\beta^{-1})$

<div class="top2"></div>

待估计参数是$\wv$和$\beta$，似然为

$$
\begin{align*}
    \quad p (D | \wv, \beta) & = \prod_{i \in [m]} p (\xv_i, y_i | \wv, \beta) = \prod_{i \in [m]} p (\xv_i) p (y_i | \xv_i, \wv, \beta) \\
    & \propto \prod_{i \in [m]} p (y_i | \xv_i, \wv, \beta) = \prod_{i \in [m]} \Ncal(\wv^\top \xv_i,\beta^{-1})
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 线性回归 极大似然

---

对数似然为

$$
\begin{align*}
    \quad \ln p (D | \wv, \beta) & = \const + \sum_{i \in [m]} \ln \Ncal(\wv^\top \xv_i,\beta^{-1}) \\
    & = \const + \frac{\ln \beta}{2} - \frac{\beta}{2} \sum_{i \in [m]}  (y_i - \wv^\top \xv_i)^2
\end{align*}
$$

极大似然估计$\wv$对应的优化问题为

$$
\begin{align*}
    \quad \min_{\wv} ~ \frac{\beta}{2} \sum_{i \in [m]} (y_i - \wv^\top \xv_i)^2 = \frac{\beta}{2} \| \Xv \wv - \yv \|_2^2
\end{align*}
$$

我的启示 在上页的假设下，{==极大似然估计等价于最小二乘回归==}

<!-- slide data-notes="" -->

##### 线性回归 贝叶斯视角

---

取先验分布$p(\wv) = \Ncal(\wv | \muv_0, \Sigmav_0)$

根据贝叶斯公式，后验为

<div class="top1"></div>

$$
\begin{align*}
    \quad p & (\wv | D) \propto p(\wv) p(D | \wv) \\
    & \propto \exp \left( -\frac{1}{2} (\wv - \muv_0)^\top \Sigmav_0^{-1} (\wv - \muv_0) \right) \prod_{i \in [m]} \exp \left( - \frac{\beta}{2} (y_i - \wv^\top \xv_i)^2 \right) \\
    & = \exp \left( -\frac{1}{2} (\wv - \muv_0)^\top \Sigmav_0^{-1} (\wv - \muv_0) - \frac{\beta}{2} \| \Xv \wv - \yv \|_2^2 \right) \\
    & \propto \exp \bigg( -\frac{1}{2} \wv^\top (\underbrace{\Sigmav_0^{-1} + \beta \Xv^\top \Xv}_{\Sigmav_m^{-1}}) \wv + \wv^\top (\underbrace{\Sigmav_0^{-1} \muv_0 + \beta \Xv^\top \yv}_{\Sigmav_m^{-1} \muv_m} )\bigg) \\
    & \propto \exp \left( -\frac{1}{2} (\wv - \muv_m)^\top \Sigmav_m^{-1} (\wv - \muv_m) \right) \propto \Ncal(\wv | \muv_m, \Sigmav_m)
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 岭回归

---

特别的，取$\muv_0 = \zerov$、$\Sigmav_0 = \alpha^{-1} \Iv$，则

$$
\begin{align*}
    \quad p(\wv | D) & \propto \exp \left( -\frac{1}{2} (\wv - \muv_0)^\top \Sigmav_0^{-1} (\wv - \muv_0) - \frac{\beta}{2} \| \Xv \wv - \yv \|_2^2 \right) \\
    & = \exp \left( -\frac{\alpha}{2} \wv^\top \wv - \frac{\beta}{2} \| \Xv \wv - \yv \|_2^2 \right)
\end{align*}
$$

最大后验估计$\wv$只需求解优化问题

<div class="top1"></div>

$$
\begin{align*}
    \quad \min_{\wv} ~ \bigg\{ \underbrace{\frac{\beta}{2} \| \Xv \wv - \yv \|_2^2}_{\text{来自似然}~~} + \underbrace{\frac{\alpha}{2} \|\wv\|_2^2}_{\text{来自先验}~~} \bigg\}
\end{align*}
$$

- 在原本最小二乘的基础上，多了一个关于$\wv$的$\ell_2$范数项
- 平方损失 + $\ell_2$范数 = {==岭回归==} (ridge regression)

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">LASSO</span>

---

取先验分布$p(\wv) = \mathrm{Lap}(\wv | \muv_0, \alpha^{-1}) = \frac{\alpha}{2} \exp (- \alpha \| \wv - \muv_0 \|_1)$

根据贝叶斯公式

$$
\begin{align*}
    \quad p (\wv | D) \propto p(\wv) p(D | \wv) = \exp \left( - \alpha \| \wv - \muv_0 \|_1 - \frac{\beta}{2} \| \Xv \wv - \yv \|_2^2 \right)
\end{align*}
$$

<div class="top-3"></div>

特别的，取$\muv_0 = \zerov$，最大后验估计$\wv$只需求解优化问题

<div class="top1"></div>

$$
\begin{align*}
    \quad \min_{\wv} ~ \bigg\{ \underbrace{\frac{\beta}{2} \| \Xv \wv - \yv \|_2^2}_{\text{来自似然}~~} + \underbrace{\alpha \| \wv \|_1}_{\text{来自先验}~~} \bigg\}
\end{align*}
$$

- 在原本最小二乘的基础上，多了一个关于$\wv$的$\ell_1$范数项
- 平方损失 + $\ell_1$范数 = 最小绝对值收敛和选择算子 (<u>l</u>east <u>a</u>bsolute <u>s</u>hrinkage and <u>s</u>election <u>o</u>perator, {==LASSO==})

<!-- slide vertical=true data-notes="" -->

##### 回归总结

---

<div class="threelines column1-border-right-solid fs13">

|  模型  |               线性回归               |                              岭回归                              |                                                  LASSO                                                  |
| :----: | :----------------------------------: | :--------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------: |
|  数据  |                  >                   |                                >                                 | 先随机选取$\xv_i$，再计算$y_i = \wv^\top \xv_i + \epsilon_i$，其中$\epsilon_i \sim \Ncal(0,\beta^{-1})$ |
|  先验  |                  -                   |                             高斯分布                             |                                              拉普拉斯分布                                               |
|  估计  |               极大似然               |                             最大后验                             |                                                最大后验                                                 |
|  优化  | $\min_{\wv} \| \Xv \wv - \yv \|_2^2$ | $\min_{\wv} \{ \| \Xv \wv - \yv \|_2^2 + \lambda \|\wv\|_2^2 \}$ |                     $\min_{\wv} \{ \| \Xv \wv - \yv \|_2^2 + \lambda \|\wv\|_1 \}$                      |
|  形式  |               平方损失               |                     平方损失 + $\ell_2$范数                      |                                         平方损失 + $\ell_1$范数                                         |
| 解析解 | $\wv = (\Xv^\top \Xv)^{-1} \Xv \yv$  |        $\wv = (\Xv^\top \Xv + \lambda \Iv)^{-1} \Xv \yv$         |                                                    -                                                    |

</div>

<!-- slide data-notes="" -->

##### 再看对率回归

---

设训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，似然为

$$
\begin{align*}
    \quad p(D | \wv) \propto \prod_{i \in [m]} p(y_i | \xv_i, \wv) = \prod_{i \in [m]} \sigma(y_i \wv^\top \xv_i) = \prod_{i \in [m]} \frac{1}{1 + \exp(- y_i \wv^\top \xv_i)}
\end{align*}
$$

取先验分布$p(\wv) = \Ncal(\wv | \zerov, \alpha^{-1} \Iv)$，则

$$
\begin{align*}
    \quad p(\wv | D) & \propto \exp \left( -\frac{\alpha}{2} \wv^\top \wv \right) \prod_{i \in [m]} \frac{1}{1 + \exp(- y_i \wv^\top \xv_i)}
\end{align*}
$$

最大后验估计$\wv$只需求解优化问题

$$
\begin{align*}
    \quad \min_{\wv} \left\{ \sum_{i \in [m]} \ln (1 + \exp(- y_i \wv^\top \xv_i)) + \frac{\alpha}{2} \| \wv \|_2^2 \right\}
\end{align*}
$$
