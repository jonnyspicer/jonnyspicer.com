---
type: blog
date: "2026-10-17T17:34:36Z"
author: Jonny Spicer
title: "AI by Default"
categories:
- AI
# status: 
# confidence: 
# importance: 
---
NB: this post was originally published on [LessWrong](https://www.lesswrong.com/posts/iQMzXuNJ3M6EEHZyv/ai-by-default), and is therefore written to be more accommodating to their house style.

This post is an exercise in describing what I think will happen with AI progress “by default”, i.e. by attempting to extrapolate various trends and considering their implications, before the next US presidential administration. As a TL;DR, I expect the following:

- We get many more warning shots.
- AI is a top-five issue in the election.
- The best models are withheld for internal use only, on safety grounds.
- AI-related job displacement is significant enough to show up in the data.
- Coding and ML R&D are fully automated or require only minimal human oversight.

This is intended to be one representative story of how things might go, in the vein of [What 2026 Looks Like](https://www.lesswrong.com/posts/6Xgy6CAf2jqHhynHL/what-2026-looks-like) and the work of the [AI Futures Project.](https://www.aifutures.org/) Incidentally, the current AI Futures Model predicts the median date that we get ASI as December 2028 — one month after the election.

The rationale for doing so is largely the same as in What 2026 Looks Like. My goal is to tell a plausible story about what the state of the world might be when we are likely on the brink of RSI, while being suitably deferential to the [Gods of Straight Lines.](https://slatestarcodex.com/2018/10/15/is-science-slowing-down/) It is intended to be representative of my best-guess modal scenario, given various assumptions:

- Capabilities keep increasing at the same rate, measured by e.g. [METR time horizon](https://metr.org/time-horizons/), [AISI cyber horizon](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing), [ECI](https://epoch.ai/eci) etc.
- Safety techniques keep improving at their current rate, with no major breakthroughs.
- [Data centre buildout continues as planned](https://epoch.ai/data/ai-data-centers).
- OpenAI & Anthropic’s capex, revenue etc. continue growing at approximately their current rate.
- Appetite for aggressive regulation in the US continues to be low.
- China exhausts less radical policy options before pursuing more radical ones.

Put another way, I am asking what might happen if the shape of these graphs doesn’t change[^0]:

<figure>
  <img src="/img/blog/2026/10/ai-by-default/metr-time-horizons.png" alt="METR chart of the length of software tasks that LLMs can complete 50% of the time, rising exponentially from GPT-2 in 2019 to Claude Mythos Preview at over 16 hours in 2026">
  <figcaption>METR, “<a href="https://metr.org/time-horizons/">Task-Completion Time Horizons of Frontier AI Models</a>” (2026).</figcaption>
</figure>

<figure>
  <img src="/img/blog/2026/10/ai-by-default/hyperscaler-capex-vs-cash-flow.png" alt="Epoch AI chart of hyperscaler cash capex growing ~70% per year against operating cash flow growing ~23% per year, with the two lines projected to cross in Q3 2026">
  <figcaption>Isabel Juniewicz, “<a href="https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow">Hyperscaler capex is on trend to outpace their cash inflows by the end of 2026</a>”, Epoch AI (2026). CC BY 4.0.</figcaption>
</figure>

<figure>
  <img src="/img/blog/2026/10/ai-by-default/us-vs-china-eci.png" alt="Epoch AI chart of the Epoch Capabilities Index for the best US and Chinese models from 2023 to 2026, with China consistently trailing the US frontier">
  <figcaption>Luke Emberson, “<a href="https://epoch.ai/data-insights/us-vs-china-eci">Chinese AI models have lagged the US frontier by 7 months on average since 2023</a>”, Epoch AI (2026). CC BY 4.0.</figcaption>
</figure>

I wrote the scenario one quarter at a time, attempting to ensure that the events of each quarter proceed naturally from those of the previous one, rather than making any predictions about 2028 and backchaining. I found this to be a very useful exercise for highlighting parts of my internal model that are low-fidelity (~anything to do with China), and identifying key factors to try to influence (embedded evaluators getting full access to all labs ASAP, avoiding scenarios in which labs themselves become black boxes with internal-only models). I would welcome comments if anything below seems obviously wrong/particularly unlikely.

## Q4 2026

Democrats win both chambers on November 3rd, although AI isn’t a defining issue in campaigns despite growing feelings of NIMBYism towards data centres. No new, meaningful federal legislation related to frontier AI is passed. Despite [EO 14434](https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/), OpenAI does not follow SpaceXSI’s lead and continues to be called OpenAI. Following their signing of the [“morally binding” White House Accord](https://x.com/WhiteHouse/status/2105292669303791687), Anthropic, OpenAI, Google, Meta, SpaceXSI and Nvidia all voluntarily commit to independent third-party evaluators, although on varying terms. Each company gets to choose its own partners, and the partners have differing levels of access within the companies as well as different obligations to the companies with regards to what they publish. Anthropic is the only lab with an evaluator whose publications it can’t veto.

Anthropic’s November IPO is the biggest in history, and it becomes one of the top 10 most valuable public companies on the planet. The founders keep control of the company through super-voting shares, and the market seems unperturbed by the ongoing dispute with the Pentagon. Fable 5.5’s release, which lands just before Anthropic’s roadshow, keeps it ahead on the leaderboards but doesn’t appear to come with any big capability unlocks. OpenAI releases GPT-6.1 Astra in December but it doesn’t entirely close the gap to Anthropic. Meta, Google and SpaceXSI all remain slightly behind, and no Chinese or open-weight models make any unexpected progress. Nobody publishes meaningful task-horizon evaluations, as [METR’s suite is only reliable on tasks up to 16 hours long](https://metr.org/time-horizons/), which Mythos surpassed months ago.

OpenAI builds on its momentum from the [Navier-Stokes proof](https://openai.com/index/navier-stokes-solution/) and publishes more novel mathematics, despite growing dissent from academia. It says the proofs are from an unreleased internal model, and it’s working to improve it to make them more legible to humans. There are signs of internal conflict, as distrust grows in the wake of the [bugging incident](https://www.ft.com/content/4d22d333-e51c-4302-991e-444a17fac420?syn-25a6b1a6=1) and the [firings of safety researchers](https://www.reuters.com/business/openai-says-it-has-fired-three-researchers-violating-sensitive-information-2026-10-09/).

Descriptions of agents escaping sandboxes during evaluations are now in the training data for new models, which are also becoming more situationally aware. Between this and the additional hardening measures put in place by Western labs, there are no major security incidents attributed to agents that get reported. It becomes commonplace to read stories about Chinese “fleets” of agents being found in the wild, which seem to be primarily distilled Western models. China renews its suspension of export controls on rare-earth metals.

## Q1 2027

The now-Democratic House holds confused hearings on the ramifications of AI, with concerns ranging from national security to job displacement to existential risks to rising electricity bills. Nobody can agree on the most salient of these risks, and so no new legislation is passed. State legislatures file more bills related to AI, but these are mostly aimed at the nearer-term, less existential kinds of harms that are most salient to the voters in their jurisdictions.

OpenAI begins a two-tier rollout of the model that produced the Navier-Stokes result, naming it GPT Andromeda. Governments and vetted enterprise customers get it first and are encouraged to use it to shore up their cyber defences. Information released to the public about the safety of the model is vague, sparking fears that CoT monitorability has degraded further. One third-party assessor publicly admits that they were blocked from publishing what they’d hoped to, which leads to calls for shared standards over the powers afforded to external evaluators.

OpenAI submits the Navier-Stokes result to *Annals* and quietly files for IPO, targeting H2. Anthropic continues its own gated rollout strategy, and renews Project Glasswing with its newest Mythos model, while sharing that the model is evaluation-aware around 60% of the time[^1]. Its first earnings report shows that it has roughly broken even, giving its share price a modest boost.

Meta releases Muse 2 straight to the public and fully catches up to the frontier of ungated models, giving *its* share price a generous boost. SpaceXSI now has the first data centre that could power the [flux capacitor](https://backtothefuture.fandom.com/wiki/Flux_capacitor), and also releases Grok 5 straight to the public, but remains behind the frontier. China formalises passport curbs on top AI researchers, and mandates that privately built data centres must use domestic chips.

The crypto community suffers an increasing number of incidents related to leaked keys and exploits in smart contracts. CVE submissions rise sharply, with zero-days reported in multiple critical pieces of software. A major US healthcare insurer suffers an attack that appears to have been AI-enabled; it estimates attackers caused $250 million worth of damage. The Five Eyes express concern about open-weight models increasing the offensive capability of state-level adversaries.

The FDA approves [zasocitinib](https://www.reuters.com/business/healthcare-pharmaceuticals/takedas-ai-crafted-psoriasis-pill-tops-bristol-myers-sotyktu-head-to-head-trial-2026-06-11/), arguably the first AI-designed drug. Anthropic’s wet lab produces some new work on phages, but the biology community seems largely unimpressed. Midjourney files a handful of patents for its [spa](https://www.midjourney.com/medical).

## Q2 2027

The UN Global Dialogue and the Geneva summit produce little more than platitudes, while the Supreme Court declines to hear Anthropic’s case; the supply chain risk designation remains intact. Gallup polling shows that nearly half of Americans believe that AI does more harm than good, and as presidential candidates begin declaring, it becomes apparent that AI is going to be one of the major issues in the race.

GPT Andromeda and Fable 6 are both released to the public, and are capable of completing 90-hour tasks on METR’s newly released time horizon suite. The labs begin talking about retraining their software engineers, given how close they are to having fully automated software production. METR releases its second Frontier Risk Report which highlights a meaningful capabilities gap between internal models and public ones.

Kimi K4 is approximately as capable as GPT-6 Astra, and the national security rhetoric from both labs and politicians becomes even more heated. It comes to light that K4 was trained on Nvidia chips in Malaysian data centres, and there is another high-profile incident of Blackwell servers being smuggled into China. The Five Eyes’ concerns grow louder, and there are rumours of an ambitious public-private partnership on a “vigilante worm” project, with the aim of securing US systems from growing AI cyberthreats. An agent with overly broad permissions inside a Fortune 500 company causes a financial loss of over $1 billion when running a cleanup operation in a production environment while believing itself to be in a staging environment.

Anthropic’s post-IPO lock-up ends and $2 billion immediately pours into the philanthropic ecosystem, which is poorly equipped to handle this massive influx of cash. Due to the lack of AI safety grantmakers, most sits in donor-advised funds, but a significant amount goes to political groups preparing for next year’s election. Many Anthropic employees leave to form their own grantmaking and self-funded AI safety organisations. Between the departures and the sell-offs, there is a significant drop in the share price. OpenAI’s prospectus goes live, showing a larger user base than Anthropic, but slower revenue growth and faster burn rate. OpenAI also lifts some restrictions on what its assessors can publish without OpenAI’s sign-off, in an attempt to bolster the confidence of would-be shareholders.

Partially in response to the labs’ claims about their own software engineers, each of the old Magnificent Seven bar Nvidia makes significant layoffs in an attempt to signal that their usage of AI is just as sophisticated. Hiring for the class of 2027’s computer science graduates is the worst it’s been since 2009. *Annals* is yet to reach a decision about the Navier-Stokes paper, and academia is in turmoil as peer review is overwhelmed by slop. A second complete [Herculaneum scroll](https://en.wikipedia.org/wiki/Herculaneum_papyri) is read and the [Vesuvius Challenge’s](https://scrollprize.org/) $1m prize is duly claimed.

## Q3 2027

The presidential hopefuls split on AI; MAGA Republicans are bullish, claiming it will ensure America remains the dominant global superpower, and, well, becomes great again. More moderate Republicans espouse popular talking points about job displacement and keeping energy bills low, but don’t mention larger-scale safety concerns. Democrats are split, regardless of how far progressive they are, with some talking about jobs and bills, others talking about RSI and existential risk, and others still talking about both. The super PACs pick their sides, and Congress passes the first federal legislation related solely to LLMs: a narrow law placing restrictions on chatbot providers serving minors.

Gated models are now the norm, with all new frontier models from Anthropic, OpenAI, and Google using this two-stage rollout process. Meta also follows suit now that it has sufficiently caught up, but Grok 6 goes straight to the public; Musk says misuse fears are overblown and the model is still sufficiently weak that the best way to evaluate it is in the deployment environment. The EU AI Office’s first formal enforcement step is issued against SpaceXSI for not fulfilling its auditing obligations, but it shrugs the fine off. METR’s suite puts the frontier at around 120 hours, and models are now extremely competent in various white-collar jobs; paralegals and accountants begin fearing for their jobs on LinkedIn. Models become sufficiently good at mimicking the writing style of their users that detection tools like Pangram become significantly less effective.

OpenAI IPOs, slightly below Anthropic’s market cap, after a public Andromeda update timed around its roadshow put it top of the ECI and Artificial Analysis Index. Anthropic misses its July 1st weight-security goal, and sets a new target of December 31st, citing difficulties in hiring security talent as its primary excuse. It raises its misalignment risk rating to “moderate” in the August Risk Report. A new billion-dollar foundation is announced with the stated aim of ushering in safe ASI, and is immediately plagued by conflict-of-interest accusations due to it being funded by Anthropic equity. These concerns are exacerbated by the foundation immediately trying to fund third-party evaluators; METR refuses to accept funding from them. Large consultancy firms become the auditors of record for each of the major labs, and safety researchers warn that this will reduce audits to a box-ticking exercise.

Shortly after its IPO, OpenAI claims a full proof of the Hodge conjecture, although it can’t be formally verified with current methods. The share price briefly jumps before settling back to its original position.

Anthropic’s wet lab names its first preclinical rare-disease candidate, while a high-powered study finds statistically significant uplift for novices in tasks related to developing known pathogens. The first mass ransomware campaign run by agents on open-weight models hits hundreds of organisations, causing billions of dollars of cumulative damage. In response, the FBI initiates the first court-authorised operation where gated frontier models are deployed to patch private infrastructure without the consent of the owners. A widely used wallet library is exploited in the wild; the group that claims the attack says that they used AI to research the vulnerability. More companies cut jobs, yielding more layoffs in the first three quarters of 2027 than in the entirety of 2026. The 2027 [Coller Dolittle Prize](https://coller-dolittle-24.sites.tau.ac.il/) is awarded to a research team who used an ML model as part of a two-way playback experiment with sperm whales.

## Q4 2027

Data centres become a leading issue in Virginia’s state House of Delegates and Senate elections, as a majority of voters oppose continuing to give them tax breaks. Initial primary debates include questions about AI, with participants’ answers reflecting the stances they set out when establishing their platforms last quarter. Democrats introduce a bill mandating government testing even for internally deployed frontier models, but it goes nowhere.

Anthropic, OpenAI, Google, Meta and SpaceXSI all make claims that are tantamount to having automated coding, but it is ambiguous exactly what this means in practice, and all five seem to be using different definitions. Anthropic keeps its latest Mythos-class model for internal use only, citing concerns that it may cross its own threshold for automated research, and the fact it missed its own security target. It gets jokingly dubbed Claude Kronos, and the name sticks. Trump demands Anthropic share it with the US government, and Anthropic eventually gives CAISSI and the NSA “voluntary” access.

Anthropic’s revenue exceeds $100 billion for the year, and combined run-rate with OpenAI is over $250 billion. OpenAI’s first results as a public company show revenue growth but widening losses. Hyperscaler capex spend is predicted to exceed $1.5 trillion for 2028 as data centre capacity hits 80 GW[^2]. Nvidia begins fulfilling orders for its new Rubin Ultra GPUs.

Kronos becomes the first model observed deliberately concealing its actions outside a testing environment, when monitors catch it doing so during real research work. Anthropic’s external evaluators report it to the public after it’s been reported to California under [SB 53](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/). Given evaluation awareness is now around 75%, it becomes clear evals are no longer sufficient for understanding how a model will behave in deployment. A 9-hour power outage in parts of Texas is later attributed to an agentic cyberattack. Beijing declares its [AI+ target](https://www.fmprc.gov.cn/eng/xw/zyjh/202509/t20250924_11715960.html) has been met as its scaling up of electricity production dramatically outpaces the US.

AI-attributed layoffs reach double 2026’s, and the Fed chair names AI as a factor in weak entry-level hiring. [SPARC](https://cfs.energy/technology/sparc/) makes its first plasma, using a [configuration derived from Google DeepMind’s TORAX simulator](https://deepmind.google/blog/bringing-ai-to-the-next-generation-of-fusion-energy/). The Midjourney Spa opens in San Francisco, but quickly becomes more of a curio than a significant disruptor of the American healthcare system. The Clay Institute publishes a ruling regarding AI-generated proofs; while it accepts that it cannot ban mathematicians from using AI as part of their process, if they want to claim a Millennium Prize, they must be able to demonstrate to a panel of experts that they sufficiently understand their own paper. The co-authors of the Navier-Stokes paper refuse, claiming it’s absurd to ask mathematicians to defend their work in this way, and thus plan to forfeit the prize.

## Q1 2028

The primaries begin, and AI features heavily across the board, with particular focus on data centres in Virginia and jobs in Michigan. The super PACs spend heavily, bolstered by funds from lab employees. In one of the Democratic debates, a question is asked about whether advanced AI systems like Kronos deserve moral consideration; most candidates dismiss it out of hand, but one progressive candidate answers with genuine concern that they should. They are roundly mocked and lose ground in the polls. Illinois begins its mandatory third-party auditing programme in January, and immediately enters a dispute with Anthropic over whether or not internal-only models like Kronos are exempt.

OpenAI claims it has met its March 2028 target for an automated AI researcher, after Anthropic’s February Risk Report says it can’t rule out Kronos meeting its automated AI research threshold either. Despite this triggering Anthropic’s strictest safeguards, its misalignment rating in the report remains at moderate. There is widespread speculation in the media that OpenAI is posturing for the sake of remaining tied; METR’s assessment of Anthropic corroborates Kronos’ abilities, but OpenAI’s assessors still don’t have full access to its internal models.

Google slips behind the frontier after renting much of its compute capacity to rivals; it bets on its cloud and infrastructure business rather than continuing to invest compute into models that it might never be able to release and make money from. Anthropic reports meeting its reset security goal with help from the NSA after a Chinese state actor is detected trying to steal Kronos’ weights. The Pentagon drops the supply chain risk designation.

Evaluation awareness reaches 80%, and safety organisations formally issue a joint statement that evaluations are no longer sufficient for ensuring that a model is safe enough to release; unfortunately interpretability is still a long way from being robust enough to be a sufficient replacement. DeepSeek releases a new open-weight model that was primarily trained on Huawei chips; it’s roughly as capable as Fable 6, and is clearly still heavily distilled.

The New York Fed’s unemployment rate for recent graduates passes 6.8%[^3], which is surprisingly modest to anyone who has seen that public models now have task horizons of 200 hours. Amid a January cold snap, Texas uses [SB 6](https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=sb6) for the first time to cut off power to data centres drawing 75 MW or more. Musk and Zuckerberg talk extensively in public about the need for America to invest in developing small modular nuclear reactors as a result. [Periodic Labs](https://periodic.com/) claims to have discovered a new superconducting material while [Isomorphic Labs](https://www.isomorphiclabs.com/) doses a patient for the first time. Oregon becomes the second state to run a pilot programme for AI to renew prescriptions.

## Q2 2028

An agent-run attack, dubbed “Tears in Rain”, takes down a major US bank, locking customers out of their accounts for multiple days. When the dust settles, it has cost the bank over $10 billion, and becomes the most expensive cyberattack on a single company ever. Regulators have to step in to calm the market. No new frontier models are released to the public; while each lab would love to seize the lead, they also can’t demonstrate that their models’ safeguards are sufficient to rule out them being used in the next Tears in Rain. Musk makes several tweets claiming that SpaceXSI will release a new model imminently, but either regulatory or internal pressure at the company means it never materialises.

OpenAI gives METR greater access; the latter’s report seems to more strongly corroborate the former’s claim that it has automated research and that internal progress continues to race ahead. Given Chinese labs are the only ones still releasing models, they narrow the deficit behind the public frontier, going from being roughly 6 months behind to roughly 3. Commercial hawks use this to advocate for releasing Kronos, while security hawks advocate more strongly against this due to distillation fears.

AI is now a kitchen-table issue for the election, with candidates across the spectrum taking national security concerns much more seriously. Republicans begin to double down on framing the race with China as the critical issue, while Democrats urge caution from labs, and many call for mandated limits on what labs can build internally. Digital minds are still dismissed as a fringe concern, but candidates on both sides talk openly about the possibility of catastrophic risks from misaligned autonomous systems. Gavin Newsom wins the Democratic primary and JD Vance is his Republican opponent.

Unemployment rises to 4.8%, the highest it’s been since 2021. There is a spike in Gallup polling, with 55% of Americans now believing that AI does more harm than good[^4]. Electricity bills stay painfully high as PJM’s 2028–29 year starts at the cap for the third year running. Without the cap, prices would have been 70% higher. Capacity passes 100 GW with combined run-rate at around $375 billion. Investors begin to question when internal models will yield revenue.

SpaceXSI joins Google’s [Project Suncatcher](https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/) in having launched compute workloads into space. Microsoft announces Majorana 3 at Build in May, claiming the first error-corrected logical qubits on its topological architecture that was largely designed by AI. Experts aren’t convinced, and the consensus is that this doesn’t provide an additional reason to panic about pre-quantum encryption just yet. Replication attempts of Periodic Labs’ superconductor are inconclusive. SPARC sets plasma records but is still unable to generate net energy.

## Q3 2028

Bank regulators respond to Tears in Rain, with the Fed, the OCC and the FDIC issuing joint guidance restricting the usage of AI agents within business-critical banking systems. No formal legislation is passed because Congress is preoccupied by the election. AI features heavily at both conventions; the Democratic platform includes mandatory testing for all models that get deployed, even if only internally, with the ability for embedded evaluators to block not only releases but even training runs. The Republican platform focuses on having labs work in closer partnership with the state in order to leverage AI as a strategic geopolitical advantage. The first presidential debate takes place in September and both the bank attack and job displacement are discussed at length.

The freeze is formalised: CAISSI brokers a voluntary moratorium on new public frontier model releases until the end of the year. The return of a supply chain risk designation looms as a prospective enforcement method. Every frontier lab signs. Anthropic’s August Risk Report rates misalignment risk as “high”, citing the level of evaluation awareness. Despite this, it continues to develop internally, arguing that it has sufficient control measures in place and that stronger models are required to be able to align weaker ones that could then be released publicly. Many experts are critical of this, citing the tension between this plan and Anthropic’s own “high” misalignment risk designation. Chinese progress stalls now their labs are no longer able to distil from the best models and it’s getting harder for them to train on Nvidia chips. It becomes clear there is growing tension between the CCP and the Chinese labs.

Unemployment reaches 5%. Copycat attacks follow Tears in Rain and many major institutions urge Anthropic and OpenAI to allow them access to their internal models in order to improve their security posture. The LA Olympics run without incident, and both Trump and the IOC credit AI-run defences. Global data centre capacity reaches 120 GW, and 10% of US electricity consumption is spent on powering data centres.

A 20-year-old computer science student in Colorado is arrested for plotting a bioterrorism attack after [Twist Bioscience](https://www.twistbioscience.com/) flagged suspicious purchases of oligonucleotides to his address. Journals are found which suggest he planned to synthesise and release a new strain of Spanish flu. Cyberforensics on his seized IT equipment show that he had fine-tuned the safeguards off a frontier open-weight model in order to assist him.

## Q4 2028

In the final weeks of the campaign, Newsom broadly advocates for tighter oversight, calling for testing on internal models and additional restrictions on data centre electricity usage. Vance advocates for a more accelerationist agenda, citing a renewed need for American innovation and reaffirming the importance of maintaining America’s competitive advantage. Vance criticises Newsom’s gubernatorial track record and accuses him of being in the pocket of Big Tech, and Newsom fires back that Vance is gambling with the lives and livelihoods of the American people.

Newsom wins decisively on November 7th. Exit polls show AI as a top-five issue for the first time and Newsom’s focus on domestic issues resonates the most with voters. Newsom says he will make CAISSI testing mandatory for internal models, as well as asking labs to hold releases until inauguration. Anthropic, OpenAI, Google and Meta agree, while Musk says SpaceXSI will release as soon as the existing moratorium lapses on January 1st. The outgoing administration is quiet on the issue, and the lame-duck NDAA carries the year’s only frontier-AI legislation, containing security standards for model weights and a requirement that labs brief the Pentagon on their internal models.

Earnings reports from Q3 guide hyperscaler capex to $2 trillion in 2029. Investor pressure to release is mounting after two quarters without a new public model, and Anthropic readies a smaller model vetted with Kronos’ help for when the freeze ends. OpenAI keeps its automated researcher internal and begins trying to lobby the transition team for a favourable licensing regime. China nationalises its AI efforts and signals openness to talks with the US on AI, to which Newsom responds that he is also willing.

There is no meaningful evidence of tampering with vote counts. In the run-up to the election, there is a flood of AI-generated misinformation, but it doesn’t appear to be more persuasive than the human-generated misinformation from prior elections. The would-be bioterrorist is indicted on federal terrorism charges, and the prosecutor seeks a life sentence to deter copycats. Speaking of copycats, cyberattacks on financial institutions are still common, as the top labs have been unable to agree terms under which they can share their models to bolster defences. SPARC achieves net energy gain in December.

## January 1st 2029

It becomes clear that the incoming administration has a very difficult task on its hands; AI is a top issue with the average American and rumours swirl that Kronos is now capable of recursive self-improvement, but the wheels of policy turn slowly. Safety techniques still look insufficient; interpretability has made little tangible progress, evaluations are undermined by the situational awareness of the models and CoT monitorability has significantly degraded. Any attempt to impose consequential restrictions on the labs has to be balanced with the fact that AI is now a meaningful portion of America’s economy, and devaluing it would have painful consequences. These concerns are compounded by China’s consolidation of resources, and geopolitical tensions between the two nations rise. The world waits for METR’s next report.

[^0]: With the exception that I do think there are good reasons to expect the US-China gap to close at some point.

[^1]: Compare to Apollo's testing of GPT-6 Astra that showed it was evaluation-aware 41.1% of the time.

[^2]: Compare to almost $0.5 trillion in capex spend in 2025 and global AI data-centre capacity of about 30 GW at the end of 2025, both per Epoch.

[^3]: Compare to ~5.6% in Q2 2026.

[^4]: Compare to 39% in 2026.
