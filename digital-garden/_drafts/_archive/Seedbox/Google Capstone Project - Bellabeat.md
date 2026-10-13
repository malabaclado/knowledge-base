---
tags:
alias:
creation-date: Wednesday 30th August 2023
---

**Scenario**
You are a junior data analyst working on the marketing analyst team at Bellabeat, a high-tech manufacturer of health-focused products for women. Bellabeat is a successful small company, but they have the potential to become a larger player in the global smart device market. Urška Sršen, co-founder, and Chief Creative Officer of Bellabeat, believes that analyzing smart device fitness data could help unlock new growth opportunities for the company. You have been asked to focus on one of Bellabeat’s products and analyze smart device data to gain insight into how consumers are using their smart devices. The insights you discover will then help guide the marketing strategy for the company. You will present your analysis to the Bellabeat executive team along with your high-level recommendations for Bellabeat’s marketing strategy.

**Characters**
- Urška Sršen: Bellabeat’s co-founder and Chief Creative Officer
- Sando Mur: Mathematician and Bellabeat’s co-founder; key member of the Bellabeat executive team
- Bellabeat Marketing Analytics Team: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide Bellabeat’s marketing strategy. You joined this team six months ago and have been busy learning about Bellabeat’s mission and business goals — as well as how you, as a junior data analyst, can help Bellabeat achieve them.

**Products**
- Bellabeat App: The Bellabeat app provides users with health data related to their activity, sleep, stress, menstrual cycle, and mindfulness habits. This data can help users better understand their current habits and make healthy decisions. The Bellabeat app connects to their line of smart wellness products.
- Leaf: Bellabeat’s classic wellness tracker can be worn as a bracelet, necklace, or clip. The Leaf tracker connects to the Bellabeat app to track activity, sleep, and stress.
- Time: This wellness watch combines the timeless look of a classic timepiece with smart technology to track user activity, sleep, and stress. The Time watch connects to the Bellabeat app to provide you with insights into your daily wellness.
- Spring: This is a water bottle that tracks daily water intake using smart technology to ensure that you are appropriately hydrated throughout the day. The Spring bottle connects to the Bellabeat app to track your hydration levels.
- Bellabeat Membership: Bellabeat also offers a subscription-based membership program for users. Membership gives users 24/7 access to fully personalized guidance on nutrition, activity, sleep, health and beauty, and mindfulness based on their lifestyle and goals.

# Ask Phase

In this phase, we define the problem and business objectives, and identify the key stakeholders.

**Scenario**
You are a junior data analyst working on the marketing analyst team at Bellabeat, a high-tech manufacturer of health-focused products for women. Bellabeat is a successful small company, but they have the potential to become a larger player in the global smart device market. Urška Sršen, co-founder, and Chief Creative Officer of Bellabeat, believes that analyzing smart device fitness data could help unlock new growth opportunities for the company. You have been asked to focus on one of Bellabeat’s products and analyze smart device data to gain insight into how consumers are using their smart devices. The insights you discover will then help guide the marketing strategy for the company. You will present your analysis to the Bellabeat executive team along with your high-level recommendations for Bellabeat’s marketing strategy.

## Key Stakeholders
- Urška Sršen: Bellabeat’s co-founder and Chief Creative Officer
- Sando Mur: Mathematician and Bellabeat’s co-founder; key member of the Bellabeat executive team
- Bellabeat Marketing Analytics Team: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide Bellabeat’s marketing strategy. You joined this team six months ago and have been busy learning about Bellabeat’s mission and business goals — as well as how you, as a junior data analyst, can help Bellabeat achieve them.

## Deliverables
For this project, we'll be preparing the following deliverables:
1. A clear summary of the business task
2. A description of all data sources used
3. Documentation of any cleaning or manipulation of data
4. A summary of your analysis
5. Supporting visualizations and key ﬁndings
6. Your top high-level content recommendations based on your analysis

