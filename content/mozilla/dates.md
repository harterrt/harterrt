title: Submission Date vs Activity Date
slug: dates
date: 2017-12-04

My comments on
[Bug 1422892](https://bugzilla.mozilla.org/show_bug.cgi?id=1422892)
started to get long,
so I started untangling my thoughts here.

---
From
[the bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1422892):

> We experimented with using `activity_date` instead of `submission_date`
> when developing the `clients_daily` etl job.
> We should summarize our findings and decide on 
> which of these measures we'd like to standardize against in the future. 

## Summary of the problem

`activity_date` is generally preferable to `submission_date`
because it's closer to what we actually want to measure.
There's a delay between user activity and us receiving the data.
:chutten has some
great analysis[[1]](https://chuttenblog.wordpress.com/2017/02/09/data-science-is-hard-client-delays-for-crash-pings/)
on the empirical difference between submission and activity dates,
if you want to read more.
95% of pings are received within two days of the actual activity 
[[2]](https://chuttenblog.wordpress.com/2017/09/12/two-days-or-how-long-until-the-data-is-in/),
but that means using 
**`submission_date` "smears" data between today and yesterday** (mostly).

However, **`submission_date` is much easier to work with computationally**.
When we partition by `submission_date`,
most jobs only need to process one day of data at a time.
This makes it much easier to continuously update datasets and backfill missing data.

`clients_daily` is currently limited to 6 months of historical data
because the **entire dataset needs to be regenerated every day**.
This is inconvenient and causes real limitations when using the dataset [3].
The job takes between 90 and 120 minutes to run and currently finishes near 9:00 UTC.
Adding more data to this job will push that completion time back,
meaning the data will be unavailable for the first few working hours every day.
Eew.

## Solutions

I see three possible options:

1. Standardize to `submission_date`
2. Standardize to `activity_date` and try to mitigate the performance losses
3. Allow both, but provide guidance for when to use each configuration

So far, the data engineering team has strongly recommended using `submission_date`.
The difference between `submission_date` and `activity_date`
has become even smaller with our team's work on ping sender
[[4]](https://chuttenblog.wordpress.com/2017/07/12/latency-improvements-or-yet-another-satisfying-graph/).
Without a strong counter argument, I recommend continuing with `submission_date`.

If we do have a strong reason to continue keying datasets by `activity_date`,
I recommend only using `activity_date` on "small" datasets.
These are datasets built over a sample of our data,
build over a rarer type of ping (e.g. not main pings),
or heavily aggregated (e.g. to country-day).
Someone should provide documentation on when `activity_date` is [un]necessary
to be included in [docs.tmo](https://docs.telemetry.mozilla.com).

---
1. https://chuttenblog.wordpress.com/2017/02/09/data-science-is-hard-client-delays-for-crash-pings/
2. https://chuttenblog.wordpress.com/2017/09/12/two-days-or-how-long-until-the-data-is-in/
3. https://bugzilla.mozilla.org/show_bug.cgi?id=1414044
4. https://chuttenblog.wordpress.com/2017/07/12/latency-improvements-or-yet-another-satisfying-graph/
