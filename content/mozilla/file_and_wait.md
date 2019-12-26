title: File and Wait Data Science
date: 2019-01-01
status: draft

File and wait
Our primary goal is fixing the organizational consternation we have over our retention metrics.

Originally, this project was started by Shani with the goal of “Find[ing] a 2% increase in retention”. However, because this is a Data Science project it makes more sense for this goal to be something like “Enable Product to find a 2% increase in retention”. 

Mozilla often has a dark pattern of dispatching data questions to data scientists, even for small investigations. In the ideal world product would do most of their exploration individually. Data science would be available to debug data problems, handle longer term research projects, and making it easier for product to work with the relevant data.

This doesn’t work and is frustrating for both parties. Data scientists are inundated with small requests that require a lot of context switching. Product teams are constantly delayed waiting on answers to small questions. More so, understanding data is iterative which means product often gets more questions with each response!

Part of this issue is context. As you work with data you start to build a gut-feeling about the data. What looks right and what looks off. This context helps the researcher hypothesize about explanations for data oddities and helps them formulate hypotheses about where to look next and what is important to understand. When teams follow the file-and-wait approach the data scientists build context but the product team issues direction. This is no good! Data science wants product to be issuing the direction, but the person with the most context is the most capable of issuing direction.

This leads to frustration. Most context is never documented or written down. This isn’t laziness, it’s just the nature of the work. When you explore data you get an understanding of what’s reasonable and what is not. Three days ago your DS looked at a graph that suggests your new direction doesn’t make sense. The product manager isn’t convinced (rightfully so) and the data scientist is frustrated to chase down a lead that doesn’t exists (rightfully so).

Hillary Mason summarizes this phenomenon: “Data leave scars”. You want this accumulated knowledge to sit with the product team.

---

There’s still a problem though. In new areas, product often doesn’t know where to begin.

File-and-wait iteration happens a lot in the beginning of a research project. It can be difficult and overwhelming to start research into a new area. It’s best if data scientists start the investigation, build up some context and guardrails, and hand the scoped problem space over to product.


---

Think of the data scientist as a woodshop manager. They are available for questions and advice on difficult projects. They maintain the equipment so that they’re safe and usable. In general, they don’t interfere with your project unless they see something unsafe happening.

This avoids most of the risks evoked when we think about “home dentistry”.

We often talk about self-serve data tools or democratized data. On the other hand, we have a history of “home dentistry” when it comes to data.

