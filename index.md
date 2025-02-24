@import "css/theme/solarized.css"
@import "css/index.css"

## 机器学习 课堂二 <span style="font-weight:900">2025</span> 春

---

#### 概况

授课：张腾 _tengzhang@hust.edu.cn_

- 28 学时理论，周二 5 ~ 6 节课、周四 1 ~ 2 节课 (第 2 ~ 8 周)，西十二 N401
- 12 学时实验，周二 9 ~ 12 节课 (第 5 ~ 7 周)

<div class="top-2"></div>

#### 考核

实验：头歌平台，华为 MindSpore 平台；期末：1 次大作业

#### 课件

推荐用火狐在线浏览，Space 翻页，Esc 导航，可能需科学上网，[常见符号表](pages/notation.html)

<div class="threelines outline head-highlight">

|        |             讲义              | 内容                                                |
| :----: | :---------------------------: | :-------------------------------------------------- |
| 第零讲 |     [绪论](pages/00.html)     | 1. 机器学习的常见应用，机器学习算法是一种元算法     |
|   ^    |               ^               | 2. 图灵测试，达特茅斯会议                           |
|   ^    |               ^               | 3. 人工智能三次浪潮：推理期、知识期、学习期         |
| 第一讲 | [基本概念 上](pages/01.html)  | 1. 机器学习的常见任务类型：监督、半监督、无监督     |
|   ^    |               ^               | 2. 机器学习的不同学派：符号、连接、统计、类推       |
|   ^    |               ^               | 3. 模型评估：均方误差，错误率，查准率，查全率，F1   |
|   ^    |               ^               | 4. 模型选择：欠拟合，过拟合，交叉验证               |
|   ^    |               ^               | 5. 偏差方差分解                                     |
| 第二讲 | [基本概念 下](pages/02.html)  | 1. 特征提取：词袋模型，tf-idf 特征                  |
|   ^    |               ^               | 2. 特征处理：独热编码，缺失处理，标准化             |
|   ^    |               ^               | 3. 特征选择：方差分析，卡方检验，互信息，相关性分析 |
|   ^    |               ^               | 4. 特征选择：稀疏范数                               |
|   ^    |               ^               | 5. 特征变换：主成分分析，随机投影，核映射，函数复合 |
| 第三讲 |    [决策树](pages/03.html)    | 1. ID3 决策树，C4.5 决策树，分类回归树 (CART)       |
|   ^    |               ^               | 2. 信息增益，增益率，基尼指数                       |
|   ^    |               ^               | 3. 鸢尾花分类                                       |
|   ^    |               ^               | 4. 决策树剪枝                                       |
| 第四讲 |    [感知机](pages/04.html)    | 1. M-P 神经元模型，激活函数                         |
|   ^    |               ^               | 2. 感知机模型与算法，实现与或非运算                 |
|   ^    |               ^               | 3. 感知机理论分析：Novikoff 定理                    |
|   ^    |               ^               | 4. 感知机的对偶形式，核感知机，实现异或运算         |
| 第五讲 | [对数几率回归](pages/05.html) | 1. 对率回归用线性函数拟合几率的对数，输出后验概率   |
|   ^    |               ^               | 2. 最终形式由极大似然法或最小化交叉熵损失导出       |
|   ^    |               ^               | 3. 将对率函数换成 softmax 变换可得多分类对率回归    |
|   ^    |               ^               | 4. 梯度下降，随机梯度下降，动量法，加速梯度法       |
| 第六讲 |   [神经网络](pages/06.html)   | 1. 激活函数：Sigmoid、ReLU、Swish、Maxout           |
|   ^    |               ^               | 2. 反向传播求解参数，梯度消失，残差网络             |
|   ^    |               ^               | 3. sklearn、tensorflow 实现                         |
|   ^    |               ^               | 4. 卷积神经网络，循环神经网络，图神经网络           |
| 第七讲 |  [朴素贝叶斯](pages/07.html)  | 1. 贝叶斯决策论，贝叶斯风险，贝叶斯最优模型         |
|   ^    |               ^               | 2. 后验概率最大化：判别式方法，生成式方法           |
|   ^    |               ^               | 3. 朴素贝叶斯：条件独立性假设，极大似然估计         |
|   ^    |               ^               | 4. 拉普拉斯平滑                                     |
| 第八讲 |  [贝叶斯概率](pages/08.html)  | 1. 频率主义，极大似然 _vs._ 贝叶斯主义，最大后验    |
|   ^    |               ^               | 2. 共轭先验，二项式 - 贝塔，多项式 - 狄利克雷       |
|   ^    |               ^               | 3. 贝叶斯视角下的朴素贝叶斯、对率回归               |
|   ^    |               ^               | 4. 贝叶斯视角下的线性回归：岭回归、LASSO            |
| 第九讲 |    [k-近邻](pages/09.html)    | 1. k-近邻法，度量空间，度量学习                     |
|   ^    |               ^               | 2. 泛化错误率分析                                   |
|   ^    |               ^               | 3. 多数表决的变种：加权、带拒绝                     |
|   ^    |               ^               | 4. 维度灾难                                         |
| 第十讲 |  [支持向量机](pages/10.html)  | 1. 最大间隔准则：最小间隔最大化                     |
|   ^    |               ^               | 2. 拉格朗日对偶，弱对偶，强对偶，KKT 条件           |
|   ^    |               ^               | 3. 核支持向量机，软间隔支持向量机                   |
|   ^    |               ^               | 4. 正则化，损失函数                                 |

