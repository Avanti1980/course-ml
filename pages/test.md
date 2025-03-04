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

##### 模型选择

---

NFL 定理的例子中可以看到，在已见数据上学得好不算什么

给定数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$

$$
\begin{align*}
    \quad h(\xv) = - \prod_{i: y_i = 1} \| \xv - \xv_i \|
\end{align*}
$$

对任意$D$中正样本输出为 0，对任意$D$中负样本输出为负，

因此$\sgn(h(\xv))$在任意数据集上都可以做到 100% 对，然而没用

终极目标：在{==未知数据==}上表现好，即{==泛化==} (generalization) 好

样本空间$\Xcal \subseteq \Rbb^d$，标记空间$\Ycal$，$\Xcal \times \Ycal$上的{==未知==}概率分布$\Dcal$

给定模型$f$，{==训练==}数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，其中$(\xv_i, y_i) \overset{\mathrm{iid}}{\sim} \Dcal$

几点说明：

- 数据集细分为训练集、测试集，训练集 (training set) 用来学习模型
- 测试集 (test set) 用来评估模型，在训练时不可见
- 训练集和测试集中的样本都{==独立同分布==} (iid) 地来自分布$\Dcal$，若无独立同分布假设，无法保证学习效果
- 分布$\Dcal$定义在$\Xcal \times \Ycal$上，即允许同一样本有多种标记，标记有随机性
- 若$\Dcal$只定义在$\Xcal$上，样本标记由某未知函数给出，则为确定性情形

<!-- slide data-notes="" -->

##### 模型选择

---

NFL 定理的例子中可以看到，在已见数据上学得好不算什么

终极目标：在{==未知数据==}上表现好，即{==泛化==} (generalization) 好

样本空间$\Xcal \subseteq \Rbb^d$，标记空间$\Ycal$，$\Xcal \times \Ycal$上的{==未知==}概率分布$\Dcal$

给定模型$f$，{==训练==}数据集$D = \{ (\xv_i, y_i) \}_{i \in [m]}$，其中$(\xv_i, y_i) \overset{\mathrm{iid}}{\sim} \Dcal$

几点说明：

- 数据集细分为训练集、测试集，训练集 (training set) 用来学习模型
- 测试集 (test set) 用来评估模型，在训练时不可见
- 训练集和测试集中的样本都{==独立同分布==} (iid) 地来自分布$\Dcal$，若无独立同分布假设，无法保证学习效果
- 分布$\Dcal$定义在$\Xcal \times \Ycal$上，即允许同一样本有多种标记，标记有随机性
- 若$\Dcal$只定义在$\Xcal$上，样本标记由某未知函数给出，则为确定性情形
