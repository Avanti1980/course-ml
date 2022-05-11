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

##### 行列式对矩阵求导

---

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，其中$\Av, \Bv$与$\Xv$无关

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} = \frac{\partial |\Yv|}{\partial x_{ji}} = \sum_{p,q} \frac{\partial |\Yv|}{\partial y_{pq}}\frac{\partial y_{pq}}{\partial x_{ji}} = \tr \left( \frac{\partial |\Yv|}{\partial \Yv} \frac{\partial \Yv}{\partial x_{ji}} \right)
\end{align*}
$$

记$y_{ji}$有增量$\epsilon$后的矩阵为$\Yv(y_{ji} + \epsilon)$，根据第$j$行拉普拉斯展开

$$
\begin{align*}
    |\Yv(y_{ji} + \epsilon)| - |\Yv| = \epsilon ~ C_{ji}
\end{align*}
$$

<div class="top-4"></div>

其中$C_{ji}$是关于$y_{ji}$的<span class="blue">代数余子式</span>，于是

$$
\begin{align*}
    \left[ \frac{\partial |\Yv|}{\partial \Yv} \right]_{ij} & = \frac{\partial |\Yv|}{\partial y_{ji}} = \lim_{\epsilon \rightarrow 0} \frac{|\Yv(y_{ji} + \epsilon)| - |\Yv|}{\epsilon} = C_{ji} ~ \Longrightarrow ~ \frac{\partial |\Yv|}{\partial \Yv} = \Yv^*
\end{align*}
$$

<div class="top-4"></div>

其中$\Yv^*$是$\Yv$的<span class="blue">伴随矩阵</span> (adjugate matrix)

<!-- slide vertical=true data-notes="" -->

##### 行列式对矩阵求导

---

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，其中$\Av, \Bv$与$\Xv$无关

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} = \frac{\partial |\Yv|}{\partial x_{ji}} = \sum_{p,q} \frac{\partial |\Yv|}{\partial y_{pq}}\frac{\partial y_{pq}}{\partial x_{ji}} = \tr \left( \Yv^* \frac{\partial \Yv}{\partial x_{ji}} \right)
\end{align*}
$$

<div class="top-4"></div>

又第二项

$$
\begin{align*}
    \frac{\partial \Yv}{\partial x_{ji}} = \frac{\partial \Av \Xv \Bv}{\partial x_{ji}} = \Av \frac{\partial \Xv}{\partial x_{ji}} \Bv = \Av \Ev_{ji} \Bv
\end{align*}
$$

<div class="top-4"></div>

代入可得

$$
\begin{align*}
    \left[ \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} \right]_{ij} & = \tr (\Yv^* \Av \Ev_{ji} \Bv) = [\Bv \Yv^* \Av]_{ij} \\
    & \Longrightarrow \class{blue}{\frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av}
\end{align*}
$$

<!-- slide vertical=true data-notes="最后一个例子解决了极大似然里的ln sigma对sigma求导的问题" -->

##### 行列式对矩阵求导

---

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{l \times m}, \Bv \in \Rbb^{n \times l}, \Yv = \Av \Xv \Bv \in \Rbb^{l \times l}$，其中$\Av, \Bv$与$\Xv$无关

$$
\begin{align*}
    \class{blue}{\frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av}
\end{align*}
$$

<div class="top-2"></div>

若$\Xv, \Av, \Bv$均为可逆方阵，则$\Yv = \Av \Xv \Bv$亦为可逆方阵，于是

$$
\begin{align*}
    \frac{\partial |\Av \Xv \Bv|}{\partial \Xv} = \Bv (\Av \Xv \Bv)^* \Av = \Bv |\Av \Xv \Bv| (\Av \Xv \Bv)^{-1} \Av = |\Av \Xv \Bv| \Xv^{-1}
\end{align*}
$$

<div class="top-2"></div>

进一步若$\Av = \Bv = \Iv$，则$\frac{\partial |\Xv|}{\partial \Xv} = \Xv^* = |\Xv| \Xv^{-1}$，由此可得

$$
\begin{align*}
    \frac{\partial |\Xv^n|}{\partial \Xv} = \frac{\partial |\Xv|^n}{\partial \Xv} = n |\Xv|^{n-1} \Xv^* = n |\Xv|^n \Xv^{-1} = n |\Xv^n| \Xv^{-1}
\end{align*}
$$

<div class="top-2"></div>

若$a$与$\Xv$无关，则$\frac{\partial \ln |a \Xv|}{\partial \Xv} = \frac{\partial \ln a^m |\Xv|}{\partial \Xv} = \frac{\partial \ln |\Xv|}{\partial \Xv} = \frac{\Xv^*}{|\Xv|} = \Xv^{-1}$

<!-- slide vertical=true data-notes="" -->

##### 行列式对矩阵求导

---

设$\Xv \in \Rbb^{m \times n}, \Av \in \Rbb^{m \times m}, \Yv = \Xv^\top \Av \Xv \in \Rbb^{n \times n}$可逆，其中$\Av$与$\Xv$无关，易知

$$
\begin{align*}
    \left[ \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} \right]_{ij} & = \tr \left( \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Yv} \frac{\partial \Yv}{\partial x_{ji}} \right) = \tr \left( \Yv^* \frac{\partial \Xv^\top \Av \Xv}{\partial x_{ji}} \right) \\
    & = \tr \left( \Yv^* \frac{\partial \Xv^\top}{\partial x_{ji}} \Av \Xv \right) + \tr \left( \Yv^* \Xv^\top \Av \frac{\partial \Xv}{\partial x_{ji}} \right) \\
    & = \tr ( \Yv^* \Ev_{ij} \Av \Xv ) + \tr ( \Yv^* \Xv^\top \Av \Ev_{ji} ) = [\Av \Xv \Yv^*]_{ji} + [\Yv^* \Xv^\top \Av]_{ij}
\end{align*}
$$

<div class="top-4"></div>

于是

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} & = (\Av \Xv \Yv^*)^\top + \Yv^* \Xv^\top \Av \\
    & = (\Av \Xv |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1})^\top + |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av \\
    & = |\Xv^\top \Av \Xv| (\Xv^\top \Av^\top \Xv)^{-1} \Xv^\top \Av^\top + |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av \\
    & = |\Xv^\top \Av \Xv| ((\Xv^\top \Av^\top \Xv)^{-1} \Xv^\top \Av^\top + (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av)
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 行列式对矩阵求导

---

如果$\Av$对称，则

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} = 2 |\Xv^\top \Av \Xv| (\Xv^\top \Av \Xv)^{-1} \Xv^\top \Av
\end{align*}
$$

若$\Xv$、$\Av$是方阵，则其均可逆，于是

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Av \Xv|}{\partial \Xv} = 2 |\Xv^\top| |\Av| |\Xv| \Xv^{-1} \Av^{-1} \Xv^{-\top} \Xv^\top \Av = 2 |\Xv|^2 |\Av| \Xv^{-1}
\end{align*}
$$

若$\Av = \Iv$，则

$$
\begin{align*}
    \frac{\partial |\Xv^\top \Xv|}{\partial \Xv} = 2 |\Xv^\top \Xv| (\Xv^\top \Xv)^{-1} \Xv^\top = 2 |\Xv^\top \Xv| \Xv^\dagger, \quad \frac{\partial \ln |\Xv^\top \Xv|}{\partial \Xv} = 2 \Xv^\dagger
\end{align*}
$$

<div class="top-4"></div>

其中$\Xv^\dagger$是$\Xv$的<span class="blue">伪逆</span> (pseudoinverse)
