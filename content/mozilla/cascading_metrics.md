title: Leading with Data - Cascading Metrics
slug: cascading_metrics
date: 2020-11-05
status: draft

Leading a company is difficult.

Let's start with a case study to illustrate.

## An Example: 2020 Firefox Goals 

Firefox is losing users. We have been for a while.

We obviously want to turn this around.
We started by setting a goal for 2020:
Slow the loss of Firefox users.

This is vague,
so we decided on metrics to track our progress
and set targets that we wanted to hit by end of year.
At the end of the year we want to have 238 million
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

We have two metrics in this example, MAU and Retention.
Retention is called a **leading** metric
and MAU is called a **lagging** metric.

Our main goal is to improve MAU,
but to make the goal more manageable 
we focused our strategy on improving retention.
Our hope is that improving retention will in-turn improve MAU.

I've seen this concept of leading and lagging metrics
discussed pretty often in leadership literature,
so I won't go too deep into it here <sup>1</sup>.
The important point is that this is a **very powerful pattern**.
Ideally, we can see constant improvements in our leading metrics,
which motivates the company and gives employees a positive feedback loop.

Alternatively, **working against goals that are too big is demoralizing**.
When faced with an obviously over-sized goal,
some respond by ignoring the new goal
and going back to what they were working on before.

## Cascading Metrics

Sometimes, setting a leading metric isn't enough to make a goal tractable.
In this example, our lead metric (improving retention)
is still very difficult to achieve for any one team at Mozilla.
We need to break this goal down further.

Let's say Alice is a senior leader at Firefox 
and is responsible for improving MAU.
Alice identifies retention as the leading metric she wants to focus on improving.
Alice can then delegate responsibility for improving retention to Bob.

Bob now has the goal of improving retention.
He thinks that new users will be more likely to keep using Firefox
if we make the browser faster.
Accordingly, he identifies a leading metric to measure
how quickly Firefox loads websites on average.

In this example, Alice's leading metric becomes Bob's lagging metric.
This pattern can continue as needed to match the complexity of the goal.
I call this pattern **Cascading Metrics**.

At each level of delegation,
there's a chance to **match an employee's responsibility with their influence**.
For example, increasing MAU might be a fine goal for a C-Suite executive,
but it would be an unachievable goal for a single manager with only a few reports.
Similarly, an executive shouldn't be setting goals for individual teams.

Here's a visual of what this flow might look like:

<img src="https://via.placeholder.com/600x300">

## Developing Leading Metrics

One particular advantage of this framework is that 
it's explicit about where these leading metrics come from.










----

Of course, when leading with metrics
it's important to be clear about *why* any particular metric is important
to avoid [Surrogation](/surrogation.html)

---

## Footnotes

[1] If you want to read more, I can recommend 
[The 4 Disciplines of Execution](https://www.amazon.com/Disciplines-Execution-Achieving-Wildly-Important/dp/1451627068/)
which is referenced heavily in 
[Deep Work](https://www.amazon.com/Deep-Work-Focused-Success-Distracted/dp/1455586692/).
