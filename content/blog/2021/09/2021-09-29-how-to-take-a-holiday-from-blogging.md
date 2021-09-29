---
type: blog
date: "2021-09-29T16:03:59Z"
author: Jonny Spicer
title: "How To Take A Holiday From Blogging"
categories:
- Blogging
---
I'm going to Scotland for a few days tomorrow, and I'd like to spend as little as possible of my time there interacting with technology. To that end, I don't want to take my laptop, but I also don't want to lose this dumb bet. Fortunately, with the tech stack this site
is built on, it was actually incredibly trivial to find a way to solve this problem.

Firstly, [Hugo](https://gohugo.io/) doesn't publish content with a date that's in the future (although you can change the settings to allow this), meaning I can have the relevant posts written and saved and they won't get published until the date is right. At the moment
AWS Amplify runs a Hugo build every time there are changes to the Github repository, but I won't be making any changes to the repo when I'm away. You can also use webhooks to trigger an Amplify build, meaning all I'd need to do would be to sent a curl request to the right
URL every day... getting warmer, but still not quite what I want. It is again trivial to use a Lambda function to make the request - see this [short and sweet blog post](https://www.outcoldman.com/en/archive/2021/01/21/scheduled-aws-amplify-builds/) which has all the code
you need, and then all that needs doing is to have the Lambda be triggered regularly, which can be done using Cloudwatch Events running on cron expressions.

Despite having a few moving parts, this is all super straightforward, and a big part of the selling point of AWS. Now all I have to do is write four more blog posts this evening and then check that the auto-poster works tomorrow morning before I leave. Hopefully I'm on to
a winner.
