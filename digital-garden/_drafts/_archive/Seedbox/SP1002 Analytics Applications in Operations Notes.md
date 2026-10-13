
---
tags: type/lecture-note 
alias:
creation-date: Sunday 6th August 2023
---

This course tackles use-cases such as **quality control**, **capacity planning**, and **failure and fault modelling**.

Instructor: Larmie Felizcuzo

> [!NOTE]- Learning Outcomes
> Upon completion of this course, the learners are expected to:
> - gain skills by  proposing operational and business improvements and solutions based on data-driven analysis, with the use of the appropriate type of analytics and applicable analytical technique/s
> - learn to streamline analysis and modeling for solving operations and process-related problems using Excel functionalities

# Module 1:Analytics and Operations Management at a Glance

## What is big data?
- According to Cavanillas, et al. (2015): Big data differs from regular data in terms of the following characteristics:
	1. Volume (*amount of data*) - big data has very large size 
	2. Velocity(*speed of data*) - big data can be accessed real-time via cloud ;and
	3. Variety(*range of data types/sources*) - have different data types and sources
- (Riahi, 2018) Added two more characteristics in addition to Volume, Velocity and Variety:
	- Veracity - quality, accuracy of data
	- Value - value and potentiality of data



## The Big Data Value Chain

1. Data Acquisition
	- Is the process of gathering, filtering and cleaning data before it is put in a data warehouse.
2. Data Analysis
	- Concerned with making the raw data amenable to use in decision-making as well as domain-specific usage.
	- It involves exploring, transforming and modelling data with the goal of highlighting relevant data, synthesizing and extracting useful hidden information with high potential from a business point of view.
3. Data Curation
	- Is the active management of data over its life-cycle to ensure it meets necessary data quality requirements for its effective usage.
4. Data Storage
	- Is the management of data in a scalable way that satisfies the needs of applications that require fast access to data.
5. Data Usage
	- Covers the data-driven business activities that need access to data,its analysis, and the tools needed to integrate the data analysis within the business activity.

![[Pasted image 20230808170524.png]]

## Types of Analytics
1. Descriptive Analytics - answers the question: *what is happening?*
2. Diagnostic Analytics - answers the question: *why did it happen?*
3. Predictive Analytics - answers the question: *what is most likely to happen?*
4. Prescriptive Analytics - answers the question: *what should be done?*

Basically, descriptive and diagnostic analytics focus on the past and present situations while predictive and prescriptive analytics focus on the future.

## Some terminologies
- **Statistics** - It aims to provide a scientific framework to collect, analyze, and derive conclusions and inferences through testing. 
- **Machine Learning** - It provides computer algorithms to uncover insights and enhance knowledge by learning from the given data.
- **Data mining** - It is a foundation of business intelligence where *insights are extracted* from a given dataset.
- **Optimization** - It is a foundation of business intelligence where insights are extracted from a given dataset.

## Techniques in Descriptive Analytics
- Association rules - detects patterns between items
- Sequence rule - detects sequences of events
- Clustering - detects homogenous (similar) objects

> [!NOTE]
> Predictive analytics seeks information that can predict a future outcome from data based on previous patterns.
## Methods in predictive analytics
- Probabilistic methods
	- Examples: Markov chain, Monte-carlo, Bayesian network, Hidden Markov Model
- Machine learning methods
	- Eg. [[Support Vector Machines|SVM]], ANN
- Statistical analysis
	- Eg. Linear regression, Multiple Linear Regression, [[Logistic Regression]]

> [!NOTE]
> Prescriptive analytics seeks information that is helpful in finding the best course of action in a given situation.

## Methods in prescriptive analytics
1. Probabilistic models
2. Machine learning models
3. Mathematical programming - used in optimal allocation of resources
4. Evolutionary computation - uses a family of algorithms for optimization
5. Simulation - models in real-life, includes what-if scenarios and risk assessment
6. Logic-based models - hypothesized descriptions of cause-effect chains

> [!NOTE]
> For this course, we will mainly use statistical analysis and simulations to demonstrate analytics in business operations.

## What is Operations Management?
- *Operations management is defined as ==the design, operation and improvement of the systems that create and deliver the firm's primary products==.* (Chase, Jacobs and Aquilano, 2007)
- *Operations management is commonly known as ==the discipline which employs scientifically sound analytical methods to help make optimal/near-optimal decisions== for organizations.* (Choi, et al., 2018)
- (Reid and Sanders, 2013) ![[Pasted image 20230806005212.png]]
- The success of operations and management is attributable to the ==value added== during transformation process. ![[Pasted image 20230806005411.png]]
- *"The role of operations management has become the focal point of efforts to increase competitiveness by improving value added and efficiency."*

