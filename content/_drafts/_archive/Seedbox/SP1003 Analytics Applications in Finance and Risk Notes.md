---
tags:
alias:
creation-date: Saturday 27th May 2023
---

> [!NOTE]- Learning Objectives
> Upon completion of this course, you are expected to: 
> - recommend initiatives that would increase profitability, reduce cost, or optimize capital based on analytics and modeling done on finance and risk data; and
> - perform financial and risk analysis using statistical, modeling, optimization, and simulation techniques in Excel
> You will learn:
> - Forecasting & Correlation Analysis
> - Risk and Fraud Detection

# Week 1

> [!NOTE]- Week 1 Learning Objectives
> - articulate the relevance of analytics in finance and risk management;
> - identify appropriate analytical tools to aid decision making in the areas of finance and risk management problems; and
> - explain use cases of analytical tools as applied in finance and risk management.

- # Relevance of Analytics in Finance
	- ==*Why is analytics important in the field of Finance?*==
	- Application 1: It allows us to predict future trends by using past and current data.
	- Application 2: It allows us to determine which internal and external factors are indicative of financial performance.
- # Relevance of Analytics in Risk Management
	- ==*Why is analytics important in risk management?*==
	- Risk cannot be avoided but it can be minimized. Analytics provides tools that can be used to identify and manage risks.
	- Application 1: It allows us to identity potential high risk customers. This is very useful for businesses involved in lending. This is known as [[credit scoring]]
	- Application 2: It allows us to identify anomalous transactions
	- Application 3: It allows us to identify the worst level of loss of a financial asset. 
	- Application 4: It helps in identifying and minimizing potential operational risks in backend operational 
		- Staffing: Forecast how manpower is needed in high workload situations
		- Supply chain management


- # Use cases of analytics in Finance
	- Forecasting 
		- Forecasting is the process of projecting future performance of a business by using historical trends and influencing factors.
		- Forecasting Sales Volume, Expenses, Loses
		- Allows businesses to set reasonable goals
	- Correlation and classification
		- Used to identify economic indicators that are high predictors
	- Price optimization
		- Determines how the demand for a product will move with different prices.
	- Customer Lifetime Value (CLV) Analysis - Calculates the value of customers across the lifetime of their relationship with the bank.
		- Used to create retention startegies for customers, expansion startegies for gathering more customers and segmenting customers when creating new products.

- # Use cases of analytics in Management
	- Credit scoring 
		- This is the process of assessing the credit worthiness of a customer based on past and current transactions and information
		- This is a tool used to identify potential high-risk customers
		- ## Types of credit score
			- Application score - should a potential creditor be approved or not?
			- Behavior score - should a credit line of a customer be increased?
			- Collection score - what kind of collection strategy would be most effective to a customer
			- Recovery score - is there a chance to recover from a customer or not
	- Anomaly detection 
		- Is used to identify potential fraudulent activities
		- Is the process of surfacing activities that are outside the normal pattern.
	- Value at risk analysis
		- It is the process of estimating the worst level of losses that an investment may incur
	- Demand forecasting
		- This minimizes the risk of under/over production as well as under/over inventory.

Reflect:: For each use cases, ask ourself: WHY? Why is it important to a business/company? What problems does it solve or processes does it improve?

---
See also: [[SP1003 Analytics Applications in Finance and Risk]]


# Week 2

> [!NOTE]- Learning Objectives
> - explain the concept of correlation analysis;
> - explain the use and limitations of correlation analysis;
> - calculate correlation statistics given financial and economic data; and
> - interpret the results of correlation analysis.

