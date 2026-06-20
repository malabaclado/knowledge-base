
### Details
Source:  
- M1502THW 05062021 ZoomDisc(Lec9) Video
### Notes
In this lecture, we discussed:
- What is a statistical hypothesis?
- Simple vs Complex Hypothesis
- What is Hypothesis Testing
- Type I and Type II Error

---

> Definition. (**Statistical Hypothesis**)
> A **statistical hypothesis** is an assertion or conjecture about the distribution of one or more random variables. 

**Simple vs Composite Hypothesis.** If the statistical hypothesis completely specifies the distribution, then is called **simple**; otherwise, it is called **composite.**

In a composite hypothesis, we may not know the distribution or the parameters of the distribution are unknown.



Next, we move on to **hypothesis testing**.

> Definition. (**Hypothesis Test**)
> A **test of a statistical hypothesis** H is a rule or procedure for deciding whether to reject the hypothesis H.


> Definition. (**Nonrandomized Test**)
> These are statistical tests of the form:
> Reject $H_0$ if and only if $(x_1, x_2, . . . , x_n) \in C$, where $C$ is a subset of all possible values of $(X_1, X_2, . . . , X_n)$.

In the above definition, $C$ is known as the **critical region.
**

In any hypothesis testing problems,** there are always two hypothesis that are being discussed.**

- Null Hypothesis - the one being tested, usually denoted as $H_0$
- Alternative Hypothesis - the complement of the null hypothesis; denoted as $H_A$ or sometimes, $H_1$

Note that the **null and alternative hypothesis** does **not necessarily complement** each other. However, they **must be strictly disjoint.**

**On acceptance of $H_0$**: When we say that "$H_0$ is not rejected", it does not mean that we accept $H_0$. There is always a possibility that accepting or rejecting a null hypothesis is false. Thus, when one says $H_0$ is not rejected, it is not really accepting $H_0$ but rather there is not enough evidence to reject $H_0$.

**Two Types of Error**

> Definition. (**Type I and Type II Errors**)
> - Type I: Rejecting $H_0$ when $H_0$ is true.
> - Type II: Accepting $H_0$ when $H_0$ is false.

**Power Function**

Next, we define the [[Power Function]] which is the probability that the null hypothesis $H_0$ gets rejected. This is denoted by $\Pi_C(\theta)$ where $C$ is the critical region of the null hypothesis.

> $$\begin{align}
> \Pi_C(\theta) &=\mathbb{P}[reject H_0]\\
> &= \mathbb{P} [(X_1, X_2,...,X_n) \in C]
> \end{align}$$

Now, we formally define the term [[Level of Significance]] that is always used in hypothesis testing. The level of significance, denoted $\alpha$ is the supremum of the power function at C. That is, $$\alpha = \sup [\Pi_C(\theta)] $$



### Comments

