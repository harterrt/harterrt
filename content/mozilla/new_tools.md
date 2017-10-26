title: Evaluating New Tools
slug: new_tools
date: 2017-10-26
tags: tools, mozilla


At Mozilla, we're still relatively early in our data science journey.
As such, we're always evaluating new tools to improve our analysis workflow
([jupyter](http://jupyter.org/) vs. [Rmd](http://rmarkdown.rstudio.com/)),
or make our infrastructure more usable
(our home-rolled [ATMO](https://github.com/mozilla/telemetry-analysis-service)
vs. [databricks](https://databricks.com/)),
or scale our knowledge
([knoledge-repo](https://medium.com/airbnb-engineering/scaling-knowledge-at-airbnb-875d73eff091).
vs. [gitbook](https://www.gitbook.com/))

Most of these tools look like they have compelling wins over our existing solutions.
But when we build a demo,
our users ignore some tools and rave about others.
Why?
I think it's because some of **the costs of adopting a new tool are subtle**.

Unless your new tool is a perfect match for the problem at hand (very rare)
I need to spend time learning, coding, or configuring the tool to work for me. 
At the same time,
I have **work due today** and an existing set of tools that are good enough.

What follows are some thoughts I have when deciding whether to adopt a new tool.
Maybe they will help you (or future me) **debug problems with adoption**.

## What am I taking home?

If your new tool is internal-only, uncommon in the industry, or expensive
I'm going to be less likely to adopt it.

In this case, anything I learn while adopting your tool
is **unlikely** to be **valuable to future employers**.
I think of my 
[career as an asset](https://esimoney.com/two-huge-reasons-why-your-career-matters/),
so if I get to do work that builds **transferable skills**,
I count that as **part of my compensation**.
On the other hand,
if I'm writing glue scripts to deal with idiosyncrasies in an internal tool,
I'm missing out.

I think this is a major reason
**why large tech companies open source internal technologies**. 
Consider 
[prestodb](https://code.facebook.com/projects/552007124892407/presto/)
or [golang](https://golang.org/).
How much would it suck to spend time learning these tools
if they were internal-only?
When you leave the company all of that skill becomes useless.
By open-sourcing these technologies,
you've just **increased your employee compensation without spending a dollar**.

## How long will I have access?

If your tool is closed source or expensive,
I'm going to hesitate before spending any time with it.
I depend on my tools and it hurts to lose them.

This is why I prefer Python or R to MATLAB.
I can use my experience with Python or R build side projects
that scratch my own itch.
MATLAB is expensive, so I don't have that benefit.

## How long will it be relevant?

Even if the tool is open source,
I want it to be configurable and composable.
This ensures it can grow with me.
I have no idea what the tech landscape will look like in 10 years,
but I do know it will be different.
**I want your tool to play nicely with technology that doesn't exist yet**.

Even better, if your tool is configurable and composable
it is probably going to take me much less time to get comfortable with it.

Composability is one of my bigger complaints about Jupyter.
Jupyter is a great tool for exploratory analysis,
but I don't want to use your GUI for editing code.
I'm much happier when I get to use my own tool chain.

However, Jupyter's saving grace is that it's configurable.
I'm working on a tool that will make it easy to develop
python packages and Jupyter notebooks side-by-side.
Hopefully, this will give us the best of both worlds.

## Conclusion

All this to say,
I'm going to carefully gauge the lifetime value of any new tool I adopt.
If your users are ignoring a new tool you've created,
**look carefully for hidden restrictions to lifetime value**.

On the other hand,
if your tool solves a critical enough problem,
I'll stand barefoot in the snow to use it.

Does this all make any sense?
Am I missing something important?
Why do you roll your eyes when someone tries to sell you a new tool?
