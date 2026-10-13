- Bayesian optimization is a global optimization method for noisy black-box functions. 
- Applied to hyperparameter optimization, Bayesian optimization builds a probabilistic model of the function mapping from hyperparameter values to the objective evaluated on a validation set.
- **How does Bayesian optimization work?** By iteratively evaluating a promising hyperparameter configuration based on the current model, and then updating it, Bayesian optimization aims to gather observations revealing as much information as possible about this function and, in particular, the location of the optimum. It tries to balance exploration (hyperparameters for which the outcome is most uncertain) and exploitation (hyperparameters expected close to the optimum).
- **Bayesian optimization VS Grid Search/Random Search**In practice, [Bayesian optimization has been shown to obtain better results in fewer evaluations compared to grid search and random search](https://en.wikipedia.org/wiki/Hyperparameter_optimization), due to the ability to reason about the quality of experiments before they are run.
- **Advantage to computational cost.** Bayesian optimization is particularly advantageous for problems where $f(x)$ is difficult to evaluate due to its computational cost.
- **How Bayesian Optimization works**
	1. Select a sample by optimizing the acquisition function 
	2. Evaluate the sample with the objective function 
	3. Update the data, and the surrogate function 
	4. Repeat steps 1-3 until a good enough solution is found or maximum iterations is reached.
- **Surrogate function**
	- Technique used to best approximate the mapping of input examples to an output score.
	- In probability, it summarizes the conditional probability of an objective function $f(x)$ given the available data $D$
		- $$P(f|D) \approx P(D|f) \cdot P(f)$$
	- A number of techniques can be used for this, although the most popular is to treat the problem as a regression predictive modeling problem with the data representing the input and the score representing the output to the model. This is often best modeled using a random forest or a Gaussian Process.
- 
 

# Related 
- [[Hyperparameter Optimization]]
- [[kriging]]