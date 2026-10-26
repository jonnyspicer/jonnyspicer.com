---
type: blog
date: "2026-10-26T19:25:00Z"
author: Jonny Spicer
title: "Are The Robots Coming For Us?"
categories:
- AI
tags:
- egghaven
# status: 
# confidence: 
# importance: 
---
*I’m shamelessly ripping off Inkhaven and doing my own challenge, Egghaven. This is the first post.*

## What are the right questions to ask?

Many common arguments that advanced AI poses an existential risk include robots in some way. I know nothing about robotics. I suspect that many people who make x-risk arguments *also* know nothing about robotics, and often have a reasoning step along the lines of "and then the superintelligent AI system uses its unfathomable cognitive powers to produce huge numbers of robots with dramatically improved capabilities in an unprecedentedly short space of time". There's some chance this is a perfectly reasonable claim to make, but it's the kind that makes me suspicious. Due to the prevalence of robotics as a vector for catastrophe, understanding the reality of the field is necessary in order to have any kind of rigorous model of the risks of developing AGI. I want to have such understanding, at least in its minimum viable form.

The common arguments I have in mind include[^1]:

- **Concentration of power** achieved through AI-enabled coups or an overwhelmingly dominant military force. Robots replace soldiers or officials who are needed to perpetuate the new authoritarian state. Relatively small numbers of robots might be required if they have the ability to occupy key positions. Alternatively, broader military might could be achieved through dramatic advances in robotics, brought about by superintelligent AI systems. The (extremely undesirable) values of the hegemony are locked in, as it is impossible for other groups to overcome the advantages afforded by the quantity and/or capability of their robots.
- **Misaligned takeover** whereby AI no longer needs humans to achieve its goals. Robots perform every physical task necessary for the AI's aims (including potentially killing people). This might include maintaining factories, data centres and energy production. The robots are the ones who [actually turn the people into paperclips](https://nickbostrom.com/papers/ethical-issues-in-advanced-ai/).
- **Gradual disempowerment** in which robots remove humanity's last competitive advantage: competence at physical labour. We have no remaining bargaining power with superintelligent AI systems and are essentially vassals (or worse). Akin to The Matrix, but worse -- at least in that movie, the machines have *some* use for the humans; they can plug them in and extract energy from them. In reality, we might not even have that much value.
- **Great power war** fought with autonomous weapons that are extremely effective. Essentially a MAD scenario. The war is conducted primarily with UAS, of various shapes and sizes; these include tiny drones that are capable of poisoning people or carrying explosive charges.

