title: Beer and Probes
slug: probes
date: 2017-08-23

Quick post to clear up some terminology.
But first, an analogy to clear up my thinking:

## Analogy

Temperature control is a big part of brewing beer.
Throughout the brewing process I use a thermometer
to measure the temperature of the soon-to-be beer.
Because I take several temperature readings throughout the brewing process,
one brew will result in a list of a half dozen temperature readings.
For example, I take a mash temperature,
then a sparge temperature,
then a fermentation temperature.
The units on these measurements are always in Fahrenheit,
but their interpretation is different.

## The Rub

In this example, I would call the thermometer a "probe".
The set of all temperature readings share a "data type".
Each temperature reading is a "measurement" which is stored in a given "field".

At the SFO workweek I uncovered some terminology I found confusing.
Specifically, we use the word "probe" to refer to data we collect.
I haven't encountered this usage outside of Mozilla.

Instead, I'd suggest we call histograms and scalars "data types".
A "probe" is a unit of client-side code that collects a measurement for us.
A single "field" could be be a column in one of our datasets (like `normalized_channel`).
A measurement would be a value from a single field from a single ping (like the string "release").
