title: Don't make me code in your text box!
slug: bs_textbox
date: 2018-03-08

# Bullshit Textboxes

Whenever I start a new data project,
my first step is rooting out any false assumptions I have about the data.

The key here is iterating quickly.
My workflow looks like this:
Code a little, plot the data, what do you see?
Ah, outliers.
Code a little, plot the data, what do you see?
Shoot, why are there so many NULL's in the dataset?

This is a pretty critical part of working with data,
so we have a ton of tools tuned for fast iteration loops.
These are the tools in the "Building Intuition"
[stage of experimental analysis](/stages_e13n.html).
Jupyter notebooks are a perfect example.
Great way to explore a dataset quickly.

Once I'm done exploring,
I need to distill what I've learned so I can share it and reference it later.
This is where I run into problems.
Often, these fast-iteration tools are really **hard to escape**,
and and a **horrible way to store code**.
As a result,
these tools end up getting used for things they're not built to do.
It's hard to spot if you're not looking out for it.

I've boiled this down to a rule:

> Don't make me code in your text box!

## Examples

We use [Re:dash](https://redash.io/) extensively at Mozilla.
For the unfamiliar,
Re:dash provides an interactive SQL front-end
where you can query and visualize your data.
It's a great tool for getting quick answers to data questions.
What percentage of users are on Windows?



I already noted that Jupyter is a perfect example of a fast-iteration-loop tool.

