---
type: blog
date: "2024-07-22T20:50:36Z"
author: Jonny Spicer
title: "Concrete Ways I Use AI"
categories:
- AI
---
Below is a list of concrete uses I’ve had for AI tools in the past month. In each case, I list the tool or model I used, and in some cases I added some additional context on how to get the best results (in my opinion).

I wrote this because many people don’t realise that AI tools can already be extremely useful in day-to-day life. While some of the tools I use are paid (currently I am paying for [Claude Pro](https://claude.ai/) and [GitHub Copilot](https://github.com/features/copilot)), there are free alternatives that are only marginally worse, if at all (eg [GPT-4o](https://chatgpt.com/) and [Tabnine](https://www.tabnine.com/)). I find the paid tools to be excellent value for money, and overall think that these tools make many aspects of my life easier, quicker and more successful.

## General tips

1. Learn the very basics of how language models work (i.e., where they get their training data from, how the training process works, and how they are next-token predictors). This can be *extremely* simple, pasting the previous sentence into ChatGPT would probably be sufficient. Understanding how models are trained will give you a better intuition for the kinds of tasks they will perform well on, as well as hint at what prompting techniques might be beneficial.
2. Give examples where feasible. Models perform significantly better on many common tasks with even one example. 
3. Use the system prompt to add context for frequent tasks. Mine includes a little bit about me, the people in my life, my job and my interests.
4. Make use of long context windows. You can now feed language models a huge amount of input data, which it can utilise effectively. Use this to your advantage by adding API documentation, your favourite author’s top 10 blog posts, or a PDF of a long, technical report as context to your queries. Claude’s projects feature is particularly handy for this.

## Coding

### Code generation

**Tools:** Claude 3.5 Sonnet (£18/month), GitHub Copilot ($10/month)

**Value:** Both tools save me a lot of time writing boilerplate code. Copilot is good at filling out “obvious” code blocks, Claude is good at writing business logic and unit tests,  and can do neat things like write structs that correspond to a provided JSON input. The latter can take business requirements as well as existing code and implement the described changes, and will often produce high quality classes/methods from scratch with business requirements as the only input. 

**Tips:** Claude’s projects feature can be used to have shared context like API documentation or repository coding style guidelines added to all your chats. Depending on your usage, you could also add info about code style, number of comments etc to your system prompt. 

### Debugging

**Tools:** Claude 3.5 Sonnet

**Value:** Copy and paste stack traces and relevant code, simply ask Claude to identify the bug and it will often rewrite the offending section for you. 

**Tips:** If you tell Claude there is a bug in a piece of code and there in fact isn’t, it will usually hallucinate one. I find that if Claude doesn’t immediately fix the problem, any subsequent solutions it offers tend to deteriorate in quality after you’ve pointed out the initial failure. It’s usually better to start a fresh chat and try to craft the initial prompt better (or fix the bug yourself).

### Software architecture

**Tools:** Claude 3.5 Sonnet

**Value:** Helps me lay out coding projects in a way that is intuitive and easy to maintain, and follows best practices for any given language or framework.

### Teaching me NeoVim

**Tools:** Claude 3.5 Sonnet

**Value:** Transforms natural language queries into the commands I need to run in order to get [NeoVim](https://neovim.io/) to do my bidding. Easier and quicker than having to go through a cheatsheet, particularly for multi-step workflows.

**Tips:** Upload your `init.lua` config as context so Claude knows your exact keybindings.

## Writing

### CV optimisation

**Tools:** Claude 3.5 Sonnet

**Value:** Quickly highlight strengths and weaknesses of a CV against a given job description. Can suggest improvements.

**Tips:** Models are generally a bit sycophantic, so Claude will be more positive about a CV if it thinks it’s yours. Prompt it in a more adversarial way - e.g. say that you’re a hiring manager, you’ve had this CV sent in and its absolutely critical that the right hire is made so there is an extremely high bar etc. Alternately, simply ask Claude to only list the negatives of the CV, rather than to provide a balanced view.

### Magazine pitch optimisation

**Tools:** Claude 3.5 Sonnet

**Value:** If you are writing a pitch for a story to a magazine for the first time ever, then you probably have no idea what you’re doing - at least I didn’t. Rather than trawling through the websites of various dubiously-credentialed digital-nomad-influencer-types to figure out how to write a good pitch, let Claude critique and improve yours instead.

**Tips:** Similar to above - prompt Claude that you are a magazine editor and are reviewing the pitch, rather than the prospective author. Also be careful about copying Claude’s output verbatim - magazine editors worth their salt will at least be suspicious that they’re reading AI-generated copy.

### LinkedIn post/email drafting

**Tools:** Claude 3.5 Sonnet

**Value:** I feel anxious when I think about writing certain emails or posting on LinkedIn. This often makes me procrastinate, which is somewhat inconsequential in the LinkedIn case but sometimes alarmingly consequential in the email case. The consensus is that current LLMs aren’t conscious and so can’t feel anxiety, so I outsource these emotionally-challenging tasks to Claude.

**Tips:** Consider having Claude turn bullet points into a full post or email, and give it an example of writing in your own voice. The average post quality on LinkedIn is already impressively low, but I still don’t want to be partially responsible for exacerbating it with AI-generated copy, and nobody likes receiving an email that is obviously LLM-generated.

### Spell/grammar checking

**Tools:** Notion AI (free)

**Value:** I want to make it as quick and easy as possible for me to post something on here, which means I don’t want to worry too much about editing. I draft all my posts in Notion, and now I can have AI simply fix any spelling and grammar mistakes for me, potentially reducing the total time spent on a post by half. 

## Expert advice

### Medical advice

**Tools:** Claude 3.5 Sonnet

**Value:** If I have a minor injury, Claude is at my fingertips to give me the same advice the median physio would at a fraction of the cost. Similarly if I have a cold, my GP has a waiting list, but Claude doesn’t. Last month I uploaded pictures of the rash on my hand as well as a description, and it gave me three plausible sounding possible diagnoses, as well as common causes and interventions to try.

**Tips:** My model for lots of interactions with medical professionals is that they’re triaging, and giving me the diagnosis and treatment that is *most likely* to work, not one that is guaranteed. Claude works well if you treat it the same way. Hopefully it goes without saying, but for anything serious, consult a human being.

### Legal advice

**Tools:** Claude 3.5 Sonnet

**Value:** Legal advice is expensive, often prohibitively so, but not with Claude. Recently my former employer sent me an email saying that they had overpaid me and providing instructions for how I ought to repay them, however I didn’t (and don’t) believe they are correct about the overpayment. Claude was helpful in advising me how best to respond.

**Tips:** Again, use your judgment - a human lawyer will be the best option for anything non-trivial.

## Day-to-day

### Journal dictation

**Tools:** Notion AI

**Value:** The merits of journaling are often-touted, but finding the time to sit and write out my thoughts is tough, even with my [fancy keyboard and90 wpm typing speed.](/blog/zsa-voyager-review/) Using Notion AI’s speech-to-text feature, I can dictate my journal entries, and still be able to easily read them later and search through them. This is quicker, easier, and possibly has some of the additional catharsis benefits of saying something out loud, a little like in a therapy session.

### Book recommendation

**Tools:** Claude 3.5 Sonnet

**Value:** There’s so many books to read, and so little time. When I’m reading a book I love, I often tear through it in a few days, but if I get stuck on one that isn’t sparking joy then it drags on for weeks. Ideally I would get better at giving up on books, but the sunk cost fallacy is a powerful thing. As far as I know, there aren’t any book recommendation algorithms out there (please correct me if I’m wrong), but Claude will do in a pinch.

**Tips:** [Export your Goodreads history](https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590) and create a new project in Claude with it as context. Now you can ask Claude for recommendations based on your previous ratings, and constrain it by asking for books of a certain length or genre, authors of a certain nationality or period etc.

### Recipe generation

**Tools:** Claude 3.5 Sonnet

**Value:** I like cooking, but most recipe websites are full of awful SEO spam, and many don’t offer ingredient substitutions. Some don’t even have metric units! You can specify to Claude that you want a source of protein as well as several vegetables, as well as let it know what ingredients you already have in the fridge, and voilà. I’ve used Claude to design whole menus for 15 people!

**Tips:** Add “Units: metric” to your system prompt to stop Claude giving you everything in cups. Good for substitutions, making recipes vegan/gluten free etc. Save the recipes you like somewhere, as they can be hard to find in chat history - eventually you can start a new Claude project with your favourite recipes and have it figure out other recipes that you’d enjoy.

### Interactive encyclopaedia

**Tools:** Claude 3.5 Sonnet

**Value:** There are some questions I feel stupid asking a person, and that are difficult to find answers to with a search engine. In the latter case, follow up questions can also be extremely difficult if the topic is one I know nothing about. Historically this has been my most-common use case for ChatGPT/Claude. One recent concrete example was having to implement in code some functions related to [Brier score.](https://en.wikipedia.org/wiki/Brier_score) This involved a tiny bit of maths as well as a lot of probabilistic jargon that I was scared of. Claude graciously held my hand while explaining the whole thing to me.

**Tips:** I’ve had very good results without much explicit prompt engineering. If the subject of your question is less well-established or more recent then consider trying [Perplexity](https://www.perplexity.ai/), an LLM-powered search engine. I’ve had OK results with it, but it doesn’t feel as powerful as Claude for things that are in the latter’s training data.

## Miscellany

### Archive

**Tools:** GPT-4o (free)

**Value:** Sometimes things disappear off the internet, for various reasons. However, if they are in GPT-4o’s training data, it can often recall them. 

**Tips:** Useful if you don’t know the exact URL to use https://archive.is/ or similar.

### Logo creation

**Tools:** Dall-e 3 ($20/month, included with ChatGPT plus)

**Value:** Sometimes I need a logo for a [hackathon that I’m running](https://lu.ma/wa2o5ws0), but alas I have no creative ability whatsoever. Fortunately, Dall-e can easily knock together something that the [Effective Altruism](https://www.effectivealtruism.org/) logo, the [Apart Research](https://www.apartresearch.com/) logo, and deception detection.

---

I’m always on the lookout for new AI tools that offer value, although so far I’ve found most domain-specific tools to be less useful than frontier LLMs. If you know of any tool that you think I ought to try not on the list, or any use case I might have for LLM-powered tools that I’m overlooking, then please [get in touch](/contact) and let me know!
