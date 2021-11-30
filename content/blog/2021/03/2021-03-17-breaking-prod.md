---
type: blog
date: "2021-03-17T16:39:31Z"
author: Jonny Spicer
title: Breaking Prod
categories:
- Programming
tags:
- Perl
- Bugs
- Incidents
extras: prismjs
---
Breaking prod can seem like every developer's worst nightmare, the one scenario that must be avoided at all costs. The whole point of code reviews, pull requests, test suites and
staging environments is to stop you from breaking prod, and we all put a huge amount of effort into those things, which implies that maintaining the unbrokenness of prod is a very
high priority to your entire team & organisation.

Anyway I broke prod yesterday, at my Big Serious Technology Company. The errant code I'd authored, once deployed, resulted in a priority one incident - one being the highest possible
priority rather than the lowest. I caused my colleagues a lot of stress in the process as they rushed to try to work out what was on fire, why it was on fire, and finally how to put
the fire out.

Fortunately, my Big Serious Technology Company has a very mature process for dealing with incidents like these, and nobody actually blamed me for anything (the code had also passed
unit tests & code review). The fire was put out, a couple of hours after it'd ignited, with minimal damage caused. Those interim hours were unpleasant for me, but important. Breaking
prod is a rite of passage at any new company. If you are unnecessarily terrified of it then your work will be slow, uninnovative and unfulfilling, and it's important to learn the
lesson that making mistakes is OK, that they can be rectified.

As it turns out, the issue was to due to me expecting Perl to do something very different when accessing properties of objects:

```perl
# Say we have an object:
my $foo = {
        bar => "bar"
    };

# And then we try to read a property on the object
# that doesn't exist:
my $oof = $foo->{'level_1'}->{'level_2'};

# We might anticipate the following to be true:
$oof == undefined;

# And if you didn't know any better, like me until 
# yesterday, you'd probably also anticipate that...
$foo == {
    bar => "bar"
};

# ... However you'd be wrong. The following is true:
$foo == {
    bar => "bar"
    level_1 => {}
};

# Because when we try to access level_2 which
# doesn't exist, Perl creates an empty level_1
# on the original object. This can obviously
# cause problems if you, like me, assume you're
# not manipulating the original object. 
```

This behaviour is similar to the [observer effect,](https://en.wikipedia.org/wiki/Observer_effect_(physics)) meaning it can cause, as one of my colleagues so wonderfully put it... a
Heisenbug.

I'm not exactly glad that I managed to cause the incident yesterday, but I am certainly glad that I got the experience of breaking prod out of the way relatively early on, before it
became a monkey on my back. I also learned a lot about Perl, about not taking language behaviour for granted and about incident management. But most importantly, now I've broken
prod, I feel like I'm a fully fledged part of my team, and I can start to feel at home.
