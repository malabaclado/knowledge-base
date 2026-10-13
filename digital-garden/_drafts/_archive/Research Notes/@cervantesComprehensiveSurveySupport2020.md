---
tags: type/research-note 
alias: [A comprehensive survey on support vector machine classification: Applications, challenges and trends]
---
# A comprehensive survey on support vector machine classification: Applications, challenges and trends

> [!info]
> - **Cite Key:** [[@cervantesComprehensiveSurveySupport2020]]
> - **Abstract:** In recent years, an enormous amount of research has been carried out on support vector machines (SVMs) and their application in several fields of science. SVMs are one of the most powerful and robust classification and regression algorithms in multiple fields of application. The SVM has been playing a significant role in pattern recognition which is an extensively popular and active research area among the researchers. Research in some fields where SVMs do not perform well has spurred development of other applications such as SVM for large data sets, SVM for multi classification and SVM for unbalanced data sets. Further, SVM has been integrated with other advanced methods such as evolve algorithms, to enhance the ability of classification and optimize parameters. SVM algorithms have gained recognition in research and applications in several scientific and engineering areas. This paper provides a brief introduction of SVMs, describes many applications and summarizes challenges and trends. Furthermore, limitations of SVMs will be identified. The future of SVMs will be discussed in conjunction with further applications. The applications of SVMs will be reviewed as well, especially in the some fields.
> - **Bibliography:** Cervantes, J., Garcia-Lamont, F., Rodríguez-Mazahua, L., & Lopez, A. (2020). A comprehensive survey on support vector machine classification: Applications, challenges and trends. _Neurocomputing_, _408_, 189–215. [https://doi.org/10.1016/j.neucom.2019.10.118](https://doi.org/10.1016/j.neucom.2019.10.118)
> - **Tags:** #Machine-learning, #Classification, #SVM



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- evolve algorithms

- There are many good classification techniques in the literature including k-nearest-neighbor classifier [2,3], Bayesian networks [4,5], artificial neural networks [6–10], decision trees [11,12] and SVM [13–15].

- A notable advantage of SVMs lies in the fact that they obtain a subset of support vectors during the learning phase, which is often only a small part of the original data set. This set of support vectors represents a given classification task and is formed by a small data set.

- The principal objective in pattern classification is to get a model which maximizes the performance for the training data. Conventional training methods determine the models in such a way that each input–output pair is correctly classified within the class to which it belongs.

- The main motivation of SVM is to separate several classes in the training set with a surface that maximizes the margin between them. In other words, SVM allows to maximizing the generalization ability of a model. This is the objective of the Structural Risk Minimization principle (SRM) that allows the minimization of a bound on the generalization error of a model, instead of minimizing the mean squared error on the set of training data, which is the philosophy often used by the methods of empirical risk minimization.

- The generalization ability is maximized if the optimal separation hyperplane is selected as the separation hyperplane.

- Karush-Kuhn-Tucker conditions (KKT) [31,32] play a very important role in the theory of optimization, because they give the conditions to obtain an optimal solution to a general optimization problem

- Definition 1. (Dimension Vapnik–Chervonenkis -VC-) The VC dimension describes the capacity of a set of functions implemented in a learning machine. For binary classification, h is the maximum number of points in which two classes can be separated in all the 2h possible ways using the functions of the learning machine.

- We checked the type of kernel used in some real-world applications. Table 1 shows a summary of the four main kernels found. In some papers, more than one kernel was applied, in these cases we consider the kernel that produces the better results. Without a doubt, Gaussian RBF function is the most commonly used in many different type of applications.

- some authors such as [34] have performed tests to identify the performance of SVM with different kernels, reaching the general conclusion that the polynomial and the Gaussian RBF function are the best option for acoustic signals.

- On the other hand, Kasnavi et al. [35] found that Gaussian RBF and hyperbolic tangent are the best for genome wide prediction

- Hasan concludes that Laplace kernel is the ideal one for intrusion detection.

- The observation in which all the authors agree, is that the selection of the kernel should be based on the characteristics of data, and that to obtain good results it is necessary to determine the optimal parameters of the kernel used.

- Mercer’s theorem [60,13] determines the conditions of functions to be kernels.

- The approach presented above can be easily extended to create non-linear decision functions. The reason for this extension is that an SVM can create a non-linear hyper surface of decision, capable of classifying non-linearly separable data. Generally, for n dimensional input patterns, instead of a non-linear curve, an SVM will create a non-linear separation hyper-surface

- Despite the generalization capacity and many advantages of the SVM, they have some very marked weaknesses, among which are: the selection of parameters, algorithmic complexity that affects the training time of the classifier in large data sets, development of optimal classifiers for multi-class problems and the performance of SVMs in unbalanced data sets

- Maybe the principal disadvantage of SVM is due to its excessive computational cost in large data sets, because the training kernel matrix grows in quadratic form with the size of the data set, which provokes that training of SVM on large data sets is a very slow process.

- According to the strategy used, the training methods for SVM can be categorized into data selection, decomposition, geometric, parallel implementations and heuristics. Their core ideas and the most representative algorithms are presented in this section.

- Simple random sampling (SRS) is probably the most basic strategy to reduce the size of training sets. It consists in choosing a number of instances and then training a SVM with them. The works presented in [64–66] show that uniform random sampling is the optimal robust selection scheme in terms of several statistical criteria. However, although SRS is computationally cheap, the standard deviation of classification accuracy is large in most cases

- Most of the current distance-based methods are inspired on two observations: (1) the instances closest to those ones with opposite label have high chances to be SVs [72] and (2) instances far from hyperplane do not contribute to the definition of the decision boundary [74].A problem with naive implementations that require to compute all distances between objects is that this task has a temporal and a spatial complexity of Oðn2Þ.

- The Condensed Nearest Neighbor (CNN) [75] chooses instances near to class frontiers, reducing the size of training sets. However, CNN is not noise tolerant. Reduced Nearest Neighbor (RNN) [76], Selective Nearest Neighbor (SNN) [77] and Minimal Consistent Set (MCS) are methods based on CNN, and therefore, they have also problems with noisy data sets. RNN, SNN and MCS are more costly than CNN.

- Clustering has been proved to be an effective method to collaborate with SVM on classifying large data sets. For example, hierarchical clustering [81,82], k-means [83] and parallel clustering [84]. Clustering-based methods can reduce the computations burden of SVM, however, the clustering algorithms themselves are still complicated for large data set.

- Apart of the proved convergence [88], a clear advantage of decomposition is that memory requirement is linear in the number of training examples

- equential minimal optimization (SMO) is a fast method to train SVM [91,84]. Training SVM requires the solution of the QP optimization problem. SMO breaks this large QP problem into a series of smallest possible QP problems. It considers the smallest size working set: only two training samples, and it is faster than the projected conjugate gradient (PCG) chunking algorithm.

- Dong et al. [61] introduced a parallel optimization step where block diagonal matrices are used to approximate the original kernel matrix so that SVM classification can be split into hundreds of sub-problems. A recursive and computational superior mechanism referred as adaptive recursive partitioning was proposed in [92], where the data are recursively subdivided into smaller subsets.

- The SVMlight [97] is another important state-ofthe-art decomposition method.

- Geometric methods for SVM are based on that computing the optimal separating hyperplane is equivalent to find the closest pair of points belonging to convex hulls [63,109,110].

- Among all heuristic methods, the alpha seeding [116] consists of providing initial estimates of the ai values for the starting of the QP problem. Alpha seeding seems to be a practical method to improve training time of SVM. Recently, an improvement of this method has been proposed in [117].

- Classification for imbalanced data sets has been studied by machine learning community since the last decade

- There are many methods that are applied to imbalanced data sets in order to improve the performance of classifiers [135]. Generally, these methods are divided into two categories: external methods and internal methods.

- External methods involve a pre processing of training data sets in order to make them balanced. Internal methods deal with modifications of the learning algorithms in order to reduce their sensitiveness to class imbalance. In other words, external methods attempt to balance the data sets by considering the number of examples for each class, whereas internal methods consider the costs associated with misclassification and include these costs in the model.

- The under sampling and over sampling method [146] balances the data sets by randomly selecting small number of objects from majority class, and doubling the objects in the minority class. The main drawback is that some important points, such as support vectors, may be neglected by the random algorithm.

- The synthetic minority over sampling technique [140] generates artificial data in the minority class by multiplying a random number in each original object. [152] showed that SMOTE is better than under sampling and over sampling.

- Although sampling methods and cost-sensitive learning methods seem to dominate the current research efforts in imbalanced learning, Genetic Algorithm (GA)-based approaches have also been pursued by the community. These algorithms use GAs in order to balanced data sets


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:42.218+08:00 %%
