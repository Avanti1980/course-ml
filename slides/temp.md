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

##### 剪枝

---

```python {.line-numbers .top-1 .bottom0 .left4 highlight=[4-6,8,11]}
class sklearn.tree.DecisionTreeClassifier(*,
  criterion='gini',
  splitter='best',
  max_depth=None,
  min_samples_split=2,
  min_samples_leaf=1,
  min_weight_fraction_leaf=0.0,
  max_features=None,
  random_state=None,
  max_leaf_nodes=None,
  min_impurity_decrease=0.0,
  class_weight=None,
  ccp_alpha=0.0
)
```

- max_depth：限制树的最大深度
- min_samples_split：结点至少要包含 min_samples_split 个样本
- min_samples_leaf：结点每个分支至少包含 min_samples_leaf 个样本
- max_features：限制分支时考虑的特征个数
- min_impurity_decrease：信息增益小于设定数值的分支不会发生

<!-- slide data-notes="" -->

##### 本章小结

---

决策树的每一个分支都是一条逻辑规则

决策树转化成规则集，经合并、删减，泛化性能可能会变得更好

除信息增益、增益率、基尼指数外，还有许多划分准则，它们

- 对决策树的尺寸有很大影响
- 对泛化性能的影响很有限

<div class="top2"></div>

剪枝的方法和程度对决策树泛化性能的影响很显著

多变量决策树

- 内部结点对属性的线性组合进行测试
- 分界面不再与坐标轴平行，故也称“斜决策树”
