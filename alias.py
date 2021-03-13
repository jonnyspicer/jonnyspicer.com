import os
from glob import glob
from pathlib import Path

dir = "content/blog"

posts = glob(dir + '/**/*.*', recursive=True)

for post in posts:
    filename = os.fsdecode(post)[21:].split('.')
    with open(post, 'r') as file:
        text = file.read()
    if "Featured" in text[1]:
        alias = "---\naliases:\n- /tartarus/" + \
            filename[0][:10].replace('-', '/') + "/" + filename[0][11:]
    else:
        alias = "---\naliases:\n- /mendokusai/" + \
            filename[0][:10].replace('-', '/') + "/" + filename[0][11:]
    text = text.replace("---", alias, 1)
    with open(post, 'w') as file:
        file.write(text)
