---
tags: type/concept 
alias:
creation-date: Saturday 19th February 2022
last-modified-date: Saturday 19th February 2022 16:27:43
---




> [!NOTE] Definition: Survival Function $S_{x}(t)$
> Let $(x)$ denote a person with age $x$. 
> 
> The **survival function**, denoted $S_{x}(t)$, denote the probability that $(x)$ would survive the next $t$ years.





It is the complement of the distribution function of the [[Future Lifetime Random Variable|future lifetime]] random variable. $$S_{x}(t) = 1 - F_{x}(t)$$


---
## Some properties of the [[Survival Function]]
1. The survival function at $t=0$ is equal to 1.
$$S_{x}(0) = \space_0p_{x}= 1$$
```ad-note


If a person is alive, then at that precise moment ($t=0$), we are sure that the probability of their survival is 1 or 100%.

```

2. Its limit approaches zero as $t$ approaches infinity.
$$\lim_{t \to +\infty} S_{x}(t) = 0$$
```ad-note

Everyone dies at a certain point in time. 😢

```

3.  It is a nondecreasing function.