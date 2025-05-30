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
@import "https://cdn.bootcdn.net/ajax/libs/jquery/3.5.0/jquery.js"

<!-- slide data-notes="" -->

<div class="bottom20"></div>

# 机器学习

<hr class="width50 center">

## k-近邻法

<div class="bottom8"></div>

### 计算机学院 &nbsp;&nbsp; 张腾

#### _tengzhang@hust.edu.cn_

<!-- slide vertical=true data-notes="" -->

##### 大纲

---

@import "../vega/outline.json" {as="vega" .top-2}

<!-- slide data-notes="" -->

##### <span style="font-weight:900">k-</span>近邻法

---

基本假设：{==相似的样本属于相同的类别==}

如何刻画相似？{==距离函数==}：$\dist(\cdot, \cdot): \Xcal \times \Xcal \mapsto \Rbb^+$

<div class="top2"></div>

输入：$D = \{ (\xv_i, y_i) \}_{i \in [m]} \subseteq \Xcal \times \Ycal$，近邻数$k$，待预测样本$\xv$

<div class="top-3"></div>

输出：$\xv$的类别$y$

1. {==寻找近邻==}：求解$N_k(\xv) \subseteq D$使得$|N_k(\xv)| = k$，且对$\forall (\xv', y') \in D \setminus N_k(\xv)$，有$\dist(\xv, \xv') \geq \max_{\zv \in N_k(\xv)} \dist (\xv, \zv)$
2. {==多数投票==}：输出$\mode(\{ y'': (\xv'', y'') \in N_k(\xv) \})$，其中$\mode(\cdot)$表示众数

<div class="top4"></div>

我的批注 近邻法没有{==显式==}的学习过程

<!-- slide vertical=true data-notes="" -->

##### 空间划分 <span style="font-weight:900">1-</span>近邻

---

@import "../tikz/knn.svg" {.center .width50 .top5}

<!-- slide vertical data-notes="" -->

##### 超参设置

---

近邻数$k$：取值范围$[m] \wedge \{2 \Zbb + 1\}$

- {==奇数==}可保证取众数时不会出现{==打平==}的情况，zyzzj 常委都是奇数位
- 越小越容易过拟合，越大越容易欠拟合，实践中多通过交叉验证选取

<div class="top2"></div>

距离函数：

- 闵可夫斯基距离$\dist(\xv, \zv) = \| \xv - \zv \|_p$，由$\ell_p$范数诱导出
- 马氏距离$\dist_\Mv (\xv, \zv) = \| \xv - \zv \|_\Mv$，当$\Mv = \diag \{w_1, \ldots, w_d\}$时，即为加权平方距离$\sqrt{\sum_{j \in [d]} w_j (x_j - z_j)^2}$

<div class="top2"></div>

{==度量学习==} (metric learning)：学一个更好的距离函数，以马氏距离为例，记$\Mcal$/$\Ccal$分别为同类/异类样本对构成的集合

$$
\begin{align*}
    \quad \min_\Mv & \sum_{(\xv_i, \xv_j) \in \Mcal} \dist_\Mv(\xv_i, \xv_j), \quad \st \sum_{(\xv_i, \xv_j) \in \Ccal} \dist_\Mv(\xv_i, \xv_j) \ge 1, ~ \Mv \succeq \zerov
\end{align*}
$$

<!-- slide vertical data-notes="" -->

##### 优劣

---

优点

- 简单，全方位的
- 无训练过程，只需存下数据，惰性学习 (lazy learning)
- 样本极少时也能用
- 特征空间维度不高时效果很好
- {==一致性==}：若贝叶斯最优分类器的错误率$R^\star = 0$，k-近邻也能渐进达到

<div class="top4"></div>

缺点

- 预测很慢，要计算待预测样本与训练集中所有样本的距离
- {==维度灾难==}：高维空间中的距离会失效，k-近邻效果很差

<!-- slide data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 分析

---

一些符号：

- 设输入空间$\Xcal \subseteq \Rbb^n$，类别标记集合$\Ycal = \{ 0, 1\}$
- 定义在$\Xcal \times \Ycal$上的联合分布$P(X,Y)$，$\Xcal$上的边际分布为$P_\Xcal$
- 训练集$\Dcal = \{ (\xv_i, y_i) \}_{i \in [m]} \subseteq \Xcal \times \Ycal$，其中每个$(\xv_i, y_i) \overset{\text{iid}}{\sim} P(X,Y)$
- 记$\eta(\xv) = P(y = 1 | \xv)$，$\Dcal$的生成可以看成先从$P_\Xcal$中独立同分布地采样出$\Dcal_\Xcal = \{ \xv_i \}_{i \in [m]}$，然后对每个$\xv_i$，从$\Bern(\eta(\xv_i))$中采样出$y_i$
- 贝叶斯最优学习器$h^\star(\xv) = \argmax_{\yhat \in \Ycal} P(\yhat | \xv)$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 分析

---

设预测样本为$(\xv, y)$，$\Dcal_\Xcal$按与$\xv$的距离升序排列为$\xv_1, \ldots, \xv_m$，于是 1-近邻的泛化错误率为

$$
\begin{align*}
    \quad \er & (h) = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}, y \sim \Bern(\eta(\xv)), y_1 \sim \Bern(\eta(\xv_1))} [\Ibb(y \ne y_1)] \notag                                                                                                                                     \\
           & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [\Pbb_{y \sim \Bern(\eta(\xv)), y_1 \sim \Bern(\eta(\xv_1))} (y \ne y_1)] \notag                                                                                                                                   \\
           & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ \eta(\xv) (1 - \eta(\xv_1)) + (1 - \eta(\xv)) \eta(\xv_1) ]                                                                                                                                               \notag \\
           & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ \eta(\xv) (1 - \eta(\xv) + \eta(\xv) - \eta(\xv_1)) \\
           & \qquad \qquad + (1 - \eta(\xv)) (\eta(\xv) - \eta(\xv) + \eta(\xv_1)) ]       \notag \\
           & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ 2 \eta(\xv) (1 - \eta(\xv)) + (\eta(\xv) - \eta(\xv_1)) (2 \eta(\xv) - 1) ] \notag                                                                                                                               \\
           & = 2 \Ebb_{\xv \sim P_{\Xcal}} [ \eta(\xv) (1 - \eta(\xv))] + \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ (\eta(\xv) - \eta(\xv_1)) (2 \eta(\xv) - 1) ]
