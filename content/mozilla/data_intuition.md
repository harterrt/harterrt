title: Defining Data Intuition
slug: data_intuition
date: 2020-10-20
tags: data-intuition

Last week, one of my peers asked me to explain what I meant by "Data Intuition",
and I realized I really didn't have a good definition.
That's a problem! I refer to data intuition all the time!

Data intuition is one of the three skills I interview new data scientists for
(along with statistics and technical skills).
In fact, I just spent the first nine months of 2020
building Mozilla's data intuition.
I'm really surprised to realize I can't point to
a good explanation of what I'm trying to cultivate.

So - I'll make one up. I propose the following definition for Data Intuition:

> **Data Intuition is a resilience to misleading data and analyses.**

In other words, it's harder to mislead someone with data
if they have strong data intuition.
Think of this as **a defense against the dark data arts**.

So what does that look like in practice?

## Data Stink

Someone with strong data intuition can quickly spot "data-stink"
(a close cousin to "[code smell](https://en.wikipedia.org/wiki/Code_smell)").
These are data issues that don't necessarily invalidate an analysis,
but certainly draw suspicion on the results.
For example:

* An analysis prominently reports a seemingly **arbitrary metric** -
  4-day retention increased by 0.5%!
  Where did 4-day retention come from? Don't we usually track 7-day retention?
  This needs more attention before I trust the results.
* An analysis reports **extraordinary results** where nominal results are expected -
  this feature increased retention by 10%!
  But, past efforts were trying to increase retention by 0.5% - 
  and isn't retention already 90%? How'd we get and increase of 10%?

These are extreme examples. 
Usually the problems are more subtle
and result in a general sense of uneasiness with the results
(that's why it's called "intuition").

It's clear to me that data intuition is *related* to product intuition,
though these *are* different skills.
Product intuition can contextualize our results
and make it easier to identify extraordinary claims in analyses.
To know a 10% gain in retention is ridiculous
we need to know that users retain pretty well already.

## Methods issues

Strong data intuition can also help you 
spot issues with how the analysis was designed.
Things like: how did the author collect data? Is it a representative sample?
Do they need to have an experiment to establish causation?

Here's an example -
say an analysis reports that Firefox users who create a Firefox account
retain 10% higher than users who don't.
By default, a lot of folks interpret this to mean that
if we invest some time in helping users open accounts
we'll see an increase in retention.
Folks with stronger data intuition will instead 
recognize these results are just correlational (not causal).

Users who use the product a lot tend to stick around longer.
Users who open an account are more active users, thus they retain better.
Users who *crash* Firefox are more active users, and also retain *better*.

I think this intuition is more than just understanding statistics well.
A strong stats background can help me identify issues
when reading the *methods section of a white paper*.
Strong data intuition helps me determine how much I trust
results I hear about in a *news headline*.
Data intuition helps me establish whether results are
[true-enough](/pub-true.html).

## More than Skepticism

I almost defined data intuition as a type of skepticism,
but I think this is a bad characterization.
Skepticism over-focuses on disregarding results.

Intuition is more than being skeptical.
It's **incorporating new data as part of a body of existing knowledge**.
A lot of times, that means deciding new incoming data are inconsistent
and need more investigating before we can trust them.
But other times, it means changing our opinions in the face of new data
that are more authoritative than our existing body of knowledge.

## What do you think?

I want to hear your thoughts on this.
I'm posting this definition publicly in part because I want to invoke
[Cunningham's Law](https://meta.wikimedia.org/wiki/Cunningham%27s_Law).
The best way to get to the right answer is to post the wrong answer!

Does this definition for data intuition resonate with you?
Am I missing something important? Let me know! 
My email is at the bottom of this page.

I'm spending the next few month building some self-service trainings
to help non-data people at Mozilla build data intuition.
I'd rather be wrong now than next year!
