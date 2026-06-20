---
tags: type/research-note 
alias: [A tutorial on support vector regression]
---
# A tutorial on support vector regression

> [!info]
> - **Cite Key:** [[@smolaTutorialSupportVector2004]]
> - **Abstract:** In this tutorial we give an overview of the basic ideas underlying Support Vector (SV) machines for function estimation. Furthermore, we include a summary of currently used algorithms for training SV machines, covering both the quadratic (or convex) programming part and advanced methods for dealing with large datasets. Finally, we mention some modifications and extensions that have been applied to the standard SV algorithm, and discuss the aspect of regularization from a SV perspective.
> - **Bibliography:** Smola, A. J., & Schölkopf, B. (2004). A tutorial on support vector regression. _Statistics and Computing_, _14_(3), 199–222. [https://doi.org/10.1023/B:STCO.0000035301.49549.88](https://doi.org/10.1023/B:STCO.0000035301.49549.88)
> - **Tags:** #Journal



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- In a nutshell, VC theory characterizes properties of learning machines which enable them to generalize well to unseen data.

- In its present form, the SV machine was largely developed at AT&T Bell Laboratories by Vapnik and co-workers (Boser, Guyon and Vapnik 1992, Guyon, Boser and Vapnik 1993, Cortes and Vapnik, 1995, Sch ̈ olkopf, Burges and Vapnik 1995, 1996, Vapnik, Golowich and Smola 1997). Due to this industrial context, SV research has up to date had a sound orientation towards real-world applications. Initial work focused on OCR (optical character recognition). Within a short period of time, SV classifiers became competitive with the best available systems for both OCR and object recognition tasks (Sch ̈ olkopf, Burges and Vapnik 1996, 1998a, Blanz et al. 1996, Sch ̈ olkopf 1997). A comprehensive tutorial on SV classifiers has been published by Burges (1998). But also in regression and time series prediction applications, excellent performances were soon obtained (M  ̈ uller et al. 1997, Drucker et al. 1997, Stitson et al. 1999, Mattera and Haykin 1999). A snapshot of the state of the art in SV learning was recently taken at the annual Neural Information Processing Systems conference (Sch ̈ olkopf, Burges, and Smola 1999a). SV learning has now evolved into an active area of research.

- In ε-SV regression (Vapnik 1995), our goal is to find a function f (x) that has at most ε deviation from the actually obtained targets yi for all the training data, and at the same time is as flat as possible. In other words, we do not care about errors as long as they are less than ε,but will not accept any deviation larger than this. This may be important if youwant to be sure not to lose more than ε money when dealing with exchange rates, for instance.

- Flatness in the case of (1) means that one seeks a small w. One way to ensure this is to minimize the norm,3 i.e. ‖w‖2 =〈w, w〉.

- Analogously to the “soft margin” loss function (Bennett and Mangasarian 1992) which was used in SV machines by Cortes and Vapnik (1995), one can introduce slack variables ξi ,ξ∗ i to cope with otherwise infeasible constraints of the optimization problem (2).

- The constant C > 0 determines the trade-off between the flatness of f and the amount up to which deviations larger than ε are tolerated.

- This corresponds to dealing with a so called ε-insensitive loss function |ξ |ε described by

- This is the so-called Support Vector expansion, i.e. w can be completely described as a linear combination of the training patterns xi .Inasense, the complexity of a function’s representation by SVs is independent of the dimensionality of the input space X , and depends only on the number of SVs.

- Moreover, note that the complete algorithm can be described in terms of dot products between the data. Even when evaluating f (x)weneed not compute w explicitly. These observations will come in handy for the formulation of a nonlinear extension.

- This allows us to make several useful conclusions. Firstly only samples (xi , yi ) with corresponding α(∗) i = C lie outside the εinsensitive tube. Secondly αi α∗ i = 0, i.e. there can never be a set of dual variables αi ,α∗ i which are both simultaneously nonzero

- Another way of computing b will be discussed in the context of interior point optimization (cf. Section 5). There b turns out to be a by-product of the optimization process. Further considerations shall be deferred to the corresponding section. See also Keerthi et al. (1999) for further methods to compute the constant offset.

- The examples that come with nonvanishing coefficients are called Support Vectors.

- The next step is to make the SV algorithm nonlinear. This, for instance, could be achieved by simply preprocessing the training patterns xi byamap  : X → F into some feature space F

- As noted in the previous section, the SV algorithm only depends on dot products between patterns xi . Hence it suffices to know k(x, x′):=〈(x),(x′)〉 rather than  explicitly

- Also note that in the nonlinear setting, the optimization problem corresponds to finding the flattest function in feature space, not in input space.

- So far the SV algorithm for regression may seem rather strange and hardly related to other existing methods of function estimation (e.g. Huber 1981, Stone 1985, H ̈ ardle 1990, Hastie and Tibshirani 1990, Wahba 1990).

- While there has been a large number of implementations of SV algorithms in the past years, we focus on a few algorithms which will be presented in greater detail.


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:46.334+08:00 %%
