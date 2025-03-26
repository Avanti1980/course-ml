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

##### 语言模型

---

对于给定序列$\xv_1, \ldots, \xv_T$，计算联合概率$p(\xv_T, \ldots, \xv_1)$

- $p(\text{make America great again}) > p(\text{great America make again}) ?$，判别给定序列人言否
- 预测下一个词：hello [ world | China | Wuhan | HUST ]？

<div class="bottom4"></div>

前面的词很重要：As the debugger reports no error, the screen prints hello <span class="blue">world</span>

根据条件概率公式

$$
\begin{align*}
    \quad p(\xv_T, \ldots, \xv_1) = p(\xv_T | \xv_{T-1}, \ldots, \xv_1) \cdots p(\xv_3 | \xv_2, \xv_1) ~ p(\xv_2 | \xv_1) ~ p(\xv_1)
\end{align*}
$$

引入马尔可夫假设：当前词出现的概率只依赖于前 n - 1 个词

<!-- slide vertical=true data-notes="" -->

##### n-gram 统计语言模型

---

当前词出现的概率只依赖于前 n - 1 个词

- n = 1：$p(\xv_i | \xv_{i-1}, \ldots, \xv_1) = p(\xv_i)$
- n = 2：$p(\xv_i | \xv_{i-1}, \ldots, \xv_1) = p(\xv_i | \xv_{i-1})$
- n = 3：$p(\xv_i | \xv_{i-1}, \ldots, \xv_1) = p(\xv_i | \xv_{i-1}, \xv_{i-2})$

<div class="bottom2"></div>

优点：

- 采用极大似然估计，参数易训练 (数数)
- 完全包含了前 n - 1 个词的全部信息
- 可解释性强，直观易理解

<div class="bottom2"></div>

缺点：

- 不够灵活，只能固定地看前 n - 1 个词
- 随着 n 的增大，参数空间呈指数增长
- 单纯的基于统计频次，泛化能力差

<!-- slide vertical=true data-notes="" -->

##### 神经语言模型

---

第一层为嵌入 (embedding) 层

- 设词典里共有 N 个词
- N 维独热编码 → d 维词向量
- 可学习参数总个数为 N × d

<div class="threelines width50 lefta right4 top-20per bottom-2 tighttable">

| 编号 |   单词   | 独热编码 |    词向量     |
| :--: | :------: | :------: | :-----------: |
|  1   |    as    | 0…00001  | [1.2, 3.1, …] |
|  2   |   the    | 0…00010  | [0.1, 4.2, …] |
|  3   | debugger | 0…00100  | [1.0, 3.1, …] |

</div>

考虑 4 个词的滑动窗口，词向量维度 d = 5，隐藏层神经元 = 13

@import "../dot/nn4langmodel.dot" {.top-1}

<p class="width28 lefta right6 top-24per bottom-2">
神经网络的结构必须先固定，因此 n 就得先固定，模型灵活性不够
</p>

<!-- slide data-notes="" -->

##### 循环神经网络

---

处理任意长序列，记住之前得到的信息

给定序列$\xv_1, \ldots, \xv_T$，循环神经网络更新为

$$
\begin{align*}
    \quad \av_t = h(\class{yellow}{\Uv \av_{t-1}} + \Wv \xv_t + \bv), ~ \av_0 = \zerov
\end{align*}
$$

<div class="bottom-3"></div>

其中$h$是一个非线性激活函数

我的批注 循环神经网络隐藏层神经元存在自指，时间维度上权值共享

<img src="../tikz/rnn-simple.svg" class="width75 center top2">

<img src="../tikz/rnn.svg" class="width26 lefta right4 top-56per">

<!-- slide vertical=true data-notes="" -->

##### 动力系统观点

---

<div class="top2"></div>

$$
\begin{align*}
    \quad \zv_t & = \class{yellow}{\Uv \av_{t-1}} + \Wv \xv_t + \bv \\
    \av_t & = h(\zv_t)