</div>

#### 补充

[矩阵求导](notes/matrix-calculus.pdf)，[拉格朗日对偶](notes/Lagrange-dual.pdf)，[AdaBoost](notes/adaboost.pdf)

#### 资料

[_Foundations of Machine Learning 2ed_](book/Foundations%20of%20Machine%20Learning%202ed%20-%20Mehryar%20Mohri%2C%20Afshin%20Rostamizadeh%2C%20and%20Ameet%20Talwalkar.pdf) <br>Mehryar Mohri, Afshin Rostamizadeh, Ameet Talwalkar

[_Understanding Machine Learning: From Theory to Algorithms_](book/Understanding%20Machine%20Learning%20From%20Theory%20to%20Algorithms%20-%20Shai%20Shalev-Shwartz%2C%20Shai%20Ben-David.pdf) <br>Shai Shalev-Shwartz, Shai Ben-David

[_Pattern Recognition and Machine Learning_](book/Pattern%20Recognition%20and%20Machine%20Learning%20-%20Christopher%20M.%20Bishop.pdf) <br>Christopher M. Bishop

#### 代码

第零讲：[测试环境](python/demo.ipynb)

第一讲：[二分类](python/binary-classif.ipynb)、[多分类](python/multi-classif.ipynb)、[回归](python/regression.py)、[k-均值聚类](python/clustering.ipynb)、[密度估计](python/density-estimation.ipynb)、[模型评估](python/model-evaluation.ipynb)、[过拟合](python/overfitting.ipynb)、[偏差方差分解](python/bias-var-dec.ipynb)

第二讲：[文本特征提取](python/feat-text.ipynb)、[独热编码](python/feat-one-hot.ipynb)、[缺失特征处理](python/feat-missing.ipynb)、[特征标准化](python/feat-scaler.ipynb)、[特征选择](python/feat-selection.ipynb)、[稀疏范数](python/sparse-norm.ipynb)、[主成分分析](python/pca.ipynb)、[随机投影](python/random-projection.ipynb)

第三讲：决策树[分类鸢尾花](python/dt-iris.ipynb)

第四讲：感知机[预测约会](python/perceptron-date.ipynb)、感知机[实现与或非](python/perceptron-logic.ipynb)、核感知机[实现异或](python/perceptron-kernel.ipynb)

第五讲：对率回归[预测约会](python/lr-date.ipynb)、对率回归[分类鸢尾花](python/lr-iris.ipynb)、[梯度下降](python/gd.ipynb)、[动量法](python/momentum.ipynb)

第六讲：多层感知机实现异或：[sklearn 实现](python/mlp-xor.ipynb)、[tensorflow 实现](python/dnn-xor.ipynb)
