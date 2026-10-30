"""Fetch Marina's EggHaven posts from Substack into data/egghaven_marina.json.

Run at build time (see amplify.yml) before `hugo`. Hugo reads the JSON file as
site.Data.egghaven_marina and the /egghaven page lists the posts alongside mine.

Substack's archive API returns every post with its tags, so we page through it
and keep the ones tagged `egghaven`. If anything goes wrong (network, Substack
changing its API), the script writes nothing and exits 0: the page then just
lists my posts, and a Substack hiccup never breaks the site build. The JSON
file is gitignored; it only ever exists inside a build.
"""

import json
import os
import sys
import urllib.request

PUBLICATION = "https://emptyswords.substack.com"
TAG_SLUG = "egghaven"
AUTHOR = "Marina"
PAGE_SIZE = 50
MAX_PAGES = 10
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "egghaven_marina.json")


def fetch_archive_page(offset):
    # No sort=new: that ordering can omit a just-published post. main() sorts by date.
    url = f"{PUBLICATION}/api/v1/archive?offset={offset}&limit={PAGE_SIZE}"
    req = urllib.request.Request(url, headers={"User-Agent": "jonnyspicer.com build (EggHaven page)"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def extract_posts(archive):
    """Keep posts tagged TAG_SLUG and reduce them to what the page needs."""
    posts = []
    for post in archive:
        tags = post.get("postTags") or []
        if not any((t.get("slug") or "").lower() == TAG_SLUG for t in tags):
            continue
        url = post.get("canonical_url")
        title = (post.get("title") or "").strip()
        date = post.get("post_date")
        if not (url and title and date):
            continue
        posts.append({
            "title": title,
            "url": url,
            "date": date,
            "subtitle": (post.get("subtitle") or "").strip(),
            "description": (post.get("description") or "").strip(),
            "author": AUTHOR,
            "wordcount": int(post.get("wordcount") or 0),
        })
    return posts


def main():
    posts = []
    try:
        for page in range(MAX_PAGES):
            archive = fetch_archive_page(page * PAGE_SIZE)
            if not archive:
                break
            posts.extend(extract_posts(archive))
            if len(archive) < PAGE_SIZE:
                break
    except Exception as exc:  # noqa: BLE001 - never fail the build over this
        print(f"fetch_egghaven: could not fetch Substack posts ({exc}); skipping Marina's posts", file=sys.stderr)
        return

    posts.sort(key=lambda p: p["date"])
    with open(OUT_PATH, "w") as f:
        json.dump(posts, f, indent=2)
        f.write("\n")
    print(f"fetch_egghaven: wrote {len(posts)} post(s) to {OUT_PATH}")


if __name__ == "__main__":
    main()
