---
tags:
alias:
creation-date: Thursday 24th August 2023
---

- What is the minimum wage in Metro Manila?
- How many barangays are in Metro Manila?
---
# Basic Information
1. Manpower: 10 people
2. Work hours: 8 AM to 12 PM; 1 PM to 5 PM (Includes travel time) = ==basically 8 hours==
3. Length of interaction:
	1. **Answered:** Wait time (20 sec); Spiel Talk Time; Signing TIme (10 sec) => 60 secs
	2. **Did not answer:** Wait time (30 sec)
4. Sampler walk speed: 4 km/hr
5. Restriction 1: (at most) 10% of houses do not answer
6. Marketing agency claims:
	1. Hit success rate: 75% (Marketing agency claims; possible hypothesis)
	2. 25% conversion rate
	3. Average revenue: 200.00/year/person
7. Manufacturing cost: 40 PHP/SIM (including initial load)
8. Budget proposal: 5M
	1. Van rent: 10K/day => ==1M for 100 days== => 
---
- **Working budget: 5M**
	- Van: 1M
		- 10K/day => 1M for 100 days
	- Wage: 520,000
		- Minimumm wage in MM: 
			- 2020: 500 to 537 (520)
				- Total wage: 520 * 10 * 100
			- 2023: 610
				- Total wage: 610,000
---

# Planning
 Main question: Should we go with the agency or not?
 
 >  Objective is to increase the subscriber base (*increase conversion rate*) while obtaining a net profit (*revenue*).

## Problem
- Objective: Maximize Profit
- Constraints:
	- Budget (5M)
	- Time

# Profit
- Number of converted people * 200
	- `# converted` =  ` # of hits` * 25% (conversion rate)

Profit: Number of converted * 200
Number of converted: Number of hits * 25%
Number of hits: Total visited house * 10% * 75%

Total door-to-door time = 8 hours - Travel Time (from BGC)

Total working time (in mins): 8 * 60 = 480 mins
- Total households: 528 per worker
	- 10% of the time = rejected => 48 mins 
		- Total households = 48 mins/0.5 mins = 96 households
	- 90% accepted: 
		- Total households = 432 min/1 min = 432


> [!NOTE] Total Households
In one day: 5280 households.


---
## KPI's
- Hit: When the sample successfully given a SIM card
- Conversion rate: percent of activated SIMs
- Revenue return
---
Needed data: 
- Baranggays in MM, with population/household data.
- Traffic data, distance of baranggays from BGC
- SIM card use/Load use/Cellphone use data


---

- [ ] V. **Financial Feasibility**
   A. Estimate all costs associated with the project.
   B. Predict potential sources of revenue and income.
   C. Analyze whether benefits outweigh costs through a cost-benefit analysis.
   D. Determine the potential return on investment (ROI) for stakeholders.
- [ ] VI. **Operational Feasibility**
   A. Explore how the project will integrate with existing processes.
   B. Assess how resources will be allocated and utilized.
   C. Discuss potential impacts on the organization's operations.
   D. Evaluate the practicality of the proposed implementation plan.
- [ ] XI. **Stakeholder Analysis**
   A. Identify all parties involved or affected by the project.
   B. Understand their interests, concerns, and roles.
   C. Provide strategies to manage and engage stakeholders effectively.


---
# Proposed Research Design
**Research Design**
This research follows an operational research design. Operational research focuses on understanding how the proposed project will be managed and operated. It involves assessing factors such as human resources, skills required, operational processes, and potential challenges.

Main objective: Maximize profit

- [x] Cost-benefit analysis: Should we take on the marketing agency or not?
- [ ] Nonlinear Integer Programming

---
## Net Profit
Let P denote the net profit.
Let D denote the number of campaign days.
Let H be the ave num of visited houses per worker.
Let W denote the number of workers

Number of SIMS to make: $DH \times 0.9 \times 0.75$

Objective function: Net Profit

$$P = [200(0.25)(0.75)(0.9)DH] - [10000D + 610DH + (40)(0.9)(0.75)DH]$$

Constraints:


---
P = REVENUE - COST
P = H(0.9)(0.75)(0.25)(200)