\end{align*}
$$

<div class="bottom-2"></div>

循环神经网络的更新可以看成一个<span class="blue">动力系统</span>，因此隐藏层的输出$\av_t$在很多文献上也称为<span class="blue">状态</span> (state)

梯度下降就是在用 (前向) 欧拉法离散地求解动力系统

$$
\begin{align*}
    \quad \wv_{t+1} = \wv_t - \eta f'(\wv_t) \Longrightarrow \frac{\wv_{t+1} - \wv_t}{\eta} = - f'(\wv_t) \Longrightarrow \dot{\wv} = - f'(\wv)
\end{align*}
$$

<div class="bottom-2"></div>

Nesterov 加速梯度的动力系统表示：$\ddot{\wv} + (3/t) \dot{\wv} = - f'(\wv)$

<p class="footnote book"> 动力系统 (dynamical system)：使用 (微分) 方程描述空间中所有点随时间变化情况的系统</p>

<!-- slide vertical=true data-notes="" -->

##### 动力系统观点

---

梯度下降的微分方程表示：$\dot{\wv} = - f'(\wv)$

引入函数

$$
\begin{align*}
    \quad \Ecal(t) & = t (f(\wv) - f^\star) + \frac{1}{2} \| \wv - \wv^\star \|_2^2 \\
    \Ecal'(t) & = f(\wv) - f^\star + t \dot{\wv}^\top f'(\wv) + \dot{\wv}^\top (\wv - \wv^\star) \\
    & = - \|f'(\wv)\|_2^2 + f(\wv) - f^\star - f'(\wv)^\top (\wv - \wv^\star) \\
    & = - \|f'(\wv)\|_2^2 + f(\wv) + f'(\wv)^\top (\wv^\star - \wv) - f^\star \leq 0
\end{align*}
$$

根据$\Ecal$单调下降可得梯度下降的收敛率

$$
\begin{align*}
    \quad f(\wv) - f^\star \leq \frac{\Ecal(t)}{t} \leq \frac{\Ecal(0)}{t} = \frac{\| \wv_0 - \wv^\star \|_2^2}{2t} = O \left( \frac{1}{t} \right)
\end{align*}
$$

<!-- slide data-notes="" -->

##### 应用到机器学习

---

序列到类别的模式

输入$\xv_1, \ldots, \xv_T$，输出$\yhat \in [c]$，例如文本分类、情感分析

两种模式：

- 序列的最终表示$\av_T$输入给分类器$g$进行分类：$\hat{y} = g(\av_T)$
- 将整个序列的平均状态$\av$输入给分类器$g$进行分类：$\hat{y} = g(\av)$

<img src="../tikz/seq2class.svg" class="width80 center top4">

<!-- slide vertical=true data-notes="" -->

##### IMDB 情感分析

---

