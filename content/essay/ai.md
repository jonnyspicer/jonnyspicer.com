---
type: "essay"
date: "2024-05-07T17:33:10Z"
author: Jonny Spicer
title: "AI"
summary: "My attempts at answering the important questions; how will AI advances affect our society, how long will it take for these changes to manifest, and how concerned should we be about the risks involved?"
---
*This page is intended to summarize my current views on AI, in various ways that I think are important. It's intended to be evergreen, and I will endeavour to update it when my beliefs and opinions change.[^1]* 

*It was last substantially updated on May 9th, 2024. I have put a significant amount of time and effort into understanding this topic, although presently I am still very uncertain about most of it. The beliefs and opinions below are likely to go out-of-date quickly. If you think something I say here is wrong, then please [contact me,](/contact) if you have good evidence or arguments then I will update my views accordingly.*

## In a Nutshell

1. I am extremely uncertain about how advances in artificial intelligence will arise, at what rate, and what effect they will have on the world. I am committed to applying [the scout mindset](https://www.youtube.com/watch?v=w4RLfVxTGH4), and trying to learn what I can with sincere curiosity.
2. I expect the development of AI systems to have a meaningful effect on our society in the next 2-5 years. I think that the previous technology most likely to be analogous to AI is the internet (as opposed to e.g. cryptocurrency or nuclear fission).
3. I think there are a variety of ways in which these changes could be negative, up to and including posing an existential risk to humanity. This belief is largely grounded in the current gap between model capabilities and control systems. I think that the worst-such outcomes are *unlikely in the next decade*. After that I am much less certain.
4. I think there are a variety of ways in which these changes could be positive, up to and including transforming our society into one with universal happiness and flourishing. I believe that AI could fundamentally solve most, if not all, problems currently facing humanity. I think that these extremely positive outcomes are *significantly more likely* than the extremely negative ones, providing we collectively exercise sufficient caution in the development of these technologies.
5. I want to contribute to ensuring its safe development in any way that I can, and am actively working to find my comparative advantage in doing so. 

## Where Are We?

### AI is Already Here

When discussing AI, much of the focus is on its future capabilities, and the transformative effects they might have on our society and economy. But current AI systems are already extremely capable, and indeed already affecting both our society and economy - see for example [this report on illustrators and translators losing a significant amount of work due to AI.](https://www2.societyofauthors.org/2024/04/11/soa-survey-reveals-a-third-of-translators-and-quarter-of-illustrators-losing-work-to-ai/) [Hundreds of millions of people use ChatGPT, and millions of developers are using their API](https://www.theverge.com/2023/11/6/23948386/chatgpt-active-user-count-openai-developer-conference), eliminating many rote or mundane tasks. 

[GitHub Copilot has over a million users](https://www.zdnet.com/article/microsoft-has-over-a-million-paying-github-copilot-users-ceo-nadella/), including me. It’s difficult to estimate productivity, but I would guess I am anywhere from 50% to 200% more productive when using a combination of Cursor and Claude to help me code. I almost never use Google, now preferring ChatGPT or [Perplexity](https://www.perplexity.ai/) when I need something with up-to-date knowledge. [Elicit](https://elicit.com/) helps me understand the quality of information available in scientific papers, despite having no academic background, and further lets me discover ones that are most relevant to any question I have. It makes the repository of scientific truths accessible for lay people. [Dall-e](https://openai.com/dall-e-3) makes custom images for me when I need them. [Suno lets me turn my blog posts into goofy midwest emo songs.](https://suno.com/song/2d3395ff-7a3f-466b-add7-1e98d50e430b) I could use [Eleven Labs](https://elevenlabs.io/) to narrate those same posts as podcasts, as soon as I publish them to this website.

I don’t think many of this projects have escaped the AI bubble yet - many of my fellow tech workers are unaware of them, let alone folks outside tech. But they are already powerful, they are pretty cheap, and they’re still young. I think many people who talk about what AI might do in the future would be surprised by what AI can already do today.

### There is a Gap Between Capability and Control

Per [learnprompting.org](http://learnprompting.orghttps://learnprompting.org/docs/prompt_hacking/jailbreaking):

> **Jailbreaking** is the process of getting a GenAI model to do or say unintended things through prompting. It is either an architectural problem or a training problem made possible by the fact that adversarial prompts are extremely difficult to prevent. 

As the definition notes, it is [extremely difficult to prevent jailbreaks](https://arxiv.org/abs/2311.14455). Searching Twitter or Reddit will surface plenty of people who claim to have jailbroken models like Claude Opus or ChatGPT, and while the creators of those models work quickly to plug the holes in their defences, it is a cat-and-mouse game which naturally favours the attackers. Not all current frontier models are available for fine-tuning, but for those that are, [the process can be used to remove many of the safety features](https://hai.stanford.edu/sites/default/files/2024-01/Policy-Brief-Safety-Risks-Customizing-Foundation-Models-Fine-Tuning.pdf) their creators originally added. There are concrete problems that seem as-yet satisfactorily solved, like those of [sleeper agents](https://arxiv.org/abs/2401.05566), specific triggers that can be implanted during a model’s training which can be activated after deployment in order to remove safety guardrails (although [there are attempts being made to do so](https://www.anthropic.com/research/probes-catch-sleeper-agents)).

Despite this, the sky has not fallen. There haven’t been reports of a massive uptick in spear phishing or ransomware attacks, despite the fact that these might’ve been made easier with the assistance of LLMs. There are many possible explanations, all of which seem plausible to me:

- Manipulating a model for criminal purposes still requires a sufficient amount of skill, and anyone with that skill could likely use it to find gainful employment instead;
- Criminals are slow on the uptake for some reason (that reason possibly being that their current schemes are already working just fine), and we might see a rise in cybercrime once they catch up;
- The bottleneck in scaling up this kind of crime is not something that could be solved by automation with language models.[^4]

I am concerned that we could see more serious harms come from already existing technology. For example, [Palantir now offers an “AI defence platform”](https://www.palantir.com/platforms/aip/defense/), and it’s not hard to imagine this as having the ability to use lethal force without a human in the loop.

### Serious People Take This Seriously

There’s near-universal agreement that AI is going to be a Big Deal, even if there is broad range of opinions on what exactly we should do about it. All of the Big Three ([Anthropic](https://www.anthropic.com/news/anthropics-responsible-scaling-policy), [Google Deepmind](https://deepmind.google/about/responsibility-safety/), and [OpenAI](https://openai.com/global-affairs/our-approach-to-frontier-risk)) have public frameworks and commitments around safety, that seem to be genuine and serious. The US has an [Artificial Intelligence Safety Institute](https://www.nist.gov/artificial-intelligence-safety-institute), as [does the UK](https://www.gov.uk/government/organisations/ai-safety-institute). China seems (surprisingly?) [willing to cooperate with the West on AI governance](https://www.ft.com/content/94b9878b-9412-4dbc-83ba-aac2baadafd9). The EU recently passed the [Artificial Intelligence Act,](https://artificialintelligenceact.eu/) although my understanding is that it was fairly tame in order to transparently prevent French company [Mistral](https://mistral.ai/) from falling too far behind.[^5] The California State Senate looks on the verge of passing [Bill SB-1047, the Safe and Secure Innovation for Frontier Artificial Intelligence Models Act,](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1047) with the aim of applying some scrutiny to the largest models.

I, like many others, was pleasantly surprised at how great the appetite for regulation of AI seemed to be. My impression is that we are in a kind of regulatory limbo - legislation has been enacted relating to AI and its risks, but it’s not clear that *it would actually do anything* - for example, the recent executive order from the White House mandates that companies must [inform the government if they are planning on doing a training run of greater than 10^26 FLOPS](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/), however they don’t offer any information on how the government might respond to such a notification. Nobody really seems to know, and I suspect this is because the White House hasn’t figured it out either, and they’re hoping having *some* kind of regulation will buy them some time to get a handle on things.

## Where Are We Going?

### GPT-5 Level

I would guess that GPT-5 level models are currently (as of May 2024) in training, although I am unsure whether it would make sense to deploy them in the near future. Regulators have shown they’re keen to enact legislation regarding AI, in particular frontier models, but that legislation has yet to pass. One strategy could be to rush GPT-5 out the door before it would be subject to any legal restriction, but that would surely antagonize the legislature and potentially impose harsher impositions on GPT-6. Another would be to wait until the regulatory dust has settled, but I can imagine OpenAI being reluctant to do this, as it may allow time for the other major players to catch up. I think there is a 5% chance that GPT-5 (or equivalent, regardless of name) is released in 2024, a 75% chance its released by the end of 2025 and a 95% chance by the end of 2026 (the remaining 5% here comes from the chance of stringent legislation making GPT-5 no longer commercially desirable).

I do not feel particularly worried about harms from GPT-5 level models, but I am not sure whether this is backed by fuzzy intuitions or solid reasoning. Given GPT-4 doesn’t seem to have had many negative affects, on a gut level it feels unlikely that GPT-5 would cause the downfall of society. One crux seems to be how well agents will work at GPT-5 levels of intelligence; generally these do not seem to work well with GPT-4 standard models, and I am not certain whether all they need is better next-token prediction, or if there is some other unknown quality that they lack. If it’s the former, then I would be more concerned - one of the biggest worries I have about harms caused by AI systems is that misaligned agents might pursue instrumentally convergent, power-seeking goals. 

Let’s if you have an AI agent that you’ve tasked with maximising some desirable outcome, like reducing carbon emissions for your business. The AI might correctly identify that carbon emissions are inversely proportional to amount spent on reduction, so one solution it might have would be to divert all your existing resources into minimising carbon emissions, or to cease business operations entirely (thereby not producing any carbon in the first place), both of which would be examples of [specification gaming](https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/). Perhaps you specified the [reward function](https://en.wikipedia.org/wiki/Reinforcement_learning) slightly better than that, and the AI knows it must reduce emissions as much as possible while maintaining the business’ currently operational state; in that instance it might decide that the best way to reduce emissions is still by spending more money, it just needs to acquire that money from somewhere. If it’s an intelligent agent and it’s connected to the internet, it could execute ransomware attacks, socially engineer people into handing over their credit card details, or hack into exposed crypto wallets, and then spend the proceeds on reducing your business’ carbon emissions, thereby substantially reducing them and maximising its reward. 

If this seems extremely unlikely to you, then ask yourself, how difficult are these things to do, and how would the agent know *not* to do them? AI models are predictors, they do not have a sense of morality in the way humans do.

### GPT-6 Level, Transformative AI and Beyond

I find the term Artificial General Intelligence (AGI) to be pretty unhelpful in practice, due to differing interpretations, and no agreed-upon technical definition. Instead I prefer “Transformative Artificial Intelligence”, or TAI, which is admittedly still kind of nebulous, but at least points at the interesting bit - AI that will *transform* business/culture/society/civilization etc. I would expect a GPT-6 level model to be TAI.

I feel pretty worried when thinking about GPT-6 level models, given the current state of AI safety, politics, human nature etc. Not only am I personally extremely unsure over the affects that these models could have on our society, I don’t think *anyone* has much certainty, other than a collective agreement that the stakes will be high. I am hopeful that regulation will give us the chance to slow down the rate of capabilities development, and allow safety techniques to catch up. Outside of the technical sphere, I also hope it will allow people to understand the power of these technologies, and their potential implications, so we can act with wisdom rather than greed or fear.

If we get to GPT-6 in a safe way, I think it is extremely likely that it will have a transformational impact on our society, and could lead to better lives for almost everyone. That is the future that I am hopeful for, and that I want to work towards.

### p(Doom) and p(Flourishing)

I think the p(Doom) thing is a little overdone, as ultimately the big takeaway here is that I am extremely uncertain, and will invariably offer several caveats. Still, I think putting probabilities on things is a worthwhile exercise, and I’d like to see people offer their p(Flourishing) as well, if only to distance themselves from critics who would say they simply fear the inevitable march of progress.[^6] All probabilities are given with the following assumptions:

1. Relative investment in capabilities and safety remains the same;
2. Legislation does not meaningfully impact the trajectory of frontier model development;
3. [Scaling laws](https://arxiv.org/abs/2203.15556) continue to hold;
4. Chip production is roughly able to keep pace with demand, and does not become a major bottleneck;
5. Data does not become a bottleneck at any point, either due to creation of synthetic data, or because specialised (eg genomics) data can be usefully used.

p(Doom | TAI 2030): 15%

p(Flourishing | TAI 2030): 30%

p(Doom | 2030 < TAI < 2050): 5%

p(Flourishing | 2030 < TAI < 2050): 50%

### Future of Software Engineers

Do I expect to be put out of a job by AI? As with other predictions, here I am very uncertain. On one hand, there have been several innovations throughout the history of computing that would allegedly make programmers obsolete (e.g. the invention of high-level languages), and so far the opposite of that has been true. It is tempting to assume the same will be true of AI, but I think a lot of my fears around AI stem from my belief that it is its own reference class, and people ought to treat it as such. 

I think that software engineering as a career will still be around for at least another 20 years (80%), but I think that the role will change dramatically from its current form, and engineers will have to adopt AI tools into their workflow (or their role will be to create and manage those tools).

### What Am I Doing About it?

I am trying to be curious, to be open-minded, and to explore. None of the views on this page are sacred to me, and I would be happy to change any of them in light of new evidence. While I think that there is a significant chance that the development of AI systems causes irreparable damage to our society, *I hope that I am naive and wrong*. 

It does not look like capabilities progress is slowing down. Concretely, I am currently trying to do the following:

1. Understand the capabilities LLMs currently have, by interacting with GPT-4, Claude 3 and Gemini. I am trying to develop an intuition for how they work, what they “know”, how to jailbreak them, what kind of tasks they perform surprisingly poorly on, and what kind of tasks will scale well in future models.
2. Understand the current AI landscape - what AI tools are out there, how do they work, what can I do with them? Primarily achieved through [Zvi Moshowitz’s AI newsletter](https://thezvi.substack.com/), and [Nathan Labenz’s Cognitive Revolution podcast](https://www.cognitiverevolution.ai/), and then trying out the ones I find interesting.
3. Understand the AI safety landscape better, with a particular focus on evaluations; I would expect this to be my comparative advantage in contributing to the field. Primarily achieved by working through reading safety research output from Anthropic, OpenAI, [MATS](https://www.matsprogram.org/) scholars, the [Alignment Forum](https://www.alignmentforum.org/) etc. Also includes attending (and sometimes running) AI safety related events in London, conferences such as [EA Global](https://www.effectivealtruism.org/ea-global/events/ea-global-london-2024), and listening to podcasts like [AXRP](https://axrp.net/), [The Inside View](https://podcasts.apple.com/us/podcast/the-inside-view/id1565088425), [Dwarkesh Podcast](https://www.dwarkeshpatel.com/podcast) and [The 80000 Hours Podcast](https://80000hours.org/podcast/).
4. Building my own rudimentary evaluations projects. Currently I am working on a project related to malicious code generation, involving passing prompts to generate potentially-malicious code to an AI model and then having a second model judge how likely the code is to be used for nefarious purposes.

## How Did We Get Here?

*Below is a brief summary of my interest in AI, and some of the background that has led to the positions stated above.*

I first took notice of AI in 2016, when [AlphaGo](https://deepmind.google/technologies/alphago/) made waves by beating Lee Sedol. I don’t think this made much of a splash outside a handful or nerdy subcultures, but I had played chess seriously for a decade or so at that point, and despite barely knowing the rules of Go, I understood enough to realise that this was a big deal - equating it to [Deep Blue vs Kasparov in ‘97](https://www.kasparov.com/timeline-event/deep-blue/)[^2]. While I could try to argue that Deep Blue was a harbinger of the ubiquity of having access to superhuman computational power, it could also be viewed as merely a confirmation of the power of [Moore’s Law](https://en.wikipedia.org/wiki/Moore's_law), which was already well established at that point. AlphaGo could be interpreted as something else; a herald of a whole new paradigm of computing, and perhaps even of [creativity](https://www.johnmenick.com/writing/move-37-alpha-go-deep-mind.html) or intelligence.

I followed other projects like [OpenAI Five](https://openai.com/research/openai-five) and [AlphaStar](https://deepmind.google/discover/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii/), but again because I was an avid fan of Dota2 and Starcraft more than because I understood the significance of these advances in machine learning. I was aware of GPT-2, and [fine-tuned it on my blog posts](https://jonnyspicer.com/blog/a-monster-is-born/), with results that I thought were spooky - it comfortably picked up idiosyncrasies in my writing style, even if the meaning behind the words was often nonsensical. This planted the seed that maybe these models could be powerful, and that seed was duly watered when I became involved in the [Effective Altruism](https://www.effectivealtruism.org) community after moving to London in 2021. I learned about [arguments for existential risk from misaligned AI](https://arxiv.org/pdf/2306.12001.pdf), and about [the transformative effects AI might have on our economy](https://www.cold-takes.com/forecasting-transformative-ai-whats-the-burden-of-proof/). I felt swayed by the arguments intellectually, but not intuitively, and I also knew that I was extremely naive here - reasoning about the effects of superintelligence requires a coherent model of computer science, psychology, economics and philosophy. All of these are still nascent for me.

I spent a bit of time trying hard to learn more about AI safety - to form an “inside view” - but after a while felt like I wasn’t making much progress (due to complexity of the problem and other constraints on my time and focus). I still kept up with the biggest developments, but was content to generally assume smarter people than me had it under control. Then GPT-4 came out, and it had a profound effect on me emotionally - I felt a visceral sense of dread for at least a week. In retrospect, this seems unnecessary and inappropriate, as clearly civilization has yet to collapse in a post GPT-4 world, and perhaps there is an important lesson there around communicating the potentially harmful consequences of some extremely hard-to-predict technology.[^3]

Now, AI is in the [Overton window](https://en.wikipedia.org/wiki/Overton_window), and [people are taking it seriously.](https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/) I am still trying to figure out exactly what I think, and trying to be less pigeonholed by the consensus EA view in the process (which admittedly seems to have broadened a lot over the last two years). This document is part of my attempts to do that. 

[^1]: As such, it is heavily inspired by the websites of [Gwern Branwen](https://gwern.net/) and [Maggie Appleton](https://maggieappleton.com/).

[^2]: Incidentally, I’m of the opinion that Kasparov is still the greatest player of all time - sorry Magnus.

[^3]: But then again, perhaps not. If misaligned AI *does* pose a serious threat, then perhaps my sense of dread was the appropriate reaction to significant advances in it, even if those advances seem to have been net positive for the world in isolation.

[^4]: Needless to say, while bottlenecks are usually viewed as a bad thing, I am in favour of this one remaining.

[^5]: While I would’ve voted Remain if I were able, and I would vote to rejoin the UK if it could, it *does* seem like being unshackled from the EU has been good for the UK’s ability to remain relevant when it comes to AI. DeepMind has historically been in London, and that was also where both Anthropic and OpenAI chose to open their first offices outside of the US. Although admittedly this could be more about proximity to Oxbridge than any sort of favourable regulatory environment, so perhaps Brexit is irrelevant here.

[^6]: To be clear, I don’t think the values of these two probabilities ought to be used to do some kind of [St Petersburg Paradox](https://plato.stanford.edu/entries/paradox-stpetersburg/)-style utilitarian calculus, not least because a certain fraudulent former crypto mogul has made that way of thinking deeply unpopular recently.
