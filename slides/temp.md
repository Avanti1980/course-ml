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

<!-- slide data-notes="" -->

##### 特征 离散类别 → 数值

---

<div class="threelines column7-border-right-solid head-highlight-1 tr-hover row5-border-top-dashed">

| 次序 | 时间 | 方式 | 天气 | 课业 | 疫情 | 电视 | 约会 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 |  是  |
|  6   | 周六 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  是  |
|  10  | 周六 | 学习 | 雨天 | 轻松 | 严峻 | 无聊 |  否  |
|  13  | 周六 | 逛街 | 晴天 | 正常 | 清零 | 精彩 |  否  |

</div>

- {==序数编码==} (ordinal encoding)：清零 - 0、平缓 - 1、严峻 - 2，需类别特征本身有序，否则若吃饭 - 0、逛街 - 1、学习 - 2，为何 |吃饭 - 学习| > |吃饭 - 逛街| ？
- {==独热编码==} (one-hot encoding)：吃饭 - 001、逛街 - 010、学习 - 100，一碗水端平，所有取值距离相等，但若取值很多码会很长，且不适应动态出现的新取值
- {==哈希编码==} (hash encoding)：用哈希函数将任意输入映射到有限整数范围，码长固定，也能适应动态出现的新取值，但可能存在信息丢失

<!-- slide vertical=true data-notes="" -->

##### 特征独热编码

---

```python {.line-numbers .top0 .left4 highlight=[12,16-19,22-23]}
import numpy as np
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder

X = np.array([
    [ 1, '周六', '吃饭', '晴天', '轻松', '清零', '精彩'],
    [ 6, '周六', '逛街', '晴天', '轻松', '平缓', '无聊'],
    [10, '周六', '学习', '雨天', '轻松', '严峻', '无聊'],
    [13, '周六', '逛街', '晴天', '正常', '清零', '精彩'],])
y = np.array(['是', '是', '否', '否'])

LabelBinarizer().fit_transform(y).squeeze()  # 标记二值化
[1 1 0 0]

enc = OneHotEncoder()
enc.fit_transform(X[:,1:7]).toarray() # 对6个类别特征采用独热编码
[[1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.],
 [1., 0., 0., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0.],
 [1., 0., 1., 0., 0., 1., 0., 1., 1., 0., 0., 1., 0.],
 [1., 0., 0., 1., 1., 0., 1., 0., 0., 0., 1., 0., 1.]]

enc.get_feature_names_out() # 独热编码对应的原始特征
['x0_周六', 'x1_吃饭', 'x1_学习', 'x1_逛街', 'x2_晴天', 'x2_雨天', 'x3_正常',
 'x3_轻松', 'x4_严峻', 'x4_平缓', 'x4_清零', 'x5_无聊', 'x5_精彩']
```

<!-- slide data-notes="有时会因为特殊原因，特征不是完整的，比如医院的病人数据，病人不可能把你的所有检查都来一遍，都是能省则省 <br><br> 本来机器学习的目的是要找到特征到类别标记的映射，对于缺失特征，可以将其先看作要预测的类别标记，先学一个无缺失特征到有缺失特征的映射，利用这个映射先将缺失的特征都补上，然后再学习类别标记 <br><br> 比如图里这个例子，含糖率有缺失，我就先用除含糖率外的特征学习一个到含糖率的映射，这是一个回归问题" -->

##### 特征缺失处理

---

<div class="threelines column9-border-right-solid head-highlight-1 tr-hover row5-border-top-dashed">

| 次序 | 时间 | 方式 | 天气 | 课业 | 疫情 | 电视 | 温度 | 距离 | 约会 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  1   | 周六 | 吃饭 | 晴天 | 轻松 | 清零 | 精彩 | 25.2 | 0.5  |  是  |
|  6   | 周六 | 逛街 | 晴天 | 轻松 | 平缓 | 无聊 |  -   | 2.0  |  是  |
|  10  | 周六 |  -   | 雨天 | 轻松 | 严峻 | 无聊 | 32.6 | 8.2  |  否  |
|  13  | 周六 | 逛街 | 晴天 | 正常 | 清零 | 精彩 | 36.4 | 9.8  |  否  |

