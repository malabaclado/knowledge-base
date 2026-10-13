---
tags:
alias:
creation-date: Monday 11th September 2023
---

In this course, participants will learn how to design, run, and analyze experiments that allow simultaneous testing of all factors. This course imparts practical knowledge of experimental design and analysis by illustrating cases on the real-world implementation of experimentation.

Supplementary courses to study:
- [The Open Educator - Design of Experiments](https://www.theopeneducator.com/doe)
- [Welcome to STAT 503! | STAT 503 (psu.edu)](https://online.stat.psu.edu/stat503/)
- [Experimental Design and Process Optimization with R (bookdown.org)](https://bookdown.org/gerhard_krennrich/doe_and_optimization/)

Instructor: 
- Atty. Rudolph Val Guarin, BS Statistics UP DIliman, MBA DLSU, Law grad JRU.
- Joyce Raymond Punzalan, Faculty member and PHD Candidate at UPD School of Sta

# Week 1. Introduction to Experimental Designs

> [!NOTE]-  Objectives
> - define what an experimental design or design of experiment (DOE) is
> - recognize the various relevant purposes of designing experiments
> - enumerate the basic steps in conducting experimental designs and the factors to obtain good results from DOE

## What is experimental design?
Experimental design in research refers to the process of planning and organizing an experiment to investigate a specific research question or hypothesis. It involves making deliberate choices about how to manipulate variables, collect data, and control potential sources of bias or error to ensure that the results are reliable and valid. Experimental design is a crucial aspect of scientific research, particularly in fields like psychology, biology, chemistry, and many others.

## Experiment VS Experimental Design
![[Pasted image 20230911204733.png]]


## Terminologies
- Controllable input factors: input paramaters that can be modified in the experiment
- Uncontrollable input factors: parameters that cannot be changed in an experiment
- Responses: (also output measures or output) these are the dependent variables
- Hypothesis testing: The use of sample data to evaluate a hypothesis about a population.
	- Null hypothesis: valid if status quo is true
	- Alternative hypothesis: true if the status quo is not valid
- Blocking: an experimental tecnique used to avoi any unwanted variations in the experimental process (eg. using the same equipment to avoid equipment variation)
- Replication: performing the same combination run more than once
- Interaction:  situation where the simultaneous of two variables to an independent variable is not additive.



## What is the purpose of experimental design?
- Conducting Comparative Experiment
- Screening experiment
	- Answers the question: *which experimental variable has a real influence on the output?*
	- is an efficient way of determining the important factors with a minimal number of runs.
	- Screening designs are used to find the important factors from a large numebr of two-level factors 
		- fractional replication (4,8,16,32)
		- Plackett-Burman design (12,20,24,28)
- Response Surface Modelling
	- explores the relationships between **several explanatory variables** and **one or more response variables**
	- a compilation of mathematical and statistical methods, helpful for fitting models and analyzing the problems in which a lot of independent parameters control the independent parameters
	- After the primary factors have been identified, additional objectives might follow, such as: ^0d4az5
		- **Hitting a certain target/goal**
			- Trying out different settings until the desired target is *hit* consistently. 
		- **Maximizing/minimizing the response**
		- **Reducing variation/variability in the process**
			- Problem: internal variation too high
			- ![[Pasted image 20230911213143.png]]
		- **Making a process more robust.**
		- **Seeking multiple goals**
- Regression modelling - a method to mathematically formulate relationship between variables that in due course can be used to estimate, interpolate and extrapolate.

## Steps in Design of Experiments

1. **Define Objectives and Problem Statements:**
   - This initial step involves clearly defining the objectives and the problem statement for your experiment. What do you want to achieve, learn, or optimize through the experiment? What specific questions or hypotheses do you aim to address?
   - This step sets the direction for your entire experiment and helps ensure that your research efforts are focused and purposeful.
   - All objectives should be written down - even the unspoken ones.
   - Examples of objectives:
      - Comparative designs - to compare which option is better
      - Screening designs - identify which factors are important
      - Response surface - might have multiple objectives
         - ![[SP602 Experimental Design and Analysis Notes#^0d4az5]]
      - Regression modelling - to quantify the dependent/response variable based on process inputs

2. **Identify Process Variables:**
   - In this step, you identify the relevant process variables, which are also known as factors. These are the independent variables that you suspect might influence the outcome or response variable of your experiment.
   - It's important to distinguish between factors that you can control or manipulate (independent variables) and those that you cannot control, which may act as confounding variables.

1. **Selecting an Experimental Design:**
   - Based on your objectives, available resources, and the nature of the factors, you choose an appropriate experimental design. The choice of design can significantly impact the efficiency and effectiveness of your experiment.
   - Common experimental designs include full factorial, fractional factorial, response surface, and more. The selected design will specify how factors are varied and how data will be collected.
   - Choose from the following designs:
      - Comparative design
      - Screening design
      - Response surface method design
      - Mixture design - if you have factors that are proportions of a mixture and you want to know the *best* proportions so as to maximize/minimize a response
      - Regression design - if you want to model a response as a mathematical function
   - ![[Pasted image 20230911214604.png]]

4. **Conducting the Experiments:**
   - This step involves executing the experiments according to the experimental plan laid out in the chosen design. You manipulate the factors at specified levels and collect data on the response variable.
   - It's crucial to ensure that the experiments are conducted under controlled conditions, and any potential sources of bias or variability are minimized.

5. **Checking Data Consistency with Experimental Assumptions:**
   - As data is collected, it's essential to check whether the experimental assumptions are met. These assumptions may include randomness, independence of observations, and the normality of data.
   - Data consistency ensures that the statistical analysis and conclusions drawn from the data are valid and reliable.

1. **Analyze and Interpret the Results:**
   - Once you have collected data, you proceed to analyze it using appropriate statistical methods. The analysis aims to uncover relationships between the factors and the response variable, including main effects and interactions.
   - Interpretation of the results involves understanding the practical significance of the findings and drawing conclusions about the impact of the factors on the system or process under study.
   - ## To analyze DOE data, the following steps are usually adopted:
      - Plot the data
      - Modelling the data
      - Testing and revising the models
      - Interpreting the results
      - Confirming the results

7. **Present the Results:**
   - The final step involves presenting the results of your experiment. This typically includes creating reports, charts, graphs, and presentations to communicate the findings to stakeholders, decision-makers, or the scientific community.
   - Effective presentation of results is crucial for conveying the significance of your work and any recommendations or insights derived from the experiment.

These seven steps guide researchers and scientists through the process of designing and conducting experiments systematically. Properly executed DOE helps ensure that experiments are well-planned, efficiently executed, and capable of producing meaningful and statistically valid results, which can then be used for decision-making or further research.

## Important Practical Considerations in Planning and Conducting Experiments
1. Check the performance gauges/measurement devices first.
2. Keep the experiments as simple as possible.
3. Check that all planned runs are feasible.
4. Watch out for process drifts and shifts during the run.
5. Avoid unplanned changes (eg. swap operators at halfway point)
6. Allow some time for unexpected events.
7. Obtain buy-in from all parties involved.
8. Maintain effective ownersip of each step in the experiment plan.
9. Preserve all raw data.
10. Record everything that happens.
11. Reset equipment to its original state after the experiment.

Key questions to ask:
1. Is the measurement system capable? 
2. Is the process stable?
	1. It is desirable to experiment on a stable process. Otherwise, process instability must be accounted for.
3. Is there a simple model?
4. Are the residuals well-behaved?
	- Carefully looking at residuals can tell us whether our assumptions are reasonable and our choice of model is appropriate. 
	- Must be approximately normal with mean 0 and no variance.
	- Three types of graph to examine normality:
		- Histogram
		- Normal probability plot
		- Dot plot

# Week 2. Important Considerations in Planning and Running Experiments



> [!NOTE] On prioritizing objectives
> - The objectives for an experiment are best determined by a team discussion. All of the objectives should be written down, even the unspoken ones;
> - The group should discuss which objectives are the key ones, and which ones are "nice but not really necessary".
> - Prioritization of the objectives helps you decide which direction to go with regard to the selection of the factors, responses, and particular design.
> 
> Sometimes prioritization will force you to start over from scratch when you realize that the experiment you decided to run does not meet one or more critical objectives.

## Objectives for different experimental designs

**Comparative Design**
1. Choose between alternatives, with narrow scope, suitable for an initial comparison  
2. Choose between alternatives, with a broad scope, suitable for a confirmatory comparison

**Screening Design**
The objective of a screening design is to identify which factors are important:
1. When you have 2 - 4 factors and can perform a full factorial   
2. When you have more than 3 factors and want to begin with as small a design as possible   
3. When you have some qualitative factors, or you have some quantitative factors that are known to have a non-monotonic effect

**Response Surface Modelling**
The objective of RSMis to achieve one or more of the following:
1. Hit a target  
2. Maximize or minimize a response  
3. Reduce variation by locating a region where the process is easier to manage  
4. Make a process robust (note: this objective may often be accomplished with screening designs rather than with response surface designs)

**Regression modelling**
To estimate a precise model, quantifying the dependence of response variable(s) on process inputs

## How to select and scale process variables
**Process variables** include both inputs(factors) and outputs(responses).

> [!NOTE] Selection of process variables as a team effort
> The selection of these variables is best done as a team effort. The team should:
> - Include all important factors (based on judgment)
> - Be bold (but not foolish) in choosing low and high factor levels.
> - Check factor settings for impractical combinations
> - Include relevant responses

The most popular experimental designs ==two-level designs==.

## How to select an experimental design

> [!NOTE]
> The choice of design depends on:
> 1. amount of resources available
> 2. degree of control over making wrong decisions
> 
> It is a good idea o choose a design that requires:
> 1. somewhat fewer runs than the budget permits
> 2. backup resources are available to redo runs that hae processing mishaps


![[Pasted image 20230912102057.png]]
![[Pasted image 20230912102109.png]]

## Steps in Design of Experiments (DOE) Analysis
![[Pasted image 20230912102459.png]]

> [!NOTE] Remarks
> - The above flowchart and sequence of steps should **not** be regarded as a **"hard-and-fast rule"** for analyzing all DOEs.
> - Different analysts may prefer a different sequence of steps and not all types of experiments can be analyzed with one set of procedures.
> - There still remains some **art** in both the design and the analysis of experiments, which can only be learned from experience. In addition.
> - The role of **engineering judgment** should not be underestimated.


**A. Look at the data**
**Examine it for outliers, typos, and obvious problems.** Construct as many graphs as you can to get the big picture. Eg:
- Response distributions (histograms, box plots, etc.)
- Responses versus time order scatter plot (a check for possible time effects)
- Response vs. factor levels (first look at the magnitude of factor effects)
- Typical DOE plots (which assume standard models for effects and errors)
	1. Main effects mean plots
	2. Block plots
	3. Normal or half-normal plots of the effects
	4. Interaction plots

Sometimes the right graphs and plots of the data lead to obvious answers for your experimental objective questions. In most cases, however, you will want to continue by fitting and validating a model that can be used to answer your questions.  
  

**B. Create the theoretical model**  
The experiment should have been designed with this model in mind.   
  

**C. Create a model from the data**  
Simplify the model, if possible, using stepwise regression methods and/or parameter p-value significance information.  
  

**D. Test the model assumptions using residual graphs**
- If none of the model assumptions were violated, examine the ANOVA.
- Simplify the model further, if appropriate. If the reduction is appropriate, then return to step 3 with a new model.
- If model assumptions were violated, try to find a cause.
- Are necessary terms missing from the model?
- Will a transformation of the response help? If a transformation is used, return to step 3 with a new model. 

**E. Use the results to answer the questions in your experimental objectives**   
Finding important factors, finding optimum settings, etc.  

![[Pasted image 20230912102800.png]]

![[Pasted image 20230912102917.png]]

![[Pasted image 20230912102930.png]]

## How to interpret and confirm DOE results?
![[Pasted image 20230912103201.png]]

![[Pasted image 20230912103148.png]]

![[Pasted image 20230912103220.png]]

![[Pasted image 20230912103247.png]]

**Confirming DOE results**

![[Pasted image 20230912103319.png]]

![[Pasted image 20230912103338.png]]


## Completely Randomized Design
This text discusses the concept of completely randomized design in experimental research. Here's a summary of the key points arranged logically:

1. **Definition of Completely Randomized Design**:
   - In a completely randomized design, there is only one primary factor being studied.
   - The experimenter compares the values of the response variable based on different levels of this primary factor.
   - Levels of the primary factor are randomly assigned to the experimental units.

2. **Randomization**:
   - Randomization refers to the process of determining the sequence of experimental units randomly.
   - Randomization can be carried out using computer programs, random number tables, or physical mechanisms (e.g., drawing slips of paper).

3. **Design Parameters**:
   - Completely randomized designs with one primary factor are defined by three numbers:
     - **K**: The number of factors (in this case, just one primary factor).
     - **L**: The number of levels for the primary factor.
     - **n**: The number of replications.
   - The total sample size or the total number of runs is denoted by capital **N**, which equals K times L times n.

4. **Balanced Design**:
   - Balance dictates that the number of replications should be the same at each level of the factor.
   - This ensures that subsequent statistical tests are maximally sensitive.

5. **Example of a Completely Randomized Design**:
   - An example is given with the following parameters:
     - K = 1 (one primary factor)
     - L = 4 (four levels)
     - n = 3 replications per level
   - The total number of runs (N) is 4 (levels) x 3 (replications) x 1 (factor) = 12 runs.
   - A randomized sequence of trials is provided as an example of how the levels are assigned to each run.

1. **Model for Response**:
   - The response variable is represented by the equation: **yij = μ + ti + random error**.
   - yij represents any observation for which X1 (the primary factor) is equal to I.
   - I and J denote the level of the primary factor and the replication within that level, respectively.
   - μ is the general location parameter.
   - ti represents the effect of having treatment level I.
   - μ is estimated by the average of all the data (Y-bar).
   - ti is estimated by the difference between the average of Y for level I (Y-bar I) and the overall average (Y-bar).

![[Pasted image 20230912160022.png]]

## One-way Analysis of Variance (ANOVA)

Sample dataset:
![[Pasted image 20230912160058.png]]

This dataset consists of 10 batches, each batch with 10 measurements = 100 entries.

 ![[Pasted image 20230912160451.png]]
 ![[Pasted image 20230912160613.png]]



# Week 3. Utilizing Randomized Block and Factorial Designs using ANOVA


## Randomized Block Design
In randomized block design experiments, there is one factor or variable that is of primary interest.  However, there are also several nuisance factors.

**Nuisance factors** are those factors that may affect the measured result but are not of primary interest in the experiment.  Examples of nuisance factors can be the specific operator who prepared the treatment, the time of day the experiment was run, or the room temperature.  

**All experiments have nuisance factors.**  The experimenter needs to spend time deciding which nuisance factors are important enough to keep track of or control, if possible, during the experiment.

### Blocking
When we can control nuisance factors, an important technique known as **blocking** can be used to reduce or eliminate the contribution of the nuisance factors to the experimental error.  

The basic concept is to create homogeneous blocks in which the nuisance factors are held constant and the factor of interest is allowed to vary.  Within blocks, it is possible to assess the effect of different levels of the factor of interest without having to worry about variations due to changes of the block factors, which are accounted for in the analysis.

> [!NOTE]
> The general rule is _“Block what you can, randomize what you cannot”_.  Blocking is used to remove the effects of a few of the most important nuisance variables, then Randomization is used to reduce the contaminating effects of the remaining nuisance variables.

## Example: Randomized Block Design (RBD) in Semiconductor Manufacturing Experiment
In the context of the semiconductor manufacturing experiment example, a randomized block design is a type of experimental design that is used to investigate the effects of different factors while accounting for the presence of a nuisance factor. Let's break down how this design works in this specific context:

**Objective of the Experiment:**
The semiconductor manufacturing experiment aims to test whether different dosages of wafer implant materials have a significant effect on resistivity measurements after a fusion process in a furnace.

**Factors Involved:**
1. **Primary Factor (x sub 1):** This is the dosage level of the wafer implant material. It has four different levels or settings that the engineers want to test.

2. **Blocking Factor (x sub 2):** The blocking factor in this experiment is the furnace run. Each furnace run differs from the last and can impact many process parameters. It is considered a nuisance factor because it introduces variability that is not of primary interest but needs to be controlled for.

**Design Parameters:**
- **K (Number of Factors):** In this case, K is equal to 2, representing two factors being studied (dosage level and furnace run).

- **L sub 1 (Levels of x sub 1):** There are 4 levels of the primary factor, corresponding to the different dosage settings.

- **L sub 2 (Levels of x sub 2):** There are 3 levels of the blocking factor, indicating the number of different furnace runs.

- **Small n (Replication per Cell):** Each combination of dosage level and furnace run is replicated once (small n equals 1).

- **Capital N (Number of Runs):** The total number of experimental runs before randomization is calculated as the product of L sub 1 and L sub 2, which is 4 times 3, equaling 12 runs.

**Experimental Design:**
In a randomized block design, the goal is to ensure that each combination of the primary factor (dosage level) and blocking factor (furnace run) is tested, but the order in which they are tested is randomized to minimize the impact of nuisance factors. However, because regular production wafers have priority in furnace runs, only a few experimental wafers can be included in each run.

**Statistical Model:**
The statistical model for this randomized block design is represented as:

y sub i j = mu + T sub I + b sub J + random error

- **y sub i j:** Represents the observation for a specific combination of dosage level (i) and furnace run (j).
- **mu:** Represents the general location parameter.
- **T sub I:** Represents the effect of being in treatment I (a specific dosage level).
- **b sub J:** Represents the effect of being in Block J (a specific furnace run).
- **Random error:** Represents the variability not accounted for by the factors.

In summary, the randomized block design in the semiconductor manufacturing experiment allows researchers to systematically test different dosage levels of wafer implant materials while controlling for the variability introduced by different furnace runs. This design helps ensure that the results are not unduly influenced by the nuisance factor (furnace run) and allows for a more rigorous assessment of the primary factor's impact on resistivity measurements.

## Example: Randomized Block Design (RBD) in Construction Company Experiment 

In the context of the construction company experiment, a randomized block design is a specific experimental design used to investigate whether three estimators tend to produce estimates at the same mean level or if one or more estimators consistently submit high or low bids on construction projects. Let's break down how this design works in this specific context and mention some statistical figures:

**Objective of the Experiment:**
The objective is to assess whether three estimators (E1, E2, and E3) produce estimates at the same mean level or if there are significant differences in their bidding behaviors for the same set of construction projects.

**Factors Involved:**
1. **Estimators (E1, E2, E3):** These represent the three different estimators responsible for producing cost analysis estimates and bids for construction projects.

2. **Construction Projects (P1, P2, P3, P4, P5):** These represent the five different construction projects for which estimates and bids are being produced.

**Experimental Design:**
In a randomized block design, the primary goal is to control for variability introduced by a nuisance factor (in this case, the specific construction project) while assessing the impact of the primary factor (the estimator). Here's how the design is structured:

- Each estimator (E1, E2, E3) is required to produce cost analysis estimates and bid prices for all five construction projects (P1, P2, P3, P4, P5).
- This means that each estimator provides estimates and bids for the same set of projects, ensuring that differences in bids can be attributed to the estimator rather than variations between projects.
- The blocking factor is the construction project (the specific project being estimated), and it serves to control for project-specific variability.

**Analysis of Variance (ANOVA):**
In the context of this experiment, an analysis of variance (ANOVA) is performed to assess the significance of differences among the estimator means and the project block means.

![[Pasted image 20230912173732.png]]

**Statistical Figures:**
Here are some key statistical figures that would be derived from the ANOVA analysis:

- **SST (Sum of Squares Total):** This measures the total variability in the data.
- **SSE (Sum of Squares Error or Residuals):** This quantifies the variability that cannot be explained by the differences between estimators. It measures the variation within each project.
- **SSB (Sum of Squares Between or Treatment):** This represents the variability that can be attributed to the differences among the estimators.
- **Degrees of Freedom:** Degrees of freedom for SST, SSE, and SSB are determined based on the number of levels of the factors and the number of observations.
- **F-Statistic:** F-statistics are calculated to test the null hypotheses:
  - Null Hypothesis 1: There are no differences among the estimator means.
  - Null Hypothesis 2: There are no differences among the project block means.

![[Pasted image 20230912173801.png]]

![[Pasted image 20230912173842.png]]


**Computation of Confidence Interval:**
$$\bar{x_{i}} - \bar{x_{j}} \space \pm t_{\frac{\alpha}{2}, n-b-k+1} \sqrt{ MSE\left( \frac{2}{b} \right) }$$

The F-statistics are used to compare the observed variability among the estimator means (SSB) and the random variability within each project (SSE) to determine whether there are significant differences among the estimator means or the project block means.

The specific values for SST, SSE, SSB, degrees of freedom, and F-statistics would depend on the data collected during the experiment and the results of the ANOVA analysis. These figures would help researchers make conclusions about the differences among the estimators and whether one estimator consistently submits higher or lower bids on construction projects.


## What is Factorial Design? 
In the context of the Design of Experiments (DOE), a **factorial design** is a *type of experimental design that allows researchers to study the effects of multiple factors (independent variables) simultaneously by varying them at different levels or settings*. Factorial designs are particularly useful for understanding how different factors interact with each other and influence a response variable.

Key characteristics of factorial designs include:
1. **Involves Multiple Factors:** *Factorial designs involve two or more factors, each with two or more levels.* Factors are the variables that researchers manipulate to observe their impact on a response variable.
2. **Full Factorial:** *A full factorial design examines all possible combinations of factor levels.* 
	- For example, in a 2x2 factorial design with two factors, Factor A and Factor B, there are four treatment combinations: A1B1, A1B2, A2B1, and A2B2, where "A1" and "A2" represent the two levels of Factor A, and "B1" and "B2" represent the two levels of Factor B.
3. **Can Assess Interaction Effects:** *One of the primary advantages of factorial designs is their ability to assess interaction effects between factors.* 
	- **Interaction** occurs when the effect of one factor on the response variable depends on the level of another factor. Interaction effects can be synergistic (positive interaction) or antagonistic (negative interaction).
4. **Identifies Main Effects:** In addition to interaction effects, factorial designs allow researchers to determine the main effects of each factor. *Main effects represent the influence of a single factor on the response variable while averaging over the levels of the other factors.*
5. **Randomization:** To minimize bias and control for extraneous variables, researchers often randomize the order in which treatments are applied or the assignment of subjects to treatment groups in factorial experiments.
6. **Replication:** Replicating experimental runs is important to increase the precision and reliability of the results. Each treatment combination is often replicated multiple times.

Factorial designs are commonly used in various fields, including engineering, biology, social sciences, and manufacturing, to investigate complex relationships among factors. *They help researchers identify which factors have a significant impact on the response variable, whether there are interactions between factors, and the direction and magnitude of these effects.*

Factorial designs are versatile and can be extended to more complex designs, such as **fractional factorial designs** (which examine a subset of factor combinations to reduce the number of experimental runs) and **higher-order factorial designs** (which involve three or more factors). These designs play a crucial role in optimizing processes, identifying influential variables, and gaining a deeper understanding of the system being studied.


## Full Factorial Designs in Two Levels
1. **Factorial Design Introduction**
   - Factorial design is a common experimental design.It involves multiple independent variables or factors in an experiment. These factors are combined to study their effects on a single dependent variable.

2. **Factorial Design Structure**
   - Each level of one independent variable is combined with each level of the other independent variables.
   - All possible combinations are investigated in each replication.

4. **Advantages of Factorial Design**
   - Avoids misleading conclusions by considering interactions.
   - Allows estimating factor effects at various levels of other factors, making conclusions valid over different experimental conditions.
   - Results in savings in experimental resources and time.

5. **Disadvantages of Factorial Design**
   - Challenges arise when experimenting with many factors or levels, leading to large and complex experiments.
   - Requires meticulous planning to avoid errors that could jeopardize the entire experiment.

### Two-Level Full Factorial Design
A **two-level factorial design**, as described in the text, is *a type of experimental design where all input factors are set at two levels each*. These two levels are typically referred to as "high" and "low," or they can be represented as "+1" and "-1." In such a design, each factor is varied at these two levels, and all possible combinations of the factors at these levels are explored in the experiment.

Key characteristics of a two-level factorial design are:
1. **Two Levels**: Each independent factor in the experiment is set at two distinct levels. These levels represent the extreme values or conditions that the factor can take.
2. **Combinations**: The design examines all possible combinations of the factors at these two levels. This means that if there are multiple factors involved, the experiment will systematically vary each factor at both the high and low levels.
3. **Factorial Design**: It follows the principles of a factorial design, which means it investigates how these factors interact with each other and how they collectively affect a single dependent variable.
4. **Exponential Growth**: The number of runs or experimental trials in a two-level factorial design grows exponentially with the number of factors involved. Specifically, for K factors, there will be 2^K experimental runs.
5. **Efficiency**: While two-level factorial designs are efficient for a small number of factors, they can become impractical when dealing with a large number of factors due to the exponential increase in runs. In such cases, fractional factorial designs or other approaches may be more suitable.

In summary, a two-level factorial design is a systematic experimental approach that investigates the effects of multiple factors, each set at two distinct levels, on a dependent variable. It allows researchers to understand how these factors interact and impact the outcome of the experiment.

### Examples of Full Factorial Design
Here are the examples and how a two-level full factorial design might be used:

1. **Social Research**
   - Example: Social researchers often use factorial designs to assess the effects of educational methods while taking into account the influence of some socioeconomic factors.
   - Application of Two-Level Full Factorial Design: In this context, a two-level full factorial design could be employed to investigate the impact of different educational methods (Factor A) and socioeconomic factors (Factor B) on educational outcomes. Each factor would have two levels: for educational methods, it could be traditional teaching methods (low level) and innovative teaching methods (high level); for socioeconomic factors, it could be low-income families (low level) and high-income families (high level). The design would systematically vary these factors to study their interactions and effects on student performance.
2. **Agriculture**
   - Example: Factorial designs are usually used to test the effect of variables on crops.
   - Application of Two-Level Full Factorial Design: In agricultural research, a two-level full factorial design could be applied to study the effects of various factors (e.g., types of fertilizers, irrigation levels) on crop yield. For instance, Factor A could represent different types of fertilizers (low and high), and Factor B could represent irrigation levels (low and high). Researchers would systematically apply these combinations to different plots or areas to assess their impact on crop yield.
3. **Engineering (Battery Testing)**
   - Example: An engineered test three plate materials for a new battery at three temperature levels.
   - Application of Two-Level Full Factorial Design: In this engineering example, a two-level full factorial design would involve varying the plate materials (Factor A) and temperature levels (Factor B) at two levels each. For plate materials, it could be two different materials (low and high), and for temperature levels, it could be three different temperature settings (low, medium, high). Researchers would then test the battery's performance under all possible combinations of plate materials and temperature conditions, providing insights into which combinations yield the desired battery performance.
4. **Consumer Behavior (Food Consumption)**
   - Example: Studying the effects of reduced food size and package size on the consumption behavior of restrained and unrestrained eaters.
   - Application of Two-Level Full Factorial Design: In this consumer behavior study, a two-level full factorial design could be used to explore how food size reduction (Factor A) and package size reduction (Factor B) influence eating behavior among both restrained and unrestrained eaters. Each factor would have two levels: for food size reduction, it could be small portion (low level) and large portion (high level); for package size reduction, it could be small package (low level) and large package (high level). Researchers would systematically expose participants to all combinations of these factors to analyze their effects on food consumption patterns.

In these examples, a two-level full factorial design involves systematically varying multiple factors at two levels each to examine all possible combinations. This allows researchers to assess the main effects of each factor and the interactions between factors, providing a comprehensive understanding of their impact on the studied outcomes. However, it's essential to consider the practical feasibility of conducting experiments with all possible combinations, especially when dealing with a large number of factors or levels. In such cases, fractional factorial designs or other approaches may be more practical.

### Symmetrical Factorial Design
A symmetrical factorial design, in experimental research, is a type of factorial design where all independent factors are manipulated at the same number of levels. This design ensures that each factor is equally represented and systematically tested, making it balanced and unbiased. For example, in a symmetrical 2x2x2 factorial design, three factors are each varied at two levels, resulting in eight experimental conditions (2^3 = 8). This allows researchers to explore the effects of each factor and their interactions comprehensively, with an equal emphasis on all factors involved in the experiment.

## Steps in Conducting Factorial Design
**Step 1: Data Exploration and Visualization**
- Begin by looking at the data.
- Plot the response data in various ways to identify trends and check for normality.
- Examine the distribution of the response variable, regardless of factor levels, using normal probability plots, box plots, histograms, and Run Order Plans.
- Identify any structural patterns in the data that need to be considered when fitting a response model, such as distinct groups in the histogram.

**Step 2: Creating the Theoretical Model**
- Develop a theoretical model for a two to the fifth full factorial experiment.
- Initially assume that high-order interaction terms are non-existent, reducing the complexity of the model.
- Start with a model containing a mean term, main effects, two-factor interactions, three-factor interactions, and so on.
- Accumulate sums of squares for high-order interaction terms to estimate an error term, simplifying the model.
- Begin with a theoretical model containing 26 unknown constants, allowing data to reveal significant main effects and interactions.

**Step 3: Fitting the Model to the Data**
- Use statistical tools like R or Python to fit the model to the data.
- Generate a summary of the model, including R square, adjusted R square, root mean square error, mean of the response, and the number of observations.
- Identify significant effects by eliminating unnecessary terms with high p-values.
- Apply stepwise regression and remove terms with p-values larger than 0.05, arriving at a more concise model.
- Compare the new model's summary with the previous one, noting improvements in R square and adjusted R square, and a lower root mean square error.

**Step 4: Testing Model Assumptions**
- Plot residuals against predicted responses to assess common variance assumptions.
- Examine residual distribution using normal quantile plots, box plots, histograms, and Run Order Plans.
- If needed, transform the data and refit the model to achieve residuals with the assumed properties.
- Calculate an Optimum Box-Cox transformation to improve model behavior.
- Verify that the transformed model has better residuals and adheres to model assumptions.

**Step 5: Answering Experimental Objectives**
- Analyze the effect estimates to determine the importance of different factors and interactions.
- Identify the most critical factors, such as direction, batch, and real grid, based on effect magnitudes.
- Consider interactions' roles in influencing the response.
- Plot main effects and significant two-way interactions.
- Translate significant factor settings to maximize the desired outcome.
- Note that batch may have a significant impact on the response and explore ways to improve it.
- Discuss the impact of different experimental designs (e.g., longitudinal vs. transverse cuts) on model complexity and results.
- Mention the possibility of using a natural logarithm transformation for the response variable for further analysis.

### Step-By-Step Factorial Design Example Explained
 Here's how factorial design is applied in the example:

**Step 1: Data Exploration and Visualization**
Factorial design begins with data exploration and visualization. In this step, the text discusses how to look at the response data in different ways, such as through normal probability plots, box plots, histograms, and Run Order Plan diagrams. These visualizations help researchers identify trends, patterns, and distributions in the data. Factorial design emphasizes the importance of thoroughly understanding the data before proceeding with the analysis.

**Step 2: Creating the Theoretical Model**
Factorial design involves creating a theoretical model that represents the expected relationship between the factors and the response variable. In the example, a theoretical model for a two to the fifth full factorial experiment is developed. This model includes main effects, two-factor interactions, three-factor interactions, and so on. The assumption is made that high-order interaction terms are non-existent or negligible, simplifying the model. This step illustrates how factorial design helps structure and formalize the modeling process.

**Step 3: Fitting the Model to the Data**
Factorial design emphasizes the importance of fitting the theoretical model to the data using statistical tools like R or Python. The text mentions generating a summary of the model that includes various statistical metrics, such as R square, adjusted R square, root mean square error, and p-values. This step demonstrates how factorial design helps researchers quantitatively assess the model's goodness of fit to the data.

**Step 4: Testing Model Assumptions**
Factorial design includes a critical step of testing model assumptions. Residual analysis is performed by plotting residuals against predicted responses and examining residual distributions. If assumptions are violated, as indicated by plots and statistical tests, researchers may transform the data to meet the assumptions. This step highlights how factorial design ensures that the chosen model aligns with the data's characteristics.

**Step 5: Answering Experimental Objectives**
Factorial design is ultimately used to answer specific experimental objectives. In this example, the goal is to identify the most influential factors and interactions that affect the response variable (ceramic strength). Researchers analyze the magnitude of effect estimates and select factor settings that maximize ceramic strength. The example demonstrates how factorial design helps researchers draw meaningful conclusions and make informed decisions based on the experimental results.

Overall, factorial design provides a structured framework for conducting experiments, modeling relationships, and systematically analyzing data to gain insights into the effects of multiple factors on a response variable. It allows researchers to efficiently explore complex interactions and make data-driven decisions.



# Week 4. Fractional Factorial and Other Experimental Designs

Topics:
- Latin Square Design
	- Graeco-Latin Square Design
	- Hyper Graeco-Latin Square Design
	- Plackett-Burman design


## Fractional Factorial Design

Catapult Experiment: Determine the significant factors that affect the distance the ball is thrown by the catapult.
- Response: Distance (30,60,90)
	- The ball is a plastic gold ball
- Number of observations: 20
- Factors
	- Factor 1: Band height (2.25, 4.75)
	- Factor 2: Start angle (0,20 degrees)
	- Factor 3: Number of rubber bands (1,2)
	- Factor 4: Arm length(0,4 inches)
	- Factor 5: Stop angle (45, 80 degrees)
- Replication: 5 confirmatory runs at each setting

# Week 5. Regression and Response Surface Design 