## Business Task


## Guide for analysis 
We'll focus on the bellabeat app, leaf and time.  Leaf and Time are bellabeat products that track activity, sleep and stress.

**Key Questions for Analysis**
1. How many users track their:
	1. (Physical Acvitity) Calories, Steps, Intensity 
	2. Sleep 
	3. Weight
	4. Heart Rate
2. How many days did each user track their:
	1. (Physical Acvitity) Calories, Steps, Intensity 
	2. Sleep 
	3. Weight
	4. Heart Rate
3. Calculate the average number of minutes per activity per user
4. Calculate the average number of minutes per activity over the entire population
	1. On the average, how many minutes were the users:
		1. very active?
		2. fairly active?
		3. lightly active?
		4. sedentary?
	2. Calculate summary statistics (min, max, median)
5. Determine the time when users are :
	1. mostly active
	2. mostly sedentary
6. Determine the days when users are 
	1. mostly active
	2. mostly sedentary




**Key questions for analysis**
1. What are some trends in smart device usage?
2. How could these trends apply to Bellabeat customers?
3. How could these trends help inﬂuence Bellabeat marketing strategy?

## Key Questions for Data Exploration
- What is your data all about? What data is being tracked?
- How many respondents track their sleep? their steps? their heart rate? their physical activity?
- Can you profile the respondents?
	- What is their BMI? What is their body type?
	- How many of them have active lifestyle? sedentary lifestyle?
	- How many of them have complete sleep? Less sleep?
	- How many naps do they take in a day?
- Can you find a general behavior among the respondents?
	- When do they usually walk? workout? 
	- Is there a difference in their behavior during weekends than on weekdays?
- Others
	- How many days are the participants considered active? 
	- How much time do they consider being sedentary? What could be the possible effects of this to their health?
	- What time do people have the highest calorie burn? The lowest calorie burn? What could be a contributing factor to this?
	- Have the participants been following a steady sleep schedule?
	- What is their sleep time?

- Inspiring visualizations
	- Days of the week VS Number of steps; Calories burned' Minutes active/Sedentary

- **Goal**
	- Have a daily and hourly dataset.
	- Have a weight of each participant.


# Prepare

