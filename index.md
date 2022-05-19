@import "css/theme/solarized.css"
@import "css/index.css"

## 机器学习 课堂二 2022 春

---

#### 概况

授课：张腾 _tengzhang@hust.edu.cn_

- 28 学时理论，周三 7 ~ 8 节课、周五 1 ~ 2 节课 (第 10 ~ 16 周)
- 12 学时实验，周四 9 ~ 12 节课 (第 12、15 ~ 16 周，在线)

<div class="top-2"></div>

#### 考核

实验：头歌平台编程，期末：1 次大作业

#### 课件

在线浏览，Space 翻页，Esc 导航，可能需{==科学上网==}才能打开

<div class="threelines outline head-highlight">

|        |              讲义              | 内容                                                |
| :----: | :----------------------------: | :-------------------------------------------------- |
| 第一讲 |     [绪论](slides/01.html)     | 1. 机器学习的常见应用，机器学习算法是一种元算法     |
|   ^    |               ^                | 2. 图灵测试，达特茅斯会议                           |
|   ^    |               ^                | 3. 人工智能三次浪潮：推理期、知识期、学习期         |
| 第二讲 | [基本概念 上](slides/02.html)  | 1. 机器学习的常见任务类型：监督、半监督、无监督     |
|   ^    |               ^                | 2. 机器学习的不同学派：符号、连接、统计、类推       |
|   ^    |               ^                | 3. 模型评估：均方误差，错误率，查准率，查全率，F1   |
|   ^    |               ^                | 4. 模型选择：欠拟合，过拟合，交叉验证               |
|   ^    |               ^                | 5. 偏差方差分解                                     |
| 第三讲 | [基本概念 下](slides/03.html)  | 1. 特征提取：词袋模型，tf-idf 特征                  |
|   ^    |               ^                | 2. 特征处理：独热编码，缺失处理，标准化             |
|   ^    |               ^                | 3. 特征选择：方差分析，卡方检验，互信息，相关性分析 |
|   ^    |               ^                | 4. 特征选择：稀疏范数                               |
|   ^    |               ^                | 5. 特征变换：主成分分析，随机投影，核映射，函数复合 |
| 第四讲 |    [决策树](slides/04.html)    | 1. ID3 决策树，C4.5 决策树，分类回归树 (CART)       |
|   ^    |               ^                | 2. 信息增益，增益率，基尼指数                       |
|   ^    |               ^                | 3. 决策树剪枝，分类鸢尾花数据集                     |
| 第五讲 |    [感知机](slides/05.html)    | ---                                                 |
| 第六讲 | [对数几率回归](slides/06.html) | ---                                                 |

</div>

#### 补充

[矩阵求导](slides/supp-matrix-calculus.html)

#### 资料

[_Foundations of Machine Learning 2ed_](book/Foundations%20of%20Machine%20Learning%202ed%20-%20Mehryar%20Mohri%2C%20Afshin%20Rostamizadeh%2C%20and%20Ameet%20Talwalkar.pdf) <br>Mehryar Mohri, Afshin Rostamizadeh, Ameet Talwalkar

[_Understanding Machine Learning: From Theory to Algorithms_](book/Understanding%20Machine%20Learning%20From%20Theory%20to%20Algorithms%20-%20Shai%20Shalev-Shwartz%2C%20Shai%20Ben-David.pdf) <br>Shai Shalev-Shwartz, Shai Ben-David

[_Pattern Recognition and Machine Learning_](book/Pattern%20Recognition%20and%20Machine%20Learning%20-%20Christopher%20M.%20Bishop.pdf) <br>Christopher M. Bishop

#### 代码

第一讲：[测试环境](python/demo.ipynb)

第二讲：[二分类](python/binary-classif.ipynb)、[多分类](python/multi-classif.ipynb)、[回归](python/regression.py)、[k-均值聚类](python/clustering.ipynb)、[密度估计](python/density-estimation.ipynb)、[模型评估](python/model-evaluation.ipynb)、[过拟合](python/overfitting.ipynb)、[偏差方差分解](python/bias-var-dec.ipynb)

第三讲：[文本特征提取](python/feat-text.ipynb)、[独热编码](python/feat-one-hot.ipynb)、[缺失特征处理](python/feat-missing.ipynb)、[特征标准化](python/feat-scaler.ipynb)、[特征选择](python/feat-selection.ipynb)、[稀疏范数](python/sparse-norm.ipynb)、[PCA](python/pca.ipynb)、[随机投影](python/random-projection.ipynb)

第四讲：[鸢尾花分类](python/dt-iris.ipynb)

第五讲：[感知机实现与或非](python/perceptron-logic.ipynb)
