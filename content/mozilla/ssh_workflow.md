title: Working over SSH
date: 2016-08-25
status: draft

[TOC]

## Introduction

Working over SSH can be impossibly frustrating if you're not using the right tools. 
Over the recent London work week, I asked my teammates how they were configuring their cluster instances and most said that they weren't.
I promised to write up my tools, which I think work pretty well. 

## Tools

### tmux
tmux is the single tool most important for me getting work done over SSH.
tmux does a lot of really cool things, but the most relevant feature to this discussion is session persistence.

#### Session Persistence
tmux sessions can be detached and reattached at will.
That means when you execute some long running command on an AWS cluster you can kill the ssh session and the command will keep running.
Later, you can reconnect to the cluster and session, it will be as if you hadn't left.
So much nicer than cussing out your flaky WiFi connection.

More often, I use tmux just to save my place when I need to wrap up for the day.
Next morning, I can reattach my session and I'm already looking at the most relevant files for today's work.

#### Multiplexing
This is probably tmux's primary purpose.
It allows you to open a bunch of terminals in a single ssh connection.
Think of tmux as a tiling window manager for the terminal.
Here's a screen shot of how I developed this blog post:

{{TODO IMG}}

That's all in one terminal window.
On the left I have a process serving up drafts of this document and on the right I have my test editor.
The extra context is indispensable when trying to figure out WTF is going on with a failing job.

### Homeshick
Configuring a new machine is a PITA.
For a while I refused to make custom configurations to the tools I used because I didn't want to have to configure everything again on my next machine.
But, your tools should be a joy to use, and a customized system is much more enjoyable than a stock system.

Homeshick pulls all of your dotfiles into a central git repository and handles linking these files to the right location.
Now, I can boot up a new Ubuntu instance on AWS and feel at home within ~5 minutes.
When I connect to a machine for the first time, I grab [this snippet](https://github.com/harterrt/TIL/blob/master/linux/new-machine.md) and all of the initialization is done.
Even better, the meaningful config changes I make on my work machine magically materialize on my personal machine and VPS with a simple `git pull`.
