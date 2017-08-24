title: Documentation Style Guide
slug: docs-style-guide
date: 2017-08-24
category: mozilla
tags: mozilla,documentation

I just wrote up a style guide for our 
[team's documentation](https://docs.telemetry.mozilla.org).
The documentation is rendered using Gitbook and hosted on Github Pages.
You can find the 
[PR here](https://github.com/mozilla/firefox-data-docs/pull/41)
but I figured it's worth sharing here as well.

## Style Guide

Articles should be written in
[Markdown](https://daringfireball.net/projects/markdown/syntax)
(not [AsciiDoc](http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)).
Markdown is usually powerful enough and is a more common technology than AsciiDoc.

Limit lines to **100 characters** where possible.
Try to split lines at the end of sentences.
This makes it easier to reorganize your thoughts later.

This documentation is meant to be read digitally.
Keep in mind that people read digital content much differently than other media.
Specifically, readers are going to skim your writing,
so make it easy to identify important information

Use **visual markup** like **bold text**, `code blocks`, and section headers.
Avoid long paragraphs.
Short paragraphs that describe one concept each makes finding important information easier.

Please squash your changes  into meaningful commits  and follow these
[commit message guidelines](https://chris.beams.io/posts/git-commit/).
