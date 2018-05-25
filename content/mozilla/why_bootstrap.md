title: Why bootstrap?
slug: why_bootstrap
date: 2018-05-24

Over the next few quarters,
I'm going to focus my attention on Mozilla's experimentation platform.
One of the first questions we need to answer is
how we're going to calculate and report the necessary measures of variance.
Any experimentation platform needs to be able to
 compare metrics between two groups.

For example, say we're looking at retention for a control and experiment group.
Control shows a retention of 88.45% and experiment shows a retention of 90.11%.
Did the experimental treatment cause a real increase in retention
or did the experiment branch just get lucky when we assigned users?
We need to calculate some measure of variance to be able to decide.

The two most common methods to do this calculation are the frequentist's
[two-sample t-test](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)
or some form of
[the bootstrap](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)).

In ye olden days, we'd be forced to use the two-sample t-test.
The bootstrap requires a lot of compute power
that just wasn't available until recently.
As you can imagine, the bootstrap is all the rage in the Data Science world.
Of course it is. We get to replace statistics with raw compute power!
That's the dream!

Still, the bootstrap isn't perfect for every problem.
Let's look at a few arguements for and against the bootstrap:

## Computational Efficiency

The bootstrap obviously requires more compute resources.
Still, it's worth highlighting how 
**amazingly computationally efficient the t-test is**.
You can calculate all you need for the t-test in a single pass through the data.
For each branch of the experiment all you need to calculate is:
a count, the sum of the data, and the sum of the square of the data
([to calculate the variance](https://en.wikipedia.org/wiki/Variance#Formulae_for_the_variance)).
All of these are easy to calculate in a map-reduce framework.
On the other hand,
the bootstrap is difficult to compute when your data do not fit in memory.

## The normality assumption

T-tests feel arcane and make assumptions about the distribution of the data.
Most notably, t-tests *require your metric to be normally distributed*.
Assuming normal distributions sets of alarms
for anyone who's worked with real-world data.
On the other hand,
the bootstrap uses the sample distribution to describe the population's distribution
which feels like a much smaller assumption to make.

In reality, the bootstrap method and t-tests actually
make very similar assumptions about the underlying data.
Since the t-test is comparing two *means*,
the t-test's normality assumption holds so long as 
[the CLT](https://en.wikipedia.org/wiki/Central_limit_theorem) holds.
The CLT holds so long as
(1) you have a lot of data and 
(2) the data have finite variance.
We generally have "a lot of data"
but the finite variance bit can be a problem<sup>1</sup>.
However! The bootstrap also fails if the data have infinite variance<sup>2</sup>.
All that to say,
**if the t-test's normality assumption fails, the bootstrap is in trouble too**.

On the other hand,
it can take a large sample for the CLT to make some datasets look normal
(like, N > 5000).
If you have a small, skewed data set, the bootstrap may be a better choice.
However, this is rarely a problem when you're working with Big Data™.

## Weird metrics

It becomes practically impossible to calculate a t-test
if your metric isn't a mean.
The classic example here is testing for a change in the median.
What's the variance of a median?
Is the median normally distributed?

¯\\\_(ツ)_/¯

*This* is where the bootstrap really shines!
With the t-test, you only have your one sample to work with.
With the bootstrap, you have as many samples as you want!
You can calculate any metric you want and get a confidence interval.

Personally, I think calculating the median is a lame example.
Percentiles, like the median, are notoriously hard to calculate over big data.
Instead, consider this (nearly) real life example:

Firefox collects anonymized performance data on a daily basis.
That data could look like this:

| `client` |        `day` | `active_hours` | `janky_loads` |
|:---------|-------------:|---------------:|--------------:|
| 'aaa'    | 2018-01-01   | 4.5            | 0             |
| 'bbb'    | 2018-01-01   | 9.2            | 3             |
| 'ccc'    | 2018-01-01   | 0.5            | 1             |
| ...      | ...          | ...            | ...           |

Let's say we launch a new feature that is supposed to
reduce the number of janky page loads a user sees per hour.
There's no obvious way to calculate a t-test for
`sum(janky_loads)/sum(active_hours)`.
What is the variance of that metric?
Remember, we only get one observation per sample.
The bootstrap handles this case trivially.

# Conclusion

In summary, the bootstrap is awesome.
We get to replace arcane formulas with intuitive simulations
and we can calculate confidence intervals for any arbitrary metric.

On the other hand, the t-test is *much* more computationally efficient.
If you have really big data and you *know* you're only going to compare means,
the t-test may be a better choice.

---

1. For example, a
   [power law distribution](https://en.wikipedia.org/wiki/Power_law#Power-law_probability_distributions)
   can easily have infinite variance.
2. [Bootstrap of the mean in the infinite variance case Athreya, K.B. Ann Stats vol 15 (2) 1987 724-731](https://projecteuclid.org/download/pdf_1/euclid.aos/1176350371)

---