## About the dataset
The [FitBit Fitness Tracker dataset](https://www.kaggle.com/datasets/arashnic/fitbit) is a result of individuals engaging in a distributed survey via Amazon Mechanical Turk spanning from March 12, 2016, to May 12, 2016. Within this timeframe, thirty eligible Fitbit users willingly contributed their personal tracker data. This dataset comprises comprehensive daily, hourly and on-the-minute-level records of physical activity, heart rate, and sleep monitoring. It was downloaded from Kaggle.

## Licensing
The information is made available under the [Creative Commons CC0](https://creativecommons.org/publicdomain/zero/1.0/) Public Domain license. This allows anyone to freely use, modify, and distribute the data without seeking permission or providing attribution to the original creator.

## Usability
The dataset holds a Kaggle usability score of 10.0. This usability score which assesses the data's comprehensiveness, reliability, and suitability for use.

## Dataset Columns
1. Daily Activity
	1. id: varchar
	2. activitydate:dataset 
	3. totalsteps
	4. totaldistance
	5. trackerdistance
	6. loggedactivitydistance
	7. veryactivedistance
	8. moderatelyactivedistance
	9. lightactivedistance
	10. sedentaryactivedistance
	11. veryactiveminutes
	12. farlyactiveminues
	13. lightlyactiveminutes
	14. sedentaryminutes
	15. calories
2. 


## Importing the dataset 
Create `fitbit` database and import the csv files.
![[Pasted image 20230901192604.png]]

Checking the data type of each table.
![[Pasted image 20230901192730.png]]

# Process
## Tools
SQL - for data cleaning and initial analysis
Tableau - for data visualization

## Data Cleaning
- [ ] Remove nulls
- [ ] Check data type
- [x] Checking data integrity

## Verifying data integrity 
- Checking for NULL values
- 

# Analyze


## User tracking
**How many users track their physical activity?** 35 users
**How many users track their sleep?** 24 users
**How many users track their weight?** 11 users
**How many users track their heart rate?** 15 users


**How many days did each user track their physical activity?**
The number of tracking days among users is inconsistent. One user has records for 60 days. Most of them has records from 30 to 42 days. Two users track below 10 days only.

**How many days did each user track their sleep?**
The number of sleep tracking days among users is also inconsistent. 12 users tracked for more than 20 days, the other 12 users have records less than 20 days.

**How many days did each user track their weight?**
Most users tracked their weight only once. Three of them tracked their weight multiple times over the study period. One user tracked 14 times. 

**How many days did each user track their heart rate?**
The number of days heart rate is tracked also varies among users. 13 users tracked for more than 25 days while two users tracked for less than 10 days.


> [!NOTE]
> For daily activity data, we will narrow down our analysis to 30 users who used the tracker under 30 days from April 1 to May 1. For the hourly data, we'll focus on 35 users over 30 days. For weight data, we'll consider 11 users

**Calculate the average number of minutes per activity per user**
Overall, the average amount of time where users are very active is 24 mins, fairly active for 14 mins, lightly active for 200 mins ans sedentary for 986 mins. This calls for a need to remind or to motivate people to become active.

On the average, the participants spend around 236 mins with varying degrees of activity while 986 mins being sedentary. This is a 24% ratio of active to sedentary time.


==Visual: ==


**Determine when the users are most active/ most sedentary**
Highest mins:
- very active: Monday (26 mins)
- fairly active: Saturday & Thursday (15 mins)
- lightly active: Saturday (214 mins)
- sedentary: Monday (1021 mins)


Most active: Saturday (251 avg active minutes)
Most sedentary: Monday (1021 avg sedentary mins)

**Determine the average number of steps, distance and calories burned per user and overall**

Overall, the average steps of the 30 users over the period of study is 7,821. The average distance covered is 5.45 with an average of 2,307 calories burned.

Insight:
- As expected, the total distance covered is proportional to number of steps.
- It seems that the number of calories burned does not depend on the number of steps.

**Determine the day with the most number of steps, distance and calories burned**
- Most steps: Saturday
- Most distance: Saturday
- Most calories burned: Thursday

**Determine the time when users are most active/most sedentary:**
- Time Division:
	- 4-division
		- Morning: 6 AM to 12 NN
		- Afternoon 12 NN to 6 PM
		- Evening: 6 PM to 12 MN
		- Late Evening: 12 MN to 6 AM
	- 6-division
		- 6 AM to 10 AM: Morning
		- 10 AM to 2 PM: Midday
		- 2 PM to 6 PM : Afternoon
		- 6 PM to 10 PM: Evening
		- 10 PM to 2 AM: Late evening
		- 2 AM to 6 AM: Early morning
- Most active: Afternoon (12 NN to 6 PM)
- Least active: Late Evening (12 MN to 6 AM)

**Is there a difference in hourly activities in weekdays and weekends?**
There is no noticeable difference between weekdays and weekends

### SLEEP DATA
- Average sleep mins: 377.67
- Average time in bed: 420.13
- Average idle time in bed: 42.42
- Of the time spent in bed, 90% was used for sleeping, 10% was used idle.


What factors affect the number of calories burned?


# Share
Visuals to investigate:
1. Determine what day the users have the highest activity time and sedentary time -- show that the users are
2. Compare the users' steps, distance and calories burned
3. Determine the day with the most number of steps, distance and calories burned
4. Determine what time of the day users are most active
5. Determine if there is a difference in activity in weekdays and weekends
6. Compare the average sleep time, time in bed and idle time spent in bed.



## Dashboard ideas
1. Heatmap of daysxtime - showing activity


# Act
Give recommendations
