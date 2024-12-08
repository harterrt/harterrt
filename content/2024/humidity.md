---
title: Humidity and ratios
date: 2024-12-07T17:24:00
slug: humidity
---



My house gets super dry in the winter and I didn't understand why.

My weather station says it's drier inside than outside,
which didn't make a ton of sense. 
I'm cooking, and sweating, and showering inside.
It should be _more_ humid.

I suspected my forced hot air system was to blame,
but I didn't understand the mechanism.
_Cooling_ air makes it drier, but _heating_ shouldn't remove any water.
Like - I know my A/C has a drain on it, but my furnace definitely doesn't.

# _Relative_ humidity

As it turns out, I didn't understand my metric.
My weather station reports _relative_ humidity,
and I guess I always just ignored the "relative" part?

<!-- 
I assumed 60% humidity meant that there was more water in the air 
than at 30% humidity,
which is not necessarily true.
-->

Relative humidity is how close we are to the maximum humidity
_at a given temperature_.
Hot air can hold a lot of water, cold air holds very little water.
The difference is huge - air at 68°F can hold ~4x more water than at 32°F
(at least that's what I understand from skimming this 
[wikipedia article](https://en.wikipedia.org/wiki/Vapour_pressure_of_water)).

So when I opened my windows to let in the 60% humidity 32° air,
the relative humidity dropped to 15% after heating it to 68°.
Mystery solved.

# Beware shifting denominators

When a ratio moves, people tend to think it's because the numerator shifted.
It can be very misleading when the denominator changes instead.

For example: 
the percent of users buying a product after visiting your store
increases by from 25% to 50%! 
That's great! Unless you just lost a bunch of traffic to your store:

<style>
	table {
			border-collapse: collapse; /* Removes extra spacing between cells */
			margin: 20px 0;
			font-size: 16px;
      text-align: right;
	}
	th, td {
			padding: 10px;
			border: 1px solid #ddd; /* Adds a light border */
	}
	th {
			background-color: #f4f4f4; /* Adds a subtle background for headers */
			font-weight: bold;
	}
	tr:nth-child(even) {
			background-color: #f9f9f9; /* Alternating row colors */
	}
	tr:hover {
			background-color: #f1f1f1; /* Highlight rows on hover */
	}
  th:first-child, td:first-child {
      text-align: left; /* Align the first column to the left */
  }
</style>

<table>
  <tr>
    <th> Date </th><th> Purchases </th><th> Visits </th><th> Purchase Rate</th>
  </tr>
  <tr>
    <td> Yesterday </td><td> 20 </td><td> 80 </td><td> 25% </td>
  </tr>
  <tr>
    <td> Today </td><td> 15 </td><td> 30 </td><td> 50% </td>
  </tr>
</table>

Sure your purchase rate increased, but you made fewer sales overall.
Damn the denominator!


"Be skeptical of ratios" is pretty good advice -
at least make sure you understand how the denominator moves.

# It's still useful

Some folks take this skepticism of ratios to an extreme
and say you shouldn't use ratios when reporting data.
**That's a mistake**.

You shouldn't make your reader work harder than they need to.
A ratio is often the easiest way to describe what's happening in the data.

_You_ have a responsibility to make sure the data aren't misleading,
but hopefully your reader trusts you to guide them to the right conclusion.
This is **critical to good data storytelling**.

Relative humidity wasn't useful for understanding _why_ my house was dry.
It _is_ useful for measuring how dry the air feels.
It would be maddening to report absolute humidity 
next to a saturation vapor pressure table instead.


<!--
When reporting data it's best to make the ratio, numerator, and denominator all available separately.

So like, as a metric, 
relative humidity is not very useful for figuring out why my house is so dry.

My gut reaction is to say it's a stupid metric.
Report absolute humidity instead.
Then we have a constant denominator.

"Don't use ratios" is pretty common advice for data work.
Being skeptical of ratios is data intuition 101.


----

I tried cycling the air in the house - 
opening windows and doors to let some of the humid outdoor air inside.
That didn't seem to improve the humidity at all

-->
