---
tags: type/research-note 
alias: [Pattern recognition and machine learning]
---
# Pattern recognition and machine learning

> [!info]
> - **Cite Key:** [[@bishopPatternRecognitionMachine2006]]
> - **Bibliography:** Bishop, C. M. (2006). _Pattern recognition and machine learning_. Springer.
> - **Tags:** #Machine-learning, #Pattern-perception, #Book



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- Library of Congress Control Number: 2006922522

- Also, the practical applicability of Bayesian methods has been greatly enhanced through the development of a range of approximate inference algorithms such as variational Bayes and expectation propagation.

- The field of pattern recognition is concerned with the automatic discovery of regularities in data through the use of computer algorithms and with the use of these regularities to take actions such as classifying the data into different categories.

- The ability to categorize correctly new examples that differ from those used for training is known as generalization.

- In other pattern recognition problems, the training data consists of a set of input vectors x without any corresponding target values. The goal in such unsupervised learning problems may be to discover groups of similar examples within the data, where it is called clustering, or to determine the distribution of data within the input space, known as density estimation, or to project the data from a high-dimensional space down to two or three dimensions for the purpose of visualization.

- credit assignment problem

- A general feature of reinforcement learning is the trade-off between exploration, in which the system tries out new kinds of actions to see how effective they are, and exploitation, in which the system makes use of actions that are known to yield a high reward.

- By generating data in this way, we are capturing a property of many real data sets, namely that they possess an underlying regularity, which we wish to learn, but that individual observations are corrupted by random noise. This noise might arise from intrinsically stochastic (i.e. random) processes such as radioactive decay but more typically is due to there being sources of variability that are themselves unobserved.

- Probability theory, discussed in Section 1.2, provides a framework for expressing such uncertainty in a precise and quantitative manner, and decision theory, discussed in Section 1.5, allows us to exploit this probabilistic representation in order to make predictions that are optimal according to appropriate criteria.

- We see that, for a given model complexity, the over-fitting problem become less severe as the size of the data set increases. Another way to say this is that the larger the data set, the more complex (in other words more flexible) the model that we can afford to fit to the data.

- We shall see that the least squares approach to finding the model parameters represents a specific case of maximum likelihood (discussed in Section 1.2.5), and that the over-fitting problem can be understood as a general property of maximum likelihood.

- One technique that is often used to control the over-fitting phenomenon in such cases is that of regularization, which involves adding a penalty term to the error function (1.2) in order to discourage the coefficients from reaching large values.

- We see that in effect λ now controls the effective complexity of the model and hence determines the degree of over-fitting.

- Probability theory provides a consistent framework for the quantification and manipulation of uncertainty and forms one of the central foundations for pattern recognition. When combined with decision theory, discussed in Section 1.5, it allows us to make optimal predictions given all the information available to us, even though that information may be incomplete or ambiguous

- Note that, by definition, probabilities must lie in the interval [0, 1].

- Also, if the events are mutually exclusive and if they include all possible outcomes (for instance, in this example the box must be either red or blue), then we see that the probabilities for those events must sum to one.

- Our assessment of such matters will affect the actions we take, for instance the extent to which we endeavour to reduce the emission of greenhouse gasses. In such circumstances, we would like to be able to quantify our expression of uncertainty and make precise revisions of uncertainty in the light of new evidence, as well as subsequently to be able to take optimal actions or decisions as a consequence. This can all be achieved through the elegant, and very general, Bayesian interpretation of probability.

- For instance, Cox (1946) showed that if numerical values are used to represent degrees of belief, then a simple set of axioms encoding common sense properties of such beliefs leads uniquely to a set of rules for manipulating degrees of belief that are equivalent to the sum and product rules of probability.

- We shall see that, from a Bayesian perspective, we can use the machinery of probability theory to describe the uncertainty in model parameters such as w,or indeed in the choice of model itself.

- It expresses how probable the observed data set is for different settings of the parameter vector w. Note that the likelihood is not a probability distribution over w, and its integral with respect to w does not (necessarily) equal one.

- Given this definition of likelihood, we can state Bayes’ theorem in words posterior ∝ likelihood × prior (1.44)