- # Correlation analysis
	- **Correlation analysis** is a statistical technique which aims to establish whether a pair of variables is related. It is part of business analytics, alongside comparative and trend analysis.^[[Correlation Analysis: All the Basics You Need to Know | 365 Data Science](https://365datascience.com/trending/correlation-analysis/)]
	- # Correlation is not causation
		- Even if two variables are synchronized (correlated), it doesn't mean the one causes the other (causation).
		- Examples: [Correlation Does Not Imply Causation: 5 Real-World Examples - Statology](https://www.statology.org/correlation-does-not-imply-causation-examples/)
	- # Assumptions and Limitations *(Just keep these in mind*
		- Relationship between two variables is linear.
			- ![](https://i.imgur.com/v3jltWJ.png)

		- Correlation analysis will not work if there are outliers in the data
		- The correlation may show a high relationship when there is none. This might be because of another variable where the two are strongly correlated.
	- # What are the benefits of knowing correlation analysis?
		- By knowing **variables** that are correlated to **key financial metrics**, the business is equipped with advanced information to anticipate **potential opportunities** or **risk** and act accordingly.
		- ![](https://i.imgur.com/xzUCrEU.png)
		- Correlation is also often used to identify indicators that are external to the business that could have a high relationship to key business metrics such as sales volume or losses. This can include market data or economic data or a competitor's data (if available).  By monitoring these external indicators that have been identified through correlation, the business has an **early warning device** that they can use to create both **tactical and strategic action plans** to improve business performance.
	- Correlation analysis in excel is done using the Analysis Toolpak plugin.
	- Data diagnostic to check before computing for correlation. (See if data satisfies the assumptions)
		- The relationship should be linear (check by scatterplot)
		- There should be no outliers
	- How to compute for correlation coefficient
		- Data Tab > Data analysis > Correlation > Select Range > Results will appear in a separate sheet
	- Interpreting the correlation coefficient
		- A value of +1 indicates a strong positive relationship
		- A value of -1 indicates a strong negative relationship
		- A value of 0 means there is no correlation

# Week 3 Regression Analysis

> [!NOTE]- Learning Objectives
> - identify areas in business and finance where regression analysis can be used to forecast business metrics;
> - create a financial forecast using regression analysis;
> - interpret the result of regression analysis and provide business insights; and
> - apply regression analysis to solve a business problem.

- Regression analysis is a method of determining how the movement of one variable is influenced by the movement of one or more variables.
- There are **different types of regression analysis**, here are the most common:
	- Simple linear regression
	- Multiple linear regression
	- Nonlinear regression
- Applications of regression analysis in business includes:
	- forecasting sales volume
	- forecasting expense
	- forecasting revenue
	- forecasting losses
	- forecasting required headcount
	- forecasting supplies
- Things to check before using simple linear regression
	- 1. Homoscedasticity
	- 2. Normality
- Assessing the regression results (in Excel)
	- The Regression Statistics provides a summary of how well (or how badly) the regression result was able to predict the dependent variable.
	- The **Adjusted R-Square** measures how well the independent variable can explain the movement of the dependent variable with a penalty for the number of independent variables included in the model. (This is the [[coefficient of determination]])
		- In financial forecasting, the following guide is generally followed:
			- Below 40%: Weak
			- 40% to 70%: Moderate
			- Above 70%: Strong
	- The **Standard Error** measures on the average how far is the actual value of the dependent variable from the predicted value using the measurement of the dependent variable.
- Caveats when using simple linear regression:
	- First, the relationship of the Dependent variable and the Predictor variable is not always linear. Thus, simple linear regression might not always be the best tool to use for some data. 
	- Second, a single predictor variable may not be enough to capture the movement of the dependent variable. A combination of multiple variables may improve the prediction model.
	- Third, the forecasted value of the dependent variable is good only insofar as the value of the predictor variable is reliable. It is good practice for the analyst to put a disclaimer that the forecasted amount is based on the values of the predictor variable that was provided. Any change in the value of the predictor variable will warrant a re-calculation of the forecast. 
	- Lastly, always keep in mind that a forecast is not a crystal ball that will tell you definitively what will happen in the future. It only provides possible future outcomes for you to come up with an ”educated guess”  or “data-driven-decision”. Subject matter knowledge and judgement are still required.

# Week 4 Time Series Forecasting
- Time series is a collection of observations of well-defined data items obtained through repreated measurements over an equally-spaced time interval.
- Conditions for a time-series data
	- 1. The data needs to be well-defined (clear and consistent definition)
	- 2. Equally spaced time interval
- Three components of a time series data
	- 1. Seasonality (seasonal movement) - repetitive pattern
	- 2. Residual (irregular movement) - short term fluctuations; non-systematic, non-predictable
	- 3. Trend - long term movement
- Applications of time series analysis in finance
	- economic forecasting
	- sales forecasting
	- budgetary analysis
	- stock market analysis
	- yield projection
	- inventory analysis
	- workload projection, and the list goes on.
- **Time series analysis is most useful when the data that we want to forecast is largely dependent on the time component.**
	- For instance, companies wherein the demand for their products is driven by changes in the season would find time series analysis as an effective tool in forecasting demand as well as forecasting inputs such as inventory, manpower, capital, etc.
- **Time series analysis is also useful for businesses where the demand is dependent on the time of the day, such as:**
	- fast-food chains
	- restaurants
	- supermarkets
	- convenience stores
	- call centers
	- customer service centers, and the like
- **Time series analysis can help project the manpower requirement per time of the day or day of the week or day of the month.**
	- For food service industries, time series analysis can help determine a more detailed level of inventory to avoid spoilage.
	- For supermarkets and convenience stores, time series analysis can be used to determine the schedule of replenishment of goods on display as well as the scheduling of employees.
	- For call centers and customer service centers, time series analysis can be used to determine the optimal number of agents per time of the day and day of the week.
- Time series forecasts provide recommendation, not a definitive output.

# Week 5 Anomaly Detection
- Anomalous transactions are transactions that deviate from normal transaction patterns. 
	- Example: Logo commissioned for 3M
- Anomalous transactions that are undetected may result in losses in the business.
- How Anomalous Transactions Impact the Business
	- Reputational harm (Bangladesh bank case)
	- Losses in business
	- Possible bankruptcy
- Methods used in identifying anomalous transaction
	- Univariate Anomaly Detection
		- Uses one variable at a time
	- Multivariate Anomaly Detection
- Algorithms for Anomaly Detection
	- Machine learning-based - dependent on multiple iterations to detect outliers in the pattern
		- KMeans Clustering
		- Neural Networks
		- Nearest Neigbor
		- SVM
	- Statistics-based
		- IQR
		- Z-test
		- Student's t-test
		- Principal Components Analysis
- Anomaly Detection using IQR
	- First, visualize the data using a scatterplot. Check for (visual) outliers.
	- Calculate Quartile 1,2,3
	- Calculate IQR = Q3-Q1
	- Get the 
		- Upper bound= Q3+(IQR * 1.5)
		- Lower bound=Q1-(IQR * 1.5)
		- Note: The multiplier:1.5 may be adjusted based on the judgment of the business.
	- A record is an outlier if it is upper or lower than the upper bound and lower bound, respectively.