---
title: SQL style - where do the commas go?
date: 2024-06-05T20:45:00
slug: commas-sql-style
---

**TL;DR:** there are good arguments for leading commas,
but I recommend using trailing commas for consistency.

---

We didn't take an opinionated stance on comma placement when writing
[Mozilla's SQL Style Guide][mozilla]
probably to avoid a quagmire.
I'm trying to figure out where I stand now, so I wrote it out here.

Here's an example query so we can talk concretely:

```sql
SELECT
  column_a,
  column_b,
  column_c
FROM
  table_a
```

This query uses **trailing commas** -
where there's a comma, it's the last character on the line.
This is by far the most common style of writing queries.

On the other side, there are folks that prefer **leading commas**, like so:

```sql
SELECT
  column_a
  , column_b
  , column_c
FROM
  table_a
```

This is a less common style, but is fervently loved by its proponents.
Leading comma proponents will argue that this style is easier to work with
and makes git commits more readable.

Similarly, there are fervent proponents of trailing commas.
They'll argue that trailing commas are convention by overwhelming majority
and leading commas are jarringly ugly.

In reality, most analysts don't care either way.
They tend to use trailing commas by default.

The [spaces-vs-tabs](https://www.youtube.com/watch?v=SsoOG6ZeyUI)
absurdity of this argument is not lost on me.
But, I _do_ care about SQL style, so here I am.

## Consistency is paramount

Like [PEP8](https://peps.python.org/pep-0008/), 
[Mozilla's SQL Style Guide][mozilla]
aims to make queries 
consistent in service of readability.

Trailing commas are by far the most common pattern.
For example:

* [Mozilla's Style Guide][mozilla]
  uniformly uses trailing commas in examples
  despite not making an explicit recommendation on comma format.
* BigQuery's documentation uses trailing commas 
  ([e.g.](https://cloud.google.com/bigquery/docs/running-queries))
* Simon Holywell's SQL Style Guide ([sqlstyle.guide](https://www.sqlstyle.guide/))
  uniformly uses trailing commas
* SQLFluff's [`Rule_L019`](https://docs.sqlfluff.com/en/stable/rules.html#rule-layout.commas)
  defaults to trailing commas.

But the most convincing source I found is Ben Stancil's 
[analysis of queries in Mode][stancil]. 
He found that ~80% of sufficiently-complex queries use trailing commas.
Only ~15% of query authors frequently use leading commas.

**Trailing commas are clearly the dominant convention**.
Style guides are about consistency.
This is enough evidence for me to recommend trailing commas
as the right default.

That said, there _are_ some motivating reasons to use leading commas.

## Ergonomics

The most common argument I see for leading commas is that 
it's easier to edit queries - especially when prototyping an analysis.

Until recently, the following SQL would produce an error in most SQL engines:

```sql
SELECT
  column_a,
  column_b,
  -- column_c
FROM
  table_a
```

That **hanging comma** after `column_b` is invalid.

This can be very annoying when hacking on a query.
Commenting out a column creates an error. Yuck.

**I suspect this is why folks started using leading commas in the first place**.
We can just comment out the line if we're using leading commas:

```sql
SELECT
  column_a
  , column_b
  -- , column_c -- this line in commented out
FROM
  table_a
```

This is nice, but in practice,
many modern SQL engines have stopped throwing this error.

We owe a debt of gratitude to [DuckDB](https://duckdb.org/)
for pushing the industry forward here.
Their [Friendly SQL](https://duckdb.org/2022/05/04/friendlier-sql.html)
created some great quality-of-life improvements
that are quickly being adopted by competitors.
BigQuery, for example.

Unfortunately, the progress is incomplete.
Most query engines, like Presto or SQLite,
will still throw hanging comma errors.

Even more frustrating, 
this isn't consistently enforced even _within_ a single query.
Take this failing BigQuery query for example:

```sql
SELECT
  column_a,
  column_b, -- valid hanging comma
FROM
  table_a
WHERE
  column_a IN (
    "first",
    "second",
    "third", -- invalid hanging comma, causes an error
  )
```

SQLFluff addresses this pattern in their rule CV03, 
[Trailing commas within select clause](https://docs.sqlfluff.com/en/stable/rules.html#trailing-commas-within-select-clause).

In their own works:

> For many database backends this is allowed. For some users this may be
something they wish to enforce (in line with Python best practice). Many
database backends regard this as a syntax error, and as such the SQLFluff
default is to forbid trailing commas in the select clause.

I agree with the default of forbidding trailing commas.
I'll take it a step further:
allowing trailing commas 
**creates inconsistency within a query and should be forbidden**,
even where the query engine allows it.

It's fine to use leading commas or hanging commas
while hacking on an ad hoc query. They're convenient. I use them too.
But these conveniences should be cleaned up 
before committing the query to a code base.

## Cleaner git commit messages

A corollary to the above argument 
is that leading commas create cleaner commit messages.

We need to touch two lines to delete a column using leading commas:

```sql
SELECT
  column_a,
  column_b    -- remove a comma from this line
  -- column_c -- delete this line
FROM
  table_a
```

We can contain our changes to one line if we use leading commas

```sql
SELECT
  column_a
  , column_b
  -- , column_c -- only need to delete this line
FROM
  table_a
```

I _guess_ this is a benefit, but I don't find it motivating.

Style guides exist because code is read far more often than it's written.
A commit message is read less frequently than the code -
probably by an order of magnitude.

Making a trivial improvement to the git diff 
is not worth breaking convention.

## Commas are load bearing

The best argument I've seen is that 
commas kinda look like keywords if you squint hard enough.
We _do_ require keywords to be at the beginning of the line.
We _also_ require Boolean operators to be at the beginning of a line.

For example, if commas _were_ keywords 
it would be obvious that they should be at the beginning of the line:

```sql
SELECT
  column_a
  COMMA column_b
  COMMA column_c
FROM
  table_a
```

The consistency win becomes even more clear if we add a join 
and some Boolean operators:

```sql
SELECT
  column_a
  COMMA column_b
  COMMA column_c
FROM
  table_a
LEFT JOIN
  table_b
  USING (joint_key)
WHERE
  column_b > 0
  AND column_c = 'bbb'
```

Commas are load bearing.
They carry meaning but are easily missed at the end of a line.

This is pretty esoteric though. 
Also, commas are not actually keywords, soooo...

## Spotting errors

Another reasonable argument for leading commas 
is that it makes it easier to spot a particular type of error.

Take this query for example:

```sql
SELECT
  first_column,
  second_column
  another_column,
  final_column
FROM
  table_a
```

It looks like the resulting table will have four columns,
but in reality it will only have three columns.

There's a missing comma after `column_b`.
Most SQL interpreters will interpret this query to mean:

```sql
SELECT
  first_column,
  second_column AS another_column,
  final_column
FROM
  table_a
```

The error is more obvious if we use leading commas:

```sql
SELECT
  first_column
  , second_column
    another_column
  , final_column
FROM
  table_a
```

The solution to this problem is fairly simple: Use a code linter and formatter.
Probably [SQLFluff](https://sqlfluff.com/).

The linter will make the error even _more_ obvious than leading commas would:

```sql
SELECT
  first_column,
  second_column AS another_column,
  final_column
FROM
  table_a
```

## Conclusion

There _are_ good arguments for using leading commas.
If I were coding in a vacuum,
I might recommending standardizing around leading commas.

However, that's not the case.
Trailing commas are the dominant convention by a long shot.
The battle is lost.

Use trailing commas.

[Stancil]: https://mode.com/blog/should-sql-queries-use-trailing-or-leading-commas
[Mozilla]: https://docs.telemetry.mozilla.org/concepts/sql_style.html
