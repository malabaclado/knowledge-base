---
tags:
alias:
creation-date: Wednesday 5th July 2023
---

As a data analyst, you can do all the necessary work of planning, collecting, cleaning, and analysis. But you also need to show stakeholders what your data means in a compelling way using visuals.


# Week 1 Visualizing data
Data visualization is in many ways the culmination of the data analysis process. In this part of the course, you will be introduced to the concepts involved in data visualization. You will learn about accessibility, design thinking, and other factors that play a role in visualizing the data in your analysis.

==**Data visualization** is the graphic representation and presentation of data.== In reality, it's just putting information into an image to make it easier for other people to understand. 

As an analyst in today's world, you'll probably split your time with data visuals in two ways: 
	1. looking at visuals in order to understand and draw conclusions about data, or 
	2. creating visuals from raw data to tell a story. 

### Five-second Rule
**A quick rule for data visualization:** ==Your audience should know exactly what they're looking at within the first five seconds of seeing it.== Basically, this means the visual should be clear and easy to follow. In the five seconds after that, your audience should understand the conclusion your visualization is making.

Other people might not know or understand the exact steps you took to come to the conclusions you've made, but that shouldn't stop them from understanding your reasoning. Basically, an **effective data visualization should lead viewers to reach the same conclusion you did, but much more quickly.**


