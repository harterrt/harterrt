title: The Value of a Wild-Ass Guess
slug: wild-ass-guess
date: 2021-02-20
status: draft

My peers are currently running workshops on *opportunity sizing*.
If you're unfamiliar, 
opportunity sizing is when you take some broad guesses 
at how impactful some new piece of work might be
before writing any code.

Why? Our immediate goal is discaring projects that aren't worth the effort.
We want to **make sure the juice is worth the squeeze**
before we do any work.

Last year we were surprised by the results of 
a big A/B test we ran
(I mentioned [this experiment before](/why_experiment.html)).
Unfortunately, we didn't see the impact we were hoping for.

It was pretty clear *why* we weren't seeing that impact
once we did some back-of-the-napkin math.
Our features just didn't affect enough users.
Now we're trying to build the habit of doing this back-of-the-napkin math
earlier in the product lifecycle.

# High level overview

At a high level, these are the ingredients you need:

* How many users could your change affect?
* How many users are going to change?
* How will those users change?

Let's look at a concrete example.

# But isn't that subjective?

Yup. But subjective analyses are useful communication tools.

This analysis is a communication tool.

"We don't have data, but this feels right"
is good enough at this stage.

It _does_ have to _feel right_ though.
You'll be presenting this analysis to folks.
If your numbers are outrageous,
you'll need to be able to defend them.

There's not much incentive to oversell.
The truth comes out when the feature gets launched.
The more we commit into these projects,
the more we should commit to the opportunity sizing.
This analysis can (and should) grow with our commitment to the project.

You'll also get better at this as you build more intuition.
Your 10th opp sizing will be better than your first.

# But what if you're wrong?

I _am_ wrong. It doesn't matter.

---

My peers are currently running workshops on *opportunity sizing*.
If you're unfamiliar, 
opportunity sizing is when you take some broad guesses 
at how impactful some new piece of work might be.

Why spend the time guessing?
Our immediate goal is discaring projects that aren't worth the effort
*before we write any code*.
We want to make sure the juice is worth the squeeze.

Last year we were surprised by the results of 
a big A/B test we ran
(I mentioned [this experiment before](/why_experiment.html)).
Unfortunately, we didn't see the impact we were hoping for.
It was pretty clear *why* we weren't seeing that impact
once we did some back-of-the-napkin math.
Our feature just didn't affect enough users.

At this point it was too late; we'd already done the work.
Now we're trying to build the habit of doing this back-of-the-napkin math
earlier in the product lifecycle.

## An example

