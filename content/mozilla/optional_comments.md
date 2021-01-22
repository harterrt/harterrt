title: Optional Comments
date: 2021-01-21
slug: opt_comments
status: draft

I spend a lot of my time at Mozilla reviewing my peers' work.
It's a joy, but it's hard to do well.
Review can be a great opportunity for mentorship and growth,
but it's also an opportunity to be overbearing.
Striking the right tone is a struggle.

Part of the problem is this implicit push
for the author to incorporate every review comment into the document [1].
For example, comments must be marked as "resolved"
which suggests the author took some action.
I see this reflected in our culture too.
Consider this [HBR article](https://hbswk.hbs.edu/item/ignore-this-advice-at-your-own-peril)
that highlights the risk of jilting peers by ignoring their advice.

This bums me out.
I don't want the author to feel beholden to my comments.
My goal is to give the author as much context as I can.
Often that means my comments won't require any changes to the document.

### Examples

For example, when reviewing a project document I might note
that someone else has some related prior art.
There's no need to incorporate this into the document.
I'm arming the author with context 
in case it comes up in a future conversation.

In another example, 
I might be reviewing an analysis that has already passed its peak relevance.
It may not make sense to make edits if the document is already going stale.
Data scientists are in a constant race against irrelevance.
It's better to focus on the next piece of work.
<!--We need to get results to stakeholders before the opportunity passes.-->

In this situation I still want to leave lots of comments
if my comments can improve future analyses.
Some comments might look like: 
"Heads up, we have helper functions in another library 
to automatically do this transformation".
There's no need to refactor the already complete analysis,
but the tip is still useful to the author.

### Conclusion

I don't have a silver bullet for this problem.
I can only recommend talking with your peers
about what kind of feedback they want to receive.
I find folks are usually happy to get more feedback
so long as they understand my intent.

Hopefully I can point folks to this post in the future
to prove I really do want them to take my comments as optional.

---


<sub>
[1] I'm focusing on reviewing prose here
because that's where I spend the most time reviewing.
Most of my peers are at the level where their analyses are expected to be solid
and prose is the most impactful part of their work.
Even so, there are pretty clear corollaries to code review.
</sub>
