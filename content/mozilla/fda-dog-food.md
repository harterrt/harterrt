title: Data Intuition Case Study: Grain-free Dog Food
slug: fda-dog-food
date: 2022-02-17
status: draft

My vet told me I should stop feeding my dog grain-free dog food. Apparently,
grain-free dog food is linked with a heart condition called Dilated
Cardiomyopathy (DCM). This set off my bullshit detector, so I decided to dig
deeper.

The FDA has a great document explaining their investigation
[here](https://www.fda.gov/animal-veterinary/outbreaks-and-advisories/fda-investigation-potential-link-between-certain-diets-and-canine-dilated-cardiomyopathy).
It's very approachable. I encourage you to give it a read. But to save you some
time, here's their summary of their investigation:

> In July 2018, the FDA announced that it had begun investigating reports of
canine dilated cardiomyopathy (DCM) in dogs eating certain pet foods, many
labeled as "grain-free," which contained a high proportion of peas, lentils,
other legume seeds (pulses), and/or potatoes in various forms (whole, flour,
protein, etc.) as main ingredients \[...\]. Many of these case reports included
breeds of dogs not previously known to have a genetic predisposition to the
disease.

In short: we heard more dogs are being diagnosed with DCM. Dogs who are
diagnosed with DCM are mostly eating grain-free dog food, which is odd, so
we're digging in deeper.

Let's review the data they present.

## Evidence

The FDA started looking into the link between DCM and grain-free dog food in
July 2018. By April 2019 they had 515 reports of canine DCM. Interestingly, 91%
of the dogs reported with DCM were eating a grain-free diet:

![ingredient prevalence for dogs with reported
DCM](https://i.snap.as/9G30pk6U.png)

That's definitely suspicious. I don't have any data to back this up, but I
suspect _most_ dogs are not eating a grain-free diet. It's strange that these
dogs are almost uniformly eating grain-free. Maybe it's that simple? 

## But how, though?

It doesn't look that simple. The FDA says DCM is usually either genetic
or caused by a taurine deficiency. The FDA's tests show the grain-free dog
foods aren't missing any important nutrients. Even weirder, Google says taurine
comes primarily from _meat_ and definitely not from grain. How could
_removing_ grain cause a taurine deficiency? The opposite seems more likely.

It sounds like the current hypothesis is that replacing corn and wheat with
peas and lentils somehow interferes with how the dog digests the food. Even
that hypothesis doesn't make much sense given the data. Only about half of the
dogs tested for taurine deficiency actually _had_ a taurine deficiency
([source](https://www.fda.gov/animal-veterinary/science-research/vet-lirn-update-investigation-dilated-cardiomyopathy)). 

Overall, it sounds like we don't really know how grain-free dog food could
cause DCM. But hey, that doesn't mean it isn't happening. So far, this still
feels worthy of further investigation.

## Another interpretation

I have a different hypothesis for what's going on here. I suspect this link
between grain-free dog food and DCM is entirely caused by a good old-fashioned
sampling bias.

The FDA notes: "We suspect that cases are underreported because animals are
typically treated symptomatically, and **diagnostic testing and treatment can
be complex and costly to owners**." (bolding mine). 

Aha! Cases are being _underreported_, but they're also being _selectively_
reported. The FDA notes many of these reports include: "echocardiogram results,
cardiology/veterinary records, and detailed diet histories". Sounds expensive.
I wouldn't be surprised if most dog owners say, "Nah, just treat the dog. No
need to call the FDA."

And there's the bias. We're only seeing dogs that belong to owners with enough
free time and money to go through the rigamarole of getting their dog diagnosed
with DCM. It's no surprise to me that these dogs are more likely to be eating a
(more expensive) grain-free diet.

So far, this is just a theory. I can see _some_ evidence for my theory in this
chart, though:

![brand prevalence for dogs with reported DCM](https://i.snap.as/CepgxknW.png)

I don't know much about dog food, but I know Acana is expensive. Acana's
website suggests their dog food is not-quite-human-grade, but is made with
human-grade ingredients. Look... humans should definitely _not_ eat dog food,
but the fact that Acana needs to set the record straight tells me this is some
gourmet shit. I've probably eaten cans of Progresso with worse ingredients.

It's strange that an expensive food like Acana is the most commonly reported
dog-food brand. I'd expect that a less expensive and more accessible dog food
(like Blue Buffalo) would be more common in practice. 

Maybe the pattern we're seeing isn't "grain-free dog food is associated with
DCM" and is instead "dog owners willing to pursue a DCM diagnosis also tend to
buy expensive dog food". Maybe I'll call this an "Affluence Bias".

## Prevalence

Zooming out, this looks to be a rare disease. The FDA announced they were
investigating grain-free dog food in July 2018. Up to April 2019 the FDA
received 515 reports of canine DCM and they estimate there are 77 million pet
dogs in the US. That's ~0.0007% of dogs per year.

Even if the real case count is 100x bigger than the reported case count, that's
still less than a tenth of a percent of all dogs. I think it's safe to call
that "rare".

## In Summary

I don't plan on changing my dog's food - at least not given these data.

It looks like the FDA is demonstrating an abundance of caution by investigating
this link. From what I understand, [that's what the FDA
does](https://astralcodexten.substack.com/p/adumbrations-of-aducanumab). 

However, my vet shouldn't cite these results as fact given this level of
evidence. Vets probably shouldn't cite this relationship _at all_ given the
effect size of 0.0007% of dogs per year. We've got bigger things to worry
about.

When all is said and done, I expect we'll all be left with a vague sense that
grain-free dog food causes DCM. In reality, I suspect it's just a quirk of the
data collection.