\end{align*}
$$

其中第一项为在$\xv$处采样 2 次，类别标记不同的概率

<!-- slide data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 渐进分析

---

随着样本数$m$的增大，$\xv$与 1-近邻的距离单调递减

当$m \rightarrow \infty$时，若$\xv_1 \rightarrow \xv$，则第二项$\rightarrow 0$，只剩第一项

$$
\begin{align}
    \quad \er(h) & \rightarrow 2 \Ebb_{\xv \sim P_{\Xcal}} [ \eta(\xv) (1 - \eta(\xv))] \\
    & = 2 \Ebb_{\xv \sim P_{\Xcal}} [ P(y=1|\xv) P(y=0|\xv) ] \\
    & = 2 \Ebb_{\xv \sim P_{\Xcal}} [ \underbrace{P(y \ne h^\star(\xv)|\xv)}_{h^\star(\xv)\text{的错误率}\qquad} \underbrace{(1 - P(y \ne h^\star(\xv)|\xv))}_{h^\star(\xv)\text{的准确率}\qquad} ] \\
    & = 2 \er(h^\star) - 2 \Ebb_{\xv \sim P_{\Xcal}} [P(y \ne h^\star(\xv)|\xv)^2] \\
    & = 2 \er(h^\star) - 2 \er(h^\star)^2 - 2 \Vbb [P(y \ne h^\star(\xv)|\xv)] \\
    & \le 2 \er(h^\star) (1 - \er(h^\star))
