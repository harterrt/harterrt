title: Data Intuition Case Study: Coffee Consumption
date:2021-01-31
slug: coffee_bs
tags: data-intuition,coffee
status: draft

I found this whitepaper on the front page of Hacker News a few weeks ago:
[Coffee consumption and risk of prostate cancer](https://bmjopen.bmj.com/content/11/2/e038902).

My data intuition started raising alarms immediately.
So much so that I expect 
most data professionals immediately write this study off as bullshit.
To verify, I sent the paper to some of my peers and got similar feedback.

This is a great opportunity to work through the paper 
and demonstrate where my intuition triggers.
Think of this as a case study on [data intuition](/data_intuition.html).
I hope to write a few of these case studies.
Hopefully folks will be able to use these case studies to 
develop their intuition and spot common data problems.

The paper is pretty easy to read. 
It's only 8 pages long with a lot of graphics.
I encourage you to give it a skim and form your own opinions.
Keep in mind, there's nothing *wrong* with this paper.
I'm not calling for a retraction.
It's just at risk of being misinterpreted.

We're going to be discussing health-related topics,
so I find it necessary to note that this is not medical advice.
I am not a doctor, which means I am not *your* doctor.
This is an article on data *intuition*,
which means I didn't even read this paper all that carefully.
Caveat lector.

With that out of the way, let's dig in!

## Correlation != Causation

This is the first alarm that went off in my head,
so it's our first topic.

The authors are careful to never state this directly,
but the paper begs to be read as,
"Drinking coffee decreases the risk of prostate cancer".
I expect most people who read this paper 
will at least consider whether they should have another cup of coffee
to improve their health.

"Drinking coffee decreases the risk of prostate cancer"
is a *causal* statement.
We're saying that drinking coffee *causes* some change in our health.
However, this paper does not establish causation.
It is a correlational study, and we all know,
"Correlation does not imply causation"

I've harped on this before in [this piece](/why_experiment.html) on experimentation.
I want to give this point extra attention,
because lot's of people seem to know catch phrase
but don't apply it in practice.
To establish causation, we'd need something like a controlled experiment.

The logical jump from correlation to causation *feels* natural.
We *want* to extend the pattern.
I encourage you to resist this urge. 
More often than not, this instinct is faulty.
A careful skepticism will serve you well when working with data.

Don't get me wrong, there certainly *could* be a causal relationship here.
We just haven't looked hard enough to know.

This isn't a free pass to throw away the research.
Gordon Shotwell has a great quote to this point
in his post on Vitamin D and COVID-19:

> "There’s a particular type of person on the internet 
> who sees a graph like this 
> and reaches deep into their data science boot-camp memories 
> to exclaim 'Correlation doesn't imply causation!'"
> 
> -- Gordon Shotwell, [Vitamin D and Covid: We don't need to wait for more data](https://shotwell.ca/posts/supplment_vitamin_d/)

As always, there's also a relevant XKCD:

> Correlation doesn't imply causation, 
> but it does waggle its eyebrows [...] while mouthing "look over there" 
> [https://xkcd.com/552/](https://xkcd.com/552/)

Data intuition is a balance of championing data while remaining a skeptic.
Let's review the particulars of the paper
and decide whether we believe the results.

## ... The highest category of coffee consumption