- In the machine learning literature, the negative log of the likelihood function is called an error function.

- Because the negative logarithm is a monotonically decreasing function, maximizing the likelihood is equivalent to minimizing the error.

- One approach to determining frequentist error bars is the bootstrap

- One advantage of the Bayesian viewpoint is that the inclusion of prior knowledge arises naturally. Suppose, for instance, that a fair-looking coin is tossed three times and lands heads each time. A classical maximum likelihood estimate of the probability of landing heads would give 1, implying that all future tosses will land Section 2.1 heads! By contrast, a Bayesian approach with any reasonable prior will lead to a much less extreme conclusion.

- Reducing the dependence on the prior is one motivation for so-called noninformative priors.

- The development of sampling methods, such as Markov chain Monte Carlo (discussed in Chapter 11) along with dramatic improvements in the speed and memory capacity of computers, opened the door to the practical use of Bayesian techniques in an impressive range of problem domains.

- The square root of the variance, given by σ, is called the standard deviation

- the reciprocal of the variance, written as β =1/σ2, is called the precision

- Data points that are drawn independently from the same distribution are said to be independent and identically distributed

- In practice, it is more convenient to maximize the log of the likelihood function. Because the logarithm is a monotonically increasing function of its argument, maximization of the log of a function is equivalent to maximization of the function itself

- In particular, we shall show that the maximum likelihood approach systematically underestimates the variance of the distribution.

- Note that the bias of the maximum likelihood solution becomes less significant as the number N of data points increases, and in the limit N →∞the maximum likelihood solution for the variance equals the true variance of the distribution that generated the data.

- the issue of bias in maximum likelihood lies at the root of the over-fitting problem that we encountered earlier in the context of polynomial curve fitting.

- ere we return to the curve fitting example and view it Section 1.1 from a probabilistic perspective, thereby gaining some insights into error functions and regularization, as well as taking us towards a full Bayesian treatment.

- In our example of polynomial curve fitting using least squares, we saw that there was an optimal order of polynomial that gave the best generalization. The order of the polynomial controls the number of free parameters in the model and thereby governs the model complexity.

- In a practical application, we need to determine the values of such parameters, and the principal objective in doing so is usually to achieve the best predictive performance on new data. Furthermore, as well as finding the appropriate values for complexity parameters within a given model, we may wish to consider a range of different types of model in order to find the best one for our particular application

- In many applications, however, the supply of data for training and testing will be limited, and in order to build good models, we wish to use as much of the available data as possible for training. However, if the validation set is small, it will give a relatively noisy estimate of predictive performance. One solution to this dilemma is to use cross-validation

- One major drawback of cross-validation is that the number of training runs that must be performed is increased by a factor of S, and this can prove problematic for models in which the training is itself computationally expensive. A further problem with techniques such as cross-validation that use separate data to assess performance is that we might have multiple complexity parameters for a single model (for instance, there might be several regularization parameters). Exploring combinations of settings for such parameters could, in the worst case, require a number of training runs that is exponential in the number of parameters.

- the Akaike information criterion, or AIC (Akaike, 1974)

- Bayesian information criterion,orBIC

- Decision Theory

- We have seen in Section 1.2 how probability theory provides us with a consistent mathematical framework for quantifying and manipulating uncertainty. Here we turn to a discussion of decision theory that, when combined with probability theory, allows us to make optimal decisions in situations involving uncertainty such as those encountered in pattern recognition.

- Suppose we have an input vector x together with a corresponding vector t of target variables, and our goal is to predict t given a new value for x. For regression problems, t will comprise continuous variables, whereas for classification problems t will represent class labels. The joint probability distribution p(x, t) provides a complete summary of the uncertainty associated with these variables. Determination of p(x, t) from a set of training data is an example of inference and is typically a very difficult problem whose solution forms the subject of much of this book.

- Note that any of the quantities appearing in Bayes’ theorem can be obtained from the joint distribution p(x, Ck) by either marginalizing or conditioning with respect to the appropriate variables.

- If our aim is to minimize the chance of assigning x to the wrong class, then intuitively we would choose the class having the higher posterior probability

- contiguous

- The optimal solution is the one which minimizes the loss function.

