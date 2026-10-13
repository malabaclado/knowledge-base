These are notes from ChatGPT. Only use this as inspiration/phrase bank on how to clearly communicate how support vector regression works.

Support Vector Regression is a powerful machine learning algorithm that combines the principles of support vector machines with regression analysis. By finding an optimal hyperplane in a high-dimensional space, SVR can accurately predict continuous numerical values. Its ability to handle non-linear relationships and its robustness against outliers make it a valuable tool in various domains, including finance, economics, and engineering.

SVR seeks to find a hyperplane that maximizes the margin, which is the distance between the hyperplane and the closest support vectors. By maximizing the margin, SVR promotes a robust and generalized model.

To define the hyperplane, SVR introduces two types of margins: the epsilon-insensitive loss function and the regularization parameter. The epsilon-insensitive loss function allows for a region of tolerance around the hyperplane, wherein errors within this region are considered acceptable. The regularization parameter balances the trade-off between achieving a smaller margin and minimizing training errors. This regularization term controls the complexity of the model and helps prevent overfitting.

The training process of SVR involves solving a quadratic optimization problem to determine the support vectors and the coefficients of the hyperplane. The solution seeks to minimize the sum of the errors within the epsilon-insensitive region, while also minimizing the magnitude of the coefficients. This optimization problem can be efficiently solved using techniques such as Sequential Minimal Optimization (SMO) or quadratic programming.

**Hard Margin SVR**
The hard-margin version of Support Vector Regression (SVR) is a variant of SVR that aims to find a hyperplane with a maximum margin that separates the training data points while minimizing the training errors. In this version, the SVR algorithm assumes that the data is linearly separable and does not allow any errors within the epsilon-insensitive region.

The key concept in the hard-margin SVR is the notion of a margin. The margin represents the distance between the hyperplane and the closest training data points. The goal is to find a hyperplane that maximizes this margin, thereby achieving the best separation between the data points.

It's important to note that the hard-margin version of SVR has limitations. It assumes that the data is perfectly separable, which may not always be the case in real-world scenarios. In the presence of noise or overlapping data, the hard-margin version may fail to find a feasible solution. To overcome this limitation, the soft-margin version of SVR was introduced, which allows for some errors within the epsilon-insensitive region.

# Soft Margin SVR
  
The soft-margin version of Support Vector Regression (SVR) is an extension of the hard-margin SVR that allows for some training errors within the epsilon-insensitive region. This version is more flexible and robust when dealing with datasets that are not perfectly separable or contain noise.

In soft-margin SVR, the key idea is to introduce a slack variable ξᵢ for each training data point, which represents the amount of error allowed for that particular data point. The objective is to find a hyperplane that still maximizes the margin but also minimizes the training errors, considering the trade-off between these two objectives.

where the first term 1/2 ||w||² represents the regularization term that controls the complexity of the model, and C is the regularization parameter that balances the trade-off between achieving a smaller margin and minimizing training errors. The second term C Σξᵢ penalizes the slack variables, and the value of C determines the penalty imposed for allowing errors.

Soft-margin SVR provides more flexibility compared to the hard-margin version by allowing for training errors within the epsilon-insensitive region. This flexibility enables the algorithm to handle datasets with overlapping data points or noise, leading to a more robust and generalized model. The choice of the regularization parameter C and the width of the epsilon parameter ε is crucial for controlling the balance between margin maximization and error tolerance in the model.


# Kernel Trick

The kernel trick is a fundamental concept in Support Vector Regression (SVR) that enables SVR to implicitly operate in a high-dimensional feature space without explicitly calculating the transformation. It is a computationally efficient technique that allows SVR to handle non-linear relationships between features and the target variable.

In SVR, the kernel trick is used to map the input data from the original feature space to a higher-dimensional space, where the data points may become linearly separable. This mapping is achieved through the use of a kernel function, which calculates the similarity or inner product between pairs of data points in the higher-dimensional space.

---
Consider a kernel function $\kappa(\mathrm{x}_{i}, \mathrm{x}_{j})$ where $\mathrm{x}_{i}, \mathrm{x}_{j}$ are input feature vectors, that satisfies

$$\kappa (\mathrm{x}_{i}, \mathrm{x}_{j}) = \langle \phi(\mathrm{x}_{i}), \phi(\mathrm{x}_{j}) \rangle$$The kernel function computes the inner product or similarity between the transformed feature vectors $\phi(\mathrm{x}_{i})$ and $\phi(\mathrm{x}_{j})$  in the higher-dimensional space, without explicitly calculating $\phi(\mathrm{x}_{i})$  and $\phi(\mathrm{x}_{j})$ . This avoids the computational cost of explicitly mapping the data to the higher-dimensional space, which may be computationally expensive or even infeasible for certain kernels.