</div>

删除：直接删除有特征缺失的样本，简单粗暴，信息损失

补全：

- 用未缺失该特征的样本计算{==平均数==}、{==中位数==}、{==众数==}填充，引入噪声？
- 用没有缺失的特征{==学习并预测==}缺失特征的取值，若两者之间无关？
- 将“缺失”本身作为一种特征取值

<!-- slide vertical=true data-notes="" -->

##### 特征缺失处理

---

```python {.line-numbers .top0 .left4 highlight=[13-16,20-23]}
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer, IterativeImputer

X = np.array([
    [1, '周末', '吃饭', 25, '不精彩'],
    [2, '周末', '逛街', np.nan, '精彩'],
    [3, '周末', '-', 29, '不精彩'],
    [4, '周末', '逛街', 36, '精彩'],])

imp_mean = SimpleImputer(strategy='mean')
imp_mean.fit_transform(X[:, 3:4])  # 用均值填充
[[25.],
 [30.],
 [29.],
 [36.]]

imp_median = SimpleImputer(strategy='median')
imp_median.fit_transform(X[:, 3:4]) # 用中位数填充
[[25.],
 [29.],
 [29.],
 [36.]]
```

<!-- slide vertical=true data-notes="" -->

##### 特征缺失处理

---

```python {.line-numbers .top0 .left4 highlight=[12-15,19-22]}
import numpy as np
from sklearn.impute import SimpleImputer

X = np.array([
    [1, '周末', '吃饭', 25, '不精彩'],
    [2, '周末', '逛街', np.nan, '精彩'],
    [3, '周末', '-', 29, '不精彩'],
    [4, '周末', '逛街', 36, '精彩'],])

imp_frequent = SimpleImputer(missing_values='-', strategy='most_frequent')
imp_frequent.fit_transform(X[:, 2:3].astype('object')) # 用众数填充
[['吃饭'],
 ['逛街'],
 ['逛街'],
 ['逛街']]

imp_iter = IterativeImputer()
imp_iter.fit_transform(X[:, [0,3]]) # 回归器默认采用BayesianRidge
[[ 1.        , 25.        ],
 [ 2.        , 27.86309709],
 [ 3.        , 29.        ],
 [ 4.        , 36.        ]]
```

<!-- slide data-notes="" -->

##### 特征标准化

---

也称归一化，旨在<span class="blue">消除不同特征间的量纲影响</span>

离差标准化：将原始特征线性变换到 [0, 1] 区间

$$
\begin{align*}
    x \leftarrow \frac{x - x_\min}{x_\max - x_\min} \in [0,1]
\end{align*}
$$

最大值标准化：除以该特征的绝对值最大值

$$
\begin{align*}
    x \leftarrow \frac{x}{\max_{i \in [m]} |x_i|} \in [-1,1]
\end{align*}
$$

标准差标准化：经过处理的特征近似符合标准正态分布$\Ncal(0,1)$

$$
\begin{align*}
    x \leftarrow \frac{x - \mu}{\sigma}, \quad x \leftarrow \frac{x - x_{\text{median}}}{\sum_{i \in [m]} |x_i - x_{\text{median}}| / m}
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 离差与最大值标准化

---

```python {.line-numbers .top0 .left4 highlight=[11-14,17-20]}
import numpy as np
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler

X = np.array([
    [1, '周末', '吃饭', 25, '不精彩'],
    [2, '周末', '逛街', 28, '精彩'],
    [3, '周末', '看电影', 29, '不精彩'],
    [4, '周末', '逛街', 36, '精彩'],])

MinMaxScaler().fit_transform(X[:, [0,3]]) # 最大值变成1 同时 最小值变成0
[[0.        , 0.        ],
 [0.33333333, 0.27272727],
 [0.66666667, 0.36363636],
 [1.        , 1.        ]]

MaxAbsScaler().fit_transform(X[:, [0,3]]) # 最大值变成1
[[0.25      , 0.69444444],
 [0.5       , 0.77777778],
 [0.75      , 0.80555556],
 [1.        , 1.        ]]
```