- In fact, we can identify three distinct approaches to solving decision problems, all of which have been used in practical applications.

- Approaches that explicitly or implicitly model the distribution of inputs as well as outputs are known as generative models, because by sampling from them it is possible to generate synthetic data points in the input space.

- Approaches that model the posterior probabilities directly are called discriminative models

- Bayesian inference

- One role for the distributions discussed in this chapter is to model the probability distribution p(x) of a random variable x, given a finite set x1,...,xN of observations. This problem is known as ==density estimation==

- We begin by considering the binomial and multinomial distributions for discrete random variables and the Gaussian distribution for continuous random variables. These are specific examples of parametric distributions, so-called because they are governed by a small number of adaptive parameters, such as the mean and variance in the case of a Gaussian for example.

- conjugate priors

- One limitation of the parametric approach is that it assumes a specific functional form for the distribution, which may turn out to be inappropriate for a particular application.

- For the Gaussian distribution to be well defined, it is necessary for all of the eigenvalues λi of the covariance matrix to be strictly positive, otherwise the distribution cannot be properly normalized.

- A matrix whose eigenvalues are strictly positive is said to be positive definite.

- If all of the eigenvalues are nonnegative, then the covariance matrix is said to be positive semidefinite.

- This confirms that the multivariate Gaussian (2.43) is indeed normalized.

- We now note that the exponent is an even function of the components of z and, because the integrals over these are taken over the range (−∞, ∞), the term in z in the factor (z + μ) will vanish by symmetry.

- A further limitation of the Gaussian distribution is that it is intrinsically unimodal (i.e., has a single maximum) and so is unable to provide a good approximation to multimodal distributions.

- Thus the Gaussian distribution can be both too flexible, in the sense of having too many parameters, while also being too limited in the range of distributions that it can adequately represent.

- We will see later that the introduction of latent variables, also called hidden variables or unobserved variables, allows both of these problems to be addressed. In particular, a rich family of multimodal distributions is obtained by introducing discrete latent variables leading to mixtures of Gaussians, as discussed in Section 2.3.9.

- Markov random field,

- linear dynamical system

- precision matrix

- It should be stressed at this point that, for instance, Λaa is not simply given by the inverse of Σaa. In fact, we shall shortly examine the relation between the inverse of a partitioned matrix and the inverses of its partitions.

- Schur complement

- We noted that the mean of the conditional distribution p(xa|xb) was a linear function of xb

- Recall that the marginal distribution over a subset of the components of a Gaussian random vector takes a particularly simple form when expressed in terms of the partitioned covariance matrix.

- Recall that the results for the conditional distribution are most easily expressed in terms of the partitioned precision matrix,

- We see that the expectation of the maximum likelihood estimate for the mean is equal to the true mean. However, the maximum likelihood estimate for the covariance has an expectation that is less than the true value, and hence it is biased.

- Sequential methods allow data points to be processed one at a time and then discarded and are important for on-line applications, and also where large data sets are involved so that batch processing of all data points at once is infeasible.

- First of all, we note that the mean of the posterior distribution given by (2.141) is a compromise between the prior mean μ0 and the maximum likelihood solution μML.

- As we increase the number of observed data points, the precision steadily increases, corresponding to a posterior distribution with steadily decreasing variance.

- With no observed data points, we have the prior variance, whereas if the number of data points N →∞, the variance σ2 N goes to zero and the posterior distribution becomes infinitely peaked around the maximum likelihood solution.

- Given a training data set comprising N observations {xn}, where n =1,...,N, together with corresponding target values {tn}, the goal is to predict the value of t for a new value of x. In the simplest approach, this can be done by directly constructing an appropriate function y(x) whose values for new inputs x constitute the predictions for the corresponding values of t.

- More generally, from a probabilistic perspective, we aim to model the predictive distribution p(t|x) because this expresses our uncertainty about the value of t for each value of x. From this conditional distribution we can make predictions of t, for any new value of x, in such a way as to minimize the expected value of a suitably chosen loss function.

- The goal in classification is to take an input vector x and to assign it to one of K discrete classes Ck where k =1,...,K.

