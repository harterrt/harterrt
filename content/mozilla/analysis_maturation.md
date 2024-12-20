title: Analysis Maturation Plan
slug: analysis_maturation
date: 2019-12-12

I was talking about tooling with Mark Reid a few weeks ago.
I've been trying to find a way to simplify sharing analyses throughout the company.
This is an old problem at Mozilla that I've tried to address a couple of times
but I haven't found the silver bullet yet.
This is another attempt.

### The problem

To summarize the problem,
I need to be able to share analyses with my peers at Mozilla
(often HTML documents generated by Rmarkdown).
Currently, we effectively dump documents onto an FTP server tied to a webserver
(called Hala).
This works pretty well, but it makes it almost impossible to
search and discover other people's analyses
and makes getting review difficult.

To address these two problems,
we put together [mozilla.report](https://mozilla.report)
and [mozilla-private.report](https://mozilla-private.report).
These are effectively lightweight blog indexes for public and private analyses.
This works *OK*, but it still requires analysts to take the time to check in
their results and get review. 
It's a little heavy weight and isn't getting as much use as I would like.
Hell, I don't even use it all the time just because I'm busy.

### Levels of Maturity

I think this process has room for improvement.

Just looking at my own workflow,
I want to be able to share my report more broadly
as my results become more polished.

I see four levels of increasing maturity:

* **Private** - only accessible to the analyst
* **Indexed** - discoverable by those in-the-know
* **Reviewed** - results verified by a peer
* **Public** - report shared outside the company

In the beginning, I want a backup of my work that is difficult to discover.
This allows me to iterate without misleading anyone.
If I need to share the report with one of my immediate peers
(e.g. because I am stuck or got pulled onto a different project)
then I want to be able to share a link to the rendered report.

Sometimes, I'll start an analysis and find that I'm doing something silly.
If that's the case, fine. I'm done.
Most of the time though, I'll tie together my results into a readable report.
I want to have this readable report indexed and discoverable by my team.
This would allow me to find old reports quickly,
and find any of my peers' prior art.
Ideally, this would allow my team to keep up on my work in their own time
(like an RSS feed of peer analyses).

Most analyses stop here,
but some analyses are critical enough to require peer review.
In that case, I want to be able to get line-by-line review
for my code and commentary.
I want to be able to reference this review thread later.
Finally, I want some token to verify that the report is reviewed
to lend the analysis some authority.

Finally, some reports should be make public outside the company.

## Implementation

Thus far, I've been trying to hack this workflow together
by strapping existing tools together with duct tape and bailing wire.
Unfortunately, I think we'll need some custom tools to make this work well.

Here's the workflow I'm imagining now:

* Private reports
    * Start a new investigation by starting a git repo
    * Push results to the git repo, including rendered reports
    * Technical peers can clone the repo to review results
    * Non-technical peers need a way to see rendered reports...
* Indexed reports
    * I add my git-repo-url to a central list of analyses.
    * Some small script provides an indexed list of these repos
      with some metadata and links to any reports
      (this is similar to what [docere](https://github.com/harterrt/docere)
      does now, except it reads repos instead of reports)
* Reviewed reports
    * IDK? Maybe copy the analysis to a central repo like we do for mozilla.report?
* Public reports
    * IDK? Probably very similar to the reviewed report step...

In general, I like to avoid monolithic shared repositories -
at least while I'm prototyping analyses.
Instead, I like starting a new repository for each investigation.
When I'm prototyping an analysis I have a lot of small commits
and a lot of non-code files like CSVs and HTML reports.
This can cause merge-conflicts which are a PITA and cause a lot of stop-energy.

Unfortunately, we don't have a good way to
host private git repositories at Mozilla either.
This is task number 1!

I considered keeping analyses in branches of a central repository.
This makes it easy to get review and keeps private reports from being indexed.
However, I find it hard to manage branches and too easy to delete them.

### Call for comments

I don't have this figured out. Tell me what you think!
I'm especially interested in implementation ideas.
You can shoot me an email (harter at mozilla.com) or
you can leave comments on [this doc](https://docs.google.com/document/d/1fn2AiDBTMlxf7iZVn43LUTfkl83jpXBNQntVrztIgx8/edit#).