```python {.line-numbers}
from keras.datasets import imdb
from keras.layers import Dense, Embedding, SimpleRNN
from keras.models import Sequential
from keras.preprocessing import sequence

vocabulary = 10000 # 只用词典使用频率前10000的单词
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocabulary)

# 构建字典 key为id value为单词 +3是因为0、1、2是保留的
id_to_word = {id_ + 3: word for word, id_ in imdb.get_word_index().items()}

# 0表示填充令牌"<pad>" 1表示序列开始"<sos>" 2表示未知单词"<unk>"
for id_, token in enumerate(("<pad>", "<sos>", "<unk>")):
    id_to_word[id_] = token

# 显示前5条评论的前10个单词的id表示和原文
for i in range(5):
    print(X_train[i][:10])
    print(" ".join([id_to_word[id_] for id_ in X_train[i][:10]]))
-----------------------------------------------------------------
[1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65]
<sos> this film was just brilliant casting location scenery story
[1, 194, 1153, 194, 8255, 78, 228, 5, 6, 1463]
<sos> big hair big boobs bad music and a giant
[1, 14, 47, 8, 30, 31, 7, 4, 249, 108]
<sos> this has to be one of the worst films
[1, 4, 2, 2, 33, 2804, 4, 2040, 432, 111]
<sos> the <unk> <unk> at storytelling the traditional sort many
[1, 249, 1323, 7, 61, 113, 10, 10, 13, 1637]
<sos> worst mistake of my life br br i picked

# 每条评论截断或补齐为相同长度
X_train = sequence.pad_sequences(X_train, maxlen=500)
X_test = sequence.pad_sequences(X_test, maxlen=500)

model = Sequential()
model.add(Embedding(vocabulary, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics='acc')
model.summary()

Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding (Embedding)        (None, None, 32)          320000
_________________________________________________________________
simple_rnn (SimpleRNN)       (None, 32)                2080
_________________________________________________________________
dense (Dense)                (None, 1)                 33
=================================================================
Total params: 322,113
Trainable params: 322,113
Non-trainable params: 0

model.fit(X_train, y_train, epochs=5, batch_size=128)
model.evaluate(X_test, y_test, verbose=2)
_________________________________________________________________
Epoch 1/5
196/196 [=========] - 33s 163ms/step - loss: 0.5899 - acc: 0.6736
Epoch 2/5
196/196 [=========] - 34s 174ms/step - loss: 0.3708 - acc: 0.8447
Epoch 3/5
196/196 [=========] - 41s 207ms/step - loss: 0.2868 - acc: 0.8848
Epoch 4/5
196/196 [=========] - 40s 205ms/step - loss: 0.1785 - acc: 0.9348
Epoch 5/5
196/196 [=========] - 44s 226ms/step - loss: 0.1232 - acc: 0.9579

782/782 - 32s - loss: 0.4597 - acc: 0.8338
```

<!-- slide vertical=true data-notes="" -->

##### 应用到机器学习

---

同步的序列到序列模式

输入$\xv_1, \ldots, \xv_T$，同步输出$\yhat_1, \ldots, \yhat_T$，例如词性标注、股市预测

$$
\begin{align*}
    \hat{y}_t = g(\av_t), ~ \forall t \in [T]
\end{align*}
$$

<img src="../tikz/seq2seq-syn.svg" class="width70 center top4">

<!-- slide vertical=true data-notes="" -->

##### 应用到机器学习

---

异步的序列到序列模式，也称为<span class="blue">编码器-解码器</span> (encoder-decoder) 模型

输入$\xv_1, \ldots, \xv_T$，输出$\yvhat_1, \ldots, \yvhat_S$，无需同步输出和保持相同长度

例如机器翻译、问答系统、图像描述

$$
\begin{align*}
    \av_t & = h_1 (\av_{t-1}, \xv_t), ~ \forall t \in [T] \\
    \av_{T+t} & = h_2 (\av_{T+t-1}, \yvhat_{t-1}), ~ \forall t \in [S] \\
    \yvhat_t & = g(\av_{T+t}), ~ \forall t \in [S]
\end{align*}
$$

<img src="../tikz/seq2seq-asyn.svg" class="width80 center top-4">

<!-- slide data-notes="" -->

##### 随时间反向传播

---

对$\zv = \Wv \av + \bv$有

$$
\begin{align*}
    \frac{\partial z_j}{\partial \Wv} = \av \ev_j^\top, \quad \frac{\partial \zv}{\partial \bv} = \Iv, \quad \frac{\partial \zv}{\partial \av} = \Wv
\end{align*}
$$

<br>

同理对$\zv_k = \Uv \av_{k-1} + \Wv \xv_k + \bv$有

$$
\begin{align*}
    \frac{\partial [\zv_k]_j}{\partial \Uv} = \av_{k-1} \ev_j^\top, \quad \frac{\partial [\zv_k]_j}{\partial \Wv} = \xv_k \ev_j^\top, \quad \frac{\partial \zv_k}{\partial \bv} = \Iv, \quad \frac{\partial \zv_k}{\partial \av_{k-1}} = \Uv