- Data sets whose classes can be separated exactly by linear decision surfaces are said to be linearly separable

- In the previous chapter, we explored a variety of learning algorithms based on nonlinear kernels. One of the significant limitations of many such algorithms is that the kernel function k(xn, xm) must be evaluated for all possible pairs xn and xm of training points, which can be computationally infeasible during training and can lead to excessive computation times when making predictions for new data points.

- In this chapter we shall look at kernel-based algorithms that have sparse solutions, so that predictions for new inputs depend only on the kernel function evaluated at a subset of the training data points.

- An important property of support vector machines is that the determination of the model parameters corresponds to a convex optimization problem, and so any local solution is also a global optimum

- The SVM is a decision machine and so does not provide posterior probabilities.

- An alternative sparse kernel technique, known as the relevance vector machine (RVM), is based on a Bayesian formulation and provides posterior probaSection 7.2 bilistic outputs, as well as having typically much sparser solutions than the SVM.

- Note that we shall shortly introduce a dual representation expressed in terms of kernel functions, which avoids having to work explicitly in feature space.

- linearly separable

- There may of course exist many such solutions that separate the classes exactly. In Section 4.1.7, we described the perceptron algorithm that is guaranteed to find a solution in a finite number of steps.

- If there are multiple solutions all of which classify the training data set exactly, then we should try to find the one that will give the smallest generalization error. The support vector machine approaches this problem through the concept of the margin, which is defined to be the smallest distance between the decision boundary and any of the samples, as illustrated in Figure 7.1.

- In support vector machines the decision boundary is chosen to be the one for which the margin is maximized. The maximum margin solution can be motivated using computational learning theory, also known as statistical learning theory.

- We shall see in Figure 10.13 that marginalization with respect to the prior distribution of the parameters in a Bayesian approach for a simple linearly separable data set leads to a decision boundary that lies in the middle of the region separating the data points.

- This is known as the canonical representation of the decision hyperplane.

- In the case of data points for which the equality holds, the constraints are said to be active, whereas for the remainder they are said to be inactive. By definition, there will always be at least one active constraint, because there will always be a closest point, and once the margin has been maximized there will be at least two active constraints

- The optimization problem then simply requires that we maximize ‖w‖−1, which is equivalent to minimizing ‖w‖2

- This is an example of a quadratic programming problem in which we are trying to minimize a quadratic function subject to a set of linear inequality constraints.

- Note the minus sign in front of the Lagrange multiplier term, because we are minimizing with respect to w and b, and maximizing with respect to a.

- Here the kernel function is defined by k(x, x′)=φ(x)Tφ(x′). Again, this takes the form of a quadratic programming problem in which we optimize a quadratic function of a subject to a set of inequality constraints.

- The solution to a quadratic programming problem in M variables in general has computational complexity that is O(M 3).

- The kernel formulation also makes clear the role of the constraint that the kernel function k(x, x′) be positive definite, because this ensures that the Lagrangian function  ̃ L(a) is bounded below, giving rise to a welldefined optimization problem.

- In Appendix E, we show that a constrained optimization of this form satisfies the Karush-Kuhn-Tucker (KKT) conditions

- Any data point for which an =0will not appear in the sum in (7.13) and hence plays no role in making predictions for new data points. The remaining data points are called support vectors, and because they satisfy tny(xn)=1, they correspond to points that lie on the maximum margin hyperplanes in feature space

- Once the model is trained, a significant proportion of the data points can be discarded and only the support vectors retained.

- Having solved the quadratic programming problem and found a value for a,we can then determine the value of the threshold parameter b by noting that any support vector xn satisfies tny(xn)=1.

- Although we can solve this equation for b using an arbitrarily chosen support vector xn, a numerically more stable solution is obtained by first multiplying through by tn, making use of t2n =1, and then averaging these equations over all support vectors and solving for b to give

- For later comparison with alternative models, we can express the maximummargin classifier in terms of the minimization of an error function, with a simple quadratic regularizer

- Although the data set is not linearly separable in the two-dimensional data space x, it is linearly separable in the nonlinear feature space defined implicitly by the nonlinear kernel function. Thus the training data points are perfectly separated in the original data space.

