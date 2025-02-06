---
type: blog
date: "2022-08-24T13:43:27Z"
author: Jonny Spicer
title: "What I Learned From Applying To 100 Programming Jobs"
categories:
- Bestof
- Career
- Programming
---
## TL;DR

- Many people do not treat the job market like a market. You are trying to sell your labour, and in order to get the best possible price, you have to offer your goods to as many potential buyers as possible. Here, the "price" for your labour is not only salary, but also opportunities for career progression, intellectual stimulation, work/life harmony and company culture.
- There is an efficient way to prepare for interviews. Invest the time upfront to work out a strategy that seems optimal for you, and don't over-prepare.
- Applying for jobs is an emotional rollercoaster, and you need to be prepared for it. Ideally have someone to support you.
- You should probably ask for more money than you think you should. If your price is too high, the market can happily adjust it down for you, but if your price is too low, the market will snap your hand off.
- Have an overarching plan for your career; think about where you are headed and whether you're moving in the right direction. Don't leave it to the point where your current position is untenable to look for a new job.
- It's a great time to be a software engineer, and the hiring market continues to be resilient against "adverse macroeconomic conditions". If you're good, you'll be able to get multiple offers, ultimately landing you a better deal.
## The Strategy

Getting a new job is difficult, time-consuming and emotionally draining. For my recent search, I employed a different strategy than I had previously, and learned a lot along the way.

In a sentence, my plan was to apply for a very large number of jobs, have the most complete possible picture of my options, and then choose the best one. I am admittedly using both the number 100 and the word “applying” pretty loosely in the title - I actually only have 93 jobs in my spreadsheet, and “applying” includes when a recruiter reached out to me and I responded. The roles had a variety of titles, most of which were some flavour of “backend software engineer”, as well as a handful of machine learning engineering roles just to see if anyone might be willing to train me up in ML (spoiler: they weren’t).

### Finding Positions

