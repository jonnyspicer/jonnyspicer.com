"""
This script will do the following:
- Check to see if a post has been published today.
- If not, then it will post one.
"""

import urllib.request
import bs4 as bs
import datetime
import os
from git import Repo
from pathlib import Path

Path = Path('.')


def posted_today():
    """
    See if sites rss feed has a post with today's date
    :return: Boolean
    """
    today_date = datetime.date.today()
    # TODO: make this take an env variable
    resp = urllib.request.urlopen("https://jonnyspicer.com/index.xml").read()
    soup = bs.BeautifulSoup(resp, "lxml")
    publish_date_nodes = soup.find_all('pubdate')
    for date in publish_date_nodes:
        publish_date = datetime.datetime.strptime(date.text, '%a, %d %b %Y %H:%M:%S %z').date()
        if publish_date == today_date:
            return True

    return False


def publish_post():
    """
    Pushes a new post
    :return: No return
    """
    date = datetime.datetime.now()

    repo = Repo('.')
    origin = repo.remote('origin')
    repo.git.add(all=True)
    repo.index.commit(f"dp{date.strftime('%y%m%d')}")
    origin.pull()
    origin.push()


def choose_draft():
    drafts = [x for x in (Path / 'content/draft/queued/').iterdir()]

    return drafts[0]


def format_draft():
    date = datetime.datetime.now()

    with open(draft_to_publish, 'r') as draft:
        file = draft.read()
        date_string = '---\ndate: \"' + date.strftime('%Y-%m-%d') + 'T' + date.strftime('%H:%M:%S') + 'Z\"'
        insert = date_string + '\ntype: blog'
        post_file = file.replace("---", insert, 1)

    yearPath = os.getcwd() + '/content/blog/' + str(date.year) + '/'

    if not os.path.exists(yearPath):
        os.mkdir(yearPath)

    if date.month < 10:
        monthPath = yearPath + '0' + str(date.month) + '/'
    else:
        monthPath = yearPath + str(date.month) + '/'

    if not os.path.exists(monthPath):
        os.mkdir(monthPath)

    path = monthPath + date.strftime('%Y-%m-%d') + \
        '-' + draft_to_publish.name
    if not os.path.exists(path):
        open(path, 'w')

    if os.path.exists(path):
        f = open(path, 'a')
        f.write(post_file)


draft_to_publish = choose_draft()

if __name__ == '__main__' and not posted_today():
    format_draft()
    publish_post()
    print('Backup published')
