@import "../css/theme/solarized.css"
@import "../css/index.css"

#### 常见符号说明

<div class="threelines notation head-highlight">

|                      符号                      |                                     说明                                      |
| :--------------------------------------------: | :---------------------------------------------------------------------------: |
|         $\Rbb$、$\Zbb$、$\Nbb$、$\Qbb$         |                          实数、整数、自然数、有理数                           |
|               $x$、$\xv$、$\Xv$                |                               标量、向量、矩阵                                |
|                    $\ev_i$                     |                      第$i$个分量为$1$其余分量为$0$的向量                      |
|               $\onev$、$\zerov$                |                             全$1$向量、全$0$向量                              |
|                   $\Delta_d$                   |  $d$维单纯形$\{ \xv \in \Rbb^d \mid \xv^\top \onev = 1, ~ \xv \ge \zerov \}$  |
|                  $B_\av (r)$                   |                         以$\av$为球心、$r$为半径的球                          |
|  $[\cdot,\cdot,\cdot]$、$[\cdot;\cdot;\cdot]$  |                                行向量、列向量                                 |
|                  $\tr[\cdot]$                  |                                      迹                                       |
| $\|\xv\|_p = (\sum_i \vert x_i \vert^p)^{1/p}$ |               向量$\xv$的$\ell_p$范数，$p$缺省时为$\ell_2$范数                |
|    $\|\xv\|_\Mv = (\xv^\top \Mv \xv)^{1/2}$    |                  向量$\xv$的椭圆范数，其中$\Mv$为半正定矩阵                   |
|   $\|\Xv\|_F = (\sum_{i,j} x_{ij}^2)^{1/2}$    |         矩阵$\Xv$的 Frobenius 范数，也等于$(\tr[\Xv^\top \Xv])^{1/2}$         |
|                $\gv = \nabla f$                |                                   $f$的梯度                                   |
|               $\Hv = \nabla^2 f$               |                                 $f$的海森矩阵                                 |
|                   $\Ibb(x)$                    |                   指示函数，在$x$为真、假时分别取值$1$、$0$                   |
|                   $\sign(x)$                   |               符号函数，在$x \ge 0$、$x < 0$时分别取值$1$、$-1$               |
|                   $\sgn(x)$                    |               阶跃函数，在$x \ge 0$、$x < 0$时分别取值$1$、$0$                |
|                  $\sigma(x)$                   |                       对数几率函数$1 / (1 + \exp(- x))$                       |
|                   $p(\cdot)$                   |                               概率质量/密度函数                               |
|                  $\Ucal(a,b)$                  |                            区间$[a,b]$上的均匀分布                            |
|             $\Ncal(\muv,\Sigmav)$              |                   均值为$\muv$、协方差为$\Sigmav$的高斯分布                   |
|      $\Ebb_{\cdot \sim \Dcal} [f(\cdot)]$      | $f(\cdot)$对$\cdot$服从分布$\Dcal$时的期望，意义明确时简写为$\Ebb [f(\cdot)]$ |
|          $\var[\cdot]$、$\cov[\cdot]$          |                                 方差、协方差                                  |
|                $\argmin_x f(x)$                |                            使得$f(x)$取最小值的$x$                            |
|                $\argmax_x f(x)$                |                            使得$f(x)$取最大值的$x$                            |
|                     $\st$                      |                 $\text{subject to}$的缩写，优化问题的约束条件                 |
|                    $\Xcal$                     |                                   样本空间                                    |
|                    $\Ycal$                     |                                 类别标记集合                                  |
|                    $\Dcal$                     |                       $\Xcal \times \Ycal$上的未知分布                        |
|                    $\Hcal$                     |                                   假设空间                                    |
|                      $D$                       |                      独立同分布采样自分布$\Dcal$的数据集                      |
|                  $\triangleq$                  |                                    定义为                                     |
|                     $[c]$                      |                 集合$\{ 1, 2, \ldots, c \}$，其中$c$为正整数                  |

</div>
