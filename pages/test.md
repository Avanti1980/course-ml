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
@import "../plugin/notes/notes.js"
@import "../plugin/customcontrols/plugin.js"
@import "../plugin/customcontrols/style.css"
@import "../plugin/chalkboard/plugin.js"
@import "../plugin/chalkboard/style.css"
@import "../plugin/reveal.js-menu/menu.js"
@import "../js/anychart/anychart-core.min.js"
@import "../js/anychart/anychart-venn.min.js"
@import "../js/anychart/pastel.min.js"
@import "../js/anychart/venn-entropy.js"

<!-- slide data-notes="" -->

##### 支持向量机的求解

---

原问题：变量个数为特征数$n$

<p>
\begin{align}
    & \min_{\wv,b} \Bigg\{ \frac{1}{2} \|\wv\|_2^2 + C\sum_{i \in [m]} \max \{ 0, 1- y_i (\wv^\top \phi(\xv_i) + b) \} \Bigg\} \\
    & \min_{\wv,b,\epsilon_i} \Bigg\{ \frac{1}{2} \|\wv\|_2^2 + C \sum_{i \in [m]} \epsilon_i \Bigg\}, \quad \st ~ y_i (\wv^\top \phi(\xv_i) + b) \ge 1 - \epsilon_i, ~ \epsilon_i \ge 0, ~ \forall i \in [m] \\
\end{align}
</p>

<div class="top2"></div>

对偶问题：变量个数为样本数$m$

<p>
\begin{align}
    \max_{0 \le \alpha_i \le C} \Bigg\{ - \frac{1}{2} \sum_{i \in [m]} \sum_{j \in [m]} \alpha_i \alpha_j y_i y_j \class{blue}{\kappa(\xv_i, \xv_j)} + \sum_{i \in [m]} \alpha_i \Bigg\}, \quad \st ~ \sum_{i \in [m]} \alpha_i y_i = 0
\end{align}
</p>

<div class="top4"></div>

- 若采用线性核，原问题、对偶问题择其易解者解之
- 若采用非线性核，除非可显式写出对应的核映射，否则只考虑求解对偶问题

<!-- slide vertical=true data-notes="" -->

##### 支持向量机的求解

---

原问题：变量个数为特征数$n$

<p>
\begin{align}
    \min_{\wv,b} \Bigg\{ \frac{1}{2} \|\wv\|_2^2 + C\sum_{i \in [m]} \max \{ 0, 1- y_i (\wv^\top \xv_i + b) \} \Bigg\}
\end{align}
</p>

<div class="top2"></div>

无约束形式可直接用随机次梯度下降及其变种，参考 Pegasos

<!-- slide vertical=true data-notes="" -->

##### 支持向量机的求解

---

原问题：变量个数为特征数$n$

<p>
\begin{align}
    \min_{\wv,b,\epsilon_i} \Bigg\{ \frac{1}{2} \|\wv\|_2^2 + C \sum_{i \in [m]} \epsilon_i \Bigg\}, \quad \st ~ y_i (\wv^\top \xv_i + b) \ge 1 - \epsilon_i, ~ \epsilon_i \ge 0, ~ \forall i \in [m] \\
\end{align}
</p>

<div class="top2"></div>

有约束形式可写成标准的二次规划 (quadratic programming, QP) 形式

<p>
\begin{align}
    \min_{\wv,b,\epsilonv} & ~ \left\{ \frac{1}{2} \begin{bmatrix} \wv \\ b \\ \epsilonv \end{bmatrix}^\top \begin{bmatrix} \Iv & 0 & \zerov \\ \zerov & 0 & \zerov \\ \zerov & \zerov & \zerov \end{bmatrix} \begin{bmatrix} \wv \\ b \\ \epsilonv \end{bmatrix} + \begin{bmatrix} \zerov \\ 0 \\ C \onev \end{bmatrix}^\top \begin{bmatrix} \wv \\ b \\ \epsilonv \end{bmatrix} \right\} \\
    \st & ~ \begin{bmatrix} - \Yv \Xv & - \yv & -\Iv \\ \zerov & 0 & -\Iv \end{bmatrix} \begin{bmatrix} \wv \\ b \\ \epsilonv \end{bmatrix} \le \begin{bmatrix} - \onev \\ \zerov \end{bmatrix}
\end{align}
</p>

<!-- slide vertical=true data-notes="" -->

##### 支持向量机的求解

---

对偶问题：变量个数为样本数$m$

<p>
\begin{align}
    \max_{0 \le \alpha_i \le C} \Bigg\{ - \frac{1}{2} \sum_{i \in [m]} \sum_{j \in [m]} \alpha_i \alpha_j y_i y_j \class{blue}{\kappa(\xv_i, \xv_j)} + \sum_{i \in [m]} \alpha_i \Bigg\}, \quad \st ~ \sum_{i \in [m]} \alpha_i y_i = 0
\end{align}
</p>

<div class="top2"></div>

对偶问题也是QP，但箱式约束$0 \le \alpha_i \le C$比原问题要好处理很多

SMO：每次取一对$(\alpha_i, \alpha_j)$进行优化，参考 libSVM

坐标下降：省略$b$可去掉等式约束$\yv^\top \alphav = 0$，所有$\alpha_i$去耦合，每次可只取一个$\alpha_i$进行优化，参考 liblinear

<!-- slide data-notes="" -->

##### 楚河汉界 间隔

---

<div id="board2" class="center" style="width:420px"></div>

<div class="top-33per left-70per bottom-10">
<button id="startBtn" class="top-40per">开始</button>
<button id="clearBtn">清空</button>
</div>

@import "../js/xiangqiboardjs-0.3.3/css/xiangqiboard-0.3.3.css"
@import "../js/xiangqiboardjs-0.3.3/js/xiangqiboard-0.3.3.js"
@import "../js/xiangqiboardjs-0.3.3/js/svm-chess.js"
