import datetime
from git import Repo

# Thanks Ted
# TODO: add steps to:
# - test build and send generated html files to validator
# - send last post text to spellcheck api

date = datetime.datetime.now()

repo = Repo('.')
origin = repo.remote('origin')
repo.git.add(all=True)
repo.index.commit(f"dp{date.strftime('%y%m%d')}")
origin.pull()
origin.push()