Let me share a great example of applying opportunity sizing
that my collegue [Marissa](https://marissagorlick.org/) found.

We were considering whether to promote 
[Firefox Sync](https://www.mozilla.org/en-US/firefox/sync/)
on our mobile browser, 
[Fenix](https://play.google.com/store/apps/details?id=org.mozilla.firefox).
We know that users who sign into a Firefox account 
tend to retain better than users who don't.
The idea is that if we can get more users to sign up for accounts
they'll be happier with the browser and stick around longer.
There's a lot of fuzzy logic there,
but stick with me [1].

Before we do any real work,
let's take a very high-level look at some data
to see what type of upside this promotion might give us
in the best-case scenario.

The following table report the number of usrs,
and Week over Week (WoW) retention for Fenix users,
stratified by whether the user is signed into a Sync account:

<table width=400em>
  <tr>
    <th align='left'>Group</th>
    <th align='right'>Weekly Users</th>
    <th align='right'>WoW Retention</th>
  <tr>
  <tr>
    <td align='left'>Not Using Sync</td>
    <td align='right'>3,082,979</td>
    <td align='right'>30.45%</td>
  <tr>
  <tr>
    <td align='left'>Using Sync</td>
    <td align='right'>6,622</td>
    <td align='right'>39.95%</td>
  <tr>
</table>

At first glance, this looks like a big opportunity.
There's a 9% difference in WoW Retention, which is _huge_.
We'd be thrilled if we could cause a 1% increase in retention.

There are also a lot of eligible users.
We wouldn't have as much upside if all of our users were already using Sync.
Fortunately(?), it appears that almost none of our users are signed into Sync.






---



Right off the bat, we can see that Sync is a reletively rare feature on Fenix.
Just ~0.2% of users are signed in.
But, there _is_ a sizable difference in retention: ~9%.

The proposed promotion would effectively show users a notification
encouraging the user to sign up for a Sync account.
In the past 
 
---

---

Avoiding unnecessary work is enough reason to practice opportunity sizing,
but as I attend these workshops 
I'm finding that this isn't even the biggest benefit.
Opportunity sizing is actually
a great way to *communicate your intuition about the data*.


---



---


My peers are running workshops on opportunity sizing.

Why opportunity size?

* Throw away useless work early.
* Don't spend time on features that don't matter

That's it.

Opportunity sizing is pub-true at its finest.


---

I called a plumber to replace my kitchen sink.
When I asked him how much this was going to cost
he said, "I won't know until I can take a look at the job".

I guess that's a reasonable answer. 
He's probably done hundreds of similar jobs
and charged everywhere from $100 to $300 per job.
He needs more information.

But on the other hand, I have *no idea* how much this is going to cost.
I guess somewhere between $100 and $1000?
Even though the plumber isn't confident in his guess,
I would benefit from hearing it.

---

So, I play a game I call, "Orders of Magnitude".
I ask the plumber, how about a rough ballpark? I promise not to hold you to it.
Ehhh, it's hard to say.
So, is it closer to $100, $500, or $1000?

(the world snaps into focus) Oh, not 1000. Like, somewhere between $100 and $300.
The plumber is much more confident now.
They understand my question and my confusion much better.
The structure has helped him make a wild-ass guess.

An order of magnitude guess is *useful* to me.
I have no idea what you charge.
$100 - $300 is a much better guess than my original $100 - $1000.
This type of communication is *generous*.
It gives a lot of context while accepting some risk that you'll be over-interpreted.

---

This happens all the time in my day-to-day work.
I'll meet with an expert that has much more context than I do,
but it's hard to draw information from them 
because over-focused on their uncertainty.

Usually, their uncertainty doesn't matter to me.
Most of the time I'm trying to get a [pub-true](/pub-true.html) guess
to characterize their expertise.
In the above example, the plumber was arguing between $150 and $250.
That level of uncertainty doesn't change my decicion;
It doesn't matter.

I resort to the order-of-magnitude game frequently.
It's a useful way to shake out some context when the conversation stalls.

* A friend invites me to a party. How many people are you inviting? IDK.
  2? 20? 200? Is it a rave or a dinner party? Oh, like 10. It's a BBQ.
* How many users will see this feature? IDK. 100,000, 1 million, 1 billion?
  Oh, like 10,000. It's pretty niche.

---

My team is running a series of workshops 
to help Mozilla start doing opportunity sizing.
This pattern keeps arising.

The goal in these workshops is to get folks to take an educated guess
at how big a feature may be *before writing any code*.

Sometimes we have all the necessary data to make a decent estimate.
Other times, we need to make a guess.

Here's a great example, my collegue used in our last training

<!-- TODO: Find the example -->

Here we have some decent data to predict the population, the retention impact,
but we don't have any data for "uptake".


This creates a lot of consternation and hand-wringing.
In reality, it doesn't matter.

Focusing on the uncertainty or subjectiveness of this estimate
causes us to spend too much time on this low-value problem.
When you run into this type of uncertainty,
I encourage you to note it, and barrel through as quickly as possible
with the goal of getting to a guess as quickly as possible.

You can always come back later if your decision is on the borderline.



---

* Folks have an easier time identifying answers that are "wrong" 
  than picking the "right" answer.
* Maybe a better name is a "communicative guess". Be generous with your context.

---

<sup> 1 </sup> 
I know you want to scream "Correlation is not Causation!".
*I* want to scream correlation is not causation.
We're not really trying to get an *accurate* estimate.
We're trying to get something that's [pub true](/pub_true.html).


