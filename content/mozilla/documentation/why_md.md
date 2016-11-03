title: Why Markdown?
date: 2016-11-03
tags: documentation mozilla

[TOC]

Last week I finished a [pull
request](https://github.com/mozilla/telemetry-batch-view/pull/128) that moved
some documentation from our company wiki to a github repository.  It took a
couple of hours of editing and toying with pandoc to get right, but when I was
done, I realized the benefits were difficult to see.  So, I decided to write
them out for posterity.

# Better Process

The only way to edit our wiki is through the web front end which causes some
major problems.

For one, You're always editing the production version and there's no way to get
review before publishing. That's campfire story scary.

Second, your edits need to be submitted quickly - like within an hour, usually.
Since you're editing in a web form there's no good way to save your edits
locally.  Even worse, there's no good way to settle merge conflicts.

With markdown, I can develop my revisions over the course of weeks and preview
them locally.  When it's time to publish I get review from my peers, which
makes my documentation more readable and helps me improve as an engineer.

# Better Tools

I have powerful tools for manipulating text so using a simple web form to edit
technical documentation seems absurd to me.  With markdown, I get the joy of
using my favorite text editor in my favorite development environment

## One less tool

Our team is already using Markdown for our README's and Github provides a much
better UX for revison control.  By moving to Markdown for our user facing
documentation, we have one less tool and syntax we need to depend on.

# The documentation sits next to the code
Storing your documentation with your code has a lot of great benefits.

## Syncronization

Pull requests can include simultanious changes to code and documentation, which
makes it more likely they'll stay in sync. Both because you don't need to go
edit them elsewhere and because it can become a review requirement.

## Discoverability

Keeping the docs next to the code helps with discoverability. Your
code and your documentation should supplement each other. Keeping them close
together is only reasonable.