\end{align}
$$

最后只需确定$m \rightarrow \infty$时保证$\xv_1 \rightarrow \xv$的条件

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 渐进分析

---

条件：输入空间是{==可分==}度量空间

{==可分性==} (separability)：具有可数稠密子集

- 若度量空间$\Xcal$的子集$\Mcal$满足对$\forall x \in \Xcal$，$x$的任意邻域与$\Mcal$交集非空，则称$\Mcal$在$\Xcal$中{==稠密==}，$\Qbb$在$\Rbb$中稠密，$\Qbb$可数，因此$\Rbb$可分
- 可分性限制了空间的复杂度，即便空间中的元素可能是不可数的，但每个元素都可以被一个可数集中的元素无限逼近，而可数集更好处理

<div class="top4"></div>

几乎必然 (almost surely, a.s.) 成立也称{==以概率 1 成立==}

- 当随机事件的样本空间{==有限==}时，等价于{==必然成立==}
- 当随机事件的样本空间{==无限==}时，两者不等价

<div class="top2"></div>

在$[0,1]$上随机挑一个数$x$，$x$几乎必然不等于$0.5$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 渐进分析

---

引理：对$\forall \xv \in \Xcal$，设$\{\xvhat_m\}_{m = 1,2, \ldots}$是 1-近邻序列，$\xvhat_m \overset{\text{a.s.}}{\rightarrow} \xv$

证明：记$\xv$的邻域$B_\xv(r)$：以$\xv$为球心、$r$为半径的球

定义空间中的{==好点==}：对$\forall r > 0$有$p(B_\xv(r)) > 0$，于是

$$
\begin{align*}
    \quad \lim_{m \rightarrow \infty} p(\dist(\xvhat_m, \xv) > r) = \lim_{m \rightarrow \infty} (1 - p(B_\xv(r)))^m = 0
\end{align*}
$$

<div class="top-4"></div>

由$r$的任意性知$\lim_{m \rightarrow \infty} p(\dist(\xvhat_m, \xv) = 0) = 1$，从而$\xvhat_m \overset{\text{a.s.}}{\rightarrow} \xv$

已证“好点的 1-近邻序列收敛于自身的概率为 1”，如果“空间中好点的概率也为 1”，则结论成立

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 渐进分析

---

定义空间中的{==坏点==}：存在$r > 0$使得$p(B_\xv(r)) = 0$，设全部的坏点构成集合$N$，只需证$p(N) = 0$

<div class="width60">

根据{==可分性==}，$\Xcal$存在可数稠密子集$\Acal$，且存在点$\av \in B_\xv(r/3) \wedge \Acal$，考虑包含$\xv$的邻域$B_\av (r/2)$，易知其包含于$B_\xv(r)$，故$p(B_\av (r/2)) = 0$

</div>

<div class="width60">

每个坏点会对应一个以$\av$为球心的球，若多个坏点对应同一个$\av$，取并集，即半径最大的球，注意$\Acal$可数，因此最终只需可数个概率为零的球即可覆盖全部坏点，故$p(N) = 0$

</div>

@import "../tikz/knn-proof.svg" {.right4 .lefta .width36 .top-45per}

<!-- slide data-notes="" -->

##### 推广到多分类

---

设$\Ycal = [c]$，1-近邻的正确率 $\overset{\text{a.s.}}{\rightarrow}$ 在$\xv$处采样两次标记相同的概率

$$
\begin{align*}
    \quad p(y \ne h(\xv) | \xv) = 1 - p(y = h^\star(\xv)|\xv)^2 - \sum_{j \neq h^\star(\xv)} p(y = j|\xv)^2
\end{align*}
$$

<div class="top-4"></div>

由柯西不等式

<div class="top-2"></div>

