---
tags: #note
alias:
creation-date: Wednesday 23rd February 2022
last-modified-date: Wednesday 23rd February 2022 19:52:41
---
⬅️ 

# Machine learning - Trends, perspectives, and prospects (Jordan and Mitchell, 2015)
#topic/machine-learning 


# Extracted Annotations (2022-01-11)

> "**Machine learning addresses the question of how to build computers that improve automatically through experience.** It is one of today's most rapidly growing technical fields, lying at the intersection of computer science and statistics, and at the core of artificial intelligence and data science." ([Jordan and Mitchell 2015:1](zotero://open-pdf/library/items/IARDFMK4?page=1))
<!--ID: 1645617152394-->


> "Within artificial intelligence (AI), machine learning has emerged as the method of choice for developing practical software for **computer vision**, **speech recognition**, **natural language processing**, **robot control**, and **other applications**. Many developers of AI systems now recognize that, for many applications, it can be far easier to train a system by showing it examples of desired input-output behavior than to program it manually by anticipating the desired response for all possible inputs." ([Jordan and Mitchell 2015:1](zotero://open-pdf/library/items/IARDFMK4?page=1)) 

> "The effect of machine learning has also been felt broadly across computer science and across a range of industries concerned with data-intensive issues, such as consumer services, the diagnosis of faults in complex systems, and the control of logistics chains. There has been a similarly broad range of effects across empirical sciences, from biology to cosmology to social science, as machine-learning methods have been developed to analyze highthroughput experimental data in novel ways." ([Jordan and Mitchell 2015:1](zotero://open-pdf/library/items/IARDFMK4?page=1))

> "Conceptually, machine-learning algorithms can be viewed as searching through a large space of candidate programs, guided by training experience, to find a program that optimizes the performance metric." ([Jordan and Mitchell 2015:1](zotero://open-pdf/library/items/IARDFMK4?page=1))

> "Machine-learning algorithms vary greatly, in part by the way in which they represent candidate programs (e.g., decision trees, mathematical functions, and general programming languages) and in part by the way in which they search through this space of programs (e.g., optimization algorithms with well-understood convergence guarantees and evolutionary search methods that evaluate successive generations of randomly mutated programs). Here, we focus on approaches that have been particularly successful to date." ([Jordan and Mitchell 2015:1](zotero://open-pdf/library/items/IARDFMK4?page=1))

> "Whatever the learning algorithm, **a key scientific and practical goal is to theoretically characterize the capabilities of specific learning algorithms and the inherent difficulty of any given learning problem**: How accurately can the algorithm learn from a particular type and volume of training data? How robust is the algorithm to errors in its modeling assumptions or to errors in the training data? Given a learning problem with a given volume of training data, is it possible to design a successful algorithm or is this learning problem fundamentally intractable? Such theoretical characterizations of machine-learning algorithms and problems typically make use of the familiar frameworks of statistical decision theory and computational complexity theory." ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))

> "A specific form of computational analysis that has proved particularly useful in recent years has been that of **optimization theory**, with upper and lower bounds on rates of convergence of optimization procedures merging well with the formulation of machine-learning problems as the optimization of a performance metric" ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))

> "As a field of study, **machine learning sits at the crossroads of computer science, statistics and a variety of other disciplines** concerned with automatic improvement over time, and inference and decision-making under uncertainty." ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))

> "Related disciplines include the psychological study of human learning, the study of evolution, adaptive control theory, the study of educational practices, neuroscience, organizational behavior, and economics." ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))

#### Drivers of machine-learning progress
##### Big Data

> "The past decade has seen rapid growth in the ability of networked and mobile computing systems to gather and transport vast amounts of data, a phenomenon often referred to as " Big Data. "" ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))
<!--ID: 1645617152400-->