\end{align*}
$$

<br>

随时间反向传播 (**b**ack**p**ropagation **t**hrough **t**ime, BPTT)：

- 循环神经网络可以看作一个展开的多层前馈网络，“每层”对应“每个时刻”
- 所有层参数共享，因此参数的真实梯度是所有“展开层”的梯度之和

<!-- slide vertical=true data-notes="" -->

##### 随时间反向传播

---

对$\zv_k = \Uv \av_{k-1} + \Wv \xv_k + \bv$有

$$
\begin{align*}
    \frac{\partial [\zv_k]_j}{\partial \Uv} = \av_{k-1} \ev_j^\top, \quad \frac{\partial [\zv_k]_j}{\partial \Wv} = \xv_k \ev_j^\top, \quad \frac{\partial \zv_k}{\partial \bv} = \Iv, \quad \frac{\partial \zv_k}{\partial \av_{k-1}} = \Uv
\end{align*}
$$

记时刻$t$的损失为$\Lcal_t$，则总损失为$\Lcal = \sum_{t \in [T]} \Lcal_t$

记$\deltav_{t,k}^\top = \partial \Lcal_t / \partial \zv_k$为时刻$t$的损失对时刻$k \in [t]$隐藏层输入的导数

注意$\av_k = h(\zv_k)$，由链式法则

$$
\begin{align*}
    \deltav_{t,k}^\top = \frac{\partial \Lcal_t}{\partial \zv_k} = \frac{\partial \Lcal_t}{\partial \zv_{k+1}} \frac{\partial \zv_{k+1}}{\partial \av_k} \frac{\partial \av_k}{\partial \zv_k} = \deltav_{t,k+1}^\top \Uv ~  \diag (h'(\zv_k))
\end{align*}
$$

依然有反向传播的结构

<!-- slide vertical=true data-notes="" -->

##### 随时间反向传播

---

对$\zv_k = \Uv \av_{k-1} + \Wv \xv_k + \bv$有

$$
\begin{align*}
    \frac{\partial [\zv_k]_j}{\partial \Uv} = \av_{k-1} \ev_j^\top, \quad \frac{\partial [\zv_k]_j}{\partial \Wv} = \xv_k \ev_j^\top, \quad \frac{\partial \zv_k}{\partial \bv} = \Iv, \quad \frac{\partial \zv_k}{\partial \av_{k-1}} = \Uv
\end{align*}
$$

记时刻$t$的损失为$\Lcal_t$，则总损失为$\Lcal = \sum_{t \in [T]} \Lcal_t$

记$\deltav_{t,k}^\top = \partial \Lcal_t / \partial \zv_k$为时刻$t$的损失对时刻$k \in [t]$隐藏层输入的导数

$$
\begin{align*}
    \frac{\partial \Lcal}{\partial \Uv} & = \sum_{t \in [T]} \sum_{k \in [t]} \sum_j \frac{\partial \Lcal_t}{\partial [\zv_k]_j} \frac{\partial [\zv_k]_j}{\partial \Uv} = \sum_{t \in [T]} \sum_{k \in [t]} \av_{k-1} \deltav_{t,k}^\top \\
    \frac{\partial \Lcal}{\partial \Wv} & = \sum_{t \in [T]} \sum_{k \in [t]} \sum_j \frac{\partial \Lcal_t}{\partial [\zv_k]_j} \frac{\partial [\zv_k]_j}{\partial \Wv} = \sum_{t \in [T]} \sum_{k \in [t]} \xv_k \deltav_{t,k}^\top \\
    \frac{\partial \Lcal}{\partial \bv} & = \sum_{t \in [T]} \sum_{k \in [t]} \frac{\partial \Lcal_t}{\partial \zv_k} \frac{\partial \zv_k}{\partial \bv} = \deltav_{t,k}^\top
\end{align*}
$$

<!-- slide data-notes="" -->

##### 长程依赖问题

---

设$t > k$，反向传播公式经递推有

$$
\begin{align*}
    \deltav_{t,k}^\top = \deltav_{t,k+1}^\top \Uv ~  \diag (h'(\zv_k))  = \cdots = \deltav_{t,t} ~ \Pi_{\tau=k}^{t-1} \left( \Uv ~ \diag (h'(\zv_\tau)) \right)
