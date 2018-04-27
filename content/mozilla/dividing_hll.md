title: PSA: Don't use approximate counts for trends
slug: dividing_hll
date: 2018-04-24

I got caught giving some bad advice this week,
so I decided to share here as penance.
TL;DR: approximate counts are approximate

---

Counting stuff is hard.
We use probabilistic algorithms pretty frequently at Mozilla.
For example, when trying to get user counts,
we rely heavily on Presto's 
[approx_distinct](https://prestodb.io/docs/current/functions/aggregate.html#approx_distinct)
aggregator.
Roberto's even written a 
[Presto Plugin](https://github.com/vitillo/presto-hyperloglog)
and a 
[Spark Package](https://github.com/vitillo/spark-hyperloglog)
to allow us to include
[HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
variables in datasets like
[client_count_daily](https://docs.telemetry.mozilla.org/datasets/batch_view/client_count_daily/reference.html).

These algorithms save a lot of compute power and analyst time,
but it's important to remember that they do introduce some variance.

In fact, the error bars are substantial.
By default, Presto's `approx_distinct` is tuned to have a standard error of 2.3%,
which means one out of every three `approx_distinct` estimates
will be off by more than 2.3%.
I can set a tighter standard error by passing a second parameter,
but it 
[looks like](https://prestodb.io/docs/current/functions/aggregate.html#approx_distinct)
I can't request anything below 0.5%.
For our HLL datasets, we set a
[default standard error](https://github.com/mozilla/telemetry-batch-view/blob/master/src/main/scala/com/mozilla/telemetry/views/GenericCountView.scala#L45)
of 1.63%, which is still significant.

Unfortunately, we can't get the standard error to be much smaller than 1%.
Databricks has
[a writeup here](https://databricks.com/blog/2016/05/19/approximate-algorithms-in-apache-spark-hyperloglog-and-quantiles.html)
which explains that the compute time for their probabilistic estimate
starts to be greater than the compute time for an exact count
somewhere between an error of 0.5% and 1.0%.

Most of the time, this isn't an issue.
For example, if I'm trying to count how many clients used a 
[Container Tab](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
yesterday I don't care if it's 100mm or 105mm;
those numbers are the same to me.
However, **that noise becomes distracting**
if I'm building a dashboard to track year over year change.

I put together an
[example notebook]({filename}/images/probabilistic_counts.ipynb)
to explore a little.
I created a toy dataframe containing
7 days of data and 1000 `client_id`'s per day.
Then I got an approximate count of the clients for each day.
Here's what an arbitrary set of daily errors look like:

<img src="{filename}/images/probabilistic_count_errors.png">

By default, pyspark's 
[approxCountDistinct](https://spark.apache.org/docs/2.0.2/api/java/org/apache/spark/sql/functions.html#approxCountDistinct(java.lang.String,%20double))
aggregator has a relative standard deviation (`rsd`) of 5%!
The maximum error magnitude we see in this dataset is 7.5% (day 4).

In my opionion, Spark's documentation obfuscates the real interpretation
of this `rsd` value, calling it the: "maximum estimation error allowed".
In reality, there is no "maximum error" allowed.
The `rsd` is a standard deviation for an approximately normal distribution,
so roughly one in three errors are going to be bigger than the `rsd`.

What's worse is that this graph makes us think there's movement
in this metric over time.
In reality, the user count is perfectly flat at 1000 users every day.
Since these errors aren't correlated over time,
we see big day over day swings in the estimates.
The largest swing occurs from day 6 to day 7 where the user count
jumps by 13.7% (-6.8% to 6.9%)!