I applied to every big tech company I could think of through their website, and didn’t use any referrals. Other than that I mostly found jobs through [Otta](https://otta.com/) and [cord](https://cord.co/), I sent a few applications through [Work at a Startup](https://www.workatastartup.com/), and I also handled several applications through another job site that I had a pretty bad experience with so won’t mention them here. My bar for applying was pretty low, the only criteria being:

- Main language is Go, Python or Typescript;
- Could meet my salary expectations (I didn’t apply to companies through 3rd party job sites if they didn’t publish their salary bands);
- The role wouldn’t entail working with ads, crypto/web3 or the fossil fuel industry.

### Interview Preparation

I did my technical interviews in either Python or Go, depending on the specific format of the interview. I’m more comfortable with Go, but I think Python is a better language for quickly solving data structures & algorithms questions, so I chose that whenever I thought I would be assessed on core programming concepts more than language specifics. I generally preferred pairing interviews to take-home tests when I had the option, in part because the former are a much smaller time commitment, but also I think they tend to be slightly easier - in a pairing interview a big part of what you are being assessed on is communication (which I am strong on), whereas in a take-home test you are more likely to be assessed on performance and scalability of your code (which I am weaker on). 

I revised for data structures and algorithms interviews using [neetcode.io](http://neetcode.io). My process was:

- Attempt the problem on my own;
- If I got stuck, watch the portion of the neetcode video where he explains the relevant concepts;
- Attempt the problem again;
- If I was still stuck, watch the portion of the video where he explains the code;
- Once I have a working solution, write my own notes on how it works.

In the end I only did 96 [Leetcode](https://leetcode.com/) problems, certainly a lot less than I've seen other people talk about doing. I also concentrated on the basics; 69 of the problems I completed were labelled as easy, 27 as medium, and none as hard.

I mostly prepared for the only system design interview I took by using Donne Martin’s [System Design Primer](https://github.com/donnemartin/system-design-primer), and reading the first half of Martin Kleppmann’s [Designing Data-Intensive Applications](https://dataintensive.net/). I made notes while reading both, which I reviewed, but I didn’t do any practice designs. While I only did one explicit system design interview (which I passed), the concepts were worth learning given that almost every technical interview I had contained some discussion of scalability, be that of specific code I'd written or of a bigger system.

The only behavioural interview I specifically prepared for was Amazon’s. I wrote out each [leadership principle](https://amazon.jobs/en-gb/principles) and tried to write down 1-3 examples from my career that demonstrated it (for this I looked through my CV, feedback from colleagues and performance reviews at my current job as well as scouring my memory), but I didn't write out the full anecdote using the [STAR method](https://www.themuse.com/advice/star-interview-method) that most places encourage. This exercise seems like it was valuable for all my behavioural interviews, but equally I think I am a reasonably good storyteller, as well as fairly introspective, which appears to serve me quite well in these.

## The Numbers

- I applied for 93 jobs.
- I never heard back from 24 companies.
- I had 26 initial screening calls, a 28% hit rate from my applications.
- I decided I didn’t want to proceed with 7 roles after this initial screening call.
- 7 places didn’t get back to me after the initial call, 4 of which I felt like had gone well. Of the people that didn’t get back to me, 3 were startups where my initial call had been with one of the founders.
- I did 13 technical interviews and 3 tech tests, for 12 different roles, a 46% hit rate from my screening calls. Some processes included both a take home test and a technical interview, another had both a coding interview and a system design interview (counted for 2 in these numbers). I counted the one “loop” with multiple technical interviews I did as a single interview - if I counted each one separately, that’d be 15 technical interviews.
- 2 companies never got back to me after my technical interviews.
- I declined one final interview after passing the tech test stage.
- I did 5 behavioural/cultural interviews, a 42% hit rate from my technical interviews. Of the ones I passed, three I’d taken in Go, one in Python, and one in a mixture of both.
- I got 5 offers - a 100% success rate from my behavioural interviews!
- 1 offer was below my stated salary expectations, and 4 above.
- I accepted an offer from [AWS](https://aws.amazon.com/), and I’ll be starting in October.

## Pros & Cons

### Pros

There are several significant advantages to this approach, that all broadly amount to “you’re more likely to get a higher quality job than you would otherwise”. 

Firstly, this seems true in the probabilistic sense - the more jobs you apply for, the more offers you’ll get, the higher chance that one is of high quality. 

Secondly, the more interviews I did, the better I got at them. Every technical question that I didn’t know the answer to, I looked up afterwards and had it fresh in my mind for the next one. By the end, my behavioural anecdotes were slick and honed down to the word.

Thirdly, you get a much better understanding of your position in the market, rather than your value to a specific company. The obvious way this manifests itself is in terms of compensation; the offer I accepted had a ~35% higher salary than the first one I received. I had done a decent bit of research into salaries for software engineers in London using [levels.fyi](http://levels.fyi) and [Glassdoor](https://glassdoor.co.uk/), but this data is hard to draw meaningful insights from given I didn’t know if I ought to be comparing myself to the median engineer or perhaps the top quartile (or of course the bottom!). 
The salary for the offer I accepted was ~30% higher than the number I’d given as my expectation to every company in the process. I made the classic rookie error of not only giving a number, but giving one that was too low, however it would’ve been difficult for me to arrive at a better number without having gone through so many job processes (incidentally, at no point did anyone ask me what my current salary was, which is something I’ve had a lot in the past - a quick Google suggests employers have stopped asking this because employees simply lie, which I think is hilarious). 

There is a more subtle version of this too. Jobs are obviously about more than just money, they’re about engineering quality and culture, and ultimately doing so many applications will give you a better idea of whether the market thinks you’re a good engineer. I was fortunate enough to get some initial feedback that yes, the market *does* think I’m a good engineer, which gave me a lot of confidence in future interviews, making me not only more relaxed, but also willing to be more demanding of prospective employers. I gained deeper insight into what good engineering culture at a company looks like; an outside evaluation is only going to be so accurate, but when I spoke to so many companies about their work environments, it became clearer which answers ought to be compelling and which were red flags.

### Cons

Doing things this way is both stressful and time-consuming. I estimate I spent ~40 hours in calls and interviews, 
~100 hours preparing and 
~20 hours doing applications, all in the space of a couple of months alongside a full-time job. The sense of relief when I was done with my final interview was pretty overwhelming, and my health has definitely suffered slightly during this period.

Filling out this many applications will inevitably result in a very large number of rejections, which is difficult to handle emotionally. The main way I dealt with this was to keep a “rejection doc”, where I wrote down every rejection I got, trying to gamify it and get some good feelings from filling in another line. I also keep a “CV of Failures” from my career which serves as a good reminder that even though things seem like setbacks at the time, in the long run I’m still on an upward trajectory. These helped a little, but not a lot - I’m not sure what else I could have done to try to improve this. 

## What I’d do differently next time

Firstly, I think in general I prepared for interviews pretty well. My knowledge of data structures and algorithms seemed to be barely good enough to scrape through, which seems to suggest I didn’t spend more time on it than was necessary, likewise with system design. My confidence regarding behavioural interviews was apparently justified, so extra preparation there seems similarly unwarranted.

With that being said, there are definitely things I would do differently in the future. Broadly, the big mistake I made was nothing to do with the job search; it was the situation that led to the job search. I found myself in a position where I wanted to leave my current role as soon as possible, which meant that I had to adopt the scattergun approach and then take whichever option turned out to be best. Ideally I would apply to companies in batches in descending order of how much I wanted to work for them, or to only apply to jobs that I most wanted and if I was rejected, simply wait and reapply. 

In a similar vein, I would turn down roles earlier in the process. I had originally set out with the plan of getting as many offers as possible and then deciding which one to take, but this was far too time-consuming with the number of processes I had going on. I should’ve trusted my intuition more - if I didn’t feel excited about a role at any point (including after the initial screening call), then I shouldn’t have continued, not only because I wouldn’t ever be excited about accepting an offer, but also because the feeling is likely mutual, and I found that there was a correlation between how much I enjoyed the interviews/was excited about the company and the chance of progressing through to the next stages (but not a huge one, small sample size, confirmation bias etc). 

As alluded to above, next time I will do more research on what salary expectations I should have. I think a more optimal strategy probably involves asking people that I know and can benchmark myself against what they earn, as well as generally setting my expectations very high and letting the market adjust them down if necessary.

Lastly, I would’ve tried to get referrals, although this is primarily relevant for big tech companies. If you don’t know anyone at these companies it seems straightforward enough to find someone to refer you on [Blind](https://www.teamblind.com/), with the obvious caveats that a) I’ve not tried this myself and b) Blind has exceptionally poor vibes. 

## Final thoughts

Doing so many applications inevitably results in a lot of enlightening, weird, funny, frustrating and fulfilling moments. Most recruiters are lovely people who want to help you succeed, but there are certainly those out there that give them a bad name, and they seem to be disproportionately concentrated at external agencies (in my experience at least). Each of the many methods the tech industry uses to assess whether somebody is a good software engineer is a bad proxy in some way, however they exist on a spectrum from “somewhat bad” to “overwhelmingly terrible”. 

I found it *really* hard to make rational decisions during this whole process. As mentioned above, I found all the rejections difficult to handle emotionally, particularly up until the point that I got my first offer. Each one filled me with doubt, something which I was hardly short on in the first place, and I think I’d advise anyone to make sure they have someone to talk to and support them throughout the process. It was a struggle to remain focused on what I was optimizing for (opportunities to learn the skills that I need in order to transition to a high-impact job in the future), and I frequently found myself falling prey to my desire to be liked, to earn more money and to have higher status. I think it’s important to think hard about this before you begin your search - what are you looking for in a new role, and what are willing to trade off? Write it down, and keep referring back to it.

---

I am incredibly excited about my new job, and that I’ve made it to a FAANG company, despite frequently thinking I would never be good enough to do so. All the effort I put in seems to have been worth it, and I’m sure I’ll write in the future about what life at Amazon is like and whether it lives up to the hype. 

There are many things I didn’t cover here, including how to prepare for specific interviews, my thoughts on salary negotiation and the optimal way for companies to evaluate engineers. These things are largely omitted for brevity, but I would be more than happy to chat about them - feel free to [contact me](/contact) if you’re interested.