<!-- slide vertical=true data-notes="" -->

##### 标准差标准化

---

```python {.line-numbers .top0 .left4 highlight=[12-15,18,21]}
import numpy as np
from sklearn.preprocessing import scale

X = np.array([
    [1, '周末', '吃饭', 25, '不精彩'],
    [2, '周末', '逛街', 28, '精彩'],
    [3, '周末', '看电影', 29, '不精彩'],
    [4, '周末', '逛街', 36, '精彩'],])

x = scale(X[:, [0,3]])
x
[[-1.34164079, -1.11631261],
 [-0.4472136 , -0.3721042 ],
 [ 0.4472136 , -0.12403473],
 [ 1.34164079,  1.61245155]]

x.mean(axis=0) # 均值为0
[0.    0.]

x.std(axis=0) # 标准差为1
[1.    1.]
```

<!-- slide data-notes="经过特征提取和标准化等预处理，就剩模型学习前的最后一步了，亦有将该步与模型学习融合的做法 <br><br> 分两种，当部分特征冗余甚至有害时，挑选出对目标任务有用的特征子集，去冗余可以降低计算开销，去有害可以提高模型学习成功率，最基本的就是过滤掉低方差特征" -->

##### 特征变换

---

模型学习前的最后一步，亦有将该步与模型学习融合的做法

当部分特征冗余甚至有害时，挑选或生成有用的特征子集

- 去除低方差特征，特别是那些在所有样本上取值均不变的特征
- 先计算 F 检验值、卡方检验值、互信息、线性相关性等统计量，然后据此设立阈值选择特征
- 引入$\ell_1$等稀疏范数作为约束，将选择特征与模型学习合二为一
- 通过 PCA、随机投影等降维技术浓缩现有特征

<div class="top2"></div>

当特征稀缺时，利用现有特征构造新的特征

- 凭经验显式构造：$[x_1; x_2] \xrightarrow{\Rbb^2 \mapsto \Rbb^6} [x_1^2; x_2^2; \sqrt{2} x_1 x_2; \sqrt{2} x_1; \sqrt{2} x_2; 1]$
- 利用核函数$\kappa(\xv, \zv) = \phi(\xv)^\top \phi(\zv)$隐式构造，代表性方法为支持向量机
- 利用非线性函数复合$f_n ( f_{n-1} ( \cdots f_2 (f_1 (\xv))))$，代表性方法为神经网络

<!-- slide vertical=true data-notes="" -->

##### 特征选择 低方差过滤

---

过滤低方差特征，尤其是那些在所有样本上取值均相同的特征

```python {.line-numbers .top-2 .left4 highlight=[10,14-17,20]}
import numpy as np
from sklearn.feature_selection import VarianceThreshold

X = np.array([ # 对约会数据集的5个离散类别特征采用了独热编码
    [1., 0., 0., 0., 1., 1., 0., 0., 0., 1., 0., 1., 0.],
    [0., 1., 0., 0., 1., 0., 0., 1., 1., 0., 0., 0., 1.],
    [0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 0., 1., 0.],
    [0., 0., 0., 1., 1., 0., 0., 1., 0., 0., 1., 0., 1.]])
X.shape
(4, 13)

# 第5列由特征“约会时间”而来 四个样本都取值“周末” 独热编码后都是1 方差为0
XX = VarianceThreshold(threshold=0.01).fit_transform(X)
[[1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.],
 [0., 1., 0., 0., 0., 0., 1., 1., 0., 0., 0., 1.],
 [0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1., 0.],
 [0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 0., 1.]]

XX.shape
(4, 12)
```
