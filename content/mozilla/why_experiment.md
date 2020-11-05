title: Why Run Controlled Experiments?
slug: why_experiment
date: 2020-11-05
status: draft

I spent some time earlier this year orchestrating 
a massive experiment for Firefox.
We were planning to push a bunch of new features out with Firefox 80.
My goal was to understand how much these new features improved our metrics.

In the process, I ended up talking to a lot of Firefox engineers
and explaining why we need to run a controlled experiment.
There were a few questions that got repeated a lot,
so I figure it's worth anwering them here.
Hopefully this is useful to future-me or my peers.

## What *is* a controlled experiment?

A controlled experiment is a tool to help us establish *causation*.
We want to measure what **effect** a change to the browser has on the world.
For example, we recently launched improvements to 
[Firefox's PDF Viewer](https://support.mozilla.org/en-US/kb/view-pdf-files-firefox-or-choose-another-viewer).
A controlled experiment would help us measure whether this feature
caused users to open more PDFs in Firefox.

To run a controlled experiment, 
we take a group of users and randomly assign them to one of two subgroups,
called "branches".
We show users in one branch the improved version of Firefox
(this is the "treatment" branch).
We show users in the other branch an unimproved version of Firefox
(called the "control" branch).
This gives us a before and after group running at the same time.
When we compare data from the two branches
we get a very reliable understanding of what effect the feature had.

This is still surprisingly difficult to do with Firefox.
To experiment against a feature
we need to be able to switch it on or off remotely.
This adds a lot of complexity when building and releasing the feature.
Folks are understandibly curious about why we're going through this rigamorole.

Let's consider some simpler options (and why they don't actually work)

## Why not just look at usage?


---

We ran a huge controlled experiment for Desktop Firefox over most of October.

Part of the issue is that Firefox is installed on other peoples computer.
When Facebook experiments against a new version of their website,
they deploy the experiment to servers they own.
