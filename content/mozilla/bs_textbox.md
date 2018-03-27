title: Don't make me code in your text box!
slug: coding_in_textboxes
date: 2018-03-08

Whenever I start a new data project,
my first step is rooting out any false assumptions I have about the data.

The key here is iterating quickly.
My workflow looks like this:
Code a little, plot the data, what do you see?
Ah, outliers.
Code a little, plot the data, what do you see?
Shoot, why are there so many NULL's in the dataset?

This is a critical part of working with data
so we have a ton of tools tuned for fast iteration loops.
These are the tools in the "Building Intuition"
[stage of experimental analysis](/stages_e13n.html).
Jupyter notebooks are a perfect example.
Great way to explore a dataset quickly.

Once I'm done exploring,
I need to distill what I've learned so I can share it and reference it later.
This is where I run into problems.
Often, these fast-iteration tools are really **hard to escape**,
and are a **horrible way to store code**.
As a result,
these tools end up getting used for things they're not built to do.
It's hard to spot if you're not looking out for it.

I've boiled this down to a rule: **Don't make me code in your text box!**

## Examples

### Re:dash

We use [Re:dash](https://redash.io/) extensively at Mozilla.
For the unfamiliar,
Re:dash provides an interactive SQL front-end
where you can query and visualize your data.
It's a great tool for getting quick answers to data questions.
For example, what percentage of users are on Windows?
How many times was Firefox asked to load a page yesterday?

Re:dash is great when you're iterating quickly,
but it falls short when you want to share and maintain your queries.
I've built a few dashboards in re:dash
and I always get nervous when I hear they're getting used.
The problem is that I **can't get review or track changes** to my queries.
I wouldn't tell others to rely on untested and unreviewed code,
so it feels wrong to rely on untested queries.

I started building a tool to fix these problems.
[St. Mocli](https://github.com/mozilla/stmocli)
allows you to store queries in a git repository
and deploy the queries to re:dash.
I've been using it for about a month now, and it's great.
It's much easier to maintain queries and getting review is far less painful.

Even better there were a bunch of unexpected benefits.

* It's easier to consistently format our queries
  since we're editing queries in modern text editors instead of a HTML text-box
* We can lint our queries since the queries are now stored in text files
* There's clear ownership for each query (`git blame`)
* We have more control over what our consumers are looking at
  now that we have a central repository of queries

### Wikis

When I joined Mozilla's data team,
our documentation was in rough shape.
We had documentation, but it was a sprawling tangled mess.
It was easy to forget to update the docs or even to forget where the docs were.
Our documentation still isn't perfect,
but it's much better since switched to 
[docs.telemetry.mozilla.org](https://docs.telemetry.mozilla.org/).


What changed?
We started using
[Gitbook](https://www.gitbook.com/) and 
**stopped using a Wiki for documentation**.
Wikis are a horrible way to store technical documentation.
In fact, I should probably write a whole article on this point,
but here are some highlights:

* **Writing long-form content in a wiki is painful**.
  I either write the content elsewhere
  and publish by copy-pasting into a text-box,
  or (more commonly) I have to iteratively edit the document in the text box.
  Editing in the wiki means my half-finished article
  is indistinguishable from complete documentation.
* It's **impossible to get review**,
  which makes it difficult to fix unclear writing.
  Without review I can't tell when I'm being too terse or using a lot of jargon.
* Writing in a wiki is thankless.
  There's **no artifact of your work**.
  Sure, there's a new article in the wiki,
  but everyone built the wiki; It's not clear who wrote what.
* It's easy for documentation to get lost.
  A wiki makes it easy to have a **wandering chain of references**.
  Most of the articles at the end of these chains are forgotten and out of date.

We've also discovered some unexpected advantages
to storing our documentation in markdown.

* It was easy to integrate [mermaid.js](https://mermaidjs.github.io/)
  for [a system diagram](https://docs.telemetry.mozilla.org/concepts/data_pipeline.html).
* We were able to add spell check CI,
  which has the added benefit of highlighting jargon
  and standardizing our terminology.
* Soon we're going to add dead link CI as well.


### Jupyter

I already noted that Jupyter is a perfect example of a fast-iteration-loop tool.
I love opening up a new notebook to explore a problem and test my assumptions.
However, when it comes time to share my analysis,
I start running into problems.

First of all, Jupyter notebooks are stored as JSON objects in a text file.
This causes a whole host of problems.
It's difficult to track changes to these files in git.
Since the python code is stored as strings inside of a JSON object,
small changes to the analysis cause big changes to the storage file.
Also, it's impossible to lint or test any code stored in the `.ipynb` file.

It's easy to export the code from a notebook to a python file, which is great,
but I still want to use Jupyter to display my results.
Ideally, I could have a python package where all the logic is stored
and a Jupyter notebook that just displays the analysis results.
This actually works well, but it's still difficult.
There's no clear way to reload the development package in a live Jupyter notebook.

I don't have a great solution for this yet.
There are a few projects trying to address this problem though.
Mike outlines an interesting storage format
[here](http://droettboom.com/blog/2018/01/18/diffable-jupyter-notebooks/)
There's also [notedown](https://github.com/aaren/notedown)
and [ipymd](https://github.com/rossant/ipymd).


## Conclusion

All of these tools were built to help analysts build intuition quickly,
which is a critical part of data science.
However, most of these tools **compromise on composability**
which makes it difficult to develop an exploratory analysis
into a report in which I can be confident.