- We therefore need a way to modify the support vector machine so as to allow some of the training points to be misclassified.

- box constraints

- ν-SVM

- chunking

- Introducing the slack variables allows points to lie outside the tube provided the slack variables are nonzero

- Again, this is a constrained maximization, and to find the constraints we note that an  0 and ̂an  0 are both required because these are Lagrange multipliers.

- The corresponding Karush-Kuhn-Tucker (KKT) conditions, which state that at the solution the product of the dual variables and the constraints must vanish, are given by

- From these we can obtain several useful results. First of all, we note that a coefficient an can only be nonzero if  + ξn + yn − tn =0, which implies that the data point either lies on the upper boundary of the -tube (ξn =0) or lies above the upper boundary (ξn > 0). Similarly, a nonzero value for ̂an implies  + ξ ̂n − yn + tn =0, and such points must lie either on or below the lower boundary of the -tube.

- Furthermore, the two constraints  + ξn + yn − tn =0and  + ξ ̂n − yn + tn =0 are incompatible, as is easily seen by adding them together and noting that ξn and ξ ̂n are nonnegative while  is strictly positive, and so for every data point xn, either an or ̂an (or both) must be zero.

- The parameter b can be found by considering a data point for which 0 <an < C, which from (7.67) must have ξn =0, and from (7.65) must therefore satisfy  + yn − tn =0.

- As with the classification case, there is an alternative formulation of the SVM for regression in which the parameter governing complexity has a more intuitive interpretation (Sch ̈ olkopf et al., 2000). In particular, instead of fixing the width  of the insensitive region, we fix instead a parameter ν that bounds the fraction of points lying outside the tube

- We could therefore proceed to formulate and solve complicated probabilistic models purely by algebraic manipulation. However, we shall find it highly advantageous to augment the analysis using diagrammatic representations of probability distributions, called probabilistic graphical models.

- To do this, we start with the lowest-numbered node and draw a sample from the distribution p(x1), which we call ̂x1. We then work through each of the nodes in order, so that for node n we draw a sample from the conditional distribution p(xn|pan) in which the parent variables have been set to their sampled values.

- The primary role of the latent variables is to allow a complicated distribution over the observed variables to be represented in terms of a model constructed from simpler (typically exponential family) conditional distributions.

- If we define a joint distribution over observed and latent variables, the corresponding distribution of the observed variables alone is obtained by marginalization. This allows relatively complex marginal distributions over observed variables to be expressed in terms of more tractable joint distributions over the expanded space of observed and latent variables.

- We first of all use the Gaussian mixture distribution to motivate the EM algorithm in a fairly informal way, and then we give a more careful treatment based on the latent variable viewpoint.

- Gaussian mixture models are widely used in data mining, pattern recognition, machine learning, and statistical analysis. In many applications, their parameters are determined by maximum likelihood, typically using the EM algorithm. However, as we shall see there are some significant limitations to the maximum likelihood approach, and in Chapter 10 we shall show that an elegant Bayesian treatment can be given using the framework of variational inference.

- We now turn to a formulation of Gaussian mixtures in terms of discrete latent variables.

- We can use the technique of ancestral sampling to generate random samples Section 8.1.2 distributed according to the [[Gaussian Mixture Model]].

- it is worth emphasizing that there is a significant problem associated with the maximum likelihood framework applied to Gaussian mixture models, due to the presence of singularities

- Thus the maximization of the log likelihood function is not a well posed problem because such singularities will always be present and will occur whenever one of the Gaussian components ‘collapses’ onto a specific data point.

- To understand the difference, note that if a single Gaussian collapses onto a data point it will contribute multiplicative factors to the likelihood function arising from the other data points and these factors will go to zero exponentially fast, giving an overall likelihood that goes to zero rather than infinity.

- However, once we have (at least) two components in the mixture, one of the components can have a finite variance and therefore assign finite probability to all of the data points while the other component can shrink onto one specific data point and thereby contribute an ever increasing additive value to the log likelihood. This is illustrated in Figure 9.7. These singularities provide another example of the severe over-fitting that can occur in a maximum likelihood approach. We shall see that this difficulty does not occur if we adopt a Bayesian approach