---

Mathematically, let's consider a kernel function K(x, y), where x and y are the input feature vectors. The kernel function computes the inner product or similarity between the transformed feature vectors φ(x) and φ(y) in the higher-dimensional space, without explicitly calculating φ(x) and φ(y). This avoids the computational cost of explicitly mapping the data to the higher-dimensional space, which may be computationally expensive or even infeasible for certain kernels.

The kernel function satisfies the Mercer's condition, ensuring that it represents a valid dot product in the higher-dimensional space. Commonly used kernel functions in SVR include the linear kernel, polynomial kernel, Gaussian (RBF) kernel. Each kernel function has its own properties and characteristics, making it suitable for different types of data and non-linear relationships.

By applying the kernel trick, SVR can leverage the advantages of the high-dimensional feature space to capture complex patterns and non-linear relationships between features and the target variable. In the transformed space, SVR can find a linear hyperplane that separates the data points or approximates the non-linear relationships more effectively than in the original feature space.

The kernel trick is particularly useful in SVR because it allows for efficient and scalable computations. Instead of explicitly transforming the data, the kernel function efficiently computes the pairwise similarity between data points, significantly reducing the computational complexity. This enables SVR to handle large datasets and complex problems with high-dimensional feature spaces.

To summarize, the kernel trick is a powerful technique in SVR that enables the algorithm to implicitly operate in a high-dimensional feature space without explicitly calculating the transformation. By leveraging kernel functions, SVR can efficiently handle non-linear relationships between features and the target variable, leading to more accurate and flexible predictions.


# Different Kernel Functions
## Linear Kernel 
$\kappa(\mathrm{x}_{i}, \mathrm{x}_{j}) = \langle \mathrm{x}_{i}, \mathrm{x}_{j} \rangle$

1. Linear Kernel: K(x, y) = x·y

The linear kernel represents a linear similarity measure between the input feature vectors x and y. It is the simplest kernel and is effective when the relationship between features and the target variable is approximately linear. The linear kernel corresponds to using a linear hyperplane in the original feature space for SVR.

## Polynomial Kernel
$\kappa(\mathrm{x}_{i}, \mathrm{x}_{j}) = (a\cdot \langle \mathrm{x}_{i}, \mathrm{x}_{j} \rangle + c)^d$

2. Polynomial Kernel: K(x, y) = (αx·y + c)^d

The polynomial kernel computes the similarity between feature vectors x and y by raising the dot product αx·y plus a constant c to a power d. Here, α is a user-defined scaling factor, c is an additional constant, and d is the degree of the polynomial. The polynomial kernel captures non-linear relationships and can model curved decision boundaries in the transformed feature space.

# RBF Kernel
3. Gaussian (RBF) Kernel: K(x, y) = exp(-γ ||x - y||²)

$\kappa(\mathrm{x}_{i}, \mathrm{x}_{j}) = \exp\left( -\frac{||\mathrm{x}_{i} - \mathrm{x}_{j}||^2}{\sigma^2} \right)$



The Gaussian kernel, also known as the Radial Basis Function (RBF) kernel, calculates the similarity between feature vectors x and y based on the Euclidean distance ||x - y||² scaled by a parameter γ. The parameter γ controls the width of the Gaussian function and influences the smoothness of the decision boundary. The Gaussian kernel captures complex non-linear relationships and can effectively model intricate decision boundaries.

Now, let's discuss how these kernels work:

The linear kernel simply calculates the dot product between feature vectors x and y, measuring their similarity. It assumes a linear relationship between features and the target variable. The linear kernel is useful when the data is approximately linearly separable.

The polynomial kernel introduces non-linearity by raising the dot product between x and y to a certain power d. It captures higher-order interactions and can model curved decision boundaries in the transformed space. The choice of the degree d controls the complexity of the polynomial function.

The Gaussian (RBF) kernel measures the similarity between feature vectors based on the Euclidean distance between them, scaled by the parameter γ. It assigns higher similarity to nearby points and gradually decreases the similarity as the distance increases. The Gaussian kernel can handle complex non-linear relationships and is effective in capturing intricate decision boundaries.

In practice, the choice of the kernel depends on the specific problem and the nature of the data. The linear kernel is often a good starting point for linearly separable data, while the polynomial and Gaussian kernels are suitable for capturing non-linear relationships. The parameters associated with each kernel, such as the degree in the polynomial kernel or γ in the Gaussian kernel, need to be carefully tuned to achieve optimal performance and generalization in SVR.

---
See also: [[Thesis Scratchpad]]