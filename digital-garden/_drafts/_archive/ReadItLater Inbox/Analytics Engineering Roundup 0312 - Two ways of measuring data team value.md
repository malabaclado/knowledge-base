---
tags:
creation-date: 2023-03-13
---

[[ReadItLater]] [[article]]

# [Two ways of measuring data team value](https://roundup.getdbt.com/p/two-ways-of-measuring-data-team-value)

Are you going to be at Data Council? My co-founder Drew, along with Benn Stancil of Mode, will be up on stage answering questions and eating hot wings. From the event page:

> Spicier questions will prompt hotter wings.

One of the most simple but effective event premises out there. [Sign up here](https://www.eventbrite.com/e/off-the-record-a-spicy-evening-with-the-founders-of-dbt-mode-tickets-560735915217).

—

I recently chatted with Drew and Nick Handel, Co-founder of Transform on [episode 41 of the Analytics Engineering Podcast](https://open.spotify.com/show/4BKMMeVXk4jJnAQSqGSJvE). We talked about the semantic layer in general and specifically what everyone should expect from the new combination of the two companies. It was a fun conversation, highly recommended.

—

Emilie is [throwing down the gauntlet](https://helloturbine.substack.com/p/data-alone-is-not-enough):

> Data initiatives are too focused on democratizing access to information and not focused enough on driving business impact.

I’m very much aligned with the broader idea (that we need to have a much greater focus on business value produced by data…which doesn’t happen magically / on its own). But I \_think\_ I would say this a little differently. Here’s how I’d try to say it:

> If your data team is purely focused on democratizing access to information, its spend needs to be a very modest % of revenue.

If your centralized data function is purely focused on maintaining your data infrastructure and shared data models / metrics, that might be totally OK—but you need to roll it into [G&A](https://www.investopedia.com/terms/g/general-and-administrative-expenses.asp) and you need to keep the overall spend on this team as small as possible (in the same way you want to keep your other G&A functions as small as possible). There really *is* some level of shared data infrastructure that just needs to exist at a company for it to reasonably operate in a modern environment, after all.

If you think about other G&A teams there is a natural way to conceptualize the right amount of spend: as much as required but no more. How many in-house counsel do you need? *As many as required but no more*. There is a certain amount of legal work to be done; staff appropriately.

G&A functions are measured on their ability to do a job efficiently, and % of revenue metrics tend to be the way to norm one company’s efficiency off of another’s and define what “good” looks like.

On the other hand, functions related to acquiring or serving customers (sales / marketing / success) are evaluated on metrics that look more like ROI. And decisions are made on *marginal ROI*. So: if I hired one more sales person, how much would my revenue increase? If I spent $100k less on advertising, how much would my revenue *decrease*? Etc.

Data professionals can be valuable in this way too! There are many environments where one new data person can generate measurable ROI—imagine data practitioners embedded in product teams running experiments, or data practitioners embedded in marketing teams breaking into new channels.

So I guess my takeaway here is the following. There is some minimum viable data capability that is purely responsible for data infra and company-wide enablement, and this should be as small as is feasible. At a modestly-sized public software company, total G&A spend is maybe 10-12% of revenue, so this type of data spend (headcount and software) should probably be somewhere in the vicinity of 1% of revenue. But anything beyond this needs to be fiercely justified and defended on the basis of a specific claim about marginal ROI.

I think that some of the challenge the industry is having around valuing data work is this fundamental misunderstanding of the split between company-wide shared value and specific ROI *and the ability to accurately reflect this in a [chart of accounts](https://www.investopedia.com/terms/c/chart-accounts.asp)*. If you can’t see your data spend reflected in this way, it makes it impossible for the planning process to reason about how to grow or cut this spend. It makes it impossible for a product leader who knows how to generate ROI from a new data resource to actually get that resource added to their team. It makes it hard for “centralized” data teams to know how to set their goals or prioritize between competing interests.

These two types of activities are both valuable but need to be measured differently.

—

Pedram asks us to [reimagine dbt](https://pedram.substack.com/p/dbt-reimagined)…although what he actually seems to be focused on in the article is reimagining the dbt *developer experience*…what it feels like to write dbt code. There’s a lot of *very very good thinking* in this post; much of it very aligned with our thinking internally. As we get closer and closer to imagining playing around in this headspace with real code, the question that keeps coming up is: **one syntax or many?** There are, at this point, more ways than ever to write code that compiles to SQL. Should dbt be in the business of *choosing one mechanism*? Or should users be able to, for example, choose any of SQLGlot or PRQL or Malloy to express their logic?

I don’t have a strong stance here, and we’re not close enough yet to have a strong perspective as a company. If we do want to widen the aperture and allow more user choice, the hard part will be to continue to create a cohesive user experience—user choice is great as long as it doesn’t dilute the core UX. If you want user choice with poor UX there are plenty of ways to get that already :P

—

Speaking of dbt user experience, Kshitij Aranke, an engineer on the dbt Core team, wrote [almost a poem(!) on the topic](https://www.aranke.org/dbt-jquery/) a few weeks ago that I just ran across. Here’s a snippet:

> I can enter a [flow state](https://en.wikipedia.org/wiki/Flow_(psychology)) in dbt in a way I never can in Terraform.  
> I can *feel* my dbt models coming to life thanks to the [tight local feedback loop](https://youtu.be/PUv66718DII).  
> I don’t need to flit between reading documentation and writing code, since dbt fits in my [working memory](https://en.wikipedia.org/wiki/Working_memory).  
> I’m free to play in a dbt sandbox without worrying about [bankrupting my employer](https://twitter.com/GergelyOrosz/status/1541892021312430083).

The core point of the article is getting us to think about dbt less as Terraform (where I originally took inspiration) and more as jQuery. Having not actually been a deep user of *either* of these tools, I honestly don’t have a well-formed perspective on this. But the article does such a fantastic job of explaining *what works* about the dbt experience today…some parts of which I think we hadn’t been very good at putting into words until exactly now.

—

We just launched the [State of Analytics Engineering 2023](https://www.getdbt.com/state-of-analytics-engineering-2023/) report…567 responses from the community on a huge range of questions. There are many, many good nuggets in the report. One of the things I found the most surprising was that—in our sample at least!—*[analytics engineers in North America make more than data engineers](https://www.getdbt.com/state-of-analytics-engineering-2023/#compensation_north_america_link)*. I’m not sure it’s worth reading *too* much into this result, but I did find it fascinating considering the relative trajectory of the two roles. The role of the AE barely existed 4 years ago and apparently companies have learned to pay quite well for it during that time. 💪💪

There’s way more in this report than I can do justice to here…highly recommend you read through it. Or—if you prefer—just [install it as a dbt package](https://github.com/dbt-labs/analytics-engineering-survey) and `dbt seed` the raw survey results directly into your dev environment. If you find interesting conclusions, please write about them publicly and send me a link—I’ll be sure to link to them!

—

I just got back from a conference where I had the opportunity to speak with some of the leading figures in the AI / chatbot / large language model space. While I can’t say a lot about these conversations, what I can say is that these folks had a *tremendous* amount of confidence about the performance improvements we’re going to see from these models in the very near term (<12 months). If you’ve found yourself thinking “this doesn’t work well enough for my use case yet” my big takeaway was: keep an open mind, performance characteristics are changing quickly.

I’ve written a lot about this of late and so won’t rehash those thoughts here. I do want to share some of what I’ve been reading on this topic in the recent past.

-   I think David J’s read with [his new startup, Delphi](https://davidsj.substack.com/p/once-more-unto-the-breach), is dead on. I think LLMs + the dbt semantic layer are a beautiful combo. I’m excited to see demos!
    
-   Vicki’s [recent post](https://vickiboykis.com/2023/02/26/what-should-you-use-chatgpt-for/) brings her characteristic pragmatism and openness. Lots of good examples, and some fun quotes: “ChatGPT basically runs on statistical vibes.”
    
-   [The Waluigi Effect](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post) is … I don’t know how to describe this post. I haven’t fully digested it yet myself and am going to come back to it again myself later today. I link it here for your consideration. I did find the idea of “flattery and dialog” in prompt engineering to be *very* interesting.
    
-   Jonathan Godwin asks “[Why didn’t DeepMind build GPT3?](https://rootnodes.substack.com/p/why-didnt-deepmind-build-gpt3)” The interesting thing here is the dichotomy between the *research-oriented approach* and the *engineering-oriented approach*. OpenAI has an engineering-oriented culture, and their approach to the problem has been defined by this.