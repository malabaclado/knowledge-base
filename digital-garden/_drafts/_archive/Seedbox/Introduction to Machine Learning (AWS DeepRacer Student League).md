---
tags:
alias:
creation-date: Sunday 5th March 2023
---

Backlink: [[AWS DeepRacer Student League]] 

# What is machine learning

## Common Applications of Machine Learning 
-   Recent advancements in industries such as autonomous vehicles.
-   Accurate and rapid translation of the text into hundreds of languages.
-   AI assistants you might find in your home.
-   Worker safety improvements.
-   Quicker pharmaceutical design and development.

## Notes 
- Terminologies
	- [[Artificial Intelligence]] - human-like machines, machines with human characteristics
	- [[Machine Learning]] - a type of AI, allows computers to learn patterns and make predictions 
		- ![](https://i.imgur.com/BzoAJXx.png)
	- Supervised Learning 
		- Every training sample from the dataset has a corresponding label or output value associated with it. As a result, the algorithm learns to predict labels or output values.
	- Unsupervised learning 
		- There are no labels for the training data. A machine learning algorithm tries to learn the underlying patterns or distributions that govern the data.
	- Reinforcement learning 
		- Like training a pet: leverages rewards and penalty system. 
		- The algorithm figures out which actions to take in a situation to maximize a reward (in the form of a number) on the way to reaching a specific goal.
- Traditional Problem Solving VS Machine Learning 
	- Traditional program: Hard coded, case-by-case basis, criteria-based
	- Machine learning: Model-based, model is trained on data. 
		- *The flexibility of the model is the key*
	- ![](https://i.imgur.com/Dxn6JAX.png)
- Every machine learning task involves **three primary components**
	1. a machine learning model - *a generic program*
		- a block of code/framework, used to a specific data
		- example: linear regression model 
	2. a model training algorithm - *fitting the model to the data* 
		- model training is an **interactive process**: 
			1. analyze what needs to be changed 
			2. make changes 
			3. repeat until satisfied
	3. a model inference algorithm - *use trained model to generate predictions* 
- *Machine learning can be analogous to making a teapot: You start with a unmolded clay (model), you mold it (train model) and then you place objects in it (model inference)*



# Five steps of machine learning 
- [Major steps in machine learning process](https://i.imgur.com/BWtXeev.png) 
	- Define the problem 
		- Steps to defining a task 
			1. Be very specific - make it a problem statement 
				- ❌ *How do I increase sales?*
				- ✔️ *Does adding a $1.00 charge for sprinkles on a hot fudge sundae increase the sales of hot fudge sundaes?*
			2. Identify the machine learning task: 
				- is it supervised? unsupervised? reinforcement learning? 
				- is your training data labeled or unlabeled?
				- is it a classification or regression task? 
	- Build the dataset 
		- Working with data seems to be the *most overlooked yet most important step* of the machine learning process.
		- ML practitioners spend around 80% of their time working with data (Forbes)
			- ![](https://i.imgur.com/u9jN7ux.png)
		- 4-step process in working with data
			1. data collection - gathering data relevant to your problem
				- involves running sql queries or web scraping
			2. data inspection - inspecting the integrity of the data 
				- checking for outliers 
				- checking for missing data 
				- transforming data to the type you need
			3. summary statistics - allows you to see trends in your data 
			4. data visualization  - allows you to communicate your findings to your stakeholders
	- Train the model 
		- **The first step to model training** is splitting the dataset into training and test set
		- What does a model training algorithm do?
			- A: It iteratively updates the [[Model parameters|model parameters]] to minimize some [[Loss Function|loss function]]. 
		- Guide questions 
			- How do I actually implement model training? (which model framework to use?)
			- How do I determine which model to use? (model selection)
			- Training algorithm hyperparameters 
	- Evaluate the model 
		- *How well does our model works?*
		- to evaluate models, we often use metrics (eg. accuracy)
		- Model evaluation (along with model training) is an iterative process. You repeat adjusting the model parameters until you are satisfied with the performance of the model.
	- Model inference
		- Use your model to solve real-world problems 
- How do we further classify tasks when we don't have a label? 
	- Unsupervised learning involves using data that doesn't have a label. One common task is called **clustering**. Clustering helps to determine if there are any naturally occurring groupings in the data.
		- Example: Identifying book genres
			- Imagine that you work for a company that recommends books to readers.  
			- The assumption is that you are fairly confident that micro-genres exist, and that there is one called _Teen Vampire Romance_. However, you don’t know which micro-genres exist specifically, so you can't use **supervised learning** techniques.
- Common machine learning framework 
	- Linear models 
		- One of the most common models covered in introductory coursework, linear models simply describe the relationship between a set of input numbers and a set of output numbers through a linear function
	- Tree-based models 
		-  They learn to categorize or regress by building an extremely large structure of nested _if/else_ blocks, splitting the world into different regions at each _if/else_ block. Training determines exactly where these splits happen and what value is assigned at each leaf region.
	- Deep learning models 
		- Extremely popular and powerful, deep learning is a modern approach that is based around a conceptual model of how the human brain functions. The model (also called a neural network) is composed of collections of neurons (very simple computational units) connected together by weights (mathematical representations of how much information thst is allowed to flow from one neuron to the next).
		- Noteworthy list of deep learning models 
			- Feed-Forward Neural Network (FFNN)
				- The most straightforward way of structuring a neural network, the Feed Forward Neural Network (FFNN) structures neurons in a series of layers, with each neuron in a layer containing _weights_ to all neurons in the previous layer.
			- Convolutional Neural Networks (CNN)
				- Convolutional Neural Networks (CNN) represent nested filters over grid-organized data. They are by far the most commonly used type of model when processing images.
			- Recurrent Neural Networks (RNN) / Long Short-Term Memory (LSTM) models 
				- Recurrent Neural Networks (RNN) and the related Long Short-Term Memory (LSTM) model types are structured to effectively represent for loops in traditional computing, collecting state while iterating over some object. They can be used for processing sequences of data.
			- Transformer 
				- A more modern replacement for RNN/LSTMs, the transformer architecture enables training over larger datasets involving sequences of data.
			- 
		- Machine learning python libraries
			- For classical models: sklearn
			- For deep learning: mxnet, tensorflow, pytorch
- Key takeaways
	1. _Solving problems using machine learning is an evolving and iterative process._
	2. _To solve a problem successfully in machine learning finding high quality data is essential._
	3. _To evaluate models, you often use statistical metrics. The metrics you choose are tailored to a specific use case._



# Examples of machine learning 
- Case study: Predicting a book's genre 
	- This is a unsupervised machine learning task 
	- The input data are words from the book, the output data is the book's genre 
	- Defining the problem 
		- We use unlabeled data -> unsupervised 
		- From the words in the book, we identify the genre based on commonalities -> clustering 
	- Buliding the dataset 
		- Data cleaning: Capitalization and verb tense dont matter so we remove capitals and converted all verbs to same tense (using a python library)
		- Data preprocessing: transform a book into *bag of words representation*
	- Model training 
		- Pick a model -> k-means clustering 
	- Model evaluation 
		- Using *silhouette coefficient*: Optimal value of k is 19.
	- Model inference 
		- You inspect the 19 clusters and you see a surprisingly large cluster of books. You infer that these cluster can be considered a genre of its own.
	- Key takeaways in this case study 
		- For some applications of machine learning, you need to not only clean and preprocess the data but also convert the data into a format that is machine readable. In this example, the words were converted into numbers through a process called data vectorization.
		- Solving problems in machine learning requires iteration. In this example you saw how it was necessary to train the model multiples times for different values of k. After training your model over multiple iterations you saw how the silhouette coefficient could be use to determine the optimal value for **k**.
		- During model inference you continued to inspect the clusters for accuracy to ensure that your model was generative useful predictions.
- Case study: Detecting spills
	- Imagine you run a company that offers specialized on-site janitorial services. One client - an industrial chemical plant - requires a fast response for spills and other health hazards. You realize if you could _automatically_ detect spills using the plant's surveillance system, you could mobilize your janitorial team faster.
	- Defining the problem
		- Input: Image (contain spill/does not contain spill) -> labeled data
		- Output: classify image if there is spill or not -> image classification. 
	- Building dataset 
		- Collect images that contain both spills and non-spills in multiple lighting conditions and environments. 
		- Data vectorization: transform image data to numerical format 
	- Model training 
		- Use model: Convlolutional neural network (CNN)
	- Model evaluation 
		- Use metric: precision and recall 
		- Accuracy might not be the best evaluation metric in this case 
			-  The model will see the _does not contain spill'_ class almost all the time, so any model that just predicts _no spill_ most of the time will seem pretty accurate.
	- Key takeaways 
		- **For some applications of machine learning, you need to use more complicated techniques to solve the problem.** While modern neural networks are a powerful tool, don’t forget their cost in terms of being easily explained.
		- **High quality data once again was very important to the success of this application**, to the point where even staging some fake data was required. Once again, the process of data vectorization was required so it was important to convert the images into numbers so that they could be used by the neural network.
		- **During model inference you continued to inspect the predictions for accuracy.** It is especially important in this case because you created some fake data to use when training your model.


# Further readings 
-  [Outlier detection on a real data set — scikit-learn 1.2.1 documentation](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html#sphx-glr-auto-examples-applications-plot-outlier-detection-wine-py)