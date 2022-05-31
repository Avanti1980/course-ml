---
presentation:
  margin: 0
  center: false
  transition: "convex"
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

##### 从数据中估计概率

---

<div class="top2"></div>

$$
\begin{align*}
    \qquad \Pr(y | \xv) = \Pr(y) \cdot \Pr(x_1 | y) \cdot \Pr(x_2 | y) \cdots \Pr(x_d | y)
\end{align*}
$$

对于先验，记$\alpha_k = \Pr(y = k)$，于是

$$
\begin{align*}
    \qquad \Pr(y | \alpha_k) = \prod_{k \in [c]} \Pr(y = k)^{\Ibb(y=k)} = \prod_{k \in [c]} \alpha_k^{\Ibb(y=k)}
\end{align*}
$$

对于似然，设第$j$个特征共有$n_j$种不同取值$v_1^{(j)}, \ldots, v_{n_j}^{(j)}$

<div class="top-2"></div>

记$\theta_{jlk} = \Pr( x_j = v_l^{(j)} | y=k)$，于是对$\forall j \in [d]$和$\forall k \in [c]$有

$$
\begin{align*}
    \qquad \Pr(x_j | y = k, \theta_{jlk}) & = \prod_{l \in [n_j]} \Pr( x_j = v_l^{(j)} | y=k)^{\Ibb(x_j = v_l^{(j)})} = \prod_{l \in [n_j]} \theta_{jlk}^{\Ibb(x_j = v_l^{(j)})} \\
    \sum_{l \in [n_j]} \theta_{jlk} & = 1
\end{align*}
$$

<!-- slide vertical=true data-notes="" -->

##### 从数据中估计概率

---

待估计参数：

- $\alpha_k = \Pr(y = k)$，其中$k \in [c]$
- $\theta_{jlk} = \Pr( x_j = v_l^{(j)} | y=k)$，其中$k \in [c], j \in [d], l \in [n_j]$

<div class="top2"></div>

设训练集$D = \{ (\xv^{(i)}, y^{(i)}) \}_{i \in [m]}$，此时可采用两种估计方法：

- 极大似然估计
- 最大后验估计

<div class="top2"></div>

极大似然估计：

$$
\begin{align*}
    \log \Pr(D | \alpha_k, \theta_{jlk}) & = \log \prod_{i \in [m]} \Pr(\xv^{(i)}, y^{(i)} | \alpha_k, \theta_{jlk}) \\
    & = \sum_{i \in [m]} \log \Pr(y^{(i)} | \alphav) + \sum_{i \in [m]} \log \Pr(\xv^{(i)} | y^{(i)}, \thetav) \\
                           & = \sum_{i \in [m]} \log \prod_{k \in [c]} \alpha_k^{\Ibb(y^{(i)}=k)} + \sum_{i \in [m]} \log \prod_{k \in [c]} \Pr(\xv^{(i)} | y^{(i)} = k, \thetav)^{\Ibb(y^{(i)}=k)} \\
                           & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \log \alpha_k + \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \log \Pr(\xv^{(i)} | y^{(i)} = k, \thetav)
\end{align*}
$$

<!-- slide data-notes="" -->

##### 极大似然估计

---

训练集$D = \{ (\xv^{(i)}, y^{(i)}) \}_{i \in [m]}$，待估计参数：

- $\alpha_k = \Pr(y = k)$，其中$k \in [c]$
- $\theta_{jlk} = \Pr( x_j = v_l^{(j)} | y=k)$，其中$k \in [c], j \in [d], l \in [n_j]$

<div class="top4"></div>

$$
\begin{align*}
    \log \Pr( & D | \alpha_k, \theta_{jlk}) = \log \prod_{i \in [m]} \Pr(\xv^{(i)}, y^{(i)} | \alpha_k, \theta_{jlk}) \\
    & = \sum_{i \in [m]} \log \Pr(y^{(i)} | \alpha_k) + \sum_{i \in [m]} \log \Pr(\xv^{(i)} | y^{(i)}, \theta_{jlk}) \\
                           & = \sum_{i \in [m]} \log \prod_{k \in [c]} \alpha_k^{\Ibb(y^{(i)}=k)} + \sum_{i \in [m]} \log \prod_{k \in [c]} \Pr(\xv^{(i)} | y^{(i)} = k, \thetav)^{\Ibb(y^{(i)}=k)} \\
                           & = \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \log \alpha_k + \sum_{k \in [c]} \sum_{i \in [m]} \Ibb(y^{(i)}=k) \log \Pr(\xv^{(i)} | y^{(i)} = k, \thetav)
\end{align*}
$$
