# for file in files
# get file name
# get front matter
# parse date
# add alias

import os
from glob import glob
from pathlib import Path

dir = "content/blog"

posts = glob(dir + '/**/*.*', recursive=True)

for post in posts:
    filename = os.fsdecode(post)[21:].split('.')
    with open(post, 'r') as file:
        text = file.read()
        text = text.split('---', 2)
        if "Featured" in text[1]:
            print(text[1])
