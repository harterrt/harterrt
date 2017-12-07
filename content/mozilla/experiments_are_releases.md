title: Experiments are releases
slug: experiments_are_releases
date: 2017-12-06
tags: experimentation

[Mission Control](https://github.com/mozilla/missioncontrol)
was a major 2017 initiative for the Firefox Data team.
The goal is to provide release managers with near-real-time
release-health metrics minutes after going public.
Will has a
[great write up here](https://wlach.github.io/blog/2017/10/mission-control/)
if you want to read more.

The key here is that the data has to be updated quickly.
We're trying to **react** to bad releases so we can roll back the change.
Once we've bought some time, we can step back and figure out what went wrong.
It's like pulling your hand away from a hot stove.

This is different from the data we talk about when talking about experiments.
With experiments, we **purposely avoid looking at early data** to avoid bias.
Users behave differently on Monday and Friday.
We don't want to base a decision solely on data from a holiday.
When we've gathered all of our data,
we carefully consider metric movements then make a decision.

Since these use cases are so different,
we developed our release tools (Mission Control)
separately from our experimentation tools.
We have the [Experiments Viewer](https://github.com/mozilla/missioncontrol)
and the associated ETL jobs.
Now we're working on a new front-end called Test Tube.

However, after working with a few experiments,
I've found **we need reactive metrics for experiments** as well.
Currently, when we release an experiment
we don't get any feedback on whether the branches are behaving as expected.
The experiment could be crashing for unexpected reasons,
or the experiment branch could be identical to control (a null experiment) due to a bug.
Without these reactive metrics, it takes weeks to identify bugs.

The more I think about it,
the more it seems like experiments are actually a type of release.
I can't think of one release metric I wouldn't want to see for an experiment.
This makes me think we should expand our release tools to handle experiments as well.

This does not mean all of our decision metrics need to be real-time.
In fact, **real time decision metrics are probably undesirable**.
We want some top-level vital signs - e.g. crashes and usage hours.

When I first started thinking about this I proposed,
"all releases are a type of experiment".
I'm no longer sure this is true.
I think we **could modify our releases to be experiments**,
but our current release process doesn't look like an experiment to me.
For example, we could keep a control branch while we roll-out a new release.
This would allow us to catch regressions to our decision metrics
(e.g. a drop in URI count).

Shoot me an email if you think I'm a crazy person or if you think I'm on to something.