\end{align*}
$$

定义$\gamma = \| \Uv ~ \diag (h'(\zv_\tau)) \|$

- 若$\gamma > 1$，当$t - k \rightarrow \infty$时，出现梯度爆炸
- 若$\gamma < 1$，当$t - k \rightarrow \infty$时，出现梯度消失

<br>

长程依赖问题：循环神经网络理论上可以建立长时间间隔状态间的依赖关系，但由于梯度爆炸/消失问题，实际上只能学习短期的依赖关系

- 精心挑选激活函数，尽量使得$\| \Uv ~ \diag (h'(\zv_\tau)) \| \approx 1$，需要足够的炼丹经验
- 梯度爆炸：权重衰减，梯度截断
- 梯度消失：引入残差结构$\av_t = \av_{t-1} + f(\xv_t, \av_{t-1})$，但随着时间$t$增长，$\av_t$会变得越来越大，从而导致隐状态变得饱和，但其存储信息的能力是有限的

<!-- slide vertical=true data-notes="" -->

##### 门控机制

---

有选择地加入新信息，同时有选择地遗忘之前累积的信息

- 长短期记忆 (**l**ong **s**hort-**t**erm **m**emory, LSTM) 网络
- 门控循环单元 (**g**ated **r**ecurrent **u**nit, GRU) 网络

<!-- slide data-notes="" -->

##### LSTM 网络

---

引入一个新的内部状态$\cv_t$专门进行线性的循环信息传递，同时输出信息给隐藏层的外部状态$\av_t$

$$
\begin{align*}
    \cv_t & = \fv_t \odot \cv_{t-1} + \iv_t \odot \widetilde{\cv}_t \\
    \av_t & = \ov_t \odot \tanh(\cv_t)
\end{align*}
$$

其中$\odot$为向量元素乘积

- $\widetilde{\cv}_t = \tanh(\Wv_c \xv_t + \Uv_c \av_{t−1} + \bv_c)$是通过非线性函数得到的候选状态
- <span class="blue">遗忘门</span>$\fv_t = \sigma(\Wv_f \xv_t + \Uv_f \av_{t−1} + \bv_f) \in (0,1)$控制上一个时刻的内部状态$\cv_{t-1}$需要遗忘多少信息
- <span class="blue">输入门</span>$\iv_t = \sigma(\Wv_i \xv_t + \Uv_i \av_{t−1} + \bv_i) \in (0,1)$控制当前时刻的候选状态$\widetilde{\cv}_t$需要保存多少信息
- <span class="blue">输出门</span>$\ov_t = \sigma(\Wv_o \xv_t + \Uv_o \av_{t−1} + \bv_o) \in (0,1)$控制当前时刻的内部状态$\cv_t$需要输出多少信息给外部状态$\av_t$

<!-- slide vertical=true data-notes="" -->

##### LSTM 网络

---

<img src="../tikz/lstm.svg" class="width80 center top5">

<!-- slide vertical=true data-notes="" -->

##### LSTM 网络

---

LSTM 网络的紧凑形式

$$
\begin{align*}
    \begin{bmatrix}
        \widetilde{\cv}_t \\ \ov_t \\ \iv_t \\ \fv_t
    \end{bmatrix} & = \begin{bmatrix}
        \tanh \\ \sigma \\ \sigma \\ \sigma
    \end{bmatrix} \left( \Wv \begin{bmatrix}
        \xv_t \\ \av_{t-1}
    \end{bmatrix} + \bv \right) \\
    \cv_t & = \fv_t \odot \cv_{t-1} + \iv_t \odot \widetilde{\cv}_t \\
    \av_t & = \ov_t \odot \tanh(\cv_t)
\end{align*}
$$

循环神经网络中的隐状态$\av$存储了历史信息，可以看作是一种记忆

简单循环网络的隐状态每个时刻都会被重写，只是一种短期记忆

LSTM 中的记忆单元$\cv$可以在某个时刻捕捉到关键信息将其保存，且生命周期要长于短期记忆$\av$，因此称为长的短期记忆

<!-- slide vertical=true data-notes="" -->

##### LSTM 网络变种

---

无遗忘门的 LSTM 网络：$\cv_t = \fv_t \odot \cv_{t-1} + \iv_t \odot \widetilde{\cv}_t$，记忆饱和

<div class="bottom4"></div>

peephole 连接：三个门不但依赖于输入$\xv_t$和上一时刻的隐状态$\av_{t−1}$，也依赖于上一个时刻的记忆单元$\cv_{t−1}$

$$
\begin{align*}
    \fv_t & = \sigma(\Wv_f \xv_t + \Uv_f \av_{t−1} + \Vv_f \cv_{t−1} + \bv_f) \\
    \iv_t & = \sigma(\Wv_i \xv_t + \Uv_i \av_{t−1} + \Vv_i \cv_{t−1} + \bv_i) \\
    \ov_t & = \sigma(\Wv_o \xv_t + \Uv_o \av_{t−1} + \Vv_o \cv_{t−1} + \bv_o)
\end{align*}
$$

耦合输入门和遗忘门：LSTM 中的输入门和遗忘门有些互补关系，同时用两个门存在冗余

$$
\begin{align*}
    \cv_t = (\onev - \iv_t) \odot \cv_{t-1} + \iv_t \odot \widetilde{\cv}_t
\end{align*}
$$

<!-- slide data-notes="" -->

##### GRU 网络

---

不引入额外的记忆单元，更新方式为

$$
\begin{align*}
    \av_t = \zv_t \odot \av_{t−1} + (\onev − \zv_t) \odot \widetilde{\av}_t
\end{align*}
$$

其中

- $\zv_t = \sigma(\Wv_z \xv_t + \Uv_z \av_{t−1} + \bv_z) \in (0,1)$为更新门
- $\widetilde{\av}_t = \tanh(\Wv_a \xv_t + \Uv_a (\rv_t \odot \av_{t−1}) + \bv_a)$表示当前时刻的候选状态
- $\rv_t = \sigma(\Wv_r \xv_t + \Uv_r \av_{t−1} + \bv_r) \in (0,1)$为重置门，控制候选状态$\widetilde{\av}_t$的计算是否依赖上一时刻的状态$\av_{t−1}$

<div class="bottom2"></div>

几个特例

- $\zv_t = \onev$，当前状态$\av_t$等于上一时刻状态$\av_{t−1}$，和当前输入$\xv_t$无关
- $\zv_t = \zerov$、$\rv = \onev$，GRU 网络退化为简单循环网络
- $\zv_t = \zerov$、$\rv = \zerov$，当前状态$\av_t$只和当前输入$\xv_t$相关，和上一时刻的状态$\av_{t−1}$无关

<!-- slide vertical=true data-notes="" -->

##### GRU 网络

---

<img src="../tikz/gru.svg" class="width80 center top5">

<!-- slide data-notes="" -->

##### 深层循环网络

---

增加同一时刻网络输入到输出之间的路径$\xv_t \rightarrow \hat{y}_t$，从而增强循环神经网络的能力

堆叠循环神经网络：将多个循环网络堆叠起来

<img src="../tikz/srnn.svg" class="width60 center top2">

<!-- slide vertical=true data-notes="" -->

##### 深层循环网络

---

增加同一时刻网络输入到输出之间的路径$\xv_t \rightarrow \hat{y}_t$，从而增强循环神经网络的能力

<br>

双向循环神经网络：由两层循环神经网络组成，信息传递方向不同

<img src="../tikz/birnn.svg" class="width60 center top2">

