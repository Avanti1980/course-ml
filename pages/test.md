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

##### 神经网络的表示能力

---

考虑所有的布尔函数，$\Xcal = \{0,1\}^n$，$\Ycal = \{0,1\}$

- 计算机中任意数都是用整数个 (不妨设为$b$) 个比特来表示
- 任意$f: \Rbb^n \mapsto \Rbb$在计算机中都是$g: \{0,1\}^{nb} \mapsto \{0,1\}^b$

<div class="bottom4"></div>

对任意$n$，存在深度为$2$的神经网络表示出$\{0,1\}^n \mapsto \{0,1\}$的所有布尔函数

对任意目标函数$f: \{0,1\}^n \mapsto \{0,1\}$，设$\uv_1, \ldots, \uv_k$为正样本

- 输入层$n+1$个结点，接收输入样本$\xv$和常数$1$
- 隐藏层$2^n+1$个结点，$g_i (\xv) = \sgn (\xv^\top \uv_i - (n-0.5))$可实现$\Ibb(\xv = \uv_i)$
- 输出层$1$个结点，$\sgn (\sum_{i \in [k]} g_i (\xv) - 0.5)$

<p class="footnote comments"> 可以证明隐藏层需要指数多的神经元是没法改进的</p>

<!-- slide vertical=true data-notes="" -->

##### 神经网络的表示能力

---

考虑$\Rbb^2 \mapsto \{0,1\}$的函数

@import "../tikz/nn-power.svg" {.top2 .bottom4 .width50 .center}

- 左图，5 个半空间围成的凸多面体，两层神经网络，隐藏层每个神经元对应一个半空间，输出层取 5 个半空间的交
- 右图，4 个凸多面体，三层神经网络，前两层同左图，第二个隐藏层每个神经元对应一个凸多面体，输出层取 4 个凸多面体的并
- 交：$\sgn (\sum_{i \in [k]} x_i - (k-0.5))$、并：$\sgn (\sum_{i \in [k]} x_i - 0.5)$

<!-- slide vertical=true data-notes="" -->

##### 神经网络的表示能力

---

神经网络的抽象化表示
- 有向无环图$\Gcal = (\Vcal, \Ecal)$
- 边上的权重函数$w: \Ecal \mapsto \Rbb$
- 每个结点对应一个神经元，每个神经元有一个激活函数$\sigma: \Rbb \mapsto \Rbb$

<div class="bottom4"></div>

若神经网络的
- 激活函数为$\sgn(\cdot)$，则$\text{VC}$维为$\Ocal (|\Ecal| \log |\Ecal|)$
- 激活函数为$\sigma(\cdot)$，则$\text{VC}$维为$\Omega (|\Ecal|^2)$、$\Ocal (|\Vcal|^2 |\Ecal|^2)$

<div class="bottom4"></div>

若神经网络能表示$\{0,1\}^n \mapsto \{0,1\}$的所有布尔函数，则$\text{VC}$维为$2^n$，于是$2^n \le \Ocal (|\Ecal| \log |\Ecal|) \le \Ocal (|\Vcal|^3)$，从而$|\Vcal| \ge \Omega (2^{n/3})$

<!-- slide vertical=true data-notes="" -->

##### 神经网络的表示能力

---

设$\Fcal_n$是图灵机在$T(n)$时间内能实现的布尔函数集合，则存在常数$b$、$c$以及神经元数不超过$c T(n)^2 + b$的神经网络能实现$\Fcal_n$

证明思路：函数 => 门电路 => 阶跃激活函数实现与或非门

<div class="bottom4"></div>

万有逼近能力：设目标函数$f: [-1,1]^n \mapsto [-1,1]$是李普希茨连续函数，固定$\epsilon > 0$，存在以$\sigma(\cdot)$为激活函数的神经网络$h$使得对$\forall \xv \in [-1,1]^n$有$|f(\xv) - h(\xv)| \le \epsilon$

证明思路：将$[-1,1]^n$分解成小正方体，由于$f$李普希茨连续，因此在每个小正方体内变化很小，近似为一个常数，神经网络根据输入的$\xv$确定小正方体，然后输出$f$在那个小正方体中的均值
