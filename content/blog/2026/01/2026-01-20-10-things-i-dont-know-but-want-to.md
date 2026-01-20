---
type: blog
date: "2026-01-20T00:31:04Z"
author: Jonny Spicer
title: "10 Things I Don't Know But Want To"
categories:
- AI
- Aliens
- Blogging
- Mental Health
- Programming
---
*Artificial intelligence, extraterrestrial intelligence and emotional intelligence*

Please help me! I have recently spent a lot of time thinking about the ten questions below, and have yet to arrive at satisfactory answers for any of them. For some, I expect this to be because I haven't looked in the right places, while for others I suspect they are generally open questions. If you have something that you think would advance my understanding of any then please [leave a comment on Substack](https://heresjonny.substack.com/publish/post/185157362) or [contact me](/contact) - I will be profoundly grateful.

1. [Will AI enable precision medicine?](#will-ai-enable-precision-medicine)
2. [What would being the Werner Forssman of mental health look like?](#what-would-being-the-werner-forssman-of-mental-health-look-like)
3. [Why isn't brief psychotherapy more popular?](#why-isnt-brief-psychotherapy-more-popular)
4. [Relatedly, how can incentives be better aligned between patients and therapists?](#relatedly-how-can-incentives-be-better-aligned-between-patients-and-therapists)
5. [How can we safeguard against people having negative experience with LLM-based therapy?](#how-can-we-safeguard-against-people-having-negative-experience-with-llm-based-therapy)
6. [Will Jevons Paradox apply to AI-generated software (or do I need to totally rethink my career)?](#will-jevons-paradox-apply-to-ai-generated-software-or-do-i-need-to-totally-rethink-my-career)
7. [How can I get Claude Code multiplexing & orchestration working well?](#how-can-i-get-claude-code-multiplexing--orchestration-working-well)
8. [What new things can I try to resolve my emotional eating and body image issues?](#what-new-things-can-i-try-to-resolve-my-emotional-eating-and-body-image-issues)
9. [How can I improve my writing workflow?](#how-can-i-improve-my-writing-workflow)
10. [How likely is it that aliens have visited Earth?](#how-likely-is-it-that-aliens-have-visited-earth)

## Will AI enable precision medicine?

The concept of precision medicine has been full of promise ever since the [Human Genome Project](https://www.genome.gov/human-genome-project) succeeded in 2003. But, as is [often pointed out](https://substack.com/home/post/p-184581220?selection=3f13d70a-1de9-41be-b74e-44feaad2cfa5#:~:text=Precision%20medicine%2C%20where%20perfect%20treatments%20can%20be%20predicted%20in%20advance%2C%20would%20be%20wonderful%20but%20so%20far%20there%20are%20far%20many%20more%20articles%20written%20on%20the%20subject%20than%20patients%20who%20have%20been%20helped%20by%20it), said promise has thus far failed to yield meaningful results. Precision medicine seems like both obvious and lucrative as a use case for AI, and DeepMind seem interested in pursuing it - see for example [TxGemma](https://deepmind.google/models/gemma/txgemma/). There are a [slew of optimistic papers too](https://journals.sagepub.com/home/aii?mal-proceed=true), but as far as I can tell medicine is yet to be revolutionised.

Hypotheses: diffusion is slow but results will come, there are regulatory hurdles[^1] but results will come, machine learning techniques still aren't sufficiently powerful that they can have a material impact here.

## What would being the Werner Forssman of mental health look like?

[Werner Forssman](https://en.wikipedia.org/wiki/Werner_Forssmann) is a hero of mine, and I often wonder how I could emulate his radical autosurgery, but with the goal of dramatically improving my psychological, rather than cardiac, health. Perhaps there already have been many psychiatric analogs of Forssman's - those that experimented with psychedelics (like [Albert Hoffman](https://en.wikipedia.org/wiki/Albert_Hofmann#Discovery_of_LSD) or [Alexander Shulgin](https://en.wikipedia.org/wiki/Alexander_Shulgin)), extended periods of silent, solitary meditation or simply those that relentlessly examined their own psyche, a la Freud.

I have long worried that we have all collectively agreed to be unambitious in our approach to (neurotic) mental health. I'm trying to flesh out an ambitious vision, which I hope to write more about in due course.

Hypotheses: LLMs progress makes the present a ripe time for various kinds of self-experimentation, we're simply too far away from a comprehensive understanding of the human psyche for us to make meaningful progress.

## Why isn't brief psychotherapy more popular?

[Brief psychotherapy](https://en.wikipedia.org/wiki/Brief_psychotherapy) seems obviously good, on premise. It's cheaper, which is good for clients/public health services/insurance companies, and also aims to get patients the results they want more quickly - something that seems appealing in our modern era of instant gratification. It doesn't involve extended periods of exposition of traumatic pasts, a universally disliked component of most psychotherapy. The fact that it's a niche therapeutic modality is honestly baffling to me, especially given it doesn't appear to have a worse evidence base than any other modality.

Hypotheses: therapists are colluding to maintain their job security, brief psychotherapy is inherently worse than comparable modalities (potentially because a key ingredient of effective therapy is the therapist-client relationship, which takes time to develop), clients counter-intuitively prefer modalities with longer timelines for some reason.

## Relatedly, how can incentives be better aligned between patients and therapists?

There are obvious tensions in both private psychotherapy and non-client-funded practice. In private psychotherapy, the therapist is incentivised to keep getting paid, and therefore prolong treatment. In psychotherapy funded by insurers or taxpayers, the opposite is true - there will be pressure from whoever is funding the therapy to move the client along as soon as possible, so another client can be seen. This means the patient might not get the depth of care that they deserve, and might not achieve the results they were hoping for. [Chris Lakin](https://chrislakin.blog/) has already explored some of this tension by trialling a bounty-based approach although also discovered that it ran into issues such as clients not being sufficiently committed[^2].

Still, I think the current status quo is obviously bad and we ought to try to improve it (see point about ambition in treatment of neurotic mental health above). One incredibly crude idea; have patients regularly complete [PHQ-9](https://www.apa.org/depression-guideline/patient-health-questionnaire.pdf) (or similar) questionnaires[^3], and then only have them pay-per-point of improvement that they see. Sure, they are somewhat incentivised to underreport any improvement, but I have enough faith in humanity to think that this would be a rarity rather than the norm[^4]. 

Hypotheses: some variation of my suggestion above is a legitimately good idea and someone ought to try it, AI assessment tools like [thymia](https://thymia.ai/)[^5] will also help resolve this issue, other AI tools will be developed that might supplant human therapists and resolve this issue anyway, the nature of the client-therapist relationship is definitionally adversarial and this is an irreconcilable difference.

## How can we safeguard against people having negative experience with LLM-based therapy?

I anticipate LLM-based therapy facing similar issues to self-driving cars. At some point soon, they will become just-as-if-not-more effective than human therapists, however a general distrust of the technology will mean they are held to a much higher standard than their carbon-based counterparts. Any high-profile cases of negative effects will severely slow diffusion, and may cause regulation to stymie patients getting access to cheap, on-demand therapy[^6]. Conventional psychotherapy already has a [surprisingly high incidence of adverse reactions](https://thehumanconditionrevisited.substack.com/p/mostly-harmless-understanding-and), far above what will be tolerable for AI equivalents. What could be done to mitigate this?

Hypotheses: regulation will prevent LLM-based therapy from achieving mass adoption in part due to these kinds of concerns, LLM-based therapists will supersede their human counterparts due to being able to offer more personalised interventions (see above) and thus naturally reduce negative outcomes, specific new safeguards will need to be developed and implemented in order to protect against this category of harms.

## Will Jevons Paradox apply to AI-generated software (or do I need to totally rethink my career)?

[Jevons Paradox](https://en.wikipedia.org/wiki/Jevons_paradox) states that increasing supply can counter-intuitively also increase demand, by driving down the price such that many new buyers enter the market who were previously unwilling to purchase at the earlier higher cost. The cost of producing software seems set to drop sharply in the next couple of years, and the paradox suggests that this *might* lead to significantly increased demand for software, thus keeping software engineers gainfully employed even after their skill is far inferior to that of Claude's. Of course, this might also be cope.

Hypotheses: producing useful software requires some sort of tacit *je ne sais quoi* (often "taste") that is unknowable to LLMs but fortunately dwells deep in my bones, demand for personalised software will indeed boom and there will be some kind of bottleneck that prevents Claude Code|Cowork|Whatever from being as potent in the hands of the untrained as in those of a hardened engineer, the cost of software production will be reduced to circa nil and my only marketable skill will soon be worthless.

## How can I get Claude Code multiplexing & orchestration working well?

Getting the most out of the seemingly-omnipotent Claude Code is all anyone talks about on Hacker News these days. I have experienced first hand the dramatic improvements in CC's capabilities over the past year, and am subsequently a true believer (it writes all my code), but now the question is how to get the most out of it. Running several instances of Claude Code on a single project is now viable, but I fear my setup is too crude: currently I run 4 instances of CC in a single [tmux](https://github.com/tmux/tmux/wiki) window, visually keeping an eye on them (which is bad as it’s bound by my concentration), do all the merges myself, and don't make use of any subagents apart from the inbuilt ones like `code-simplifier`.

Hypotheses: I should get over my aversion to notifications and implement them in tmux, I should get over my aversion to being poor and safe and embrace [GasTown](https://github.com/steveyegge/gastown) (or another immature-seeming open source orchestrators), I should roll my own orchestrator, I should abandon tmux in favour of terminal tabs with system notifications [a la Boris Cherny](https://x.com/bcherny/status/2007179833990885678), I should try to get [ralph-wiggum](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) to one-shot all my projects while I'm asleep.

## What new things can I try to resolve my emotional eating and body image issues?

It's unclear to me whether I have an eating disorder - right now I mostly think that for loose definitions I would fit the criteria, whereas stricter ones I wouldn't. This causes me a lot of anguish on a day-to-day basis that I'd love to resolve. Very broadly, the things I have tried so far include an [NHS-prescribed course of CBT-E](https://www.oxfordhealth.nhs.uk/camhs/wp-content/uploads/sites/13/2019/05/Eating-Disorders-CBTE-0718.pdf)[^7], spending some number of sessions on it with my current integrative psychotherapist, social media abstinence, keeping a food diary, avoiding scales/mirrors, regular exercise, and [vulnerability-posting](/blog/eating/). As far as I can tell the most effective intervention so far has been getting tattoos, which has various drawbacks (which I trust are self-evident).

Hypotheses: I should experiment with different therapeutic modalities (there is a reasonable evidence base for DBT, IPT, CFT and ACT, see [e.g. this article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6570825/)), I should experiment with building my own AI tooling to try and help me, I should try yoga more seriously (which also [has a decent evidence base](https://www.researchgate.net/publication/334815617_Effects_of_Yoga_on_eating_disorders-a_systematic_review)), I should experiment with psychedelics, all of the above.

## How can I improve my writing workflow?

Currently my writing workflow looks something like this: write a bunch of notes in a Notion page, maybe throw together half of a first draft, let this languish for several months, redraft starting from scratch in [750 Words](https://750words.com/), copy and paste it back into Notion, repeat the previous step 1-2 more times, manually feed it into a Claude project pre-loaded with my previous writing and various style guidelines, address any feedback it gives, publish to my website with a small Python script and [neovim](https://neovim.io/) as my text editor, publish to Substack manually through the UI and faff around with having to redo things like footnotes because the Substack editor doesn't support markdown (why not???). Ideally, all these steps would take place within a single tool, and this would prevent me from having so many drafts languishing, forlorn in the cyberether.

Hypotheses: I should hack something together in neovim that would handle the whole pipeline, I should do all my drafting/editing/publishing in the Substack editor and then write a script that is triggered by the Substack email which parses/formats/publishes the post on my website too, use some third party tool of which I am currently unaware, change/simplify my current setup somehow.

## How likely is it that aliens have visited Earth?

A curveball I know, but anyone who knows me personally knows why I've been so curious about aliens recently. The best articulators of the pro-aliens position in my opinion are friends-of-the-blog Atoms vs Bits (see e.g. [here](https://www.atvbt.com/tag/ufos/), but also [here](https://www.atvbt.com/ufo-objections-extraordinary-evidence/) and [here](https://www.atvbt.com/you-might-soon-believe-in-aliens/) because alas their tagging game isn’t the strongest), and the strongest opponents are the good folks at [Metabunk](https://www.metabunk.org/). For the uninitiated, it's worth watching the recent Prime documentary [The Age Of Disclosure](https://www.primevideo.com/detail/The-Age-of-Disclosure/0NVVP9AVUZEJKG9CJC4RQE9J27), although I have various qualms with it that I might write up at a later date. The strongest evidence in favour comes from the Congressional hearings of the past couple of years, in which people have made broadly two kinds of claims *under oath*: I saw something in the sky that resembled some kind of aircraft that appeared to defy the laws of physics that I cannot otherwise explain, and they have had access to a secret sub-organisation of the Pentagon which is intentionally hiding relevant information from the general public (including evidence of crash retrieval, biological specimens etc). These people have been former or current military, intelligence services etc., with security clearances, seniority, credibility and respectable careers which they have jeopardised by participating in these hearings. There are all kinds of possible explanations that aren't extraterrestrial in nature: meteorological phenomena, novel terrestrial technology that the US government/general public aren't aware of, a US government PsyOp, [mass psychogenic illness](https://en.wikipedia.org/wiki/Mass_psychogenic_illness), folks simply deciding that their 15 minutes of fame is worth inventing some crazy story under oath. Secretary of State Marco Rubio (who was featured prominently in the documentary) skilfully articulated the crux in a [recent interview with Sean Hannity](https://www.state.gov/releases/office-of-the-spokesperson/2025/12/secretary-of-state-marco-rubio-with-sean-hannity-of-fox-news-hannity):

> It has, as I said, claims from people that were former admirals, naval fighters, people with high clearances in government.  Some of them are pretty spectacular claims.  I’m not calling these people liars.  I don’t have independent knowledge that what they’re saying is true.  The one observation I had is we had people that did very important jobs in the U.S. Government who are saying these things.  So we have people with very high jobs in the U.S. Government that are either (a) liars; (b) crazy; or (c) telling the truth, and two of those three options are not good.  I don’t know the answer.
> 

Oh, and there is one more thing. After a while of being interested in this, I started asking people I met whether or not they have a UFO story. Obviously it’s completely anecdotal but I was shocked at how many people either had a personal story, or had heard one from a friend or family member. I recently met a friend’s new partner, and they had not only a story, but pictures too, of something I simply can’t explain; a light in the night sky far too big and bright to be a celestial body, a satellite or a plane. They said it was soundless and stationary, and I don’t see why they’d lie. 

Hypotheses: aliens have visited earth and the powers that be are covering it up for possibly nefarious reasons, the powers that be are covering something even bigger than aliens up almost certainly for nefarious reasons, highly trained government and military personnel have repeatedly succumbed to mass hallucinations, we’ve collectively hyperstitioned aliens into existence, there are novel and rare meteorological phenomena that bear a spooky resemblance to aircraft, the Russians/Chinese/Atlanteans have invented field propulsion or similar sci-fi-esque technology.

[^1]: You might wonder whether clinicians are resistant to adopt AI. In what will be my first co-authorship, we recently submitted a paper for peer review that suggests this not the case.

[^2]: Chris appears to have edited his blog post discussing this, although the old versions are still available via the Wayback Machine. I am unsure of the ethics of linking to an archived version of a now-edited post, or of mentioning now-deleted content at all - I decided to go for the middle option of mentioning-but-not-linking, please let me know if you feel this is a mistake on my part.

[^3]: I would like to briefly note that I have filled in an inordinate number of PHQ-9s in my time and loathe them. Being forced to quantify one’s suffering can be extremely dehumanising.

[^4]: Again, this is a somewhat crude suggestion, I am more trying to gesture vaguely in the direction of a thing that could be useful than seriously endorsing this particular payment structure. Possibly Lakin’s hybrid low fee + results-based bounty approach would help the client feel like they have sufficient financial skin in the game to put in the necessary work to improve.

[^5]: I have no idea if their product specifically is actually any good; this is not an endorsement of it. I also have no idea why they opted not to capitalise their name.

[^6]: Arguably it already has - see for example [Illinois banning AI therapy](https://idfpr.illinois.gov/news/2025/gov-pritzker-signs-state-leg-prohibiting-ai-therapy-in-il.html).

[^7]: This is really the best link that I can find. I had CBT-E in London, not in Oxford. They promised me that the E stood for Eating (Disorders?) not “Enhanced” which seems much more common now I search for the term. In hindsight I regret not spending more time researching the legitimacy of the modality ahead of time, although I am not surprised to find little about it given how ineffective I found it as a treatment.
