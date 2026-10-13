---
tags: topic/machine-learning, datacamp, molecule, course
alias: null
creation-date: Friday 5th August 2022
last-modified-date: Friday 5th August 2022 13:27:39
---

# Machine Learning for Everyone
## AI and Machine Learning
- Artificial Intelligence is a set if tools for making computers behave intelligently. 
- Machine learning is the most prevalent subset of Artficial Intelligence 
- Machine learning model - is a statistical representation of a real-world process based on data. 

![[Pasted image 20220805133243.png]]


There are three types of machine learning: 
1. [[Reinforcement Learning]] 
2. [[Supervised Learning]] 
3. [[Unsupervised Learning]] 

> The magic of machine learning is we can analyze multiple features at once.

**Machine Learning Workflow** 
- Step 1: Extract features
- Step 2: Split to train-test data
- Step 3: Train the model
- Step 4: Evaluate the model 

---

## Machine Learning

![[Pasted image 20220805134847.png]]

**Supervised learning** 
- Classification 
	- Support vector machine - linear classifier 
	- Support vector machine - polynomial classifier 
- Regression 
	- Linear regression 

**Unsupervised learning** 
- Clustering 
	- K-Means algorithm (requires knowing how many clusters)
	- DBSCAN 
- Association (finding relationships)
- Anomaly detection (this is all about detecting outliers)
	- Use-cases 
		- Discover devices that fail faster or last longer 
		- Discover fraudsters 
		- Discover patients that resist a fatal disease 

**Model Evaluation**
- Evaluating Classification Performance
	- Overfitting
		- The first thing to look for when evaluating is overfiting 
		- ![[Pasted image 20220805135813.png]]
	- Accuracy
		- To measure model performance, use accuracy. 
		- Accuracy isn't always the best metric
	- Confusion matrix 
		- This is a better metric than accuracy
		- Sensitivity
			- ![[Pasted image 20220805180614.png]]
		- Specificity
			- ![[Pasted image 20220805180628.png]]
- Evaluating Regression Performance 
	- Regressors are evaluated by calculating errors from the original target data. 
	- Example of this is the mean-squared-error
- Evaluating Unsupervised Learning
	- Since there is nothing to compare to, we evaluate an unspervised learning model's preformance based on our hypothesis. 

**Improving Performance**
- Dimensionality reduction 
	- Reducing features. 
	- We remove features that are: 
		- Irrelevant 
		- Highly correlated
- Hyperparameter tuning 
	- Adjusting the parameters of the model
- Ensemble methods
	- Using different models


---
## Deep Learning 
- These are also known as neural networks.
- Can solve more complex problems but requires more data.
- Best when inputs are images and text
- ![[Pasted image 20220805182220.png|400]]
> Deep learning is especially useful in computer vision and natural language processing. 


![[Pasted image 20220805183212.png]]

**Limits of Machine Learning**
1. Data Quality 
	- Bad data makes a bad model 
	- ![[Pasted image 20220805183521.png|400]]
	- ![[Pasted image 20220805183706.png]]
	- ![[Pasted image 20220805183738.png]]
2. Explainability 
	- Often machine learning models are considered black boxes. 
	- ![[Pasted image 20220805183848.png]]
	- 