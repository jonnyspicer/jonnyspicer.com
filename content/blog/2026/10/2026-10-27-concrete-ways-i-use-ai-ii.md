---
type: blog
date: "2026-10-27T13:55:00Z"
author: Jonny Spicer
title: "Concrete Ways I Use AI II"
categories:
- AI
tags:
- egghaven
# status: 
# confidence: 
# importance: 
---
*i’m shamelessly ripping off Inkhaven and doing my own challenge, [Egghaven](/egghaven). This is the second post.*

In July 2024, [I wrote about the various ways I was using AI in my day-to-day life](https://jonnyspicer.com/blog/concrete-ways-i-use-ai/). A little over two years later, both my usage and the AI landscape have changed significantly. At this point, having a Claude subscription feels close to having a small team of people work for me, so I wanted to share the roles that I think AI is especially well placed to occupy.[^1] Use-cases from 2024 that aren’t explicitly mentioned here still apply — the biggest updates are that most of the “general tips” from two years ago are obsolete, now that models are much more reliable and better at tool-use.

## General tips

1. Models don't need prompting in specific ways like they used to. Now the best results often come from using very natural language.
2. Give models a way to verify their work. For longer, more complex tasks, explicitly telling the model what the success condition is, and how to check it, will give the model a chance to correct its own mistakes before handing the reins back to you.
3. Similarly, rather than adding a lot of context yourself, tell the model where to find necessary context, and then let it use tools to search that context as necessary. In general, models are now very good at using tools, so you should give them lots of tools to use.
4. Calibrate what level of risk you are willing to accept. The points below reflect that I have been somewhat liberal in giving Claude access to my data — in general I have strongly preferred to give it read-only permissions when those are sufficient for achieving its tasks, and I have taken precautions to try to minimise the blast radius of any issues arising from Claude performing some kind of harmful action on my behalf (e.g. Claude Code has no access to cloud infrastructure CLI tools).

## Personal assistant

### Automations & integrations

Most popular apps now have a Claude integration. For example, I make heavy use of the Gmail, Google Calendar, Notion and Granola connectors. Combined with Claude's "scheduled tasks" feature, these are extremely useful. Here are some of the scheduled tasks I have set up:

- A daily morning brief that includes what I've got on my calendar today, any new or urgent emails that I ought to respond to, and what items are in my Notion to-do list. It's configured with my overarching priorities, and so can help me drop or defer tasks that aren't urgent or important. It also helps plan my day, and blocks out calendar time or drafts email responses if necessary.
- A weekly review, essentially a mini retro, that lists everything that happened this week and encourages me to reflect on it. It creates a new Notion page for each review so I can fill in what went well, what didn't, and what I want to change next week. In the following week, it will then check whether I succeeded in changing what I'd wanted to.
- A weekly roundup of the relevant AI news. Pretty self-explanatory: it’s tuned to pick up on the things I care about more and synthesise them for me. This saves me having to wade through Zvi's newsletters, or trying to find some other news aggregator that would likely be too noisy for my tastes.
- A daily task that pulls new call notes from Granola and suggests action items to go into Notion off the back of them.
- A weekly roundup of analytics for my [personal website](https://jonnyspicer.com), my [business website](https://allinlabs.io) and my [Twitter account](https://x.com/jjspicer).

### Custom connectors

Claude can often make its own custom connectors for apps that don't have official integrations. I have several Hetzner VPSes, and if I ask Claude to set up a new MCP server on one, it'll usually one-shot this for me. I have custom connectors for [Kerouac](https://kerouac.allinlabs.io/), [Google Search Console](https://search.google.com/search-console/about), [Metaculus](https://www.metaculus.com/), [Zoho Mail](https://mail.zoho.eu/), a self-hosted [Postiz](https://postiz.com/) instance (which allows me to post to Twitter via Claude), Spotify and a self-hosted [Umami](https://umami.is/) instance. I even have a custom connector for [FinalSurge](https://www.finalsurge.com/), which required Claude to reverse-engineer FinalSurge's private API in order to write its own MCP implementation, rather than using an existing open-source one. This is pretty great — when my daily brief scheduled task runs, it pulls in my training plan from FinalSurge, and then blocks out time in my calendar to do it!

### Bookkeeping

I have the [Xero](https://xero.com) MCP configured, which means I can ask Claude to help with the bookkeeping for All In Labs. While it will caveat almost every message by saying it's not a qualified accountant, it is very good at spotting mistakes I've made when my accounts don't add up, suggesting correct tax codes and highlighting ways I could cut back on spending. Given that I find Xero extremely unintuitive and difficult to use, Claude's help here feels especially valuable.

## Software engineer

### Software factory

[Software factories](https://www.warp.dev/articles/what-is-a-software-factory) are inevitably the future of programming. They require some setting-up, but current models are now good enough to be able to complete the whole software development lifecycle relatively reliably. For any new personal project (e.g. [Kerouac](https://kerouac.allinlabs.io/), my bespoke writing app), my workflow is:

1. Create a plan for implementing the project with Claude. Go back and forth over the details until I am confident it is correct. Ensure that the plan includes a way for Claude to be able to test its work (e.g. tell it to use a browser or write Selenium tests), and some kind of adversarial code review (see below).
2. Tell Claude to execute the plan and notify me when it's done.
3. Review the *behaviour* of the generated programme, and then repeat steps 1-2 as necessary.

That's it! It's remarkably easy for me. I still need to pay attention to the plan, as often Claude still makes poor architectural choices. I'm also light on details of how I set this up, but perhaps I will flesh this out into a full post soon.

### Code review

For larger, production codebases (and for paying clients), models are still not reliable enough to be able to use the software factory pattern from the outset. In these projects, AI has made writing code extremely fast and cheap, so now the bottleneck to deploying more code is reviewing it. For critical systems, there is still no way around reviewing every line of every PR that Claude generates. Even so, we can take steps to improve the quality of the code as much as possible before we come to review it. The low-hanging fruit here is Claude Code's built-in GitHub code review feature, which can be set up by simply running `/install-github-app` from your session. You can then tell the agent that is writing the code to use a loop of opening a PR, waiting for the review, and making necessary changes until the review finds no substantive issues. This is still Claude checking Claude's work, though — alternatively, it's trivial to have Codex do the reviews and to instruct Claude Code to initiate the review using the Codex CLI, or vice versa.

### Continuous improvements

One of the issues with AI-generated software is bloat. Perhaps model coding capabilities will keep increasing such that they'll still be able to outrun this, but in production systems there are still going to be on-call engineers having to troubleshoot issues in the codebase. Fortunately, there are two easy ways to try to counteract this:

1. Every time a new model comes out, have it do a systematic review of your codebase where it fixes bugs and makes refactors (ensure you have high confidence in your test suite first!).
2. Ship your code with profiling and coverage tools, to understand how it behaves in production. These can help inform which code paths make up the core workflows of your software, and which ones to consider trimming or consolidating.

## Research assistant

### Deep dives

The "Research" feature is useful for being able to quickly get an overview of a specific topic. Some things I've recently asked it for include: how does progress in AI affect progress in robotics, what is the current state of AI policy in China, and what were the key events that caused the climate movement to enter the mainstream. It's still worth maintaining a healthy level of scepticism, as well as verifying that the citations actually support any claims that are made.

### Lit reviews

I often ask Claude to tell me what the evidence base is for a given intervention, and I trust its judgment enough for low-stakes questions. Some examples of recent interventions I've been curious about: various supplements, various sleep hygiene improvements, various peptides. Part of the reason I am somewhat trusting of Claude here is that Claude itself seems to be moderately sceptical by default, and requires a high bar for claiming that evidence is robust. This provides a nice counterbalance to social media, advertising, etc., where everyone is in the business of shilling silver bullets.

### Shallow dives

As I said in 2024, Claude is something of an interactive encyclopaedia. It turns out it's a huge amount of fun to learn about the world when I know I'm not going to be tested on it afterwards. Did you know that there are two octopus "cities" off the coast of New South Wales dubbed ["Octopolis" and "Octlantis"](https://en.wikipedia.org/wiki/Octopolis_and_Octlantis)? Or that [pig-tailed macaques in Thailand are used in commercial coconut-harvesting operations where they can harvest up to 1,600 coconuts a day, while a human can only manage around 80](https://www.nationalgeographic.com/animals/article/monkey-labor-continues-in-thailands-coconut-market)? Or that in WWII, the [Germans built passive radar systems on the north coast of continental Europe to use Britain's own *active* radar systems against them, by using the signals from Britain's system as illuminators for German receivers](https://en.wikipedia.org/wiki/Klein_Heidelberg)? You can even ask Claude to tell you things it thinks you'd find interesting, and it'll use its memory of you to do so. Compared to 2024, the way I use Claude now is much more curiosity-driven, and less based on fear of looking stupid asking a person. When knowledge is so accessible, curiosity feels a lot more natural.

## Editor

### Style

What is the purpose of a given piece of writing? What is its intended audience? What is it the author actually wants to say? Having answers to these questions is a prerequisite for good writing. Claude can help elucidate these, and then help match the author's natural style to one that will resonate with the intended audience. For example, I think that "AI by Default" still clearly has elements of my style, while also being tailored for LessWrong. I have a project that has a style guide synthesised from all of my posts and those of my favourite writers, and this helps Claude give meaningful feedback about whether my tone is too snarky or too neurotic, while still allowing for *some* snark and neurosis.

### Factuality

I care a lot about saying true things — this is more important to me than influencing people or having them think I'm right. Claude can go through a draft and check that all my claims are actually supported by the evidence, and offer potential counterarguments that I can get ahead of.

## In closing

It’s odd to read back my post from only two years ago; my use of AI feels so crude in comparison to today, and this highlights quite how much has changed in such a short time. I do genuinely feel significantly more productive than I was back then. With that being said, I’m sure there are still ways in which I could be extracting even more value out of my Claude subscription, or creative use cases that it hasn’t yet occurred to me to try; if you think I am missing something then please have a low bar for letting me know about it.

[^1]: In my previous post, I specified which model or tool I was using. Now, you can assume that I am using Claude, as that is the family of models I use for practically everything at the moment. I am currently on the $200/month Max plan, which I still feel represents excellent value for what I get from it.
