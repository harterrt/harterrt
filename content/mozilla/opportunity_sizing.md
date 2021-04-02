title: Opportunity Sizing: Is the Juice Worth the Squeeze?
slug: opportunity_sizing
date: 2021-03-26
status: draft

My peers at Mozilla are running workshops on *opportunity sizing*.
If you're unfamiliar, 
opportunity sizing is when you take some broad guesses 
at how impactful some new project might be before writing any code.
This gives you a rough estimate of what the upside for this work might be.

The goal here is to **discard projects that aren't worth the effort**.
We want to make sure the juice is worth the squeeze
*before we do any work*.

If this sounds simple, it is. If it sounds less-than-scientific, it is!
There's a lot of confusion around why we do opportunity sizing,
so here's a blog post.

## The Motivation

Last year we ran a huge A/B test over a full Firefox release
(I mentioned [this experiment before](/why_experiment.html)).
Unfortunately, we didn't see the impact we were hoping for
when we reviewed the results.

It was clear *why* we weren't seeing that impact
once we did some back-of-the-napkin math.
Our features just didn't affect a broad enough set of users.

This is a trap I've fallen into before too.
I've developed a pretty good sense of how much effort
a piece of technical work will take.
However, I find I don't have a great intuition
about how *impactful* a project will be.

Instead, my brain seems to group all new projects into one of two categories:
"Good thing to do" and "Pain in the a**".
A feature is generally a "good thing to do" 
if it would improve the product.
On the other hand, it's a PITA if we're trying to 
contort the product into doing something it isn't meant to do.

On the surface this may seem fine, but it's a pretty bad heuristic in practice.
Surprisingly, the "good think to do" bucket is more dangerous.
While there are some great projects in this bucket,
it's primarily filled with features 
that are nice-to-have and hard to say "No" to.
These nice-to-have features are usually not worth the effort.

The cut-off for "good thing to do" is just too low.
To start, a feature needs to be designed, built, and released.
That significant cost often dwarfs the possible upside.
There's also the opportunity cost.
All the time we spend working on an arbitrary "good thing to do"
detracts from our ability to work on more important projects [1].

In short, picking arbitrary projects
from the projects that are "good things to do"
is a great way to waste a lot of time.

## A Framework for Mozilla

Opportunity sizing helps us break free from our default heuristic
and think about projects more objectively.
The framework seems too simple to yield any real insight,
but I'm consistently surprised with how helpful it can be.
In this way, opportunity sizing is like a checklist in its
[unreasonably effectiveness](https://www.nytimes.com/2009/12/24/books/24book.html).

For the framework my peers developed,
there are three basic incredients we need to size an opportunity:

1. How many users could this project affect?
2. How many users are going to change?
3. How will those users change?

At Mozilla, we usually have pretty solid data for #1 
(How many users could this affect?).
For numbers 2 and 3 we're looking for guesses
that do a good job of communicating our assumptions about the project.
These guesses are informed by data, but are less than scientific.

Multiplying 1*2*3 gets us to a place where we can have a conversation.

# But isn't that subjective?

Yup. But subjective analyses can still be useful.

To start, guessing at the opportunity size helps clarify our assumptions
and identify weak assumptions early.
Even better, this framework is a **usefull communication tool**.
"We don't have data, but this feels right"
is good enough at this stage.

It _does_ have to _feel right_ though.
Hopefully you're sharing these results with peers.
They can gut-check your work and you can together build a shared opinion.
If your numbers are outrageous,
you'll need to be able to defend them.

There's often concern that ambitious coworkers are going to
oversell their opportunity to prioritize their pet project.
In my experience, there's not much incentive to do this.
Eventually we either recognize over-hyped numbers and redirect the project
or get underwhelming results from the launch and learn our lesson the hard way.

# But what if you're wrong?

I _am_ wrong. It doesn't matter.

First, this analysis should *not* be the entirety of our decision making process.
It's a tool to break through some common biases when choosing project work.

Second, these analysis can (and should) 
grow with our commitment to the project.

When we're early in the product lifecycle, we can make very rough estimates.
As the project matures and we learn more,
these analyses should mature as well.
When we're deciding whether to commit 20 engineers for 6 months,
we should have more confidence in our estimates.

We'll get better at this as we build more intuition.
Our 10th opporunity sizing will be better than our first.

---

<sup>1</sup> This does *not* mean we should sort all known problems 
by opportunity and commit to working on the projects at the top of the stack.
Sometimes, all of the available projects are below the line (not worth the squeeze).
In that case, it can be better to focus on finding more opportunities.