> "The scientists and engineers who collect such data have often turned to machine learning for solutions to the problem of obtaining useful insights, predictions, and decisions from such data sets." ([Jordan and Mitchell 2015:2](zotero://open-pdf/library/items/IARDFMK4?page=2))

##### Mobile Devices and Embedded Computers

> "Mobile devices and embedded computing permit large amounts of data to be gathered about individual humans, and machine-learning algorithms can learn from these data to customize their services to the needs and circumstances of each individual. Moreover, these personalized services can be connected, so that an overall service emerges that takes advantage of the wealth and diversity of data from many individuals while still customizing to the needs and circumstances of each." ([Jordan and Mitchell 2015:3](zotero://open-pdf/library/items/IARDFMK4?page=3))
<!--ID: 1645617152407-->


> "We appear to be at the beginning of a decades-long trend toward increasingly data-intensive, evidence-based decisionmaking across many aspects of science, commerce, and government." ([Jordan and Mitchell 2015:3](zotero://open-pdf/library/items/IARDFMK4?page=3))

> "With the increasing prominence of large-scale data in all areas of human endeavor has come a wave of new demands on the underlying machine learning algorithms. For example, huge data sets require computationally tractable algorithms, highly personal data raise the need for algorithms that minimize privacy effects, and the availability of huge quantities of unlabeled data raises the challenge of designing learning algorithms to take advantage of it." ([Jordan and Mitchell 2015:3](zotero://open-pdf/library/items/IARDFMK4?page=3))

#### Core methods and recent progress
##### Supervised Learning Methods

> "**Supervised learning systems**, including spam classifiers of e-mail, face recognizers over images, and medical diagnosis systems for patients, all exemplify the **function approximation problem** discussed earlier, where the training data take the form of a collection of (x,y) pairs and the goal is to produce a prediction y* in response to a query x*. The inputs x may be classical vectors or they may be more complex objects such as documents, images, DNA sequences, or graphs. Similarly, many different kinds of output y have been studied. Much progress has been made by focusing on the simple **binary classification problem** in which y takes on one of two values (for example, " spam " or " not spam " ), but there has also been abundant research on problems such as **multiclass classification** (where y takes on one of K labels), **multilabel classification** (where y is labeled simultaneously by several of the K labels), **ranking problems** (where y provides a partial order on some set), and **general structured prediction problems** (where y is a combinatorial object such as a graph, whose components may be required to satisfy some set of constraints)." ([Jordan and Mitchell 2015:3](zotero://open-pdf/library/items/IARDFMK4?page=3))
<!--ID: 1645617152414-->


> "One high-impact area of progress in supervised learning in recent years involves **deep networks**, which are _multilayer networks of threshold units_, each of which computes some simple parameterized function of its inputs ( 9 , 10 ). Deep learning systems make use of **gradient-based optimization algorithms** to adjust parameters throughout such a multilayered network based on errors at its output." ([Jordan and Mitchell 2015:3](zotero://open-pdf/library/items/IARDFMK4?page=3))

> "The **internal layers of deep networks** can be viewed as providing learned representations of the input data. While much of the practical success in deep learning has come from supervised learning methods for discovering such representations, efforts have also been made to develop deep learning algorithms that discover useful representations of the input without the need for labeled training data ( 13 ). The general problem is referred to as **unsupervised learning**, a second paradigm in machine-learning research ( 2 )." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))

##### Unsupervised Learning Methods

> "Broadly,** unsupervised learning** generally involves the analysis of unlabeled data under assumptions about structural properties of the data (e.g., algebraic, combinatorial, or probabilistic). For example, one can assume that data lie on a low-dimensional manifold and aim to identify that manifold explicitly from data. **Dimension reduction methods** — including **principal components analysis**, **manifold learning**, **factor analysis**, **random projections**, and **autoencoders** ( 1 , 2 ) — make different specific assumptions regarding the underlying manifold (e.g., that it is a linear subspace, a smooth nonlinear manifold, or a collection of submanifolds)." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))
<!--ID: 1645617152421-->


> "**Clustering** is the problem of finding a partition of the observed data (and a rule for predicting future data) in the absence of explicit labels indicating a desired partition." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))

> "A wide range of clustering procedures has been developed, all based on specific assumptions regarding the nature of a " cluster. " In both clustering and dimension reduction, the concern with computational complexity is paramount, given that the goal is to exploit the particularly large data sets that are available if one dispenses with supervised labels." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))

##### Reinforcement Learning Methods

> "A third major machine-learning paradigm is **reinforcement learning** ( 14 , 15 ). Here, the information available in the training data is intermediate between supervised and unsupervised learning. Instead of training examples that indicate the correct output for a given input, the training data in reinforcement learning are assumed to provide only an indication as to whether an action is correct or not; if an action is incorrect, there remains the problem of finding the correct action." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))
<!--ID: 1645617152428-->


> "The ties to research in **control theory** and **operations research** have increased over the years, with formulations such as **Markov decision processes** and partially observed Markov decision processes providing points of contact ( 15 , 16 )" ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))

> "**Reinforcement-learning algorithms** generally make use of ideas that are familiar from the **control-theory** literature, such as policy iteration, value iteration, rollouts, and variance reduction, with innovations arising to address the specific needs of machine learning (e.g., largescale problems, few assumptions about the unknown dynamical environment, and the use of supervised learning architectures to represent policies)." ([Jordan and Mitchell 2015:4](zotero://open-pdf/library/items/IARDFMK4?page=4))

#### Emerging trends

> "The field of machine learning is sufficiently young that it is still **rapidly expanding**, often by inventing new formalizations of machine-learning problems **driven by practical applications**." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))
<!--ID: 1645617152437-->


> "One major trend driving this expansion is a growing concern with the **environment** in which a machine-learning algorithm operates." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

