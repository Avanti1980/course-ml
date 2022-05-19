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

##### 核感知机

---

```python {.line-numbers .top-1 .left4 highlight=[2,23]}
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder

X = np.array([
    [1, '周六', '吃饭', '晴天', '轻松', '清零', '精彩'],
    ...
    [17, '周六', '吃饭', '阴天', '适中', '平缓', '精彩'],
])
y = np.array(['是', '是', '是', '是', '是', '是', '是', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否'])
X = OneHotEncoder().fit_transform(X[:, 1:7]).toarray()
y = LabelBinarizer().fit_transform(y).squeeze()

train_index = [0, 1, 2, 5, 6, 9, 13, 14, 15, 16]
test_index = [3, 4, 7, 8, 10, 11, 12]
X_train, X_test = X[train_index, :], X[test_index, :]
y_train, y_test = y[train_index], y[test_index]

clf = Perceptron(eta0=0.5)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
---
0.7142857142857143
```

<!-- slide data-notes="" -->

##### 核感知机

---

若通过核函数$\kappa(\cdot, \cdot)$隐式定义特征映射$\phi$，则得到核感知机

- 感知机算法的更新为$\wv \leftarrow \wv + \eta y_j \phi(\xv_j)$，最终$\wv = \sum_{j \in [m]} \alpha_j y_j \phi(\xv_j)$
- 除了直接维护$\wv$外，也可以维护$m$维向量$\alphav = [\alpha_1; \ldots; \alpha_m]$

输入：训练集$D = \{ (\xv_i, y_i) \}_{i \in [m]} \in (\Rbb^d \times \{ \pm 1 \})^m$，学习率$\eta > 0$<br>输出：向量$\alphav$

1. 初始化$\alphav = \zerov$
2. {==while==} 训练集中存在误分类点 {==do==}
3. &emsp;&emsp;获取样本$(\xv_i, y_i)$
4. &emsp;&emsp;{==if==} $(\xv_i, y_i)$被误分类，即$y_i (\sum_{j \in [m]} \alpha_j y_j \phi(\xv_j))^\top \phi(\xv_i) \le 0$ {==then==}
5. &emsp;&emsp;&emsp;&emsp;$\alpha_i \leftarrow \alpha_i + \eta$

将第 4 行的 if 条件换成$y_i \sum_{j \in [m]} \alpha_j y_j \kappa(\xv_j ,\xv_i) \le 0$即为核感知机<br>学习模型为$f(\zv) = \wv^\top \zv = \sum_{j \in [m]} \alpha_j y_j \kappa(\xv_j, \zv)$

<!-- slide data-notes="" -->

##### 多层感知机

---
