---
tags: type/research-note 
alias: [Python machine learning: machine learning and deep learning with Python, scikit-learn, and TensorFlow]
---
# Python machine learning: machine learning and deep learning with Python, scikit-learn, and TensorFlow

> [!info]
> - **Cite Key:** [[@raschkaPythonMachineLearning04]]
> - **Bibliography:** Raschka, S., & Mirjalili, V. (04). _Python machine learning: Machine learning and deep learning with Python, scikit-learn, and TensorFlow_ (Second edition, fourth release,[fully revised and updated]). Packt Publishing.



## Highlights
%% begin annotations %%


### Imported: 2023-02-27 8:32 pm


- In my opinion, machine learning, the application and science of algorithms that make sense of data, is the most exciting field of all the computer sciences! We are living in an age where data comes in abundance; using self-learning algorithms from the field of machine learning, we can turn this data into knowledge.

- In the second half of the twentieth century, machine learning evolved as a subfield of Artificial Intelligence (AI) that involved self-learning algorithms that derived knowledge from data in order to make predictions.

- Thanks to machine learning, we enjoy robust email spam filters, convenient text and voice recognition software, reliable web search engines, challenging chess-playing programs, and, hopefully soon, safe and efficient self-driving cars.

- three types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.

- The main goal in supervised learning is to learn a model from labeled training data that allows us to make predictions about unseen or future data.

- A supervised learning task with discrete class labels, such as in the previous email spam filtering example, is also called a classification task. Another subcategory of supervised learning is regression, where the outcome signal is a continuous value:

- Classification is a subcategory of supervised learning where the goal is to predict the categorical class labels of new instances, based on past observations.

- A second type of supervised learning is the prediction of continuous outcomes, which is also called regression analysis.

- In reinforcement learning, the goal is to develop a system (agent) that improves its performance based on interactions with the environment.

- There are many different subtypes of reinforcement learning. However, a general scheme is that the agent in reinforcement learning tries to maximize the reward by a series of interactions with the environment. Each state can be associated with a positive or negative reward, and a reward can be defined as accomplishing an overall goal, such as winning or losing a game of chess.

- In unsupervised learning, however, we are dealing with unlabeled data or data of unknown structure. Using unsupervised learning techniques, we are able to explore the structure of our data to extract meaningful information without the guidance of a known outcome variable or reward function.

- Clustering is an exploratory data analysis technique that allows us to organize a pile of information into meaningful subgroups (clusters) without having any prior knowledge of their group memberships.

- clustering is also sometimes called unsupervised classification

- McCullock and Pitts described such a nerve cell as a simple logic gate with binary outputs; multiple signals arrive at the dendrites, are then integrated into the cell body, and, if the accumulated signal exceeds a certain threshold, an output signal is generated that will be passed on by the axon.

- Only a few years later, Frank Rosenblatt published the first concept of the perceptron learning rule based on the MCP neuron model (The Perceptron: A Perceiving and Recognizing Automaton, F. Rosenblatt, Cornell Aeronautical Laboratory, 1957). With his perceptron rule, Rosenblatt proposed an algorithm that would automatically learn the optimal weight coefficients that are then multiplied with the input features in order to make the decision of whether a neuron fires or not.

- If we notice that a model performs much better on a training dataset than on the test dataset, this observation is a strong indicator of overfitting.

- L2 regularization adds a penalty term to the cost function that effectively results in less extreme weight values compared to a model trained with an unregularized cost function.

- To summarize the main message of the example, our goal is to minimize the sum of the unpenalized cost plus the penalty term, which can be understood as adding bias and preferring a simpler model to reduce the variance in the absence of sufficient training data to fit the model.

- Another useful approach to select relevant features from a dataset is to use a random forest, an ensemble technique that we introduced in Chapter 3, A Tour of Machine Learning Classifiers Using scikit-learn. Using a random forest, we can measure the feature importance as the averaged impurity decrease computed from all decision trees in the forest, without making any assumptions about whether our data is linearly separable or not.

- feature selection techniques.

- In this chapter, you will learn about three fundamental techniques that will help us to summarize the information content of a dataset by transforming it onto a new feature subspace of lower dimensionality than the original one.

- In this section, you will learn about an extremely handy tool, the Pipeline class in scikitlearn. It allows us to fit a model including an arbitrary number of transformation steps and apply it to make predictions about new data.

- One of the key steps in building a machine learning model is to estimate its performance on data that the model hasn't seen before.

- A classic and popular approach for estimating the generalization performance of machine learning models is holdout cross-validation. Using the holdout method, we split our initial dataset into a separate training and test dataset—the former is used for model training, and the latter is used to estimate its generalization performance.

- A better way of using the holdout method for model selection is to separate the data into three parts: a training set, a validation set, and a test set. The training set is used to fit the different models, and the performance on the validation set is then used for the model selection.

- A disadvantage of the holdout method is that the performance estimate may be very sensitive to how we partition the training set into the training and validation subsets; the estimate will vary for different samples of the data.

