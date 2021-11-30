---
type: blog
date: "2021-03-20T14:17:14Z"
author: Jonny Spicer
title: "Old Site, New Home II: New Stuff"
categories:
- Blogging
- Programming
series: ["Hugo Migration"]
tags:
- AWS
- Amplify
- DevOps
- Python
---
After a week of checking that none of the basics seemed to be on fire after my migration to Hugo and AWS Amplify, today I had the chance to begin playing around with some of the CI/CD actions
I mentioned in my previous post. I started off by trying to get a Python script to run during
the Amplify build pipeline - the wordcount script that you can see [here.](https://github.com/jonnyspicer/jonnyspicer.com/blob/main/wordcount.py) It's a bit of a mess right now, but when executed it will loop through all my posts, count how many words there are, and then update the homepage
with both the post count and the word count. I am quite confident that the word count it generates
is more accurate than Hugo's built-in ```Page.FuzzyWordCount```, but it does mean that I've
lost about 50,000 words simply by counting them more accurately.

There are two options for running a Python script during an Amplify build; either to use a
different build image with Python pre-installed or to install Python and any necessary
dependencies in the build environment every time its run. Given I have virtually no experience with Docker
I ruled out with the first option, and went for the second one, with the obvious drawback of
slower build times. My ```amplify.yml``` looks as follows:

```yml
version: 1
build:
  phases:
    preBuild:
      commands:
        - export BASE_PATH=$(pwd)
        - yum install -y gcc openssl-devel bzip2-devel libffi-devel python3.8-pip
        - cd /opt && wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
        - cd /opt && tar xzf Python-3.8.2.tgz 
        - cd /opt/Python-3.8.2 && ./configure --enable-optimizations
        - cd /opt/Python-3.8.2 && make altinstall
        - pip3.8 install --user pipenv
        - ln -fs /usr/local/bin/python3.8 /usr/bin/python3
        - ln -fs /usr/local/bin/pip3.8 /usr/bin/pip3
        - cd $BASE_PATH
frontend:
  phases:
    build:
      commands:
        - python3.8 -m pip install --user beautifulsoup4
        - python3.8 wordcount.py
        - hugo
  artifacts:
    baseDirectory: public
    files:
      - '**/*'
  cache:
    paths: []
```

As you can see, Python is installed in the build stage and then the script is executed
before Hugo is built. In the repo the variables for post count and word count are always 0;
they are only ever populated before the build by AWS.

The next thing I wanted to do was to get a safety net setup in case I forget to write a post one
day, akin to Ted's [backup_poster.py script](https://github.com/sted9000/sted9000.github.io/blob/master/backup_poster.py) which I edited to work with my own repo.
You can see my version [here.](https://github.com/jonnyspicer/jonnyspicer.com/blob/main/safety_net.py) The script will:

- Parse this site's [RSS feed,](/index.xml)
- Try to find an item with a ```pubdate``` of today
- If it can't, look for a draft in ```/content/drafts/queued```
- If it finds one, read it, then write the content with an updated date into the correct post directory, using mostly the same code as the ```new.py``` script.

At the moment this is on a cron that runs at 23:30 every day
utilizing GitHub Actions. This is how the workflow looks:

```yml
name: safety_net

on:
  schedule:
        - cron: "30 23 * * *" #runs at 23:30 UTC everyday

  # Allows a workflow to be run manually from the Actions tab
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: checkout repo content
        uses: actions/checkout@v2
      
      - name: setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Run a multi-line script
        run: |
          python safety_net.py
```

Obvious this means I have now split my pipeline into two, across two separate
platforms, which is... bad. I will move the cron from GitHub to AWS at some
point, it was just easier to it get setup on GitHub while that's where I'm
hosting the code. As far as I know the best way to run it on AWS will be to use a
Lambda function hooked up to a CloudWatch alarm which fires at regular intervals,
like a cron, however this approach seems like a lot of effort.

Once I do move it across though, I plan to get another cron setup to email me
at a certain time in the evening to remind me if I haven't written a post
yet. Amplify has a very convenient out-of-the-box feature to get emails about
build status updates, but under the hood all it is doing is creating an SNS
topic that you can subscribe to. I plan to have a Lambda fire at say 20:00 daily,
and publish a new event to the same SNS topic if there is no new post to be found.

There are plenty more cool DevOps features I want to build in the future, but I
am very happy with the start I've made so far.
