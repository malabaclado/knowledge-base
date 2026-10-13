# Week 1 - Importance of Data Integrity

> A strong analysis depends on the integrity of the data.

- **Data integrity** is the accuracy, completeness, consistency, and trustworthiness of data throughout its lifecycle.
- The **data manipulation process** involves changing the data to make it more organized and easier to read. Data manipulation is meant to make the data analysis process more efficient, but an error during the process can compromise the efficiency.
- **Data replication** is the process of storing data in multiple locations. If you're replicating data at different times in different places, there's a chance your data will be out of sync.
- A good analysis depends on the integrity of the data, and data integrity usually depends on using a common format.
- Here are some other things to watch out for:
	- **Data replication compromising data integrity** 
		- Continuing with the example, imagine you ask your international counterparts to verify dates and stick to one format. One analyst copies a large dataset to check the dates. But because of memory issues, only part of the dataset is actually copied. The analyst would be verifying and standardizing incomplete data. That partial dataset would be certified as compliant but the full dataset would still contain dates that weren't verified. Two versions of a dataset can introduce inconsistent results. A final audit of results would be essential to reveal what happened and correct all dates. 
	- **Data transfer compromising data integrity** 
		- Another analyst checks the dates in a spreadsheet and chooses to import the validated and standardized data back to the database. But suppose the date field from the spreadsheet was incorrectly classified as a text field during the data import (transfer) process. Now some of the dates in the database are stored as text strings. At this point, the data needs to be cleaned to restore its integrity. 
	- **Data manipulation compromising data integrity** 
		- When checking dates, another analyst notices what appears to be a duplicate record in the database and removes it. But it turns out that the analyst removed a unique record for a company’s subsidiary and not a duplicate record for the company. Your dataset is now missing data and the data must be restored for completeness.
- [[Reference - Data Constraints and Examples]]
- ==It's also important to check that the data you use aligns with the business objective.== This adds another layer to the maintenance of data integrity because the data you're using might have limitations that you'll need to deal with.
- *With incomplete data, it's hard to see the whole picture to get a real sense of what is going on.*
- Learning how to deal with data issues while staying focused on your objective will help set you up for success in your career as a data analyst.
- # # Well-aligned objectives and data
	- When there is clean data and good alignment, you can get accurate insights and make conclusions the data supports.
	- If there is good alignment but the data needs to be cleaned, clean the data before you perform your analysis.
	- If the data only partially aligns with an objective, think about how you could modify the objective, or use data constraints to make sure that the subset of data better aligns with the business objective.
- # How to deal with insufficient data
	- What you can do when you have insufficient data:
		- Identify trends with the available data
		- Wait for more daya if time permits
		- Talk with stakeholders and adjust your objective
		- Look for a new dataset
	- Types of insufficient data
		- Data from only one source
		- Data that keeps updating
		- Outdated data
		- Geographically-limited data
- [[What to do when you find an issue with your data]]
- [[Calculating the sample size]]
- # Statistical power
	- Statistical power is the probability of getting meaningful results from a test.
	- Hypothesis testing is a way to see if a survey or experiment has meaningful results.
- [[What to do when there is no data]]
- [[Sample size calculator]]
- [[About margin of error]]
- 
# Week 2 - Data Cleaning
- Dirty data is data that's incomplete, incorrect, or irrelevant to the problem you're trying to solve.
- [[Types of dirty data]]
	1. Duplicate data
	2. Outdated data
	3. Incomplete data
	4. Incorrect data
	5. Inconsistent (formatting) data
- ## Data cleaning tools and techniques
	- Before removing unwanted data, it's always a good practice to make a copy of the data set. That way, if you remove something that you end up needing in the future, you can easily access it and put it back in the data set.
- ## Data cleaning steps
	- Remove duplicate data
	- Remove unwanted/unrelated data
	- Remove spaces and blanks (in spreadsheets)
	- Fixing spellings, punctuation,and typos
- [[Common data cleaning mistakes]]
- ## Cleaning data in spreadsheets
	- Conditional formatting
		- Makes unwanted data stand out
			- Highlight blank cells
	- Remove duplicates (Data > Remove duplicates)
	- Consistent date formatting (Number > Date type)
	- Split text to columns (Data > Split text to columns)
		- Can be used to convert text string(eg. "707") to number (707).
- [[Workflow automation]]
- Sorting and Filtering
- Pivot Tables
- VLOOKUP
- 
# Week 3 - Cleaning data with SQL
- *Basic course*. Passed via assessments.
# Week 4 - Verifying and reporting your cleaning results
- **Verification** is a process to confirm that a data cleaning effort was well- executed and the resulting data is accurate and reliable. 
	- It involves rechecking your clean dataset, doing some manual clean ups if needed, and taking a moment to sit back and really think about the original purpose of the project. 
	- That way, you can be confident that the data you collected is credible and appropriate for your purposes. 
- A **changelog** is a file containing a chronologically ordered list of modifications made to a project. It's usually organized by version and includes the date followed by a list of added, improved, and removed features.
- ## Steps in verification
	- 1. Go back to your original dataset and compare your cleaned data. Go back to common problems.
	- 2. Take a big picture view of your project 
		- *Consider the business problem you're trying to solve.*
		- *Consider the goal of the project. Does the data you've collected and cleaned help your company towards this goal?*
		- *Consider the data is meeting the project objectives.*
	- *Tip: Ask teammates for fresh perspectives of the data.* 
- Verifying your data ensures that the insights you gain from analysis can be trusted. It's an essential part of data-cleaning that helps companies avoid big mistakes. 
- [[Checklist for data verification]]


# Week 5 - Optional: Adding data to your resume
- Keep in mind, you'll need to find a balance between what you want, what they want to give you, and what's fair. 
- ## Creating a resume
	- You can think of building a resume as taking a picture, a snapshot, of your skills.
	- The key here is to be brief. 
		- Try to keep everything in one page and each description to just a few bullet points. Two to four bullet points is enough but remember to keep your bullet points concise.
	- Stick to one page
		- Sticking to one page will help you stay focused on the details that best reflect who you are or who you want to be professionally. 
		- One page might also be all that hiring managers and recruiters have time to look at. They're busy people, so you want to get their attention with your resume as quickly as possible. 
	- Include your contact information
		- Name, Address, Contact Number, Email address
	- A format that focuses more on skills and qualifications and less on work history is great for people are starting out.
	- Summary: Entry-level data analytics professional; recently completed Google Data Analaytics Certificate.
	- Formula:
		- Accomplished [X] as measured by [Y] by doing [Z].
	- Technical Skills
	- Language proficiency
- ## Making your resume unique
	- For data analytics, one of the most important things your resume should do is show that you are a clear communicator.
	-  Speaking of the skill section, make sure you include any skills and qualifications you've acquired through this course and on your own.
		- You might even add in the top functions, packages or formulas that you're comfortable with in each. It also makes sense to include skills you've acquired in spreadsheets like pivot tables.
- [[Soft-skills to add to your resume]]
- Junior data analyst roles
	- Healthcare analyst
	- Marketing analyst
	- Business intelligence analyst
	- Financial analyst


# Week 6 - Course Challenge