> "The word " environment " here refers in part to the **computing architecture**; whereas a classical machine-learning system involved a single program running on a single machine, it is now common for machine-learning systems to be deployed in architectures that include many thousands or ten of thousands of processors, such that communication constraints and issues of parallelism and distributed processing take center stage." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

> "The word " environment " also refers to the **source of the data**, which ranges from a set of people who may have privacy or ownership concerns, to the analyst or decision-maker who may have certain requirements on a machine-learning system (for example, that its output be visualizable), and to the social, legal, or political framework surrounding the deployment of a system." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

> "Broadly speaking, environments provide various resources to a learning algorithm and place constraints on those resources." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

> "Increasingly, machine-learning researchers are formalizing these relationships, aiming to design algorithms that are provably effective in various environments and explicitly allow users to express and control trade-offs among resources." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

##### Privacy

> "**Privacy** can be formalized via the notion of " differential privacy, " which defines a probabilistic channel between the data and the outside world such that an observer of the output of the channel cannot infer reliably whether particular individuals have supplied data or not ( 18 )." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))
<!--ID: 1645617152443-->


> "Recent research has brought differential privacy into contact with machine learning, where queries involve predictions or other inferential assertions (e.g., " given the data I've seen so far, what is the probability that a new transaction is fraudulent? " ) ( 19 , 20 ). Placing the overall design of a privacy-enhancing machine-learning system within a decision-theoretic framework provides users with a tuning knob whereby they can choose a desired level of privacy that takes into account the kinds of questions that will be asked of the data and their own personal utility for the answers." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

##### Communication

> "**Communication** is another resource that needs to be managed within the overall context of a distributed learning system. For example, data may be distributed across distinct physical locations because their size does not allow them to be aggregated at a single site or because of administrative boundaries. In such a setting, we may wish to impose a bit-rate communication constraint on the machine-learning algorithm." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))
<!--ID: 1645617152449-->


> "A major goal of this general line of research is to bring the kinds of statistical resources studied in machine learning (e.g., number of data points, dimension of a parameter, and complexity of a hypothesis class) into contact with the classical computational resources of time and space." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

> "The ultimate goal is to be able to supply time and space budgets to machine-learning systems in addition to accuracy requirements, with the system finding an operating point that allows such requirements to be realized." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))

#### Opportunities and challenges

> "Despite its practical and commercial successes, machine learning remains a young field with many underexplored research opportunities." ([Jordan and Mitchell 2015:5](zotero://open-pdf/library/items/IARDFMK4?page=5))
<!--ID: 1645617152459-->


##### Opportunity: Collaborative Learning

> "For example, whereas most machine learning algorithms are targeted to learn one specific function or data model from one single data source, humans clearly learn many different skills and types of knowledge, from years of diverse training experience, supervised and unsupervised, in a simple-to-more-difficult sequence (e.g., learning to crawl, then walk, then run). This has led some researchers to begin exploring the question of how to construct computer lifelong or never-ending learners that operate nonstop for years, learning thousands of interrelated skills or functions within an overall architecture that allows the system to improve its ability to learn one skill based on having learned another ( 26-28 )." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))
<!--ID: 1645617152465-->


> "New machine-learning methods capable of working collaboratively with humans to jointly analyze complex data sets might bring together the abilities of machines to tease out subtle statistical regularities from massive data sets with the abilities of humans to draw on diverse background knowledge to generate plausible explanations and suggest new hypotheses." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))

> "As with any powerful technology, machine learning raises questions about which of its potential uses society should encourage and discourage." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))

##### Challenge: On Privacy and Ownership of Data

> "The push in recent years to collect new kinds of personal data, motivated by its economic value, leads to obvious privacy issues, as mentioned above. The increasing value of data also raises a second ethical issue: Who will have access to, and ownership of, online data, and who will reap its benefits? Currently, much data are collected by corporations for specific uses leading to improved profits, with little or no motive for data sharing. However, the potential benefits that society could realize, even from existing online data, would be considerable if those data were to be made available for public good." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))
<!--ID: 1645617152471-->


##### Opportunity: On mitigating the risk of a global pandemic

> "To illustrate, consider one simple example of how society could benefit from data that is already online today by using this data to decrease the risk of global pandemic spread from infectious diseases." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))
<!--ID: 1645617152477-->


> "The larger point of this example, however, is that, although the data are already online, we do not currently have the laws, customs, culture, or mechanisms to enable society to benefit from them, if it wishes to do so. In fact, much of these data are privately held and owned, even though they are data about each of us. Considerations such as these suggest that machine learning is likely to be one of the most transformative technologies of the 21st century." ([Jordan and Mitchell 2015:6](zotero://open-pdf/library/items/IARDFMK4?page=6))

# Comments