All of these rely on something akin to the industrial explosion as described in [AI 2027](https://ai-2027.com/) and further [discussed by Daniel Kokotajlo elsewhere](https://80000hours.org/podcast/episodes/daniel-kokotajlo-ai-2027-updates-china-robot-economy/). Is such an explosion feasible, and how might it play out? There are multiple relevant aspects of robotics:

- How capable are the robots, and can they generalise to new tasks?
- How reliable are the robots in deployed environments?
- How many robots can be produced per unit time?
- How does the cost per effective hour of automated labour compare to that of human labour?
- Related to all of the above, what form factor do the robots take? Are they drones, arms, humanoids?
- Who builds and controls them? China is far ahead in manufacturing but somewhat behind in AI.

What is the current state of each of these facets of robotics? How might advances in AI contribute in the future?

## Capability and generality

Labs like [Physical Intelligence](https://www.pi.website/) make bold claims and produce [flashy demos](https://www.pi.website/blog/pistar06), and do seem to be making [some meaningful progress on generality.](https://www.pi.website/download/pi07.pdf) However, these results seem brittle — this [paper shows that a Physical Intelligence vision-language-action model, π0, falls from 94.2% to 15.8% on LIBERO-Plus when its camera angle changes](https://arxiv.org/pdf/2510.13626). As with LLMs, there is a split in capabilities between open- and closed-source VLAs, but most frontier VLAs are not benchmarked against those of other companies or against open-source competitors. This makes it hard to meaningfully evaluate what the rate of progress here is; companies are naturally incentivised to inflate their own progress.

That current SotA VLAs don’t seem especially concerning isn’t much of an update — I am much more interested in how they scale with intelligence, and particularly what happens when robots have an LLM as their “brain”. There are surprisingly few benchmarks for this. Andon Labs’ [Blueprint Bench](https://andonlabs.com/evals/blueprint-bench-2) is helpful for seeing the trend of spatial reasoning improvements in frontier models, but their (imo much more useful) [Butter-Bench](https://andonlabs.com/evals/butter-bench) hasn’t been updated in over a year.

<figure>
  <img src="/img/blog/2026/10/are-the-robots-coming-for-us/butter-bench.png" alt="Screenshot from Andon Labs' Butter-Bench write-up">
  <figcaption>In a moment of art imitating life, Andon Labs reported that Sonnet 3.5 found itself in a doom-spiral on a robotic side experiment.</figcaption>
</figure>

Fortunately, Artificial Analysis have stepped up with [AA-Robotics](https://artificialanalysis.ai/articles/aa-robotics), a benchmark where frontier LLMs directly operate a robot arm.[^2] This broadly showed that models are extremely slow, incompetent and expensive when compared to humans. This is promising! But I think measuring the rate of progress here will be important. I expect LLMs to continue scaling in a way that VLAs won’t (among other reasons, because it’s much easier to produce data for LLMs than VLAs), and the history of LLMs has taught me that many surprising capabilities can be unlocked simply by having an improved understanding of language.

These results, combined with [Epoch’s work evaluating robot capabilities](https://epoch.ai/publications/where-autonomy-works-evaluating-robot-capabilities-in-2026), make me somewhat optimistic. Robots have a long way to go before they can be used in any catastrophic risk scenario. It is entirely possible that improvements in intelligence might unlock robotic capabilities past some particular threshold, or that there could be a new technique leading to an “unhobbling” of these capabilities, or that [sufficiently advanced LLMs could substantially speed up robotics R&D](https://www.anthropic.com/research/project-fetch-phase-two). However, these are largely still theoretical; the empirical evidence is early and inconclusive.

## Reliability

Clearly, robots can improve significantly, to the point where they are dramatically more reliable than humans in deployed environments — the prototypical example here being [Waymo](https://waymo.com/safety/impact/):

<figure>
  <img src="/img/blog/2026/10/are-the-robots-coming-for-us/waymo.webp" alt="Jonny in a Waymo in San Francisco">
  <figcaption>Me, in a Waymo in San Francisco, enjoying a ride that is statistically ~95% safer than taking an Uber</figcaption>
</figure>

Waymo needs to have [several nines of reliability](https://en.wikipedia.org/wiki/High_availability#%22Nines%22) in order to be able to deploy its robotaxis. It’s a clear example of a high bar for a robot, which it duly surpasses. Other deployment environments — for example, warehouses — might only require around 99% reliability for their pick-and-place robots. In warzones, drones might need far less reliability at hitting a given target before deploying them becomes acceptable.

Unsurprisingly, AA-Robotics found that not only were LLMs bad at completing tasks with a robotic arm, they were also bad at judging when the task was finished. It seems reasonable to infer that they are also bad at completing tasks reliably and consistently. Generally I find this less positive overall — there are at least some threat models which don’t require robots to be highly reliable for them to be effective, and even if that wasn’t the case, we have clearly shown that we can get robots to be extremely reliable while deployed in complex environments.

## Speed of production

There are about 5 million deployed industrial robots, of which about 600,000 were installed last year, [per the IFR](https://ifr.org/ifr-press-releases/five-million-robots-now-operate-in-factories-globally). This represents a [doubling time of around 6 years](https://www.forethought.org/research/the-industrial-explosion), although doubling times for risk-relevant categories of robots are much shorter, [notably 33 months for drones, 10 months for quadrupeds and 6 months for humanoids](https://epoch.ai/publications/how-fast-could-robot-production-scale-up)[^3]. There are also various physical limits; new factories in China take at least 6 months to build, and in the West they are often 2+ years, and high-precision reducers are a significant bottleneck to dramatically scaling up humanoid production. While factories could be repurposed, historical wartime demand shocks only raised growth rates 1.4-2.2x, although AI-induced demand shocks would presumably be able to squeeze out some additional efficiency.

A high production rate is essential for misaligned takeover and gradual disempowerment, but manufacturing capacity is generally slow to build, and there isn’t a huge volume of it already in place. There are arguments to be made for how advances in AI might be able to yield significant boosts in capacity, but again, these are currently theoretical rather than empirical, and are more speculative in my opinion. The news here is potentially especially promising if you think that the West will reach RSI/AGI first; its manufacturing capacity is significantly behind China’s, and its ability to grow it much slower. For a (much) more thorough discussion on the economics and physical limitations of an industrial explosion, I recommend [this series by Damon Binder.](https://defensesindepth.bio/ai-industrial-takeoff-part-1-maximum-growth-rates-with-current-technology/)

## Cost per effective hour

[Anthropic found](https://www.anthropic.com/research/what-work-can-robots-do) that automated labour is competitively priced against human labour for ~0.3% of US job tasks, and it would take ~40 years to reach 10% if current trends continue. Robots require significant upfront costs that have to be paid back before companies profit from them — Chinese humanoid robots cost around [$35k](https://www.cervo-tech.com/blog/robot-actuator-market-statistics-2026.html) to buy, and Goldman Sachs [estimated they cost about 2.8 years of a factory worker’s labour](https://finance.biggo.com/news/f946b229-ffdf-4471-a637-bf8798dd9aec)[^4]. For a base-model humanoid, assuming it runs at 6000 hours a year for 5 years, that’s ~$1/hour in capital, but VLA-driven robots [are 3-10x slower than humans](https://epoch.ai/publications/where-autonomy-works-evaluating-robot-capabilities-in-2026).

Cost is primarily relevant to discussions of gradual disempowerment. The findings here aren’t much of an update; widespread robotic labour isn’t currently economically viable, largely because of issues with capability and reliability. If those things improve significantly, the unit economics would change commensurately.

## Form factor

Specialised robots can already scale fast; [drone production in Ukraine increased by three orders of magnitude between 2022 and 2025](https://www.justsecurity.org/138164/ukraine-drone-superpower/). [Amazon deployed its millionth warehouse robot last year.](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) Humanoid production is much lower — only around 16k in 2025 — and robotic arms are still low at around 570k [with a comparatively flat growth rate.](https://epoch.ai/publications/how-fast-could-robot-production-scale-up)

Concentration of power and great power war largely require drones, which we are already capable of producing plenty of. Misaligned takeover likely requires significant amounts of dexterity, and gradual disempowerment likely requires even more than that.

## Geopolitical control

China already builds [>80% of the world’s humanoid robots](https://emag.directindustry.com/2026/03/17/china-humanoid-robots-market-unitree-robotics-agibot-ubtech-leju-xpeng/). It also owns large parts of the supply chain, and has [export controls on rare-earth minerals](https://www.bbc.com/news/articles/c1drqeev36qo) that it has [temporarily suspended with the US](https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later).

Military control is already a contentious issue; Anthropic [declined to remove safeguards that would allow its models to be used in autonomous weaponry](https://www.anthropic.com/news/statement-department-of-war), which led to it being designated a [supply-chain risk by the US Department of War](https://www.anthropic.com/news/where-stand-department-war) (as well as presumably costing it lucrative government contracts). The recent [UN collective statement on the use of autonomous weaponry was primarily watered down by, ah, Russia and the United States](https://www.hrw.org/news/2026/09/07/un-talks-on-killer-robots-end-with-calls-for-negotiations-growing).

LLM-brained robots also inherit all the same issues as their purely textual counterparts, possibly including jailbreaks, prompt injections, trigger phrases etc. It’s possible that robots designed and built by one actor could be vulnerable to being taken over by another actor, including at a large scale.

The current geopolitics of robotics does not fill me with confidence at all. China’s dominance as a manufacturer, combined with the US’ increasing hawkishness, will continue to concern me unless the latter changes at the next election.

## In conclusion

I think having a basic understanding of the following is useful in order to understand how advances in robotics might affect catastrophic risks:

- The capabilities of the current SotA VLAs, and of LLMs on robotic benchmarks
- The rate of progress on these two things
- The unit economics of different kinds of robot
- The bottlenecks to scaling up production of different kinds of robot

My broad takeaway here is that the current capabilities are lacklustre, but I am concerned that they could improve rapidly, enough to enable significant risk vectors from developing advanced AI systems — there is not particularly strong evidence here; I am mostly indexing off the rate of progress in other AI domains. Robots right now are extremely expensive, but costs will come down if/when improved capabilities drive increases in demand. There is evidence that global superpowers are willing to use autonomous weaponry on the battlefield, and that they have the capacity to quickly produce huge quantities of drones. I think the current state of robotics shows there is at least a somewhat clear path towards robots enabling catastrophes from concentration of power, misaligned takeover, gradual disempowerment and great power war, but that the first three are primarily contingent on above-trend improvements in capabilities. Catastrophe from great power war seems plausible in the short term even with on-trend improvements.

[^1]: NB I'm aware that none of these explicitly require robotics in order to be a catastrophic risk; I am simply highlighting that robotics is an important potential vector for each of them.

[^2]: If this benchmark catches on and/or if similar ones pop up, there’s a good chance labs would start training for it. I think it would be dangerous for them to do this without fully thinking through the potential ramifications.

[^3]: Although Epoch note in their analysis that humanoid production is starting from a tiny base, and so the doubling time figure is likely anomalous.

[^4]: Obviously apples-to-oranges for various reasons, but an average US worker costs ~$1m to bring up, including money their parents spend, the value of their parents’ time, and the value of their schooling. So, even assuming the robot is being sold with a healthy margin, companies are probably getting a phenomenal deal with human workers!
