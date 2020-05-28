title: The Problem with Democratizing Data
slug: prob_with_data_democ
date: 2019-12-26
status: draft

There's this principle called data democratization.
The goal is to enable everyone in the company
to work with and inspect any data that's critical to their job.
Some visible tech companies started this ideal
and I've seen it implemented with more or less success at different companies.
(TODO)

In particular, it seems like this can be particularly hard for
medium sized companies trying to become "data driven" for the first time.
I see this type of problem a lot at conferences.
I can be talking to a data scientists about organizational dysfunctions
and I see their face light up when I talk about data democratization.
It seems like everyone wants it to work but it just doesn't seem to be taking.

I *think* I have a feel for why this problem keeps popping up.
There's some **pre-work that the data science team needs to do
before the company sets everyone loose on the data**.
Think of this pre-work as setting guard rails
or cutting a trail through the weird and misleading raw data.
This can take some time, but it will lead to a much higher rate of success.

I'll talk more about what the solution looks like below.
But first, lets characterize what the problem looks like.

## The Failure Case

To set the stage, 
here's a characteristic example of
what a dysfunctional data democracy can feel like.

To start, some of the data is just too difficult to work with.
It takes a long time to run queries against
or it takes too long to understand how the data are collected.
Some data just aren't collected yet.
Folks usually just ignore this data
and focus their effort on what's available.

For the data that is available and easy to work with.
Well meaning employees dig into the data
and start drawing spurious conclusions from data
with too much confidence.
Each team has their own set of spurious results
which means that nobody seems to have the same understanding
of what's true or important.
Eventually, the company starts to identify these errors
which causes a whole new wave of frustration.
The analysts are frustrated
because the data are difficult to work with
and easy to draw bad conclusions with.
Leadership is frustrated because
each team seems to have their own truth
and it's impossible to interpret any analysis.


## The Solution






* Gathering specs - What problems do we have with current retention metrics? Where are the concerns coming from? Who are the players? 
* Scoping the problem space - Initial explorations, defining good-enough metrics, building datasets and example analyses to enable product. We can only hand off analyses to product if the space is scoped well enough. We don’t know how to make these analyses easy until we’ve done a few ourselves.
* Product hand off - working with product to get them comfortable working with the new datasets, helping product explore and build their own context
* Exploring weirdness - As product begins exploring the problem space they’ll find new weirdness in the data we never thought to look for. Data science will be available to track these issues down. Often this means exploratory analyses or collecting new data.
* Confidence - After a while, product will feel confident working with the data and we’ll begin finding fewer and fewer oddities. This is success.