$$
\begin{align*}
    \quad \sum_{j \neq h^\star(\xv)} p(y = j|\xv)^2 \geq \frac{( \sum_{j \neq h^\star(\xv)} p(y = j|\xv) )^2}{c-1}  = \frac{p(y \ne h^\star(\xv)|\xv)^2}{c-1}
\end{align*}
$$

<div class="top-3"></div>

回代求期望有

<div class="top-3"></div>

$$
\begin{align*}
    \quad p(y \ne h(\xv) | \xv) & \le 1 - (1 - p(y \ne h^\star(\xv)|\xv))^2 - \frac{p(y \ne h^\star(\xv)|\xv)^2}{c-1} = 2 p(e^\star|\xv) - \frac{c}{c-1} p(e^\star|\xv)^2 \\
    \Longrightarrow \er(h) & \le 2 \er(h^\star) - \frac{c}{c-1} (\er(h^\star)^2 + \Vbb [p (y \ne h^\star(\xv) | \xv)]) \\
    & \le \er(h^\star) \left( 2 - \frac{c}{c-1} \er(h^\star) \right)
\end{align*}
$$

<!-- slide data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 非渐进分析

---

渐进分析描述的是$m \rightarrow \infty$的情况，实际中只有有限个样本，我们想知道$\er(h)$随着样本数增长以怎样的速度增长

第一项还按前面的方式处理，下面处理第二项

$$
\begin{align*}
    \quad \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ (\eta(\xv) - \eta(\xv_1)) (2 \eta(\xv) - 1) ]
\end{align*}
$$

设$\eta(\cdot)$是$c$-李普希茨连续函数，即$|\eta(\xv) - \eta(\xv_1)| \le c \| \xv - \xv_1 \|_2$，注意$|2 \eta(\xv) - 1| \le 1$，于是

$$
\begin{align*}
    \quad \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ (\eta(\xv) - \eta(\xv_1)) (2 \eta(\xv) - 1) ] \le c ~ \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ \| \xv - \xv_1 \|_2 ]
\end{align*}
$$

问题转化为控制$\xv$与其 1-近邻的距离

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 非渐进分析

---

设$\Xcal = [0,1]^n$，将其均匀切分成$r^n$个小立方体$\Ccal_1, \ldots, \Ccal_{r^n}$，若$\xv$、$\xv_1$落在同一个$\Ccal_i$，则其距离$\le \sqrt{n}/r$，否则其距离$\le \sqrt{n}$

记与$\Dcal_{\Xcal}$无交集的小正方体的并集为$\Acal$、与$\Dcal_{\Xcal}$有交集的小正方体的并集为$\Bcal$

$$
\begin{align*}
    \quad \Acal = \cup_{i: \Ccal_i \cap \Dcal_{\Xcal} = \emptyset} \Ccal_i, \quad \Bcal = \Xcal \setminus \Acal = \cup_{i: \Ccal_i \cap \Dcal_{\Xcal} \ne \emptyset} \Ccal_i
\end{align*}
$$

$\xv \in \Acal$、$\xv \in \Bcal$恰有一个发生，前者代表$\xv$与任何训练样本都不在一个$\Ccal_i$内，后者代表$\xv$与某个训练样本在同一个$\Ccal_i$内，于是

$$
\begin{align*}
    \quad \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m, \xv \sim P_{\Xcal}} [ \| \xv - \xv_1 \|_2 ] \le \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m} \left[ \Pbb (\Acal) \sqrt{n} + \Pbb (\Bcal) \frac{\sqrt{n}}{r} \right]
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 非渐进分析

---

对于$\Pbb (\Acal)$有

