title: Leading with Data - Cascading Metrics
slug: cascading_metrics
date: 2020-11-05
status: draft

It's surprisingly hard to lead a company with data.
There's a lot written about how to set good goals
and how to avoid common pitfalls (like [Surrogation](/surrogation.html))
but I haven't seen much written about the practicalities
of taking action on these metrics.

I spend most of this year working with our executive team
to understand our corporate goals
and to track our progress against these goals.
I found that setting rock-solid goals **didn't do much good
if individual employees didn't know how they could contribute**.

The big and audatious goals we set for our company as a whole
can be overwhelming to a single employee.
It's hard to know where to start,
so instead overwhelmed employees
go back to whatever they were working on before.
**We have to do more** if we want to create behavior change
and get everyone working towards the same goal.

This article **introduces a new framework** for breaking down corporate goals
into metrics that are relevant and tractable for individual teams.
I call it **Cascading Metrics**.

Let's start with a case study to illustrate.

## An Example: 2020 Firefox Goals 

Firefox is losing users. We have been for a while.
Obviously, we want to turn this around.
We started by setting a goal for 2020:
Slow the loss of Firefox users.

This is vague,
so we decided on a metric to track our progress
and set targets that we wanted to hit by the end of the year.
Specifically, at the end of the year we want to have 238 million
[Monthly Active Users (MAU)](https://data.firefox.com/dashboard/user-activity).

That's a good start.
By specifying a metric and a target we've made the goal 
specific, measurable, and time-bound.
Slowing the loss of Firefox users is obviously relevant.
In the [SMART framework](https://en.wikipedia.org/wiki/SMART_criteria)
we're almost there.
The only **remaining question is whether this goal is attainable**.

Increasing MAU is a *huge* undertaking.
It's unwieldy.
It's hard to decide where to start on such a massive project.
To make this simpler, our leadership set a strategy to narrow the scope.
The team decided we're going to improve MAU
by finding a way to keep our new users around longer.

New Firefox users are at high risk of
installing Firefox and never returning again.
We decided to track this goal by measuring 
[New User 1-Week Retention](https://docs.telemetry.mozilla.org/cookbooks/retention.html).
At a high level, this metric measures:
of the people using Firefox for the first time today,
what portion use Firefox again next week?
Currently, it sits around 45-50% 
meaning a little more than half of new users don't return in the following week.

This is a more manageable goal.
Increasing retention is still a big undertaking,
but we have narrowed the scope a bit.

## Leading vs Lagging Metrics

We have two metrics in this case study, MAU and Retention.
I'd call Retention a **leading** metric
and MAU a **lagging** metric.

Our main goal is to improve MAU,
but to make the goal more manageable 
we focused our strategy on improving retention.
Our hope is that improving retention will in-turn improve MAU.

I've seen this concept of leading and lagging metrics
discussed pretty often in leadership literature,
so I won't go too deep into it here <sup>1</sup>.

The important point is that this is a **very powerful pattern**.
In the ideal case, 
employees can see consistent progress against our leading metric.
That's encouraging!
If we fail to set good leading metrics,
employess can get discouraged trying to make progress
against a metric that just won't budge.

I came across a particularly elegant explaination of this pattern in 
(of all places) East of Eden:

<!-- 
> In human affairs of danger and delicacy 
> successful conclusion is sharply limited by hurry.
-->
> So often men trip by being in a rush.
> If one were properly to perform a difficult and subtle act,
> he should first inspect the end to be achieved and then,
> once he had accepted the end as desirable,
> he should forget it completely and concentrate soley on the means.
> By this method he would not be moved to false action
> by anxiety or hurry or fear.
> Very few people learn this.
> 
>   \- John Steinbeck, East of Eden
<!-- First paragraph of chapter 21 -->

Here, our lagging metric would describe the "end"
and our leading metric the "means".
Put another way: plan the work, then work the plan.

## Cascading Metrics

There's a plot hole in this story though.
Increasing retention is still a very difficult goal to achieve.
<!--
This reminds me of [Milo](https://en.wikipedia.org/wiki/Milo_of_Croton)
who carried a calf on his back every day until he could lift a bull
4 years later!
The thing is, a 3 month calf already weights ~250#
-->
A individual team *might* be able to improve Firefox retention,
but most won't be able to.
Our leading metric didn't do enough to make our lagging metric tractable.

This is where Cascading Metrics can help.
When creating cascading metrics, we repeatedly apply this pattern of
breaking down difficult to move metrics into easier to move metrics
until we have a tractable project for an individual team.
Let's look at an example:

Let's say Alice is a senior leader at Firefox 
and is responsible for improving MAU.
Alice identifies retention as the leading metric she wants to focus on improving.
Alice can then delegate responsibility for improving retention to Bob.
So far, nothing's changed.

Now Bob has the goal of improving retention.
He thinks that new users will be more likely to keep using Firefox
if we make the browser faster.
Accordingly, he identifies a leading metric to measure
how quickly Firefox loads websites on average.


In this example, Alice's leading metric becomes Bob's lagging metric.
This pattern can continue as needed until we have a tractable goal
and our strategy has become a tactic.

Here's a visual of what this flow might look like:

<img src="https://via.placeholder.com/600x300">


At each level of delegation,
there's a chance to **match an employee's responsibility with their influence**.
For example, increasing MAU might be a fine goal for a C-Suite executive,
but it would be an unachievable goal for a single manager with only a few reports.
Similarly, an executive shouldn't be setting goals for individual teams.

## Developing Leading Metrics

Something I really like about this framework is that
it's explicit about where these leading metrics come from.
The leading metrics **describe a product strategy**.

We've looked at a goal, thought deeply about the product,
and decided on a strategy that will help us acheive that goal.
This decision making process should be informed by data,
but it's probably not *driven* by data.
It's **driven by product intuition**.

A very common failure case is to skip over the "strategy" part of this process
and hope our leading metric will just out of the data.
We focus on finding analytical solutions to increasing our metric.
Maybe we run some broad machine learning exploration to identify a leading metric.

These approaches are only occasionally successful.
More often than not, we end up finding obvious truths:
"Users who use the product frequently retain better!
We should get people to use the product more!".
If we do find a meaningful way to move our lagging metric,
it's very often something we don't have agency to change,
which limits its value as a leading metric.

We're almost always better off 
if we lean on our product experts to lead the way.
They can combine all of the tools at our disposal to find a way forward:
data science, user research, and their own product intuition.
Data science can support the product manager 
by testing their intuition against the data
(do we have enough users in Germany to focus all of our efforts in one country?)
and by helping them develop a leading metric to describe their strategy.


----

## Footnotes

[1] If you want to read more, I can recommend 
[The 4 Disciplines of Execution](https://www.amazon.com/Disciplines-Execution-Achieving-Wildly-Important/dp/1451627068/)
which is referenced heavily in 
[Deep Work](https://www.amazon.com/Deep-Work-Focused-Success-Distracted/dp/1455586692/).
