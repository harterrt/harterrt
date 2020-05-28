title: Syncthing and Open Source Data Collection
slug: syncthing_data
date: 2020-01-05

I don't see many open source packages collecting telemetry,
so when [Syncthing](https://syncthing.net/) asked me to opt-in to telemetry
I was intrigued.

I see a lot of similarities between how Syncthing and Firefox collects data.
Both collect daily pings and make it easy to view the data you're submitting
(in Firefox, go to about:telemetry to see your pings).

All of the data they're collecting looks relevant and innocuous.
For example, there's no content about *what* files are being sync-ed in Syncthing.
They just collect high level data like what version of the software is installed.
Well done!

Syncthing even has a [public data report](https://data.syncthing.net/)
similar to the [Firefox Public Data Report](https://data.firefox.com/).
This is a great way to make it clear what data is being collected
and share some data back with the users who generated it.

Interesting to see someone else doing open-source data collection in the wild!