- For the moment, Section 10.1 however, we simply note that in applying maximum likelihood to Gaussian mixture models we must take steps to avoid finding such pathological solutions and instead seek local maxima of the likelihood function that are well behaved.

- Maximizing the log likelihood function (9.14) for a [[Gaussian Mixture Model]] turns out to be a more complex problem than for the case of a single Gaussian. The difficulty arises from the presence of the summation over k that appears inside the logarithm in (9.14), so that the logarithm function no longer acts directly on the Gaussian. If we set the derivatives of the log likelihood to zero, we will no longer obtain a closed form solution, as we shall see shortly.

- An elegant and powerful method for finding maximum likelihood solutions for models with latent variables is called the expectation-maximization algorithm, or EM algorithm (Dempster et al., 1977; McLachlan and Krishnan, 1997).

- We can interpret Nk as the effective number of points assigned to cluster k.

- It is worth emphasizing that the results (9.17), (9.19), and (9.22) do not constitute a closed-form solution for the parameters of the mixture model because the responsibilities γ(znk) depend on those parameters in a complex way through (9.13). However, these results do suggest a simple iterative scheme for finding a solution to the maximum likelihood problem, which as we shall see turns out to be an instance of the EM algorithm for the particular case of the [[Gaussian Mixture Model]].

- In the expectation step, or E step, we use the current values for the parameters to evaluate the posterior probabilities, or responsibilities, given by (9.13). We then use these probabilities in the maximization step, or M step, to re-estimate the means, covariances, and mixing coefficients using the results (9.17), (9.19), and (9.22).

- In practice, the algorithm is deemed to have converged when the change Section 9.4 in the log likelihood function, or alternatively in the parameters, falls below some threshold.

- It is therefore common to run the K-means algorithm in order to find a suitable initialization for a Gaussian mixture model that is subsequently adapted using EM.

- In this section, we present a complementary view of the EM algorithm that recognizes the key role played by latent variables. We discuss this approach first of all in an abstract setting, and then for illustration we consider once again the case of Gaussian mixtures.

- The goal of the EM algorithm is to find maximum likelihood solutions for models having latent variables.

- A key observation is that the summation over the latent variables appears inside the logarithm.

- The presence of the sum prevents the logarithm from acting directly on the joint distribution, resulting in complicated expressions for the maximum likelihood solution.

- Because we cannot use the complete-data log likelihood, we consider instead its expected value under the posterior distribution of the latent variable, which corresponds (as we shall see) to the E step of the EM algorithm.

- In the subsequent M step, we maximize this expectation.

- Note that in the definition of Q(θ, θold), the logarithm acts directly on the joint distribution p(X, Z|θ), and so the corresponding M-step maximization will, by supposition, be tractable.

- The EM algorithm can also be used to find MAP (maximum posterior) solutions for models in which a prior p(θ) is defined over the parameters. In this case the E Exercise 9.4 step remains the same as in the maximum likelihood case, whereas in the M step the quantity to be maximized is given by Q(θ, θold)+lnp(θ).

- Here we have considered the use of the EM algorithm to maximize a likelihood function when there are discrete latent variables

- In fact, we can derive the K-means algorithm as a particular limit of EM for Gaussian mixtures as follows.

- As a third example of the application of EM, we return to the evidence approximation for Bayesian linear regression.

- The expectation maximization algorithm, or EM algorithm, is a general technique for finding maximum likelihood solutions for probabilistic models having latent variables (Dempster et al., 1977; McLachlan and Krishnan, 1997).

- the value of ln p(X|θold) does not depend on q(Z) and so the largest value of L(q, θold) will occur when the Kullback-Leibler divergence vanishes, in other words when q(Z) is equal to the posterior distribution p(Z|X, θold).

- The increase in the log likelihood function is therefore greater than the increase in the lower bound

- Thus in the M step, the quantity that is being maximized is the expectation of the complete-data log likelihood

- stationary points of a function

- Library of Congress Control Number: 2006922522

- We therefore need a way to modify the support vector machine so as to allow some of the training points to be misclassified.

- box constraints.

- ν-SVM,

- chunking


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:41.281+08:00 %%