## Operations Management Decisions
Business decisions can be categorized into two: ==Strategic and Tactical==
1. Strategic - set the direction for the entire company; broad in scope and long term in nature
	- eg. product design and process selection; supply chain management; total quality management
2. Tactical - specific and short-term in nature, bound by startegic decisions
	- Eg. facility layout, inventory and resource planning, scheduling

## Performance Measurement Frameworks
Once decisions has been operationalized.
- *How do we known if such decisions were right?*
- *How do we know if the business startegy is working?*
- *How do we assess if its effective or still applicable over time?*

### Performance Measurement Model

To answer these questions, a performance management framework that is aligned with the business goals must be established.

![[Pasted image 20230806010545.png]]

### Balanced Scorecard

One of the well-known frameworks used by organizations is the Balanced Scorecard. ==A balanced scorecard is a performance metric used to identify, improve, and control a business's various functions and resulting outcomes.==

The balanced scorecard is anchored on four perspectives, which include financial, business process, customer, and organizational capacity.

![[Pasted image 20230806010728.png]]

Readings
- [Balanced Scorecard 101: The Ultimate Guide | Smartsheet](https://www.smartsheet.com/all-about-balanced-scorecard)
- [What Is a Balanced Scorecard (BSC), How Is it Used in Business? (investopedia.com)](https://www.investopedia.com/terms/b/balancedscorecard.asp)

### Family of Measures Framework
This framework focuses on a group of measures that should track at least 4 of the following process variables:

![[Pasted image 20230806010851.png]]

### APQC's Input-Output Framework
![[Pasted image 20230806011008.png]]

## Process Performance Metrics
Process performance metrics measures different process characteristics that indicates how a process is performing and how it is changing over time.

### Common process performance metrics
- **Throughput time** - the average amount of time it takes to move through the system
- **Process velocity** - (aka throughput time/value-added time) is a measure of wasted time in the system
- **Productivity** - is a measure of how well a company uses its resources
- **Utilizatiion** - the proportion of time resource is actually used
- **Efficiency** - measures performance relative to a standard


> [!NOTE] Module 1 Summary
> We’ve reached the end of this week’s lesson. Here are some key takeaways:
> - Understanding the data value chain is a vital foundation of analytics because it provides perspective to the evolution of big data. 
> - There are different types of analytics and corresponding techniques/methods that can be applied to various scenarios depending on the timeline and complexity of analysis that the business requires.
> - Operational Management is a business function with the role of transforming inputs into output.
> - Efficiency and value-added during the transformation process are vital to successful operations management. 
> - Understanding operations management decisions – strategic and tactical - is critical to address business needs fully and properly.
> - Following a performance measurement framework is important in establishing the appropriate performance metrics to monitor and understand how the business process is performing.


# Module 2: Analytics Applications in Quality Management

> [!NOTE]- Learning Objectives
> _At the end of this week, learners will be able to:_
> - identify existing or potential operations management problems by dissecting available business data
> - determine how to provide data-driven insights to business solutions or decisions by using quality control tools
> - recognize how to create or propose a potential business solution by applying analytical techniques in quality management concepts

## Concepts in Quality Management
### 1. Total Quality Management
- Focused on customer. Main objective: Increase customer satisfaction.
- Process: Aims to improve uniform processes
- Approach: Everybody is committed
- Methodology: Plan, Do, Study, Act (4-stage)
- Tools: Analytical and statistical tools
### 2. Six Sigma
- Focuses on making no defects
- Process: Aims to reduce variation and improve processes
- Approach:Project management
- Methodology: Define, Measure, Analyze, Improve, Control (5-stage)
- Tools: Analytical and statistical tools
### 3. Lean Six Sigma
- Focuses on removing waste
- Process: Aims to improve flow in process
- Approach:Project Management
- Methodology: Understand customer value, Value Stream Analysis, Flow, Pull, Perfection
- Tools: Analytical tools only (such as Kanban system and Just-in-time system)

Impact
![[Pasted image 20230808173649.png]]

It is critical to undestand the impact of applying the above concepts in line with the business objectives.

## Operations Problem-Solving Tools
### Pareto Analysis
> *80% of the outcome results from 20% of the input*

Pareto analysis is the technique of arranging data according to priority/importance and and typing it into a problem-solving framework.

> [!NOTE]
> Pareto analysis is used in prioritizing and resource planning in terms of product improvement and customer service.

#### Steps in doing Pareto Analysis
1. List all elements you are looking at (eg. location, customer complaints)
2. Measure the elements
3. Rank the elements (from highest to lowest)
4. Create cumulative distributions
5. Draw the Pareto Curve
6. Interpret the Pareto Curve

![[Pasted image 20230808174457.png]]
The above Pareto chart shows that the 80% of the complaints came from the first 4 products. 

### Cause and Effect Analysis
Cause-and-Effect Analysis is a brainstorming technique that is used to draw all possible contributing factors or causes of the effect (Butterworth, 2007).

This is also called the **Ishikawa Diagram** (named after its inventor) or a **Fishbone Diagram** (named after its appearance).

Steps in doing cause-and-effect analysis
1. Idenntify the effect
2. Establish goals
3. Construct the diagram framework
4. Record the causes
5. Incubate and analyze the diagram

Example:
![[Pasted image 20230808175058.png]]

### Scatter Diagrams
 A scatter diagram is used to look at the relationship between two factors (dependent and independent factors).

![[Pasted image 20230808181328.png]]

### Stratification
Stratification is a technique that involves collection or division of datasets into groups.

![[Pasted image 20230808181642.png]]

### Control Charts
These charts are used to evaluate whether a process is operating within expectations relative to a standard.

There are two types of control chart types: Variable and Attribute.

![[Pasted image 20230808181859.png]]

## DMAIC Methodology
![[Pasted image 20230808182421.png]]

### 'Define' Stage
Key Objectives:
1. Project defintion
2. Top-level process definition
3. Team formation


### 'Measure' Stage
Key Objectives:
1. Detailed process definition
2. Define metrics
3. Process baseline estimation
4. Measurement system analysis


### "Analyze" Stage
Key Objectives
1. Analysis of value stream
2. Analysis of sources of variation
3. Determination of process drivers



### "Improve" Stage
Key Objectives:
1. Determing operating conditions
2. Failure modes analysis
3. Benefit analysis
4. Process improvement

### "Control" Stage
Key objectives:
1. Standardize the methdods
2. Verify predicted impact
3. Document lessons learned

# Module 3: Forecasting in Operations Management
## Principles of Forecasting (Reid and Sanders, 2014)
1. Forecasts are rarely perfect.
2. Forecasts are more accurate for shorter than longer time horizons.
3. Forecasts are more accurate for groups of items rather than individual items. 

## Steps in the forecasting process
1. Decide what to forecast.
	- *What is the business question?*
	- *Do we have enough data?*
2. Evaluate and analyze appropriate data
3. Select & test forecasting model
	- *Assess the validity of the model*
4. Generate forecast results
5. Monitor forecast accuracy

> [!NOTE]
> In operations management, forecasts may be used in determining:
> - product designs that are expected to sell
> - product volume
> - amount of supplies and materials needed
> - logistics requirements including space requirements and capacity & location needs
> - labor demand
> - work scheduling
> 
> In a supply chain, all units are working to meet customer demands. The demand forecast is critical and must be aligned among all units of the supply chain to ensure  a common goal and reference. For instance, when supply chain units have independent forecasts and are looking at different levels of demand, the risk of mismatch between supply and demand becomes high.

## Forecasting methods
Forecasting methods can be generalized into two:
1. **Time series models** - assume that all information needed for a forecast can be derived from time series of data. Generally, these models are easier to use and can generate forecasts more quickly if you have substantial data available.
2. **Causal models** - assume that the variable being forecast is related to other variables in the environment. These models are more complex as they consider relationships among variables and require model building.

### Time Series Models
Here are 5 commonly used time-series models
1. Naive - uses last period's actual value
2. Simple mean - uses average of ALL past data
3. Simple moving average - uses the average of a number $n$ of the most recent observations
4. Weighted moving average - like SMA but past observations have different weights
5. Exponential smoothing - like WMA but weights are declining exponentially
6. Trend-adjusted Exponential Smoothing - like exponential smoothing with trend forecasting.
	- ![[Pasted image 20230809135036.png]]

Remarks
- SMA can be used via Analysis Toolpak in Excel
- Exponential moving forecast: $\alpha (\text{Current Period's actual value}) + (1-\alpha)(\text{Current Period's forecast})$
	- Low $\alpha$ means not giving weight to current period's actual demand, High $\alpha$  gives more weight on current period's actual demand.
	- In Excel, the quantity $(1-\alpha)$ is known as the damping factor

### Causal Models
1. Linear regression
2. Multiple regression

### Common Forecast Accuracy Measures
1. Forecast Error $E_{t} = A_{t} - F_{t}$
2. Mean Absolute Deviation
3. Mean Squared Error

![[Pasted image 20230809135728.png]]

## Factors to consider when selecting the right forecasting model
- Amount and type of available data
- Degree of accuracy required
- Length of forecast horizon
- Presence of data patterns (seasonality, trend, etc)

> [!NOTE] Key Takeaways
> - Forecasting is a vital tool in operations management such that it impacts all business functions and operations decisions.
> - It is important to understand the principles and steps of forecasting in setting the proper scope and limitations of the project/plan.
> - There are several forecasting methods that can be used depending on available data and the degree of accuracy required within a specific function.

# Module 4: Operations Research in Analytics
## What is Operations Research?
- Operations research (often referred as *management science*) is a scientific approach to decision making that seeks to best design and operate a system, usually under conditions requiring the allocation of scarce resources. *(Winston and Goldberg, 2004)*
- A scientific approach to analysis and solution of management problem.  *(Lyeme and Selemani, 2012)*

## Characteristics of Operations Research
Furthermore, they presented the **Characteristics of Operations Research (OR)** as follows:
- ==System Orientation== which means that OR decisions and activities may have an impact across the entire organization or operations.
- ==Use of an interdisciplinary team== where scientists, engineers, mathematicians, economists, statisticians, and other individuals from various disciplines work together in an OR problem.
- ==Application of Scientific Methods== in solving an OR problem particularly in experimentation and simulation.
- ==Quantitative Solutions== where OR solutions are based on data and figures; coupled with the last characteristics of human factor


## Phases of Operations Research (Lyeme and Selemani, 2012)

1. ==Problem Formulation== where the objectives, decision variables, and constraints are determined and laid out which effectively results in model building.
2. ==Data collection==/acquisition
3. ==Driving solution from the model== where the appropriate optimization technique or method is used based on the problem or model and the available data.
4. ==Testing the model== and its solution through simulation or comparison based on previous data.
5. ==Controlling the solution in modifying the model==.  It can help to address possible changes in conditions/constraints.
6. ==Model implementation== and monitoring to assess possible required modifications to adapt to changes in data characteristics, operational functions, and/or business goals.

![[Pasted image 20230809174540.png]]


Optimization Models
- Linear programming
- Network models
- Integer programming
- Nonlinear programming

An optimization model is composed of:
- Objective function - the function to be optimized
- Decision variables - the variables that affect the performance of the system
- Constraints - the restrictions imposed on the values of the decision variables

The results of a linear programming may be classified into three:
- Feasible
- Infeasible
- Optimal

## Linear Programming: Simplex Method
- A mathematical algorithm that can solve linear programming problems quickly.

## Network Models
A **network** is defined by two sets of symbols: nodes (points) and arcs(lines). An **arc** is defined as an ordered pair of nodes While a **chain** is defined as a sequence of arcs. a **path** is defined as a chain in which the terminal node of each arc is identical (or is equal to) the initial node of the next arc.

> [!NOTE]
> A network flow application can be restated as a linear programming exercise. In this case, the LP objective is to minimize the total cost of all flow variables.

Three common network models problems
- Shortest path problems *(finding the shortest path from initial node to any other node)*
- Maximum flow problems *(finding the maximum amount of flow from source to sink/terminal point)*
- Transshipment model

### Shortest Path Problem
The goal is to find the shortest path from source to destination through a connecting network.

Sample Shortest Distance Excel Model:
![[Pasted image 20230809202633.png]]
![[Pasted image 20230809202708.png]]

### Maximum-Flow Problem
Sample Maximum-Flow Problem Excel Model:
![[Pasted image 20230809203123.png]]
![[Pasted image 20230809203229.png]]

### Transhipment Problem
Objective: Distribute products to depots as cheaply as possible.
![[Pasted image 20230809203541.png]]
![[Pasted image 20230809203606.png]]
![[Pasted image 20230809203637.png]]

## Integer Programming
Interger program is a linear program in which some or all of the variables are required to be non-negative whole numbers. A classic example is manpower.

## Nonlinear programming
Nonlinear programming is an optimization problem where the objective function or some of the constraints may or may not be linear constraints.

---
[[SP1002 Analytics Applications in Operations Flashcard Notes]]