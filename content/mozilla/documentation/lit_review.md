title: Literature Review: Writing Great Documentation
author: Ryan Harter
date: 2017-02-03
category: mozilla
slug: lit-review
tags: mozilla,documentation

I'm working on a big overhaul of my team's documentation.
I've noticed writing documentation is a difficult thing to get right.
I haven't seen any great example for a data product, either.
I don't have much experience in this area,
so I decided to review what's already been written about creating great documentation.
This is a summary of what I've found, 
both for my own reference and to help others understand my thought process.

## Findings

I should note, all the literature I could find focused on documenting software products.
I am willing to bet that a data product is going to have different documentation needs than most software products.
But, this is as good a place to start as any.

### Structure & What to Write

Most seem to agree that a **README** is a critical piece of documentation.
The README is usually comprised of two key parts:
 
* A quick introduction explaining what this project is, why the reader should 
  care, and whether it's worth investing time to understand it better.
* A simple tutorial to get the reader started and give a feel for what the tool
  actually does.

If the reader decides they want to learn more,
there should be a set of **topical guides or tutorials** which comprise the bulk of the documentation.
Think of each of these guides as a class focused on teaching your student (reader) a single skill.
Reading all of these guides should take "someone who has never seen your product and make them an expert user". ([TDT][TDT])
With that in mind, make sure there's some sense of order to these lessons (easy to hard).

If your reader gets this far, they are now very comfortable with your product.
From here, they need high-quality **reference material**.
In my experience, this is the most common documentation provided,
but it is needed latest in the process and only by the most advanced users!

When I started this research, 
I was having a hard time figuring out how we were going to separate our 
prose documentation from our development notes.
Now I see that these are just different stages in this learning process.
First we explain what it is, then how to use it, and finally, how to extend it.

### Style

Most articles suggest adopting a style guide to make it easier for a user to read your documentation.
The writing should pull you through the document and feel natural.

If you want your documentation to read naturally, you should try to become a better writer.
This comes as cold solace to most folks, since I need my documentation now
and I can't wait 10,000 hours to become an expert writer, but it's worth mentioning.
The overwhelming consensus is that the best way to become a better writer is to **write a lot**.
If you want to write great documentation, consider building habits that will make you a great writer.

As with programming, maintaining a consistent style will help readers understand your documentation naturally.
Note, the important word here is "consistent".
**Choose a style and stick with it**.
This sounds obvious, but I rarely find corporate documentation with consistent style across tutorials.
Have a style guide and enforce it.

As you choose your style guide, be aware that most of the advice is focused on physical media.
Your documentation is probably going to be read digitally,
so your readers will have different expectations.
Specifically, readers are going to skim your writing, so make it easy to identify important information.

Use **visual markup** like bold text, code blocks, call-outs
(e.g [[1](http://www.methods.co.nz/asciidoc/chunked/ch16.html#X22)],
[[2](http://getbootstrap.com/components/#alerts[2])], and section headers.
Similarly, avoid long paragraphs.
Short paragraphs that describe one concept each makes finding important information easier.

Most guides suggest keeping a **conversational tone**.
This makes the guide more approachable and easier to read.

Everyone seems to agree that **you should have an editor**.
In fact, Jacob Kaplan-Moss dedicated an entire article to this point [[YNAE][JKM 3]].
If you don't have access to an editor,
review your own work thrice then ask for someone else's review before publishing.
Try adjusting your margins to force the text to re-flow.
It's a very effective way to catch spelling or grammatical mistakes.

### Tools

I'll start this section with a warning.
Tools often receive an undue amount of attention, especially from programmers.
With documentation, **writing is the hard, important work**.
It's important to use good tools, but make sure you're not 
[bike shedding](https://en.wikipedia.org/wiki/Law_of_triviality).

Your documentation should be stored in **plain text and in version control**.
Most of your documentation is going to be written by programmers, 
and programmers have powerful tools for manipulating text. 
Using anything besides plain text is a frustration that makes it less
likely they'll enjoy writing documentation.

<!--
// TODO: This should be expanded upon. Version control is hugely useful for
// figuring out who to contact if you have questions, identifying the health
// of the documentation, and attributing credit for the hard, thankless work
// of writing the documentation. Wiki's do a particularly horrible job of all
// of these things. 
-->

You should have a **process for reviewing changes** to the documentation.
Review will help maintain a consistent voice across your documentation 
and will provide useful feedback to the writer.
Think of how useful code reviews are for improving your programming.
I'd jump at the chance to get feedback from an expert writer.

You **should not use a wiki** for documentation.
Wikis make documentation "everyone's responsibility",
which really means it's nobody's responsibility.
Without this responsibility, wikis tend to decay into a web of assorted links without any sense of order or importance.
Wikis make it impossible to maintain a consistent voice throughout your documentation.
Finally, it's difficult to get review for your work before publishing.

Recognize that automatically-generated documentation isn't a replacement for hand-crafted prose.
Remember that the bulk of your documentation should be tutorials meant to slowly ramp up your users to expert status.
Docstrings have very little utility in this process.


## Resources

Most of what I've summarized here came from very few sources.
I highly recommend you read the following articles if you're interested in learning more:

* [[Teach, Don't Tell] (Steve Losh)][tdt]
* [[What to Write] (Jacob Kaplan Moss)][JKM 1]
* [[Technical Style] (Jacob Kaplan Moss)][JKM 2]
* [[You Need an Editor] (Jacob Kaplan Moss)][JKM 3]

[TDT]: http://stevelosh.com/blog/2013/09/teach-dont-tell/
[JKM 1]: https://jacobian.org/writing/what-to-write/
[JKM 2]: https://jacobian.org/writing/technical-style/
[JKM 3]: https://jacobian.org/writing/editors/

For later reference, I also reviewed these articles to form opinions about
general consensus outside of the primary sources above:

* [The Science of Scientific Writing](http://www.americanscientist.org/issues/id.877,y.0,no.,content.true,page.1,css.print/issue.aspx)
  (George Gopen, Judith Swan): Good overview of how to structure a paper so 
  readers find information where they expect it to be
* [WriteTheDocs.org](http://www.writethedocs.org/), specifically 
  [A Beginner's Guide to Writing Docs](http://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
* [Art of README](https://github.com/noffle/art-of-readme): An arguement for 
  writing good READMEs and a template to help you get started
* [Scala Documentation Discussion](https://groups.google.com/forum/#!topic/scala-internals/r2GnzCFc3TY)
  A discussion of why Scala's official documentation is so bad
* [Vignettes](http://r-pkgs.had.co.nz/vignettes.html) (Hadley Wickham): Hadley
  is a rockstar in the R universe. This is an article from his style guide for
  writing R package documentation. This is the closest I could come to finding
  documentation advice for data products.
* [Programming's Dirtiest Little Secret](http://steve-yegge.blogspot.com/2008/09/programmings-dirtiest-little-secret.html)
  (Steve Yegge): Steve Yegge on why it's important to type well
* [Writing Great Documentation](https://byrslf.co/writing-great-documentation-44d90367115a#.nenvaqeng):
  This article comments on documentation's propensity towards kippleization.
* [GNU Manual Style Guide](https://www.gnu.org/prep/standards/standards.html#GNU-Manuals)


