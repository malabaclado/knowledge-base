
> [!tip] 
> Create a backup worksheet of your data before doing anything

# The Process
1. Get an overview of your data
2. Perform data cleaning
3. Make pivot tables (+ analyze/generate insights)
4. Make charts
5. Make the dashboard


> [!Tips]
> - **Create a backup** inside the excel file by duplicating the worksheet.
> - Create Pivot Tables first before creating or even thinking about the dashboard design.
> - Always add chart and axes titles
> 	- If its a count, you may remove the vertical axes title, esp if it is obvious from the chart title.
> - It is good practice to name your pivot tables so that you will not be confused when you create slicers and make connections.

# Specific Steps in the Video
- Step 1: Get an overview of your data
	- Know what the columns are, what they represent, what type of data should be there.
	- Tool: Sort and Filter  (To easily see what data are in each column)
- ## Data Cleaning
	- Step 2: Remove duplicates
		- Highlight all columns and remove duplicates
		- Tool: Remove duplicates < Data Tools
	- Step 3: Clarity
		- Replace M/S to Married/Single in Marital Status.
		- Replace M/F to Male/Female in Gender.
		- Tool: Find and Replace (Shortcut: CTRL+H)
	- Step 4: Age
		- Usually you'd want your age data to be an interval (or a category) instead of specific number.
		- Create new column with age intervals
		- Tool: IFS Function
- ## Building Pivot Tables
	- Tip: Create Pivot Tables first before creating or even thinking about the dashboard design.
	- Step 5: Create Pivot Tables
		- First table: Average income of people who bought or did not bought a bike
		- Second Pivot Table: Distance and Bike Purchase
		- Third Pivot: Age and Bike Purchase
	- Step 6: Create chart
		- Tip: Add axes titles and chart titles
		- Adding data tables makes chrrts easier to read
- ## Building a dashboard
	- Get rid of gridlines (View>Gridlines)
	- Add slicer
	- Apply slicers to all tables.
	- Tip: It is good practice to name your pivot tables so that you will not be confused when you create slicers and make connections.