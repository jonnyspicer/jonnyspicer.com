import datetime
from git import Repo

# Thanks Ted
# TODO: make this a bash script...

date = datetime.datetime.now()

repo = Repo('.')
origin = repo.remote('origin')
repo.index.add(all=True)
repo.index.commit(f"dp{date.strftime('%Y%m%d')}")
origin.pull()
origin.push()
