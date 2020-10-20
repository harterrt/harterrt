title: Follow up: Intentional Documentation 
slug: int_d11n_preso
date: 2020-10-12 18:00

Last week I presented the idea of 
[Intentional Documentation](https://blog.harterrt.com/randy_au_d11n.html)
to Mozilla's data science team.
Here's a [link to the slides](/static/int_d11n/).

The rest of this post is a transcription of what I shared with the team
(give or take).

---

In Q4, I'm trying to build a set of trainings
to help Mozillians build data intuition.
Last week, I was building a proposal for the project
and I thought to myself, "Why don't these trainings already exist?"

I spent the first half of 2020 working with Mozilla's product team 
to help build an understanding of our data and metrics.
This feels like it would have been 
the perfect opportunity to create some scalable documentation.
I've already invested a lot of time and energy into explaining our metrics.
Why didn't I think to document the work as I went?

My first thought was that writing documentation is *hard*.
Writing is difficult. Editing is difficult.
Even figuring out *what to write* is difficult.
But this wasn't convincing. Most of my work is hard.
What's so special about documentation?
Hell, I'm writing right now. I don't need to do this.

In reality, I think the problem is that documentation often *feels* useless.
It requires hard work up-front and I often don't get to see the downstream benefits.
In the best case, documentation reduces questions.
I don't get to see the questions not asked.
Even worse, if I write a lot of documentation 
all of those articles need to be maintained and organized somewhere.
Writing documentation takes work and creates maintenance!

Randy Au's post about 
[Intentional Documentation](https://counting.substack.com/p/lets-get-intentional-about-documentation)
helped break this open for me. 
Once I started thinking about documentation as a liability
everything became more clear.
Just like with software, we're better off if we can get by with fewer lines-of-code.

This is especially true at Mozilla.
The company is constantly exploring new areas so our problem-space keeps shifting.
This is in part because we're still new to working with data
and in part because the company is trying to find a way to grow.

I also think data science is harder to document than other areas (like engineering).
Data scientists are often working on a tighter time-scale.
We're trying to answer a question that becomes irrelevant in a few weeks.
There's no need to write long-lasting documentation for these investigations.
Nobody's going to read it in a month.

## Proposal

So how to we adjust?
I think we should shift our focus away from writing documentation
and towards being **prepared to backfill documentation**.
Instead of writing documentation that might not be useful in the future,
let's wait to see what documentation we need.
In the mean time, let's prepare so we can backfill our documentation later.

This *should* make writing documentation easier 
just because we'll be writing less documentation.
Even better, the documentation we do write is very likely to be used,
which is much more motivating that writing for a black hole.

We can make this even easier if we set up some useful habits.
If we focus on keeping lots of context in our tickets and weekly snippets
it will be much easier to distill that information into documentation later.
When starting a new project, writing a proposal helps me document my intentions
which helps contextualize documentation later.

Our ticketing system is working well.
I get a lot of day-to-day value from keeping my tickets up to date
(read: I get bugged less frequently when everything is up to date).

Snippets are sorta-kinda working. I alluded to this in 
[writing inside organizations](/writing_inside_organizations.html)
but I don't really enjoy writing snippets.
That's a sign to me that something's busted in the tooling.
When I'm doing useful work I tend to enjoy myself.

Finally, Slack is horrible for backfilling documentation.
By default, we only keep Slack messages for 6 months,
so unless you're confident your work will be irrelevant in 6 months from now
consider documenting elsewhere.

## Caveats

This does put some additional pressure on our real-time media (i.e. Slack).
This isn't great. Answering questions in Slack takes time and is repetitive.
But keep in mind that over-documenting has the same effect.
Unless documentation is maintained and organized,
it's just as confusing as having no documentation.
Think about how frustrating it is to find documentation that looks authoritative
but misleads because it's out of date. 

Intentional Documentation isn't a panacea.
We still need to figure out how to maintain the documentation we do write.
We still need to figure out when to delete unused documents.
But it does make this process easier.

