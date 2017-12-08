title: CLI for alerts via Slack
slug: slack_alerts
date: 2017-12-08

I finally got a chance to scratch an itch today.

## Problem

When working with bigger ETL jobs,
I frequently run into jobs that take hours to run.
I usually either step away from the computer
or work on something less important while the job runs.
I **don't have a good way to get an alert when the job completes**.
So instead of going back to my important work,
I keep toying with 
[whatever task I picked up](http://news.ycombinator.com) to fill the dead time.
I only get back to my primary task after I remember to check on it.

This is easier to fix when you're developing locally,
but I'm frequently developing jobs on EC2 instances via ATMO.
**There's no good way to forward alerts to my local system**.

Even then, I frequently step away from the computer to take a break while the job runs.
Sometimes the job stops after 10m instead of the usual execution of ~120m.
That usually means I had a command line flag set wrong
or that I fat-fingered a file name.
It would be great to be able to 
**see this alert immediately, even if I'm not at my computer,**
instead of waiting an hour until I check on my machine again.

The fix was crazy simple.
I created a little slack bot, installed a slack-cli, and added a bash command.
Now I can just issue a command like:
`sleep 10; slack Your task just completed.`
and in 10 seconds, I'll get a ping from `harterbot` on slack.
Setting this up on a remote cluster would be trivially easy as well.
You just need to be confident in storing a Slack API token.

## Action

Here's how I did this:

1. [Create a new bot](https://my.slack.com/services/new/bot),
   I called mine `harterbot`.
   Save the API token for later.
2. Install slack-cli with `pip install slack-cli`
3. Instantiate your `slack-cli` installation by issuing a test command:
   `slack-cli -d {{YOUR USERNAME}} "Test message"`.
   This will ask for the API token from step 2.
   You should see a new message from your bot.
4. (Optional) Add the following helper function to your `.bashrc`:

```bash
# Ping me with an alert on Slack
slack () {
    slack-cli -d {{YOUR SLACK HANDLE}} -- "$*";
}
```

Boom, you should be good to go!

Now I'm thinking we can generate an ATMO bot with shared credentials,
then there's no need to instantiate a new machine with your credentials.

For reference,
Slack's bot documentation is here:
[here](https://api.slack.com/bot-users),