- In k-fold cross-validation, we randomly split the training dataset into k folds without replacement, where k — 1 folds are used for the model training, and one fold is used for performance evaluation.

- A good standard value for k in k-fold cross-validation is 10, as empirical evidence shows. For instance, experiments by Ron Kohavi on various real-world datasets suggest that 10-fold cross-validation offers the best trade-off between bias and variance

- In the second half of the twentieth century, machine learning evolved as a subfeld of Artifcial Intelligence (AI) that involved self-learning algorithms that derived knowledge from data in order to make predictions. I

- Thanks to machine learning, we enjoy robust email spam flters, convenient text and voice recognition software, reliable web search engines, challenging chess-playing programs, and, hopefully soon, safe and effcient self-driving cars.

- three types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.

- The main goal in supervised learning is to learn a model from labeled training data that allows us to make predictions about unseen or future data.

- A supervised learning task with discrete class labels, such as in the previous email spam fltering example, is also called a classifcation task. Another subcategory of supervised learning is regression, where the outcome signal is a continuous value:

- Classifcation is a subcategory of supervised learning where the goal is to predict the categorical class labels of new instances, based on past observations.

- A second type of supervised learning is the prediction of continuous outcomes, which is also called regression analysis.

- In reinforcement learning, the goal is to develop a system (agent) that improves its performance based on interactions with the environment.

- There are many different subtypes of reinforcement learning. However, a general scheme is that the agent in reinforcement learning tries to maximize the reward by a series of interactions with the environment. Each state can be associated with a positive or negative reward, and a reward can be defned as accomplishing an overall goal, such as winning or losing a game of chess.

- In unsupervised learning, however, we are dealing with unlabeled data or data of unknown structure. Using unsupervised learning techniques, we are able to explore the structure of our data to extract meaningful information without the guidance of a known outcome variable or reward function.

- Clustering is an exploratory data analysis technique that allows us to organize a pile of information into meaningful subgroups (clusters) without having any prior knowledge of their group memberships.

- clustering is also sometimes called unsupervised classifcation

- McCullock and Pitts described such a nerve cell as a simple logic gate with binary outputs; multiple signals arrive at the dendrites, are then integrated into the cell body, and, if the accumulated signal exceeds a certain threshold, an output signal is generated that will be passed on by the axon.

- Only a few years later, Frank Rosenblatt published the frst concept of the perceptron learning rule based on the MCP neuron model (The Perceptron: A Perceiving and Recognizing Automaton, F. Rosenblatt, Cornell Aeronautical Laboratory, 1957). With his perceptron rule, Rosenblatt proposed an algorithm that would automatically learn the optimal weight coeffcients that are then multiplied with the input features in order to make the decision of whether a neuron fres or not.

- If we notice that a model performs much better on a training dataset than on the test dataset, this observation is a strong indicator of overftting.

- L2 regularization adds a penalty term to the cost function that effectively results in less extreme weight values compared to a model trained with an unregularized cost function.

- To summarize the main message of the example, our goal is to minimize the sum of the unpenalized cost plus the penalty term, which can be understood as adding bias and preferring a simpler model to reduce the variance in the absence of suffcient training data to ft the model.

- Another useful approach to select relevant features from a dataset is to use a random forest, an ensemble technique that we introduced in Chapter 3, A Tour of Machine Learning Classifers Using scikit-learn. Using a random forest, we can measure the feature importance as the averaged impurity decrease computed from all decision trees in the forest, without making any assumptions about whether our data is linearly separable or not.

- feature selection techniques.

- In this chapter, you will learn about three fundamental techniques that will help us to summarize the information content of a dataset by transforming it onto a new feature subspace of lower dimensionality than the original one. D

- In this section, you will learn about an extremely handy tool, the Pipeline class in scikitlearn. It allows us to ft a model including an arbitrary number of transformation steps and apply it to make predictions about new data.

- One of the key steps in building a machine learning model is to estimate its performance on data that the model hasn't seen before.

- A classic and popular approach for estimating the generalization performance of machine learning models is holdout cross-validation. Using the holdout method, we split our initial dataset into a separate training and test dataset—the former is used for model training, and the latter is used to estimate its generalization performance.

- A better way of using the holdout method for model selection is to separate the data into three parts: a training set, a validation set, and a test set. The training set is used to ft the different models, and the performance on the validation set is then used for the model selection.

- A disadvantage of the holdout method is that the performance estimate may be very sensitive to how we partition the training set into the training and validation subsets; the estimate will vary for different samples of the data. I

- In k-fold cross-validation, we randomly split the training dataset into k folds without replacement, where k — 1 folds are used for the model training, and one fold is used for performance evaluation. T

- A good standard value for k in k-fold cross-validation is 10, as empirical evidence shows. For instance, experiments by Ron Kohavi on various real-world datasets suggest that 10-fold cross-validation offers the best trade-off between bias and variance (


%% end annotations %%

## Notes 
%% begin notes %%%% end notes %%


%% Import Date: 2023-02-27T20:33:45.859+08:00 %%
