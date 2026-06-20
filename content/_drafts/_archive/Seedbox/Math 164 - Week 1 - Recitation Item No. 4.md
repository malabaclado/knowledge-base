---
tags: type/draft 
alias:
creation-date: Friday 25th February 2022
last-modified-date: Monday 28th February 2022 15:58:44
---
⬅️ 

# Math 164 - Week 1 - Recitation Item No. 4


Math 164 -  Week 1 -  Recitation Item No. 4


Show $\space_{k|}q_{0}= - \Delta S_{0}(k)$

$$\begin{align*}
\space_{k|}q_{0} &= \space_{k|1} q_{0}\\
&= \space_{k}p_{0} \cdot \space_{1}q_{x}\\
&= \space_{k}p_{0} \cdot (1 - \space_{1}p_{k})\\
&= \space_{k}p_{0} - (\space_{k}p_{0} \cdot \space_{1}p_{k})\\
&= \space_{k}p_{0} - \space_{k+1}p_{0}\\
&= S_{0}(k) - S_{0}(k+1)\\
& =- (S_{0}(k+1) - S_{0}(k))\\
&= - \Delta S_0(k)
\end{align*}$$
---

Show $\sum_{k=0}^{\infty} \space_{k|}q_{0}= 1$
$$\begin{align*}
\sum_{k=0}^{\infty} \space_{k|}q_{0} &= \lim_{n\to \infty} \sum_{k=0}^{n} \space_{k|}q_{0}\\
&= \lim_{n\to \infty} \sum_{k=0}^{n} \big[S_{0}(k) - S_{0}(k+1)\big]\\
&= \lim_{n\to \infty}  \bigg [\big[ S_{0}(0) - S_{0}(1) \big] + \big[ S_{0}(1) - S_{0}(2) \big] + \big[ S_{0}(2) - S_{0}(3) \big] + \cdots  + \big[ S_{0}(n) - S_{0}(n+1) \big]\bigg ]\\
& = \lim_{n\to \infty} \big[ S_{0}(0) - S_{0}(n+1) \big]\\
&= \lim_{n\to \infty} \big[ 1 - S_{0}(n+1) \big]\\
&= 1- \lim_{n\to \infty} \big[ S_{0}(n+1) \big]\\
&=1-0\\
&=1
\end{align*}$$




