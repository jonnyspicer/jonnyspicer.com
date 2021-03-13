---
type: blog
date: "2021-03-13T00:00:00Z"
author: Jonny Spicer
title: Old Site, New Home
categories:
- Blogging
- Software Development
tags:
- Hugo
- AWS
- Amplify
- Go
- Frontend
---
The site looks largely the same, but under the hood there have been some very big changes. There have been some more visible changes too, for example you can now [browse by series](/series) or bookmark [this url](/blog/latest) which will always show the latest blog post. Other than some minor cosmetic changes, everything else should be pretty much the same to
anybody visiting the site.

For me as a developer though, I'm very excited about what's new; the site was previously written using [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages,](https://pages.github.com/) and now it's written with [Hugo](https://gohugo.io/) and hosted on [AWS Amplify.](https://aws.amazon.com/amplify/) I made some quality of life improvements
in the migration, most notably merging my two blogs into one with a proper time-based directory structure, meaning I no longer have 900-odd files in a single ```/_posts/``` folder.
I've also got a proper taxonomy system in place with categories, series and tags, something I never got working out of the box with Jekyll, the consensus being that its "collections"
aren't great anyway. The site now takes around 5 seconds to build from a cold start, as opposed to a brutal 100+ seconds on Jekyll, which made live-reloading pointless and any
attempts at meaningful development frustrating to the point of impossibility. Hugo isn't just faster than Jekyll though, it's also more powerful and feature-rich, and while I feel
like I have made a decent first exploration of what's possible with Hugo, in the future I plan on digging deeper to see what else I could use it for on this site.

Hosting on AWS brings with it so opportunities for feature expansion and development too. It is worth noting that I am now paying something for hosting, which I wasn't previously with
GitHub Pages, but by my back-of-the-napkin maths, my bill for Amplify will be less than $0.01/month, which I think I can live with. I can see requests related to server-side metrics,
so I at least have *some* idea of how many people are visiting my site, as I still don't have any kind of client-side analytics, and I plan to keep it that way. The CI/CD options are
largely the same as with GitHub, but the thing I am especially excited for is being able to have other services integrate with the site - for example, a CloudWatch alarm that fires
a lambda function at a certain time every day, which checks to see if there is a new post on the site, raising an event to an SNS topic if there isn't, which then emails me to let me
know. Or even a lambda that simply posts for me. There are a million other possibilities with the AWS serverless stack, the only limiting factor is making sure that they don't end up
costing me a fortune in the meantime.

Even if it's virtually the same on the face of it, I'm extremely pleased with the new site, and I've put a lot of hard work into it. Please let me know if you find anything that's
broken, or if you have any feedback/suggestions for future development.