$$
\begin{align*}
    \quad \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m} [\Pbb (\Acal)]
     & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m} [\Pbb (\cup_{i: \Ccal_i \cap \Dcal_{\Xcal} = \emptyset} \Ccal_i) ] \\
     & = \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m} \left[ \sum_{i \in [r^n]} \Pbb (\Ccal_i) \Ibb(\Ccal_i \cap \Dcal_{\Xcal} = \emptyset) \right] \\
     & = \sum_{i \in [r^n]} \Pbb (\Ccal_i) \Ebb_{\Dcal_\Xcal \sim P_{\Xcal}^m} \left[ \Ibb(\Ccal_i \cap \Dcal_{\Xcal} = \emptyset) \right] \\
     & = \sum_{i \in [r^n]} \Pbb (\Ccal_i) (1 - \Pbb (\Ccal_i))^m \le \sum_{i \in [r^n]} \Pbb (\Ccal_i) \exp (- \Pbb (\Ccal_i) m) \\
     & \le r^n \max_{i \in [r^n]} \Pbb (\Ccal_i) \exp (- \Pbb (\Ccal_i) m) \le \frac{r^n}{me}
\end{align*}
$$

<div class="top-2"></div>

其中第一个不等号是根据$1 - x \le \exp(-x)$、第三个不等号是根据$a \exp (- ma) \le 1/me$

<!-- slide vertical=true data-notes="" -->

##### <span style="font-weight:900">1-</span>近邻法 非渐进分析

---

对于$\Pbb (\Bcal)$，直接用其平凡上界$\Pbb (\Bcal) \le 1$，全部回代有

$$
\begin{align*}
    \quad \er(h) \le 2 \er(h^\star) (1-\er(h^\star)) + c \sqrt{n} \left( \frac{r^n}{me} + \frac{1}{r} \right)
\end{align*}
$$

<div class="top-2"></div>

取$r = m^{\frac{1}{n+1}}$可得

$$
\begin{align*}
    \quad \er(h) \le 2 \er(h^\star) (1-\er(h^\star)) + 2 c \sqrt{n} m^{\frac{-1}{n+1}}
\end{align*}
$$

令$2 c \sqrt{n} m^{\frac{-1}{n+1}} \le \epsilon$可知$m \ge (\frac{2 c \sqrt{n}}{\epsilon})^{n+1}$，即要想控制$\xv$与 1-近邻的距离，所需样本数关于维度呈指数增长，这称为{==维度灾难==} (curse of dimensionality)

<!-- slide data-notes="" -->

##### <span style="font-weight:900">k-</span>近邻法 非渐进分析

---

对于$k > 1$的情形，可仿照前面的思路证明

$$
\begin{align*}
    \quad \er(h) \le \left( 1 + \sqrt{\frac{8}{k}} \right) \er(h^\star) + \left( 2k + \left( 2 + \sqrt{\frac{8}{k}} \right) c \sqrt{n} \right) m^{-\frac{1}{n+1}}
\end{align*}
$$

增大$k$可以改善$\er(h^\star)$的系数，但会增加第二项，因此$k$并不是越大越好

<!-- slide data-notes="" -->

##### 维度灾难 近邻不近

---

设$\Xcal = [0,1]^d$为$d$维单位立方体，训练样本在立方体内均匀分布

对任意待测试样本$\xv$，设包含其$k$-近邻的最小立方体的边长为$l$

$l^d \approx k / m$，则$l \approx \sqrt[d]{k/m}$，取$m=1000$、$k=10$

<div class="threelines column1-border1-right-solid-head row1-column1-border1-right-solid head-highlight-1 tr-hover row8-border-top-dashed">

| $d$ |  $2$  |   $3$   |  $10$   |  $100$  |  $1000$  |  $10000$  |
| :-: | :---: | :-----: | :-----: | :-----: | :------: | :-------: |
| $l$ | $0.1$ | $0.215$ | $0.631$ | $0.955$ | $0.9954$ | $0.99954$ |

</div>

当$d=1000$时，$10$-近邻近乎覆盖整个$\Xcal$，已经不是$\xv$的邻域了

<!-- slide vertical=true data-notes="" -->

##### 维度灾难 距离失效

---

在各维度下随机生成$1000$对样本，当维度很高时，任意一对样本的距离会集中在很小的范围内，没有比较的意义

@import "../python/dimension-curse.svg" {.center .width78 .top2}