## Four elements for a good data visualization (David McCandless)
![](https://i.imgur.com/cZj1WUN.png)

#article:[What Makes A Good Data Visualization? — Information is Beautiful](https://informationisbeautiful.net/visualizations/what-makes-a-good-data-visualization/)




- # Effective data visualizations
	- Two frameworks for organizing your thoughts about visualization
		- ### McCandless Method
			- McCandless Method lists four elements of good data visualization:
				- **Information (data):** The information or data that you are trying to convey is a key building block for your data visualization. Without information or data, you cannot communicate your findings successfully.
				- **Story (concept):** Story allows you to share your data in meaningful and interesting ways. Without a story, your visualization is informative, but not really inspiring.
				- **Goal (function):** The goal of your data visualization makes the data useful and usable. This is what you are trying to achieve with your visualization. Without a goal, your visualization might still be informative, but can’t generate actionable insights.
				- **Visual form (metaphor):** The visual form element is what gives your data visualization structure and makes it beautiful. Without visual form, your data is not visualized yet.
			- ==One useful way of approaching this framework is to notice the parts of the graphic where there is incomplete overlap between all four elements.== For example, visual form without a goal, story, or data could be a sketch or even art. Data plus visual form without a goal or function is eye candy. Data with a goal but no story or visual form is boring. All four elements need to be at work to create an effective visual.
		- ### Kaiser Fung's Junk Charts Trifecta Checkup
			- This approach is a useful set of questions that can help consumers of data visualization critique what they are consuming and determine how effective it is. The Checkup has three questions:
				- 1. What is the practical question?
				- 2. What does the data say?
				- 3. What does the visual say?
			- [Junk Charts Trifecta Checkup: The Definitive Guide - Junk Charts (typepad.com)](https://junkcharts.typepad.com/junk_charts/junk-charts-trifecta-checkup-the-definitive-guide.html)
- ## Pre-attentive attributes: Marks and Channels
	- Marks
		- Position - Where a specific mark is in space in relation to a scale or to other marks
		- Size - How big, small, long, or tall a mark is
		- Shape - Whether a specific object is given a shape that communicates something about it
		- Color - What color the mark is
	- Channels
		- Accuracy - Are the channels helpful in accurately estimating the values being represented?
		- Popout - How easy is it to distinguish certain values from others?
		- Grouping - How good is a channel at communicating groups that exist in the data?
- ## Design Principles
	- Choose the right visual
		- One of the first things you have to decide is which visual will be the most effective for your audience. Sometimes, a simple table is the best visualization. Other times, you need a more complex visualization to illustrate your point.
	- Optimize the data-ink ratio 
		- The data-ink entails focusing on the part of the visual that is essential to understanding the point of the chart. Try to minimize non-data ink like boxes around legends or shadows to optimize the data-ink ratio.
	- Use orientation effectively
		- Make sure the written components of the visual, like the labels on a bar chart, are easy to read. You can change the orientation of your visual to make it easier to read and understand.
	- Color 
		- There are a lot of important considerations when thinking about using color in your visuals. These include using color consciously and meaningfully, staying consistent throughout your visuals, being considerate of what colors mean to different people, and using inclusive color scales that make sense for everyone viewing them.
	- Number of things
		- Think about how many elements you include in any visual. If your visualization uses lines, try to plot five or fewer. If that isn’t possible, use color or hue to emphasize important lines. Also, when using visuals like pie charts, try to keep the number of segments to less than seven since too many elements can be distracting.
- ## Connecting images with data
	- Bar graphs - compares categories
	- Line graph - shows shifts and changes in data
	- Pie chart - shows how much something takes from a whole
	- Maps - used for geographical data
- ## Why should data analysts care about data visualization?
	- To communicate to the audience the results of your analysis without actually going through the analysis themselves.
	- It is effective because people's eyes are naturally drawn to colors, shapes and patterns.
- [[Data visualization inspirations]]
- Remember: ==an important component of being a data analyst is the ability to communicate your findings in a way that will appeal to your audience.== Data visualization has the ability to make complex (and even monotonous) information easily understood, and knowing how to utilize data visualization is a valuable skill to have. Your goal is always to help the audience have a conversation with the data so your visuals draw them into the conversation. This is especially true when you have to help your audience engage with a large amount of data, such as the flow of goods from one country to other parts of the world.
- ## How to take your findings and turn them into compelling visuals
	- ==One of your biggest considerations when creating a data visualization is where you'd like your audience to focus.== Showing too much can be distracting and leave your audience confused. In some cases, restricting data can be a good thing. On the other hand, showing too little can make your visualization unclear and less meaningful. 
	- As a general rule, as long as it's not misleading, you should visually represent only the data that your audience needs in order to understand your findings.
	- If your analysis involves how the data has changed over a certain period, which could be days, weeks, months, or years. You can set your visualization to show only the time period relevant to your objective.
	- If your data needs to be ranked, like when ordering the number of responses to survey questions. You should first think about what you want to highlight in your visualization. Bar charts with horizontal bars effectively show data that are ranked, with bars arranged in ascending or descending order. ==A bar chart should always be ranked by value==, unless there's a natural order to the data like age or time, for example. 
	- Correlation charts can show relationships among data, but they should be used with caution because they might lead viewers to think that the data shows causation. Causation or a cause-effect relationship occurs when an action directly leads to an outcome. 
- [[Correlation and Causation]]
- ## Dynamic visualizations
	- Static - do not change; Dynamic - interactive/changes over time
	- Having an interactive visualization can be useful for both you and the audience you share it with. But it's good to remember that ==the more power you give the user, the less control you have over the story you want the data to tell==. It's something to keep in mind as you learn how to create your own visualizations. ==You want to find the right balance between interactivity and control.== 
- [[Decision trees for data visualization]]
- # Design data visualizations
	- ## Elements of Art
		- Line
		- Shape 
			- The shape you use should easily inform the audience the type of data you are using.
		- Color 
			- Hue
			- Intensity
			- Value (Shades/Tints)
		- Space
			- There should always be space between data visualizations
		- Movement
			- Used to create a sense of flow
			- Should be used sparingly
	- [[Principles of Design]]
	- ## Impact of Data Visualization
		- Choosing the right visualization for your data findings can often come down to one question. Which one will make it easiest for the user to understand the point you're trying to make?
		- No matter how complex your analysis is, your audience will only care about what's in front of them and how easy they can understand it.
		- Then there's charts that show parts of a whole. This is known as **data composition**, and it's achieved by combining the individual parts of a visualization and displaying them together as a whole.
			- Eg. Stacked bar, Donut, Pie, Treemaps
		- And it all starts in the brain, when processing information our brains try to find patterns and rely on visual context. As data analysts, we can use our understanding of the human visual system to produce better visuals. When we create visualizations, we can do so in a way that helps the audience process the information and helps them remember what they're seeing.
		- ## Three elements for effective visuals
			- Visual journalists Dona Wong proposes that effective visuals, like the database we've been discussing here have three essential elements. 
				- The first is **clear meaning**, good visualizations clearly communicate their intended insight. 
				- The second is a **sophisticated use of contrast**, which helps separate the most important data from the rest using visual context that our brains naturally look for. 
				- The third essential element for effective visuals is **refined execution**. 
	- [[Examples of Good Data Visualizations]]
	- ## Design Thinking and visualizatoins
		- **Design thinking** is a process used to solve complex problems in a user-centric way.
			- When you bring design thinking into your work, you're trying to identify alternative strategies for your visualizations that might not be clear right away. You have to challenge your own thinking and explore different ways of approaching the problems and finding solutions. 
			- If you use design thinking when planning and creating your data viz, you'll be making decisions based on the needs of the people who will be viewing them. This way your audience will be engaged and enlightened by how you visualize your findings.
		- ## Five phases that you can use when creating data visualizations
			- Emphatize
				- You think about the emotions and needs of the target audience of your data viz.
				- Here you should avoid areas where people might face obstacles interacting with your visualizations.
				- You consider visually impaired audience.
			- Define
				- This phase helps you to find your audiences needs, their problems, and your insights.
				- You could use this phase to think about which data to show in your visualization.
				- While you'll need to meet your objectives, there might be data that could make these people uncomfortable.You can think of ways to position that data to make it more digestible.
			- Ideate 
				- You start to generate your data viz ideas. You'll use all of your findings from the empathize and define phases to brainstorm potential data viz solutions.
				- Creating drafts, experimenting with different shapes.
				- Tip: Always remember your audience.
			- Prototype
				- Here you'll start putting your charts, dashboards or other visualizations together.
			- Test
				- You could test your visualizations by showing them to team members before presenting them to stakeholders. 
					- If you've created more than one for the same data, you can share all of your options.
		- [[Design thinking for visualization improvement]]
- # Explore visualization considerations
	- ## On headlines, subtitles and labels
		- A headline is a line of words printed in large letters at the top of the visualization to communicate what data is being presented. It's the attention-grabber that makes your audience want to read more.
		- The typography and placement of the headline is important too. It's best to keep it simple. Make it bold or a few sizes larger than the rest of the text and place it directly above the chart, aligned to the left. 
		- Then, explain your data viz even further with a subtitle. A subtitle supports the headline by adding more context and description. Use a font style that matches the rest of the charts elements and place the subtitle directly underneath the headline. 
	- [[Pro tips for hghlighting key information]]
	- ## Making visualizations accessible
		- Before you design a data viz, it's important to keep that fact in mind. Not everyone has the same abilities, and people take in information in lots of different ways. You might have a viewer who's deaf or hard of hearing and relies on captions, or someone who's color blind might look to specific labeling for more description.
		- **Labelling.** It helps to label data directly instead of relying exclusively on legends, which require color interpretation and more effort by the viewer to understand. This can also just make it a faster read for those with or without disabilities.
		- **Text alternatives.** Alternative text provides a textual alternative to non-text content. It allows the content and function of the image to be accessible to those with visual or certain cognitive disabilities.
		- **Common color blindness.** **Red-green color blindness** is the most common and occurs when red and green look like the same color. You can avoid placing green on red or red on green in your visualizations. **Blue-yellow color blindness** is less common and occurs when it is difficult to tell the difference between blue and green, or yellow and red. You can also avoid using these colors on top of or next to each other.
		- **Distinguishing**
		- **Simplify**
- [[Designing a chart in 60 minutes]]


# Week 2 Creating data visualizations with Tableau
Tableau is a tool that can help analysts create effective data visualizations. In this part of the course, you will learn all about Tableau and its uses. You will also explore the importance of creativity and clarity while visualizing your findings appropriately.

- # Getting started with Tableau
	- Tableau is a business intelligence and analytics platform that you can use online to help people see, understand, and make decisions with data.
	- [[Tableau Resources]]
	- Visualizations in Tableau are dynamic, not static.
	- [[Types of Visualizations in Tableau]]
- # Creating visualizations in Tableau
	- [[Tableau resources for combining multiple data sources]]

# Week 3 Crafting data stories
Connecting your objective with your data through insights is essential to good data storytelling. In this part of the course, you will learn about data-driven stories and their attributes. You will also gain an understanding of how to use Tableau to create dashboards and dashboard filters.

> [!NOTE]- Week 3 Learning Objectives
> - Using Data to Develop Stories
> 	- Explain data-driven stories, including reference to their importance and their attributes
> 	- Demonstrate an understanding of how to use Tableau to create dashboards and dashboard filters
> 	- Explain how data stories can be used in different forms of on-the-job communication


- # Using data to develop stories
	- Stephen Few, an innovator, author, a teacher, and data visualization expert, once said,==*"Numbers have an important story to tell. They rely on you to give them a clear and convincing voice."*==
	- **Data storytelling** is communicating the meaning of a data set with visuals and a narrative that are customized for each particular audience. A narrative is another word for a story. 
		- Example: Year-in-review in Spotify
	- ## 3 Data storytelling steps
		- 1. Knowing how to engage your audience 
			-  Engagement is capturing and holding someone's interest and attention. When your audience is engaged, you're much more likely to connect with them and convince them to see the same story you see. 
			- Every data story should start with audience engagement, all successful storytellers consider who's listening first.
		- 2. Create compelling visuals
			- *You want to show the story of your data, not just tell it.* 
			- Visuals should take your audience on a journey of how the data changed over time or highlight the meaning behind the numbers.
		- 3. Tell the story in an interesting narrative
			- A narrative has a beginning, a middle, and an end. It should connect the data you've collected to the project objective and clearly explain important insights from your analysis.
	- [[Effective data storytelling]]
	- When you want to communicate something to others, a great story can help you reach people's hearts and minds and make them more open to what you have to say. In other words, *stories make people care*.
	- ## Engaging your audience
		- To get the response you're seeking, you've got to understand your audience's point of view. That means thinking about how your data project might affect them.
			- *What role does this audience play?* 
			- *What is their stake in the project?* 
			- *What do they hope to get from the data insights I deliver?*
		- **A good example**
			-  Let's say you're analyzing readership data from customers to help a magazine publisher decide if they should switch from quarterly to monthly issues. If your stakeholder audience includes people from the printing company, they're going to care because the change means they have to order paper and ink more frequently. They also might need to assign more staff members to the project. Or if your stakeholders include the magazine authors and editors, you'll want to keep in mind that your recommendations might change the way they work. For instance, they might need to write and edit stories at a faster pace than they're used to. Once you've considered the answers to those questions, it's time to choose your primary message.
		- To get the key message, you'll need to take a few steps back and pinpoint only the most useful pieces. Not every piece of data is relevant to the questions you're trying to answer. A big part of being a data analyst is knowing how to eliminate the less important details.
			- One way to do this is with something called spotlighting. **Spotlighting** is scanning through the data to quickly identify the most important insights.
- # Using Tableau dashboards
	- A **dashboard** is a tool that organizes information from multiple data sets into one central location for tracking, analysis, and simple visualization through tables, charts, and graphs. Dashboards do this by constantly monitoring live incoming data. 
	- When designing a dashboard, it's best to start simple with just the most important data points, and if later on you discover something's missing, you can always go back and tweak your dashboard or create a new one.
	- ==Choosing vertical or horizontal layout==
	- ==Tiled or floating layouts==
	- Dashboards put storytelling power in the hands of the viewer. That means they'll craft their own narrative and draw their own conclusions, but don't let that scare you away from being collaborative and open. Just understand the risks that come with sharing your dashboards.
	- [[Live versus static insights]]
- # Sharing data stories
	- The narrative you share with your stakeholders needs characters, a setting, a plot, a big reveal, and an "aha moment," just like any other story. 
		- The characters are the people affected by your story. This could be your stakeholders, customers, clients, and others. 
		- Next up is a setting, which describes what's going on, how often it's happening, what tasks are involved.
		- The plot, sometimes called the conflict, is what creates tension in the current situation. This could be a challenge from a competitor, an inefficient process that needs to be fixed, or a new opportunity that the company just can't pass up.
		- The big reveal, or resolution, is how the data has shown that you can solve the problem the characters are facing by becoming more competitive, improving a process, inventing a new system, or whatever the ultimate goal of your data project may be. 
		- Finally, your "aha moment" is when you share your recommendations and explain why you think they'll help your company be successful.
	- Presentation tips
		- Presentations should be less than five lines and less than 25 words per slide
		- Choose words carefully, avoid slang terms, abbreviations that people might not know, and words or phrases that are specific to one particular region.
		- Great visuals don't leave room for interpretation because the meaning is instantly understood. When you include visuals on a slide, try not to share too many details all at once. Choose just the data points that support your points, especially your key message. 
		- Ask yourself: *"What's the single most important thing I want my audience to learn from my analysis?"*
		- If you have several important things you need to include, don't cram them all on one slide; instead, create a new visual for each point. Then add an arrow, a call-out, or another clearly-labeled element to direct your audience's attention toward what you want them to look at.
		- Finally, when you get to your big reveal and aha moment, your visuals must communicate these messages with clarity and excitement. These are the most powerful discoveries from your analysis—make it feel that way.
		- It's a quick tip for knowing when to copy and paste, link, or embed a visual into a slideshow. The main difference between pasted, linked, and embedded objects has to do with where you store them and how you update them after you place them in your slideshow.

# Week 4 Developing presentations and slideshows
In this part of the course, you will discover how to give an effective presentation about your data analysis. You will consider all aspects of your analysis when creating a presentation and learn how to use multiple data sources in the data visualizations you will share. In addition, you will learn how to anticipate potential limitations and questions that might arise and how to provide useful answers to stakeholders.

> [!NOTE]- Week 4 Learning Objectives
> - Developing presentations and slideshows
> 	- Describe best practices for addressing the question-and-answer section of a presentation
> 	- Consider the caveats and limitations associated with the data in a presentation
> 	- Differentiate between strong and weak presentation content
> 	- Describe how junior data analysts are expected to use their presentation skills
> 	- Explain principles and practices associated with effective presentations
> 	- Identify appropriate responses to presentation objections


- # The art of effective presentation
	- *Remember, the business task is the question or problem your data analysis answers.*
	- ## Framework for Effective Presentation
		- Understand the business task
			- Raw data doesn't mean much to most people, but if you present your data in the context of the business task, your audience will have a much easier time connecting with it. This makes your presentation more informative and helps you empower your audience with knowledge. That's why understanding the business task early on is key.
			- Tip: Define business tasks at the start of your presentation
		- Outlining and connecting with your business metrics
			- By showcasing what business metrics you use. You can help your audience understand the impact your findings will have.
		- ## How you work data into your presentations to help your audience better understand and interpret your findings.
			- Explain to your audience what data was available during data collection.
			- This helps our audience understand what data they're actually looking at and what questions they can expect it to answer. 
			- Establish your initial hypothesis
				- Your initial hypothesis is a theory you're trying to prove or disprove with data.
				- You want to establish your hypothesis early in the presentation. That way, when you present your data, your audience has the right context to put it in.
			- Explain the solution using examples and visualizations
				- Raw data could take time to sink in, but a good example or visualization can make it much easier for your audience to understand you during a presentation.
				- Presenting your visualizations effectively is just as important as the content, if not more.
				- The McCandless method
					- ![](https://i.imgur.com/jjtHT9S.png)
					- Read here: [‘The McCandless Method’ of data presentation — ART+SCIENCE](https://artscience.blog/home/the-mccandless-method-of-data-presentation)
				- ==Tip: Add *Key Takeaways* from every visualization.==
				- ==Tip: *"Does this data point or chart support the point I want people to walk away with?"*== It's a good reminder to think about your audience every time you add data to a presentation. 
- # Presentation skills and practices
	- As a data analyst, you have two key responsibilities: 
		- 1. analyze data; and 
		- 2. present your findings effectively
	- ==*data analysis is all about turning raw information into knowledge*==
	- ## Tips when giving presentations
		- It's natural to feel your adrenaline levels rise before giving a presentation. To help keep that excitement in check, try taking deep, controlled breaths to calm your body down. As a bonus, this will also help you channel all that excitement into a presentation style that shows your passion for the work you've done. 
		- Start with the broader ideas, the obvious questions your audience might have, and what they need to understand to put your findings in context. Then you can get more specific about your analysis and the insights you've uncovered.
		- Keep a simple title, with your name and date of presentation.
		- **Five-second rule.** As a quick refresher, whenever you introduce a data visualization, you should use the five-second rule and ask two questions. First, wait five seconds after showing a data visualization to let your audience process it, then ask if they understand it. If not, take time to explain it, then give your audience another five seconds to let that sink in before telling them the conclusion you want them to understand. 
		- When it comes to presenting data, preparation is key. 
- # Caveats and limitations to data
	- ## Ways to can anticipate possible questions 
		- Understanding your stakeholder's expectations will help you predict the questions they might ask. 
			- Make sure you have a clear understanding of the objective and what the stakeholders wanted when they asked you to take on this project. 
		- A great way to identify audience questions is to do a test run of your presentation. I like to call this the "colleague test." 
			- Show your presentation or your data viz to a colleague who has no previous knowledge of your work, and see what questions they ask you.
		- Start with zero assumptions
			- Don't assume that your audience is already familiar with jargon, acronyms, past events, or other necessary background information.
			- Try to explain these things in the presentation, and be ready to explain them further if asked.
		- Finally, be prepared to consider and describe to your stakeholders any limitations in your data.
	- [[Preparing the Q&A]]
	- ## How to handle objections
		- Objections about the data
			- Sometimes, stakeholders might be asking where you got the data and what systems that came from, or they might want to know what transformations happened to it before you worked with it, or how fresh and accurate your data is. 
			- You can include all this information in the beginning of your presentation to set up the data context. You can add a more detailed breakdown in your appendix in case there are more questions.
			- When cleaning data, keeping a detailed log of data transformations is useful.
		- Objections about your analysis.
			- They might want to know if your analysis is reproducible, so it helps to keep a change log documenting the steps you took.
			- It can be useful to keep a clean version of your script if you're working with a programming language like SQL or R.
			- Making sure to include lots of perspectives throughout your analysis process will help you back up your findings during your presentation. 
		- Objections to the findings
			- "Do these findings exist in previous time periods?"
			- "Did you control for the differences in your data?" 
	- ## How to respond to objections
		- First, it can be useful to communicate any assumptions about the data, your analysis, or your findings that might help answer their questions.
		- Second, explain why your analysis might be different than expected. Walk your audience through the variables that change the outcomes to help them understand how you got there. 
		- Third, some objections have merit, especially if they bring up something you hadn't thought of before. If that's true, you can acknowledge that those objections are valid and take steps to investigate further.
- # Listen, Respond and Include
	-  More Q&A Best Practices
		- Listen to the whole question
			- It's important to listen to the whole question and wait to respond until they're done talking. Take a moment to repeat the question. Repeating the question is helpful for a few different reasons. For one, it helps you make sure that you're understanding the question. Second, it gives the person asking it a chance to correct you if you're not.
			- Anyone who couldn't hear the question will still know what's being asked. Plus, it gives you a moment to get your thoughts together. After listening to the question and repeating it to make sure you understand.
		- The appendix is a great place to keep extra information that might not be necessary for our presentation but could be useful for answering questions afterwards.
		- Remember the project goals and your stakeholders' interests in them, and try to keep your answers relevant to that specific context, just like you made sure your presentation itself was relevant to your stakeholders. 
		- Answer the question as directly as possible using the fewest words you can. From there, you can expand on your answer or add color, contexts, and detail as needed.