---
title: "Data Science for Business: What You Need to Know About Data Mining and Data-Analytic Thinking"
---
# II. Business Problems and Data Science Solutions

## The Data Mining Process

![587](https://i.imgur.com/2aGe0kN.png)


1. Business Understanding = Translate business questions into data science questions
2. Data Understanding = Understand how the available data can be used
3. Data Preparation = Transforming data into a form that can be analyzed.
4. Modeling = Capturing patterns in the data
5. Evaluation = Assessing the results of data mining
6. Deployment

**It is tempting—but usually a mistake—to view the data mining process as a software development cycle.**

This can be a mistake because data mining is an exploratory undertaking closer to research and development than it is to engineering. The CRISP cycle is based around exploration; it iterates on approaches and strategy rather than on software designs. Out comes are far less certain, and the results of a given step may change the fundamental understanding of the problem. Engineering a data mining solution directly for deploy ment can be an expensive premature commitment.

# III. Introduction to Predictive Modeling: From Correlation to Supervised Segmentation

***information is a quantity that reduces uncertainty about something***
For example: If an old pirate gives me information about where his treasure is hidden that does not mean that I know for certain where it is, it only means that my uncertainty about where the treasure is hidden is reduced. The better the information, the more my uncertainty is reduced.

**a model is a simplified representation of reality created to serve a purpose**
It is simplified based on some assumptions about what is and is not important for the specific purpose, or sometimes based on constraints on information or tractability. 
For example, a map is a model of the physical world. It abstracts away a tremendous amount of information that the mapmaker deemed irrelevant for its purpose. It preserves, and sometimes further simplifies, the relevant information.

In data science, a **predictive model** is a formula for estimating the unknown value of interest: the target. The formula could be mathematical, or it could be a logical statement such as a rule. Often it is a hybrid of the two. Given our division of supervised data mining into classification and regression, we will consider classification models (and class-probability estimation models) and regression models.

