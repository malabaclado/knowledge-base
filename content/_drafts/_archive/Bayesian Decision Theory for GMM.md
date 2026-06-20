# Bayesian Decision Theory for GMM
As a classifier that is based on Bayes decision theory, the GMM classifier uses several gaussian distributions to approach the true density of a class. It obtains class-conditional probability based on these gaussian distributions, and then computes posteriori probability.

How many gaussian distributions should be used for each class?

Assume there are $L_{i}$ candidate gaussian mixture models fro class $c_{i}$, denote these mixture models as $M_{il}$ where $l=1,2,...,L_{i}$ 

Each $M_{il}$ consists of parameters of the model $\theta_{il}$ and the number of Gaussian components $K_{il}$. $$p(x|c_{i}) = \sum_{k=1}^{K_{il}}p(x|\theta_{il}, k)$$

The best model, denoted $M_{ij}$, is the one that satisfies the condition: $$M_{ij} = \arg \max_{l}p(c_{i})\sum_{k=1}^{K_{il}}p(x|\theta_{il}, k)$$
Therefore, the selection of gaussian mixture model is significant for the GMM classifier, which includes the selection of $\theta_{il}$ and $K_{il}$. The parameter $\theta_{il}$ can be estimated using the EM algorithm.