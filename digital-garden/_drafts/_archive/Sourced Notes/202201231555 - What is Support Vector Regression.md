*Tags:* #topic/machine-learning #topic/machine-learning/regression #topic/convex-optimization #thesis #source 


# Source
[What is Support Vector Regression? | Analytics Steps](https://www.analyticssteps.com/blogs/what-support-vector-regression)
# Summary
## Understanding Regression

**Regression analysis** is a statistical procedure that is used to identify the degree and type of a connection between one dependent variable (typically *y*) and a set of other factors (known as independent variables). ^unqex7


The **goal** of regression is to reduce the sum of squared errors.

> [[Ordinary least squares]] (OLS) is a form of linear least squares approach used in statistics to estimate the unknown parameters in a linear regression model.

>  **Lasso, Ridge, and ElasticNet** are all OLS extensions with an extra penalty parameter that ==seeks to reduce the amount of features== utilised in the final model while minimising complexity. However, the purpose is to lower the error of the test set, as with many models.

Normal regression methods cannot determine the *optimum regression equation*. Support Vector Regression does this easily.

## What is a Support Vector Machine?
> The **goal of the support vector machine** method is to discover a hyperplane in an n-dimensional space, where n denotes the number of features or independent variables.

> A component of support vector machines is support vector regression. In other terms, it may be mentioned that there is a notion known as support vector machine, which can be used to analyse both regression and classification data.

> When the support vector machine is used for classification, it is referred to as support vector classification, and when it is used for regression, it is referred to as support vector regression.

> A **margin of tolerance (epsilon)** is supplied in the case of regression as an approximate estimate to the SVM that the issue would have already requested. Apart from that, there is a more challenging reason: the algorithm is more complex, thus it must be considered. However, the basic idea remains the same: to reduce error by customising the hyperplane to maximise the margin.

> The introduction of an insensitive zone around the function, known as the **$\varepsilon$-tube**, allows SVM to be generalised to SVR. The optimization problem is reformulated in this tube to discover the ~~tube~~ line that best approximates the continuous-valued function while balancing model complexity and prediction error.


> 	SVR is defined as an **optimization problem** by first constructing a convex-insensitive loss function to be reduced and then determining the flattest tube that includes the majority of the training cases. As a result, the **loss function** and the geometrical parameters of the tube are combined to form a multiobjective function.

> Then, using suitable numerical optimization methods, the **convex optimization**, which has a **unique solution**, is solved. Support vectors, which are training samples that fall outside the tube's perimeter, are used to represent the hyperplane. 

^2050f4

## Important Terms
- Kernel: A function that converts a low-dimensional data set to a higher-dimentional data set. This is useful for nonlinear data.
- Hyper-plane: This is the separating line between the data classes in SVM. Although, in SVR, we will describe it as a line that will assist us in predicting a continuous value or goal value.
- Boudary Line: Other than Hyper Plane, there are two lines in SVM that produce a margin. The support vectors might be within or outside the boundary lines. The two classes are separated by this line. 


> The premise is the same in SVR. A decision boundary line can be conceived of as a demarcation line (for simplicity), with positive examples on one side and negative examples on the other.

- Support Vectors: The data points closest to the border are listed here. The distance between the locations is little or negligible. Support vectors are locations that are outside the -tube in SVR. The smaller the value of, the more points outside the tube there are, and hence the more support vectors there are.

# Thoughts  & Comments
- Deep learning (like neural networks) demonstrate above-average performance than traditional [[Machine Learning]] methods (like, SVR). However, traditional ML methods may perceive things deep learning cannot. Good thing is that these models may be merged.

