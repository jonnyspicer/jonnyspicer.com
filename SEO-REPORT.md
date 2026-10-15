# SEO report: jonnyspicer.com

_14 October 2026 · branch `seo-improvements` · one commit per section (1, 2, 3, 6), so each can be reverted on its own._

## TL;DR

- **Nothing was blocking crawlers.** `robots.txt` was just `User-agent: *` with no sitemap line. It now explicitly welcomes search engines and AI search/retrieval crawlers and points at the sitemap.
- **The sitemap had a lot of noise (1,584 URLs). It now lists only the 1,399 indexable pages.** Before, it included 111 series pages, every tag and category page, and the `/draft/` section, which was publicly live. It also claimed that 888 posts were all last modified on 2021-03-13.
- **Head metadata was rewritten from scratch.** Titles, descriptions, canonicals and OG/Twitter tags each come from one source now. The old head emitted duplicate OG tags, 10-word descriptions and a broken feed link.
- **JSON-LD is new.** There's a Person (you) on every page and BlogPosting/Article on all 1,379 posts and essays, and it's valid JSON on every built page.
- **The biggest remaining SEO lever is content, not code.** 1,003 of 1,379 posts are under 300 words, 1,209 have no inbound links from other posts, and none of the posts has a hand-written description. Sections 4 and 5 below are the to-do list.

## Site overview

| | |
|---|---|
| Generator | Hugo 0.128.1 extended, with no theme (all layouts are in the repo) |
| Templates | `_default/baseof.html` pulls in the `head`, `header`, `footer` and `scripts` partials. Per-section layouts: `blog/`, `essay/`, `garden/`, `static/`, `archive/`, `taxonomy/` |
| Content | 1,376 blog posts (`content/blog/YYYY/MM/`, a mix of `.md` and imported WordPress/Blogger `.html`), 3 essays, 12 garden pages, about 10 standalone pages |
| Build/deploy | AWS Amplify (`amplify.yml`): `wordcount.py` → `hugo` → `generate_navbar.py`. Amplify pins `VERSION_HUGO=0.128.1`, and every change was built and tested on that version |
| Hosting/DNS | **CloudFront (Amplify) with Route53 DNS. The site is not behind Cloudflare.** See the checklist at the end |

## What changed

### 1. Crawlability (`SEO 1` commit)
- **`layouts/robots.txt`** (new). One group allows `*` plus Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, GPTBot, PerplexityBot, ClaudeBot, Claude-SearchBot, Claude-User, Google-Extended and Applebot, followed by `Sitemap: https://jonnyspicer.com/sitemap.xml`. Nothing was being blocked before. The named list documents your intent and guards against any future `Disallow` on `*` silently applying to AI crawlers.
- **`layouts/_default/sitemap.xml`** (new). Includes only HTML pages of kind home, section or page. Excludes taxonomy and term pages (categories, tags, series), drafts, anything with `noindex: true` or `sitemap: {disable: true}`, `/blog/latest/` and the navbar JS. The homepage `lastmod` is the newest post's date. Pagination pages were never in it, and they no longer exist (see section 2).
- **`content/draft/_index.md`** (new). It cascades `build: {render: never, list: never}`, so the drafts folder is never published. Before this, `/draft/` and `/draft/queued/oops/` were live.
- **`config.yaml`**:
  - `frontmatter.lastmod: [lastmod, date]`. Lastmod now comes from explicit front matter and falls back to the publish date. Git commit dates were misleading because bulk edits stamped 888 posts as "updated 13 March 2021", and Google ignores `lastmod` site-wide once it looks unreliable.
    - ⚠️ **Visible side effect:** the "updated …" line in the post metadata now only appears when a post has a `lastmod:` in its front matter. Add one when you substantively revise a post or essay. The essays especially, since they're "updated regularly".
  - `services.rss.limit: 50`. Feeds were the entire ~1,400-post archive (600 KB). Feed readers keep their own history, and the sitemap covers discovery.
  - Removed `cannonifyURLs`. It was misspelt and had never done anything.
- **Feed `<link>`.** Every page now advertises the site feed (`/index.xml`). Section and term pages also advertise their own feed. The old tag had an empty `href`.

### 2. Per-page metadata (`SEO 2` commit)
- **`head.html` rewritten** around three helper partials in `layouts/partials/seo/` (`title.html`, `description.html`, `canonical.html`), which the meta, OG, Twitter and JSON-LD tags all share.
- **Title:** `Post Title | Jonny Spicer`. The homepage is just `Jonny Spicer` (it was `Home | Jonny Spicer`).
- **Description:** front-matter `description`, then `summary`, then a cleaned plain-text excerpt of about 155 characters (HTML stripped, entities decoded, whitespace collapsed, cut at a word boundary with "…"). It was previously a raw 10-word `.Summary`. Tag, category and series pages get generated text such as "Posts by Jonny Spicer tagged "Go"."
  - **None of the 1,376 blog posts has an explicit `description:`/`summary:`.** All of them use the excerpt. The excerpt is fine for most posts, but posts that open with a quote, an image caption or an aside get a poor snippet. "Chesterton's Fence…" is one example: its description is the Chesterton quote. Writing descriptions for the 20–30 posts you most want found is high-value, ten-minute work.
- **Canonical:** an absolute, https, self-referencing URL with a trailing slash on every page. `/blog/latest/` canonicalises to the actual newest post, since it's a duplicate of it.
- **OG/Twitter:** one clean set (`og:title/description/url/image/type/site_name/locale`, `article:published_time/modified_time/author/section/tag` on posts, and a `summary_large_image` card). The default image is `/img/og.png` (1200×630); a post can override it with `image:` in front matter. Removed: duplicate `og:type`, `og:locale`, `og:site_name` and `published_time` tags (Hugo's internal templates plus hand-written copies), the author rendered as "Jonny spicer", GitHub given as `article:publisher`, and invalid head microdata.
- **`<html lang="en-GB">`** and `og:locale` `en_GB`.
- **Blog index:** the `/blog/` template called `.Paginator 5` but never rendered pager links. Hugo was generating **276 unlinked `/blog/page/N/` duplicates**, all titled "Blog | Jonny Spicer" with a canonical pointing back to `/blog/`. It now uses `first 5`, and the page looks the same.

### 3. Structured data (`SEO 3` commit)
- `layouts/partials/seo/jsonld.html` outputs a single `@graph`:
  - **Person** on every page: `@id: https://jonnyspicer.com/#person`, name, url, image (`/img/profile.jpg`), description, and `sameAs` from `params.sameAs`.
  - **WebSite** on the homepage.
  - **BlogPosting** on blog posts and **Article** on essays: headline, description, datePublished, dateModified, author and publisher (both a `{"@id": …#person}` reference), url, mainEntityOfPage, image, inLanguage, wordCount and keywords (categories and tags).
- It's built with `dict` and `jsonify`, so it is always well-formed. I validated it on **all 1,581 built HTML pages: 0 parse errors** (1,376 BlogPosting, 3 Article, 1 WebSite).

### 6. Performance (`SEO 6` commit)
- `layouts/partials/content-images.html` post-processes rendered content on blog, essay, static and garden pages. It adds `loading="lazy" decoding="async"` to any `<img>` that has no `loading` attribute, and intrinsic `width`/`height` (read with `imageConfig`) to local `/img/…` files. This covers raw HTML `<img>`, `<figure>` blocks and Markdown images. The About page's profile photo is left eager because it's above the fold.
- `img { height: auto }` in `_general.scss`, so the new attributes keep aspect ratio under the existing fixed-width image CSS.
- `preconnect` to `fonts.googleapis.com` and `fonts.gstatic.com`.

**Not done (bigger, or your call):**
| Item | Why it matters | Suggested fix |
|---|---|---|
| `hit_da_bricks.png` (1.2 MB) and `1920px-Rembrandt…jpg` (947 KB) in *Auf Wiedersehen, EA II* | Over 2 MB of images on one post | Re-export at about 1200 px wide as WebP/JPEG at quality 80, or move them to `assets/` and use Hugo `.Resize` |
| `profile.jpg` is 1574×2100 (248 KB) but displayed at 200×200 on /about | It's the About page's LCP image | Move it to `assets/img/` and render with `.Fill "400x400 webp"` |
| `og.png` is 452 KB | It's fetched by every social and link-preview crawler | Recompress to under 150 KB |
| Cloudflare Web Analytics beacon in `baseof.html` and `chat/baseof.html` | A second third-party analytics script on every page alongside Umami | Remove it if you're not using it |
| `global.js` and `footnotes.js` aren't minified or fingerprinted | They're small, and they load at the end of `<body>`, so they don't block rendering | Optional: `\| minify \| fingerprint`, like `read-depth.js` already is |
| Google Fonts stylesheet blocks rendering | It's small, with `display=swap` and now preconnect | Optional: self-host the two fonts |

## Placeholders to fill in

All of these are in `config.yaml` → `params.sameAs`. Empty strings are skipped in the output. I pre-filled the profiles I found linked from /about and in the existing config:

| Profile | Current value | Status |
|---|---|---|
| Substack | `https://heresjonny.substack.com` | Found on /about; check it |
| LessWrong | `https://www.lesswrong.com/users/jonny-spicer` | Done |
| Twitter/X | `https://twitter.com/jjspicer` | From the old `params.twitter`; **check it's still your handle** (an `x.com` URL is fine too) |
| GitHub | `https://github.com/jonnyspicer` | Linked on /about |
| LinkedIn | `https://www.linkedin.com/in/jonnyspicer` | Linked on /about |
| _(optional)_ EA Forum | n/a | Worth adding given the EA posts |

Also consider:
- `params.personImage` (`/img/profile.jpg`) is the image used in the Person schema.
- `params.description` ("…founder, software engineer, blogger, runner…") is the Person description. AI answer engines often quote it, so make sure it says what you want to be known for.

## 4. Topic clusters, hubs and orphans (report only)

### Clusters
By category volume, the blog is mostly a 2017–2021 daily journal: Personal (267), Wellbeing (157), Mental Health (156), Misc (130), Programming (75), Music (68) and Running (66). For the topics you flagged:

| Topic | Posts of 300+ words | Assessment |
|---|---|---|
| **Software engineering and career** | about 35 | **Strong.** Long, practical posts (job hunting, career retrospective, Advent of Code, LeetCode, C). The `/software/` essay is a 215-word outline that could become the hub. |
| **Effective altruism** | 9 core posts | **Strong and coherent.** It's a narrative arc from 80,000 Hours (2022) through community building to leaving EA (2025–26). |
| **AI / AI safety** | 5 (plus the `/ai/` essay) | **Thin, but it has a hub already.** The `/ai/` essay (3,483 words) is evergreen and comprehensive, yet it links to nothing but /contact. Posts: *Concrete Ways I Use AI*, *Why Hasn't ChatGPT Fixed My Eating Disorder?*, *10 Things I Don't Know But Want To*, *What I've Got Wrong and Right In My Career*. There's no dedicated AI-safety post on the blog. |
| **Forecasting / forecast evaluation** | about 0 | **There isn't a cluster.** Only *Map and Territory: Predictably Wrong* (rationality) and a 2019 marathon-predictions post touch on it, plus a mention in the hyperkaehler garden page. Your forecasting work (Fatebook tooling, prediction scoring) isn't represented on the site. If you want to be found for it, the fix is a few posts or a garden/essay page, not a hub. |
| _Also strong:_ **mental health** | about 20 long posts | Arguably the site's best and most distinctive cluster, so it's included as hub 3. |

### Proposed hubs

Each hub could be a new essay (`content/essay/…`) or, for software, the existing `/software/` essay expanded. Hubs help both kinds of search: Google gets topical structure and internal links, and AI answer engines get one citable page that summarises your position and links to the evidence.

#### Hub 1: "Software Engineering, Self-Taught": expand `/software/`
> I came to software sideways, via a couple of years as a (self-described "allegedly") professional poker player and a junior web-dev job in 2018. Since then I've worked at AWS, at an EA non-profit and as a freelancer, mostly on AI projects. This page collects what I've written about learning to program, getting hired, doing the job well, and how I expect AI to change the work, roughly in the order I'd suggest reading it.

1. [The Dream is Dead II](https://jonnyspicer.com/blog/the-dream-is-dead-ii/) (2018): leaving poker for code
2. [What I Learned From Applying To 100 Programming Jobs](https://jonnyspicer.com/blog/what-i-learned-from-applying-to-100-programming-jobs/) (2022)
3. [What I've Got Wrong and Right In My Career](https://jonnyspicer.com/blog/what-ive-got-wrong-and-right-in-my-career/) (2024)
4. [Enacting Equilibrium With Your Extremely Efficient Employer](https://jonnyspicer.com/blog/enacting-equilibrium-with-your-extremely-efficient-employer/) (2023)
5. [Think Deeply About Simple Things](https://jonnyspicer.com/blog/think-deeply-about-simple-things/) (2020)
6. [Evolution vs Design in Software](https://jonnyspicer.com/blog/evolution-vs-design-in-software/) (2019)
7. [Breaking Prod](https://jonnyspicer.com/blog/breaking-prod/) (2021)
8. [Mentoring](https://jonnyspicer.com/blog/mentoring/) and [Mentoring II](https://jonnyspicer.com/blog/mentoring-ii/) (2021)
9. [Becoming a Better Programmer: Adventures in C](https://jonnyspicer.com/blog/becoming-a-better-programmer-adventures-in-c/) (2023)
10. [Concrete Ways I Use AI](https://jonnyspicer.com/blog/concrete-ways-i-use-ai/) (2024)
11. Practice: [30 Days of LeetCode 1–5](https://jonnyspicer.com/blog/30-days-of-leetcode-days-1-to-5/), [6–10](https://jonnyspicer.com/blog/30-days-of-leetcode-days-6-to-10/); [Advent of Code](https://jonnyspicer.com/blog/advent-of-code/) [II](https://jonnyspicer.com/blog/advent-of-code-ii/) [III](https://jonnyspicer.com/blog/advent-of-code-iii/) [IV](https://jonnyspicer.com/blog/advent-of-code-iv/) [V](https://jonnyspicer.com/blog/advent-of-code-v/) [VI](https://jonnyspicer.com/blog/advent-of-code-vi/) (2021)
12. Side projects: [Chess Programming](https://jonnyspicer.com/blog/chess-programming/) (2020), [Old Site, New Home](https://jonnyspicer.com/blog/old-site-new-home/) and [II](https://jonnyspicer.com/blog/old-site-new-home-ii-new-stuff/) (2021), [ZSA Voyager Review](https://jonnyspicer.com/blog/zsa-voyager-review/) (2024)

#### Hub 2: "Effective Altruism: In and Out"
> For about four years effective altruism shaped my career, my giving and my social life: 80,000 Hours coaching, EAG conferences, running a local group and taking the Giving What We Can pledge. I then stepped back, for reasons I've tried to explain carefully and without bitterness. These posts are the record of that arc, in order, for anyone weighing up the movement for themselves.

1. [80000 Hours Career Planning I: The Beginning](https://jonnyspicer.com/blog/80000-hours-career-planning-i-the-beginning/) (Feb 2022)
2. [80000 Hours II: Personal Priorities and Pressing Issues](https://jonnyspicer.com/blog/80000-hours-ii-personal-priorities-and-pressing-issues/) (Feb 2022)
3. [On Doing The Most Good](https://jonnyspicer.com/blog/on-doing-the-most-good/) (Dec 2022)
4. [Reflections following EAG London](https://jonnyspicer.com/blog/reflections-following-eag-london-conference-strategy-and-in/outgroup-dynamics/) (May 2023)
5. [Giving What I Can](https://jonnyspicer.com/blog/giving-what-i-can/) (Nov 2023)
6. [What I Learned In My First Year of Community Building](https://jonnyspicer.com/blog/what-i-learned-in-my-first-year-of-community-building/) (Dec 2023)
7. [What I've Got Wrong and Right In My Career](https://jonnyspicer.com/blog/what-ive-got-wrong-and-right-in-my-career/) (Jul 2024): the EA-job chapter
8. [Auf Wiedersehen, Effective Altruism](https://jonnyspicer.com/blog/auf-wiedersehen-effective-altruism/) (Nov 2025)
9. [Auf Wiedersehen, Effective Altruism II: Wir Sehen Uns Wieder](https://jonnyspicer.com/blog/auf-wiedersehen-effective-altruism-ii-wir-sehen-uns-wieder/) (Apr 2026)
10. Related: [the AI essay](https://jonnyspicer.com/blog/ai/)

#### Hub 3: "Mental Health: What Has Actually Helped"
> I've written publicly about depression, disordered eating and borderline personality disorder since 2017, partly to keep myself honest and partly because reading other people's accounts helped me. This is the shortlist of what I'd want someone in a bad place to read first, followed by the longer reflections.

1. [30 things to try before you try suicide](https://jonnyspicer.com/blog/30-things-to-try-before-you-try-suicide/) (2025)
2. [Mental Health in Public](https://jonnyspicer.com/blog/mental-health-in-public/) (2020)
3. [The Happiness Project](https://jonnyspicer.com/blog/the-happiness-project/) (2021)
4. [Eating](https://jonnyspicer.com/blog/eating/) (2022)
5. [Beyond Borderline](https://jonnyspicer.com/blog/beyond-borderline/) (2022)
6. [Is Meditation Magic?](https://jonnyspicer.com/blog/is-meditation-magic/) (2023)
7. [On 30](https://jonnyspicer.com/blog/on-30/) (2024)
8. [Suffering on the Margin](https://jonnyspicer.com/blog/suffering-on-the-margin/) (2026)
9. [How to Draw an Owl](https://jonnyspicer.com/blog/how-to-draw-an-owl/) (2026)
10. [Why Hasn't ChatGPT Fixed My Eating Disorder?](https://jonnyspicer.com/blog/why-hasnt-chatgpt-fixed-my-eating-disorder/) (2026)
11. [Chesterton's Fence as a core concept in psychology](https://jonnyspicer.com/blog/chestertons-fence-as-a-core-concept-in-psychology/) (2026)
12. Series: [Things That Are More Therapeutic Than Therapy](https://jonnyspicer.com/blog/things-that-are-more-therapeutic-than-therapy-running/) (14 parts, 2020–21; see the merge suggestion in section 5)

**AI, cheaply:** you don't need a new hub. Add a short "Related writing" list to the end of the AI post (`/blog/ai/`, formerly the `/ai/` essay) that links the four AI posts above, and link it back from each of them.

### Orphans
1209 of 1379 posts have no contextual inbound link from another post or page (they're reachable only via /archive/, category pages, prev/next and the sitemap). 114 of those are 500+ words; the 47 that are 800+ words are listed below, longest first.

The highest-value fixes are linking these from the hubs above, from `/bestof/`, or from newer posts on the same topic.

| Post | Date | Words | Category |
|---|---|--:|---|
| [2023 in Review](https://jonnyspicer.com/blog/2023-in-review/) | 2023-12-29 | 4,772 | Personal |
| [AI](https://jonnyspicer.com/blog/ai/) | 2024-05-07 | 3,483 |  |
| [10 Things I Don't Know But Want To](https://jonnyspicer.com/blog/10-things-i-dont-know-but-want-to/) | 2026-01-20 | 2,713 | AI, Aliens, Blogging, Mental Health, Programming |
| [Becoming a Better Programmer: Adventures in C](https://jonnyspicer.com/blog/becoming-a-better-programmer-adventures-in-c/) | 2023-12-27 | 2,593 | Programming |
| [What I Learned In My First Year of Community Building](https://jonnyspicer.com/blog/what-i-learned-in-my-first-year-of-community-building/) | 2023-12-28 | 2,203 | Effective Altruism |
| [Gamer Culture](https://jonnyspicer.com/blog/gamer-culture/) | 2020-06-23 | 2,117 | Esports, Feminism, Allyship |
| [Bottled Feelings](https://jonnyspicer.com/blog/bottled-feelings/) | 2026-05-05 | 2,052 | Fiction |
| [Social Responsibility](https://jonnyspicer.com/blog/social-responsibility/) | 2020-06-01 | 1,986 | Allyship |
| [Advent of Code IV](https://jonnyspicer.com/blog/advent-of-code-iv/) | 2021-12-09 | 1,890 | Programming |
| [How to Draw an Owl](https://jonnyspicer.com/blog/how-to-draw-an-owl/) | 2026-05-14 | 1,864 | Mental Health |
| [Advent of Code VI](https://jonnyspicer.com/blog/advent-of-code-vi/) | 2021-12-15 | 1,823 | Programming |
| [XNRG Tring Ultra](https://jonnyspicer.com/blog/xnrg-tring-ultra/) | 2021-09-25 | 1,767 | Running |
| [30 Days of Leetcode: Days 1 to 5](https://jonnyspicer.com/blog/30-days-of-leetcode-days-1-to-5/) | 2020-04-05 | 1,689 | Programming |
| [Enacting Equilibrium With Your Extremely Efficient Employer](https://jonnyspicer.com/blog/enacting-equilibrium-with-your-extremely-efficient-employer/) | 2023-03-19 | 1,603 | Career |
| [Movie Reviews II](https://jonnyspicer.com/blog/movie-reviews-ii/) | 2018-02-17 | 1,594 |  |
| [February 2022 Retrospective](https://jonnyspicer.com/blog/february-2022-retrospective/) | 2022-03-01 | 1,556 | Personal |
| [30 Days of Leetcode: Days 6 to 10](https://jonnyspicer.com/blog/30-days-of-leetcode-days-6-to-10/) | 2020-04-10 | 1,519 | Programming |
| [2022 Goals](https://jonnyspicer.com/blog/2022-goals/) | 2021-12-31 | 1,512 | Personal, Bestof |
| [Experiences with Jekyll](https://jonnyspicer.com/blog/experiences-with-jekyll/) | 2018-10-20 | 1,508 | Programming, Blogging |
| [Mosh](https://jonnyspicer.com/blog/mosh/) | 2026-09-09 | 1,486 | Music, Guest Blogs |
| [Vir Esto](https://jonnyspicer.com/blog/vir-esto/) | 2018-02-19 | 1,462 |  |
| [Siddhartha and Me](https://jonnyspicer.com/blog/siddhartha-and-me/) | 2017-08-23 | 1,457 | Meditation and Spirituality, Mental Health |
| [Useless Skills](https://jonnyspicer.com/blog/useless-skills/) | 2018-02-24 | 1,441 |  |
| [Reflections following EAG London: Conference Strategy and In/Outgroup Dynamics](https://jonnyspicer.com/blog/reflections-following-eag-london-conference-strategy-and-in/outgroup-dynamics/) | 2023-05-29 | 1,414 | Effective Altruism |
| [Some Thoughts About Tattoos](https://jonnyspicer.com/blog/some-thoughts-about-tattoos/) | 2022-01-31 | 1,365 | Personal, Art |
| [Advent of Code V](https://jonnyspicer.com/blog/advent-of-code-v/) | 2021-12-13 | 1,337 | Programming |
| [What I learned from giving up porn - or at least trying to.](https://jonnyspicer.com/blog/what-i-learned-from-giving-up-porn-or-at-least-trying-to./) | 2017-02-22 | 1,329 |  |
| [Man vs Food: Whiny Emo Edition](https://jonnyspicer.com/blog/man-vs-food-whiny-emo-edition/) | 2018-06-14 | 1,273 | Mental Health, Wellbeing, Diet and Fitness |
| [Auf Wiedersehen, Effective Altruism II: Wir Sehen Uns Wieder](https://jonnyspicer.com/blog/auf-wiedersehen-effective-altruism-ii-wir-sehen-uns-wieder/) | 2026-04-14 | 1,244 | Effective Altruism |
| [Beyond Borderline](https://jonnyspicer.com/blog/beyond-borderline/) | 2022-12-04 | 1,226 | Mental Health |
| [Advent of Code II](https://jonnyspicer.com/blog/advent-of-code-ii/) | 2021-12-03 | 1,209 | Programming |
| [It's too late for me - save yourself](https://jonnyspicer.com/blog/its-too-late-for-me-save-yourself/) | 2018-10-03 | 1,131 | Technology, The Web |
| [The Dogbreaker](https://jonnyspicer.com/blog/the-dogbreaker/) | 2021-04-30 | 1,114 | Running |
| [30 things to try before you try suicide](https://jonnyspicer.com/blog/30-things-to-try-before-you-try-suicide/) | 2025-09-02 | 1,096 | Mental Health |
| [Suffering on the Margin](https://jonnyspicer.com/blog/suffering-on-the-margin/) | 2026-03-31 | 1,036 | Mental Health, Personal |
| [Engagement Rings For Dummies](https://jonnyspicer.com/blog/engagement-rings-for-dummies/) | 2025-03-14 | 1,022 | Dating and Relationships |
| [100 Favourite Albums of All Time](https://jonnyspicer.com/blog/100-favourite-albums-of-all-time/) | 2020-01-29 | 1,007 | Music |
| [Reckful](https://jonnyspicer.com/blog/reckful/) | 2020-07-03 | 998 | Mental Health |
| [World Chess Championship 2021 III](https://jonnyspicer.com/blog/world-chess-championship-2021-iii/) | 2021-12-10 | 963 | Chess |
| [2021 Book Reviews VII](https://jonnyspicer.com/blog/2021-book-reviews-vii/) | 2021-07-11 | 926 | Books |
| [Belonging](https://jonnyspicer.com/blog/belonging/) | 2018-11-09 | 863 | Personal, Wellbeing, Mental Health |
| [Personal top 5 moments in esports](https://jonnyspicer.com/blog/personal-top-5-moments-in-esports/) | 2017-10-23 | 863 |  |
| [What do you love about life?](https://jonnyspicer.com/blog/what-do-you-love-about-life/) | 2020-01-15 | 860 | Wellbeing |
| [Borderliner](https://jonnyspicer.com/blog/borderliner/) | 2021-10-14 | 832 | Mental Health |
| [2021 Book Reviews VI](https://jonnyspicer.com/blog/2021-book-reviews-vi/) | 2021-04-18 | 831 | Books |
| [Blog Analysis Part Two: Lexicon](https://jonnyspicer.com/blog/blog-analysis-part-two-lexicon/) | 2020-05-10 | 827 | Blogging |
| [Making a Door Less Open Review](https://jonnyspicer.com/blog/making-a-door-less-open-review/) | 2020-05-05 | 802 | Music |

## 5. Thin content (report only)

1003 of 1379 posts/essays are under 300 words. Suggested: **keep 702**, **merge 29**, **noindex 272**.

How the suggestions were assigned:
- **noindex**: under 100 words, no inbound links and not in Bestof. Most are one-line daily-journal entries, and about 30 are 2017 Spanish-practice posts from Mexico, which also won't rank on an `en-GB` site. *Fuzzy Heuristics and Blurry Lenses* (2025-04-06) has **no body at all**. The file is untracked in git and the URL returns 404, so it isn't live; finish it before committing it.
- **merge**: themed mini-series whose parts are individually thin but would make one substantial evergreen post together. Merge into the earliest post and add the later URLs as `aliases:` so nothing 404s:
- **Choosing What To Think** ← 4 follow-ups, 1,114 words combined (2020–2020)
- **Some More Thoughts About Weight Loss** ← 6 follow-ups, 1,946 words combined (2020–2021)
- **Things That Are More Therapeutic Than Therapy: Running** ← 13 follow-ups, 2,866 words combined (2020–2021)
- **Tower Bridge Lunch Reviews** ← 5 follow-ups, 2,031 words combined (2021–2021)
- **What it Means to be a Man** ← 11 follow-ups, 3,570 words combined (2020–2020)
- **Near-duplicates:** only one real pair. *The Jesse Lacey Problem* and *The Jesse Lacey Problem II* are 94% identical (5-word shingle Jaccard similarity), so merge II into I.
- **keep**: everything else. Short isn't automatically bad, and these are a real journal. But with about 70% of the site under 300 words, Google's site-wide quality signals will weigh on your best posts.

**Low-maintenance way to act on this.** `noindex: true` in front matter already works: it adds `<meta name="robots" content="noindex">` and removes the page from the sitemap. For 272 posts, one rule in `head.html` is less work than editing each file. For example: noindex when `.WordCount < 100`, the post isn't in Bestof, and front matter doesn't say `index: true`. I haven't added this rule, as you asked.

**Update (2026-10-14): applied, using Search Console data instead of word count alone.** At your request, posts under 300 words with **fewer than 10 Google impressions** between 2025-06-15 and 2026-10-13 are now noindexed. That's **765 posts**, listed in `data/seo/noindex.yaml`. `layouts/partials/seo/noindex.html` decides for both `head.html` and the sitemap, which drops from ~1,399 to ~634 URLs. None of the 765 is in Bestof. Two unpublished essays (`/software/`, `/a-good-life/`) were left off the list. Short posts that do get found stay indexed, e.g. *How Many Sheep Crossed the Bridge*, *Taikyoku Shogi* and *Lynx Titan*. Short posts drove 313 of the site's 1,483 clicks in that window, and 188 of them came from those three.

To re-index a post, delete its line from the YAML or set `index: true` in its front matter. New posts aren't on the list, so they're indexed as usual. Refresh the list from Search Console once a year or so.

**Update (2026-10-14): `/ai/` is now a dated blog post at `/blog/ai/`.** It was dated 2024-05-07, with lastmod 2025-01-13, and `/ai/` redirects to it. The Search Console queries showed it wasn't ranking for AI topics: about half its 1,786 impressions came from spam `*.aioblogs.com` lookups and most of the rest from name searches. Keeping it unchanged as a dated snapshot preserves the 2024 predictions as a record. `/essay/` is noindexed until another essay is published. Suggested follow-up: a "Revisiting my 2024 AI predictions" post that links back to it, which would also start the missing forecasting cluster.

**Update (2026-10-14): categories consolidated from 41 to 8.** The new set is Mental Health, AI, Effective Altruism, Career and Technology, Personal Development, Hobbies, Personal and Bestof. The mapping:
- **Mental Health** ← Wellbeing, Meditation and Spirituality
- **Career and Technology** ← Career, Programming, Technology, Computer Science, Hacking and Security, The Web
- **Personal Development** ← Rationality, Diet and Fitness
- **Hobbies** ← Running, Climbing, Chess, Poker and Gambling, Esports, Video Games, Gaming, Music, Film and TV, Books, Art, Food and Drink, Blogging
- **Personal** ← Misc, COVID19, Travel, Social Media, Dating and Relationships, Politics, Feminism, Allyship, Guest Blogs, Fiction, Aliens

Old `/categories/<old>/` URLs redirect to their new category via `aliases` in `content/categories/<new>/_index.md`.

**Expand candidates** (high impressions, page 2, almost no clicks; a few hundred more words could get these onto page 1): *Alexi Laiho* (5,806 impressions, 0 clicks, position 15.5), *An Ode to the Love Shack* (1,802 / 4, "love shack guernsey"), *In the Aeroplane Over the Sea* (1,933 / 1), *Chess Commentators* (571 / 1), *After Life review* (638 / 1), *The Master and Margarita review* (448 / 0).

<details>
<summary><strong>Full table: 1,003 posts under 300 words</strong> (chronological)</summary>

| Title | Date | Words | URL | Suggestion |
|---|---|--:|---|---|
| The Depths of the Blog | 2017-02-20 | 181 | /blog/the-depths-of-the-blog/ | keep |
| What if I had epilepsy? | 2017-03-11 | 253 | /blog/what-if-i-had-epilepsy/ | keep |
| Gambling and catharsis | 2017-10-15 | 181 | /blog/gambling-and-catharsis/ | keep |
| Five Things I've Learned During Five Weeks in Mexico | 2017-10-18 | 102 | /blog/five-things-ive-learned-during-five-weeks-in-mexico/ | keep |
| Ghosts | 2017-10-19 | 99 | /blog/ghosts/ | noindex |
| Balancing the coin | 2017-10-21 | 69 | /blog/balancing-the-coin/ | noindex |
| Joji | 2017-10-22 | 53 | /blog/joji/ | noindex |
| Beware of the dog | 2017-10-24 | 161 | /blog/beware-of-the-dog/ | keep |
| Time | 2017-10-25 | 58 | /blog/time/ | noindex |
| The recipe for success | 2017-10-27 | 66 | /blog/the-recipe-for-success/ | keep |
| Poker sucks | 2017-10-28 | 211 | /blog/poker-sucks/ | keep |
| Bad dreams | 2017-10-29 | 142 | /blog/bad-dreams/ | keep |
| Awful pseudo-deep post about emotions #4713 | 2017-10-30 | 72 | /blog/awful-pseudo-deep-post-about-emotions-%234713/ | noindex |
| Mi | 2017-10-31 | 49 | /blog/mi/ | noindex |
| Failure vs regret | 2017-11-03 | 89 | /blog/failure-vs-regret/ | noindex |
| The type of people who write blogs | 2017-11-04 | 74 | /blog/the-type-of-people-who-write-blogs/ | noindex |
| Variance I | 2017-11-05 | 92 | /blog/variance-i/ | noindex |
| Goals | 2017-11-06 | 157 | /blog/goals/ | keep |
| Ten ideas to make me hate myself for writing a blog less | 2017-11-07 | 128 | /blog/ten-ideas-to-make-me-hate-myself-for-writing-a-blog-less/ | keep |
| Veinte tres | 2017-11-08 | 47 | /blog/veinte-tres/ | noindex |
| Diez cosas he aprendido en Español | 2017-11-09 | 53 | /blog/diez-cosas-he-aprendido-en-espa%C3%B1ol/ | noindex |
| Swiss Army Man | 2017-11-10 | 45 | /blog/swiss-army-man/ | noindex |
| Sábado | 2017-11-11 | 29 | /blog/s%C3%A1bado/ | noindex |
| Mañana | 2017-11-12 | 25 | /blog/ma%C3%B1ana/ | noindex |
| Pesadillas | 2017-11-13 | 35 | /blog/pesadillas/ | noindex |
| Ajedrez | 2017-11-14 | 48 | /blog/ajedrez/ | noindex |
| Una perra pequeña | 2017-11-15 | 38 | /blog/una-perra-peque%C3%B1a/ | noindex |
| La salida más fácil | 2017-11-16 | 54 | /blog/la-salida-m%C3%A1s-f%C3%A1cil/ | noindex |
| Diez cosas sobre mi novia | 2017-11-17 | 66 | /blog/diez-cosas-sobre-mi-novia/ | noindex |
| Trabajo dura | 2017-11-18 | 26 | /blog/trabajo-dura/ | noindex |
| Mi mejor amiga | 2017-11-19 | 24 | /blog/mi-mejor-amiga/ | noindex |
| Corte de pelo | 2017-11-20 | 28 | /blog/corte-de-pelo/ | noindex |
| El sueño | 2017-11-21 | 19 | /blog/el-sue%C3%B1o/ | noindex |
| Mis amigos | 2017-11-22 | 32 | /blog/mis-amigos/ | noindex |
| Mi dia libre | 2017-11-23 | 31 | /blog/mi-dia-libre/ | noindex |
| Mia dia libre II | 2017-11-24 | 31 | /blog/mia-dia-libre-ii/ | noindex |
| Mi amigo Sam | 2017-11-25 | 22 | /blog/mi-amigo-sam/ | noindex |
| El torneo de ajedrez | 2017-11-26 | 42 | /blog/el-torneo-de-ajedrez/ | noindex |
| Volver a trabajo | 2017-11-27 | 19 | /blog/volver-a-trabajo/ | noindex |
| Inspiración | 2017-11-28 | 22 | /blog/inspiraci%C3%B3n/ | noindex |
| El plan para diciembre | 2017-11-29 | 24 | /blog/el-plan-para-diciembre/ | noindex |
| La vida | 2017-11-30 | 20 | /blog/la-vida/ | noindex |
| Tacos nuevos | 2017-12-01 | 46 | /blog/tacos-nuevos/ | noindex |
| Te gusta el jazz, Evan? | 2017-12-02 | 19 | /blog/te-gusta-el-jazz-evan/ | noindex |
| La Amistad | 2017-12-03 | 26 | /blog/la-amistad/ | noindex |
| El ladrón | 2017-12-04 | 23 | /blog/el-ladr%C3%B3n/ | noindex |
| Clásico del ajedrez de Londres | 2017-12-05 | 43 | /blog/cl%C3%A1sico-del-ajedrez-de-londres/ | noindex |
| Tinder en México | 2017-12-06 | 26 | /blog/tinder-en-m%C3%A9xico/ | noindex |
| Mendokusai | 2017-12-07 | 40 | /blog/mendokusai/ | noindex |
| Cryptokitties | 2017-12-08 | 33 | /blog/cryptokitties/ | noindex |
| Cuentos cortos | 2017-12-09 | 20 | /blog/cuentos-cortos/ | noindex |
| Duerme | 2017-12-10 | 11 | /blog/duerme/ | keep |
| Dungeons and Dragons | 2017-12-11 | 123 | /blog/dungeons-and-dragons/ | keep |
| Las pequeñas cosas | 2017-12-12 | 38 | /blog/las-peque%C3%B1as-cosas/ | noindex |
| Mutiny | 2017-12-13 | 28 | /blog/mutiny/ | noindex |
| La gente | 2017-12-14 | 22 | /blog/la-gente/ | noindex |
| La musica | 2017-12-15 | 26 | /blog/la-musica/ | noindex |
| New York | 2017-12-16 | 46 | /blog/new-york/ | noindex |
| Alcohol | 2017-12-17 | 88 | /blog/alcohol/ | noindex |
| Brood War | 2017-12-18 | 99 | /blog/brood-war/ | noindex |
| Productive vacation | 2017-12-19 | 162 | /blog/productive-vacation/ | keep |
| Having a blog | 2017-12-20 | 77 | /blog/having-a-blog/ | noindex |
| _______ of the Year | 2017-12-21 | 160 | /blog/_______-of-the-year/ | keep |
| (Trying to) be a better person | 2017-12-22 | 110 | /blog/trying-to-be-a-better-person/ | keep |
| Liberation | 2017-12-24 | 116 | /blog/liberation/ | keep |
| Steps forwards, backwards and/or sideways | 2017-12-25 | 122 | /blog/steps-forwards-backwards-and/or-sideways/ | keep |
| Ramblings I | 2017-12-26 | 295 | /blog/ramblings-i/ | keep |
| Ramblings II | 2017-12-27 | 49 | /blog/ramblings-ii/ | noindex |
| Ramblings III | 2017-12-28 | 141 | /blog/ramblings-iii/ | keep |
| Ramblings IV | 2017-12-29 | 84 | /blog/ramblings-iv/ | noindex |
| New Year | 2017-12-30 | 52 | /blog/new-year/ | noindex |
| Washing the dishes | 2017-12-31 | 58 | /blog/washing-the-dishes/ | noindex |
| 2018 | 2018-01-01 | 80 | /blog/2018/ | noindex |
| Sugar Pine 7 | 2018-01-04 | 105 | /blog/sugar-pine-7/ | keep |
| Captain's Draft 4.0 | 2018-01-05 | 190 | /blog/captains-draft-4.0/ | keep |
| Passion | 2018-01-06 | 117 | /blog/passion/ | keep |
| Taking things slow | 2018-01-07 | 80 | /blog/taking-things-slow/ | noindex |
| AGDQ | 2018-01-08 | 82 | /blog/agdq/ | noindex |
| Finishing what has been started | 2018-01-09 | 90 | /blog/finishing-what-has-been-started/ | noindex |
| Being a role model | 2018-01-10 | 84 | /blog/being-a-role-model/ | noindex |
| Old School Runescape | 2018-01-11 | 71 | /blog/old-school-runescape/ | noindex |
| Resolutions | 2018-01-12 | 35 | /blog/resolutions/ | noindex |
| Overwatch League | 2018-01-13 | 169 | /blog/overwatch-league/ | keep |
| AGDQ II | 2018-01-14 | 56 | /blog/agdq-ii/ | noindex |
| Blue Monday | 2018-01-15 | 23 | /blog/blue-monday/ | noindex |
| Storms | 2018-01-16 | 39 | /blog/storms/ | noindex |
| Twitter | 2018-01-17 | 44 | /blog/twitter/ | noindex |
| Overwatch League II | 2018-01-18 | 149 | /blog/overwatch-league-ii/ | keep |
| Alcohol II | 2018-01-19 | 27 | /blog/alcohol-ii/ | noindex |
| Alcohol III | 2018-01-20 | 53 | /blog/alcohol-iii/ | noindex |
| Close call | 2018-01-21 | 57 | /blog/close-call/ | noindex |
| Starting again, again (again) | 2018-01-22 | 32 | /blog/starting-again-again-again/ | noindex |
| Running out of ideas | 2018-01-23 | 129 | /blog/running-out-of-ideas/ | keep |
| Shingeki no Kyojin | 2018-01-24 | 78 | /blog/shingeki-no-kyojin/ | noindex |
| Guitar | 2018-01-25 | 66 | /blog/guitar/ | noindex |
| Switching off | 2018-01-26 | 64 | /blog/switching-off/ | noindex |
| Eleague Major | 2018-01-27 | 110 | /blog/eleague-major/ | keep |
| Free money | 2018-01-29 | 47 | /blog/free-money/ | noindex |
| What's the point? | 2018-01-30 | 77 | /blog/whats-the-point/ | noindex |
| GSL | 2018-01-31 | 98 | /blog/gsl/ | noindex |
| The next big freeroll | 2018-02-01 | 66 | /blog/the-next-big-freeroll/ | noindex |
| Day 1 | 2018-02-02 | 68 | /blog/day-1/ | noindex |
| Guitar II | 2018-02-03 | 55 | /blog/guitar-ii/ | noindex |
| Running | 2018-02-04 | 122 | /blog/running/ | keep |
| Dieting | 2018-02-05 | 59 | /blog/dieting/ | noindex |
| Falcon Heavy | 2018-02-06 | 71 | /blog/falcon-heavy/ | noindex |
| Nail Painting | 2018-02-07 | 93 | /blog/nail-painting/ | noindex |
| Tim | 2018-02-08 | 218 | /blog/tim/ | keep |
| Steve Reich | 2018-02-09 | 114 | /blog/steve-reich/ | keep |
| Poker | 2018-02-10 | 102 | /blog/poker/ | keep |
| Hoops | 2018-02-12 | 108 | /blog/hoops/ | keep |
| Things That Go Bump In The Night | 2018-02-14 | 218 | /blog/things-that-go-bump-in-the-night/ | keep |
| Poker II | 2018-02-21 | 53 | /blog/poker-ii/ | noindex |
| Shadow of the Colossus | 2018-02-22 | 68 | /blog/shadow-of-the-colossus/ | noindex |
| Internet Friends | 2018-02-23 | 87 | /blog/internet-friends/ | noindex |
| Things That Go Bump In The Night II | 2018-02-25 | 248 | /blog/things-that-go-bump-in-the-night-ii/ | keep |
| FaceIt Major 2018 | 2018-02-26 | 27 | /blog/faceit-major-2018/ | noindex |
| Snow | 2018-02-27 | 47 | /blog/snow/ | noindex |
| Things That Go Bump in The Night III | 2018-02-28 | 58 | /blog/things-that-go-bump-in-the-night-iii/ | noindex |
| More Poker | 2018-03-01 | 60 | /blog/more-poker/ | noindex |
| Emo Band Coming Soon | 2018-03-02 | 21 | /blog/emo-band-coming-soon/ | noindex |
| Never Hungover Again | 2018-03-03 | 146 | /blog/never-hungover-again/ | keep |
| Another new project | 2018-03-04 | 180 | /blog/another-new-project/ | keep |
| p3rs Youtube Channel Coming Soon! | 2018-03-05 | 163 | /blog/p3rs-youtube-channel-coming-soon/ | keep |
| Being Wrong | 2018-03-06 | 87 | /blog/being-wrong/ | noindex |
| Emo Band Coming Soon II | 2018-03-07 | 182 | /blog/emo-band-coming-soon-ii/ | keep |
| Video Editing Project | 2018-03-08 | 133 | /blog/video-editing-project/ | keep |
| First Video Done! | 2018-03-09 | 204 | /blog/first-video-done/ | keep |
| An actually goodish day | 2018-03-10 | 36 | /blog/an-actually-goodish-day/ | noindex |
| To-do list | 2018-03-11 | 13 | /blog/to-do-list/ | keep |
| RSI | 2018-03-12 | 40 | /blog/rsi/ | noindex |
| All nighter | 2018-03-13 | 36 | /blog/all-nighter/ | noindex |
| Sleep Deprivation | 2018-03-14 | 97 | /blog/sleep-deprivation/ | noindex |
| Well, I haven't done that for a while | 2018-03-15 | 33 | /blog/well-i-havent-done-that-for-a-while/ | noindex |
| Life | 2018-03-16 | 65 | /blog/life/ | noindex |
| Pills | 2018-03-17 | 52 | /blog/pills/ | noindex |
| Sigma Clan SOTW Competition | 2018-03-18 | 66 | /blog/sigma-clan-sotw-competition/ | noindex |
| Job Interview II | 2018-03-19 | 77 | /blog/job-interview-ii/ | noindex |
| Competition | 2018-03-20 | 70 | /blog/competition/ | noindex |
| Competition II | 2018-03-21 | 29 | /blog/competition-ii/ | noindex |
| Competition III | 2018-03-22 | 40 | /blog/competition-iii/ | noindex |
| Guernsey Chess | 2018-03-23 | 47 | /blog/guernsey-chess/ | noindex |
| Heroes | 2018-03-24 | 27 | /blog/heroes/ | noindex |
| Hobo Johnson | 2018-03-25 | 18 | /blog/hobo-johnson/ | noindex |
| Yarn | 2018-03-26 | 42 | /blog/yarn/ | noindex |
| Job | 2018-03-27 | 54 | /blog/job/ | noindex |
| The Dream is Dead | 2018-03-29 | 47 | /blog/the-dream-is-dead/ | noindex |
| Failure | 2018-03-30 | 51 | /blog/failure/ | keep |
| Models | 2018-03-31 | 19 | /blog/models/ | noindex |
| New Job, New Opportunity, New Me | 2018-04-02 | 44 | /blog/new-job-new-opportunity-new-me/ | noindex |
| Web Dev Day 1 | 2018-04-03 | 36 | /blog/web-dev-day-1/ | noindex |
| No sleep | 2018-04-04 | 28 | /blog/no-sleep/ | noindex |
| My first website | 2018-04-05 | 78 | /blog/my-first-website/ | noindex |
| Noodles | 2018-04-06 | 29 | /blog/noodles/ | noindex |
| Low and slow | 2018-04-07 | 175 | /blog/low-and-slow/ | keep |
| What I Want | 2018-04-08 | 41 | /blog/what-i-want/ | noindex |
| First Week | 2018-04-09 | 104 | /blog/first-week/ | keep |
| Priorities | 2018-04-10 | 74 | /blog/priorities/ | noindex |
| ASMR | 2018-04-11 | 220 | /blog/asmr/ | keep |
| First PHP programme! | 2018-04-12 | 183 | /blog/first-php-programme/ | keep |
| Aubury Update I | 2018-04-14 | 94 | /blog/aubury-update-i/ | noindex |
| Aubury Update II | 2018-04-15 | 92 | /blog/aubury-update-ii/ | noindex |
| Drupal | 2018-04-16 | 46 | /blog/drupal/ | noindex |
| Esolangs | 2018-04-17 | 84 | /blog/esolangs/ | noindex |
| Death Grips | 2018-04-18 | 86 | /blog/death-grips/ | noindex |
| A "real" blog | 2018-04-19 | 79 | /blog/a-real-blog/ | noindex |
| New website | 2018-04-20 | 53 | /blog/new-website/ | noindex |
| Xiu Xiu | 2018-04-21 | 55 | /blog/xiu-xiu/ | noindex |
| Kindness | 2018-04-22 | 36 | /blog/kindness/ | noindex |
| Sleep | 2018-04-24 | 47 | /blog/sleep/ | noindex |
| All the small things | 2018-04-25 | 79 | /blog/all-the-small-things/ | noindex |
| Tattoo researh | 2018-04-26 | 43 | /blog/tattoo-researh/ | noindex |
| Too many things | 2018-04-27 | 67 | /blog/too-many-things/ | noindex |
| Gym | 2018-04-28 | 40 | /blog/gym/ | noindex |
| Yuck | 2018-04-29 | 17 | /blog/yuck/ | noindex |
| Simone Giertz | 2018-04-30 | 70 | /blog/simone-giertz/ | noindex |
| Nothing is real anymore | 2018-05-01 | 130 | /blog/nothing-is-real-anymore/ | keep |
| We're getting the band back together! | 2018-09-24 | 116 | /blog/were-getting-the-band-back-together/ | keep |
| Goodbye, old friend | 2018-09-25 | 273 | /blog/goodbye-old-friend/ | keep |
| Counterstrike | 2018-09-26 | 58 | /blog/counterstrike/ | noindex |
| Browser Wars | 2018-09-27 | 72 | /blog/browser-wars/ | noindex |
| Critical Thinking | 2018-09-28 | 176 | /blog/critical-thinking/ | keep |
| Kali Linux | 2018-09-29 | 174 | /blog/kali-linux/ | keep |
| Choose Happiness | 2018-09-30 | 54 | /blog/choose-happiness/ | noindex |
| Male Friendship | 2018-10-01 | 127 | /blog/male-friendship/ | keep |
| Relating to People | 2018-10-02 | 72 | /blog/relating-to-people/ | noindex |
| Stress | 2018-10-04 | 54 | /blog/stress/ | noindex |
| Optimism | 2018-10-05 | 149 | /blog/optimism/ | keep |
| Always Tired | 2018-10-06 | 57 | /blog/always-tired/ | noindex |
| Jekyll | 2018-10-07 | 240 | /blog/jekyll/ | keep |
| elijah who | 2018-10-08 | 54 | /blog/elijah-who/ | noindex |
| The Codecoaster | 2018-10-09 | 116 | /blog/the-codecoaster/ | keep |
| We are Live - ish | 2018-10-10 | 241 | /blog/we-are-live-ish/ | keep |
| Open Source | 2018-10-11 | 285 | /blog/open-source/ | keep |
| Egos at the Door | 2018-10-13 | 245 | /blog/egos-at-the-door/ | keep |
| CS50 | 2018-10-14 | 199 | /blog/cs50/ | keep |
| Late Nights | 2018-10-15 | 163 | /blog/late-nights/ | keep |
| Chess Players | 2018-10-16 | 58 | /blog/chess-players/ | noindex |
| Open Source Baby Steps | 2018-10-17 | 107 | /blog/open-source-baby-steps/ | keep |
| Things that give me hope | 2018-10-18 | 207 | /blog/things-that-give-me-hope/ | keep |
| DEFCON | 2018-10-19 | 288 | /blog/defcon/ | keep |
| Want to-do list | 2018-10-20 | 147 | /blog/want-to-do-list/ | keep |
| CS50 Progress: Week One | 2018-10-21 | 160 | /blog/cs50-progress-week-one/ | keep |
| Steps, Forward and Back | 2018-10-23 | 73 | /blog/steps-forward-and-back/ | noindex |
| DEFCON II | 2018-10-24 | 106 | /blog/defcon-ii/ | keep |
| Old Photos | 2018-10-25 | 187 | /blog/old-photos/ | keep |
| Lifestyle Changes | 2018-10-26 | 63 | /blog/lifestyle-changes/ | keep |
| Baby You're A Haunted House | 2018-10-27 | 129 | /blog/baby-youre-a-haunted-house/ | keep |
| Attrition | 2018-10-28 | 138 | /blog/attrition/ | keep |
| Attrition 2 | 2018-10-29 | 81 | /blog/attrition-2/ | noindex |
| Julien Baker | 2018-10-30 | 58 | /blog/julien-baker/ | noindex |
| OGLAF | 2018-10-31 | 102 | /blog/oglaf/ | keep |
| Reflecting On: Gambling and Catharsis | 2018-11-01 | 299 | /blog/reflecting-on-gambling-and-catharsis/ | keep |
| Just like cooking | 2018-11-05 | 125 | /blog/just-like-cooking/ | keep |
| Plant Based Diet | 2018-11-06 | 156 | /blog/plant-based-diet/ | keep |
| Red and Blue | 2018-11-07 | 199 | /blog/red-and-blue/ | keep |
| Watching the World Burn | 2018-11-15 | 217 | /blog/watching-the-world-burn/ | keep |
| RE: Strong Opinions | 2018-11-16 | 257 | /blog/re-strong-opinions/ | keep |
| Happiness | 2018-11-17 | 231 | /blog/happiness/ | keep |
| Surviving Mars | 2018-11-18 | 92 | /blog/surviving-mars/ | noindex |
| The Church of Iron | 2018-11-19 | 152 | /blog/the-church-of-iron/ | keep |
| Too Busy | 2018-11-20 | 69 | /blog/too-busy/ | noindex |
| I'm a convincing actor | 2018-11-23 | 193 | /blog/im-a-convincing-actor/ | keep |
| Whining | 2018-11-24 | 101 | /blog/whining/ | keep |
| Everyone is totally winging it | 2018-11-25 | 280 | /blog/everyone-is-totally-winging-it/ | keep |
| Joy as an act of resistance | 2018-11-26 | 267 | /blog/joy-as-an-act-of-resistance/ | keep |
| Intelligent New Programme | 2018-11-27 | 219 | /blog/intelligent-new-programme/ | keep |
| Flirting | 2018-11-28 | 60 | /blog/flirting/ | noindex |
| Exhaustion | 2018-11-29 | 51 | /blog/exhaustion/ | noindex |
| Obligations | 2018-11-30 | 133 | /blog/obligations/ | keep |
| Too Fast | 2018-12-01 | 80 | /blog/too-fast/ | noindex |
| Build All The Things II | 2018-12-05 | 103 | /blog/build-all-the-things-ii/ | keep |
| Schedule | 2018-12-08 | 65 | /blog/schedule/ | noindex |
| ASMR II | 2018-12-09 | 287 | /blog/asmr-ii/ | keep |
| Christmas | 2018-12-13 | 180 | /blog/christmas/ | keep |
| s1mple | 2018-12-15 | 270 | /blog/s1mple/ | keep |
| Calorie Counting | 2018-12-16 | 203 | /blog/calorie-counting/ | keep |
| Idle Words | 2018-12-21 | 156 | /blog/idle-words/ | keep |
| The Value of Conversation | 2018-12-22 | 156 | /blog/the-value-of-conversation/ | keep |
| Booking Flights | 2018-12-24 | 149 | /blog/booking-flights/ | keep |
| Reflecting On: Ramblings I | 2018-12-25 | 93 | /blog/reflecting-on-ramblings-i/ | noindex |
| The State of the Blog II | 2018-12-26 | 212 | /blog/the-state-of-the-blog-ii/ | keep |
| Social Prescription | 2018-12-27 | 213 | /blog/social-prescription/ | keep |
| The Honesty Problem | 2018-12-28 | 288 | /blog/the-honesty-problem/ | keep |
| Lynx Titan | 2018-12-29 | 100 | /blog/lynx-titan/ | keep |
| Beware of Dog II | 2018-12-30 | 239 | /blog/beware-of-dog-ii/ | keep |
| The Language of Sadness | 2018-12-31 | 178 | /blog/the-language-of-sadness/ | keep |
| New Year's Resolutions | 2019-01-01 | 264 | /blog/new-years-resolutions/ | keep |
| Beware of Dog III | 2019-01-02 | 221 | /blog/beware-of-dog-iii/ | keep |
| Sickness | 2019-01-03 | 92 | /blog/sickness/ | noindex |
| Trip Planning | 2019-01-06 | 207 | /blog/trip-planning/ | keep |
| When it's easy, it's easy | 2019-01-09 | 236 | /blog/when-its-easy-its-easy/ | keep |
| Yudkowsky Ambititon Scale | 2019-01-11 | 262 | /blog/yudkowsky-ambititon-scale/ | keep |
| In the Aeroplane Over The Sea | 2019-01-12 | 270 | /blog/in-the-aeroplane-over-the-sea/ | keep |
| 5am | 2019-01-15 | 83 | /blog/5am/ | noindex |
| Mom Jeans | 2019-01-16 | 140 | /blog/mom-jeans/ | keep |
| Trial and Error | 2019-01-19 | 257 | /blog/trial-and-error/ | keep |
| Non Linear Perception of Time | 2019-01-21 | 164 | /blog/non-linear-perception-of-time/ | keep |
| Balancing the Coin II | 2019-01-24 | 168 | /blog/balancing-the-coin-ii/ | keep |
| Nobody Talks About the Dentist | 2019-01-25 | 121 | /blog/nobody-talks-about-the-dentist/ | keep |
| OS Installation Issues | 2019-01-28 | 101 | /blog/os-installation-issues/ | keep |
| Moving Day | 2019-01-29 | 106 | /blog/moving-day/ | keep |
| New Face | 2019-02-01 | 99 | /blog/new-face/ | noindex |
| Satisficing | 2019-02-02 | 146 | /blog/satisficing/ | keep |
| I Have Too Much Stuff | 2019-02-03 | 136 | /blog/i-have-too-much-stuff/ | keep |
| GSL 2019 | 2019-02-05 | 166 | /blog/gsl-2019/ | keep |
| I'm bad at breathing | 2019-02-08 | 150 | /blog/im-bad-at-breathing/ | keep |
| black midi | 2019-02-09 | 138 | /blog/black-midi/ | keep |
| New Ubuntu Installation | 2019-02-10 | 111 | /blog/new-ubuntu-installation/ | keep |
| GSL 2019 II | 2019-02-12 | 56 | /blog/gsl-2019-ii/ | noindex |
| Valentine's Day | 2019-02-14 | 175 | /blog/valentines-day/ | keep |
| Hope | 2019-02-15 | 122 | /blog/hope/ | keep |
| What We Want | 2019-02-16 | 241 | /blog/what-we-want/ | keep |
| Bonsai | 2019-02-17 | 186 | /blog/bonsai/ | keep |
| Good Mood | 2019-02-18 | 129 | /blog/good-mood/ | keep |
| Chess Club | 2019-02-20 | 110 | /blog/chess-club/ | keep |
| RE: An Honest Living | 2019-02-21 | 186 | /blog/re-an-honest-living/ | keep |
| Righting Old Wrongs | 2019-02-22 | 74 | /blog/righting-old-wrongs/ | noindex |
| Build All The Things III | 2019-02-23 | 162 | /blog/build-all-the-things-iii/ | keep |
| Shanghai Dragons | 2019-02-24 | 169 | /blog/shanghai-dragons/ | keep |
| Meditating for the wrong reasons | 2019-02-25 | 88 | /blog/meditating-for-the-wrong-reasons/ | noindex |
| Chess is kinda like boxing | 2019-02-26 | 143 | /blog/chess-is-kinda-like-boxing/ | keep |
| Disruption | 2019-02-27 | 102 | /blog/disruption/ | keep |
| Embracing Suffering | 2019-02-28 | 235 | /blog/embracing-suffering/ | keep |
| Paintings | 2019-03-01 | 22 | /blog/paintings/ | noindex |
| soO | 2019-03-03 | 101 | /blog/soo/ | keep |
| Industry Gurus | 2019-03-04 | 75 | /blog/industry-gurus/ | noindex |
| Chess is about disagreeing with people | 2019-03-05 | 225 | /blog/chess-is-about-disagreeing-with-people/ | keep |
| Knockoff Proleague | 2019-03-06 | 108 | /blog/knockoff-proleague/ | keep |
| Python Koans | 2019-03-08 | 50 | /blog/python-koans/ | noindex |
| Moving on from the bonsai | 2019-03-09 | 292 | /blog/moving-on-from-the-bonsai/ | keep |
| Self Love | 2019-03-10 | 99 | /blog/self-love/ | noindex |
| Black Country, New Road | 2019-03-13 | 59 | /blog/black-country-new-road/ | noindex |
| NYC todo | 2019-03-14 | 93 | /blog/nyc-todo/ | noindex |
| Friday Nights In | 2019-03-15 | 178 | /blog/friday-nights-in/ | keep |
| Back in the Saddle | 2019-03-17 | 154 | /blog/back-in-the-saddle/ | keep |
| Balancing the Coin III | 2019-03-18 | 108 | /blog/balancing-the-coin-iii/ | keep |
| The October Update | 2019-03-21 | 40 | /blog/the-october-update/ | noindex |
| Carolina Reapers | 2019-03-22 | 84 | /blog/carolina-reapers/ | noindex |
| After Life Review | 2019-03-23 | 202 | /blog/after-life-review/ | keep |
| The Dawn Wall | 2019-03-24 | 134 | /blog/the-dawn-wall/ | keep |
| Resting | 2019-03-25 | 209 | /blog/resting/ | keep |
| Nerves | 2019-03-26 | 116 | /blog/nerves/ | keep |
| GSL RO8 | 2019-03-27 | 71 | /blog/gsl-ro8/ | noindex |
| Just Checking In | 2019-03-28 | 145 | /blog/just-checking-in/ | keep |
| We Did It | 2019-03-29 | 168 | /blog/we-did-it/ | keep |
| Celeste | 2019-03-31 | 216 | /blog/celeste/ | keep |
| October 3, 2011 | 2019-04-01 | 194 | /blog/october-3-2011/ | keep |
| October 3, 2011 II | 2019-04-02 | 180 | /blog/october-3-2011-ii/ | keep |
| October 3, 2011 III | 2019-04-03 | 253 | /blog/october-3-2011-iii/ | keep |
| Book Glut | 2019-04-04 | 279 | /blog/book-glut/ | keep |
| The Adventure Begins | 2019-04-05 | 165 | /blog/the-adventure-begins/ | keep |
| Yet Another Post About Losing Weight | 2019-04-06 | 219 | /blog/yet-another-post-about-losing-weight/ | keep |
| Land of the Free | 2019-04-07 | 198 | /blog/land-of-the-free/ | keep |
| Thoughts and Words | 2019-04-08 | 105 | /blog/thoughts-and-words/ | keep |
| Climbing | 2019-04-09 | 168 | /blog/climbing/ | keep |
| Photos | 2019-04-10 | 124 | /blog/photos/ | keep |
| The New York Knicks | 2019-04-11 | 171 | /blog/the-new-york-knicks/ | keep |
| Playing at Being an Adult | 2019-04-12 | 277 | /blog/playing-at-being-an-adult/ | keep |
| Desert Island Discs | 2019-04-13 | 204 | /blog/desert-island-discs/ | keep |
| Friends' Happiness | 2019-04-14 | 225 | /blog/friends-happiness/ | keep |
| Big City Life | 2019-04-15 | 246 | /blog/big-city-life/ | keep |
| The Adventure is Almost Over | 2019-04-16 | 200 | /blog/the-adventure-is-almost-over/ | keep |
| The Long Road Home | 2019-04-17 | 76 | /blog/the-long-road-home/ | noindex |
| Falling in Love With Where I Live | 2019-04-19 | 180 | /blog/falling-in-love-with-where-i-live/ | keep |
| Pete Davidson | 2019-04-20 | 46 | /blog/pete-davidson/ | keep |
| Just Enjoy It, You Fucking Idiot | 2019-04-21 | 133 | /blog/just-enjoy-it-you-fucking-idiot/ | keep |
| Advice II | 2019-04-22 | 233 | /blog/advice-ii/ | keep |
| I'm having a baby! | 2019-04-25 | 176 | /blog/im-having-a-baby/ | keep |
| Bands To See Before I Die | 2019-04-28 | 143 | /blog/bands-to-see-before-i-die/ | keep |
| Playing at Being an Adult II | 2019-04-30 | 257 | /blog/playing-at-being-an-adult-ii/ | keep |
| I love you II | 2019-05-03 | 250 | /blog/i-love-you-ii/ | keep |
| Guernsey Literary Festival: Lionel Shriver | 2019-05-04 | 164 | /blog/guernsey-literary-festival-lionel-shriver/ | keep |
| Running III | 2019-05-05 | 78 | /blog/running-iii/ | noindex |
| Should I Call Myself a Feminist II | 2019-05-07 | 240 | /blog/should-i-call-myself-a-feminist-ii/ | keep |
| Running IV | 2019-05-08 | 186 | /blog/running-iv/ | keep |
| Being Called Out | 2019-05-09 | 236 | /blog/being-called-out/ | keep |
| The End of a Short Era | 2019-05-10 | 205 | /blog/the-end-of-a-short-era/ | keep |
| Chess Inter Insular | 2019-05-11 | 208 | /blog/chess-inter-insular/ | keep |
| First Day of a New Era | 2019-05-13 | 134 | /blog/first-day-of-a-new-era/ | keep |
| Fake It Until You Make It | 2019-05-14 | 260 | /blog/fake-it-until-you-make-it/ | keep |
| The Joy of Starting Over | 2019-05-15 | 162 | /blog/the-joy-of-starting-over/ | keep |
| An Ode to the Love Shack | 2019-05-17 | 191 | /blog/an-ode-to-the-love-shack/ | keep |
| WCS Spring | 2019-05-18 | 205 | /blog/wcs-spring/ | keep |
| Windows Terminal | 2019-05-20 | 156 | /blog/windows-terminal/ | keep |
| Smalltalk Revisited | 2019-05-21 | 224 | /blog/smalltalk-revisited/ | keep |
| Feeling Overwhelmed | 2019-05-23 | 261 | /blog/feeling-overwhelmed/ | keep |
| Park Run | 2019-05-25 | 227 | /blog/park-run/ | keep |
| Oatmeal and the Blerch | 2019-05-26 | 193 | /blog/oatmeal-and-the-blerch/ | keep |
| Some Overdue Updates | 2019-05-27 | 248 | /blog/some-overdue-updates/ | keep |
| When it's easy, it's easy II | 2019-05-29 | 244 | /blog/when-its-easy-its-easy-ii/ | keep |
| Falling In Love With Where I Live II | 2019-05-30 | 84 | /blog/falling-in-love-with-where-i-live-ii/ | noindex |
| Yet More Expectations | 2019-05-31 | 170 | /blog/yet-more-expectations/ | keep |
| Ongun Theory | 2019-06-01 | 117 | /blog/ongun-theory/ | keep |
| Sharing Your Goals | 2019-06-02 | 127 | /blog/sharing-your-goals/ | keep |
| Time Poor | 2019-06-03 | 157 | /blog/time-poor/ | keep |
| Altibox Norway Chess | 2019-06-04 | 141 | /blog/altibox-norway-chess/ | keep |
| Catching Myself Being Happy | 2019-06-06 | 76 | /blog/catching-myself-being-happy/ | noindex |
| Baldur's Gate III | 2019-06-07 | 200 | /blog/baldurs-gate-iii/ | keep |
| Hack The Box | 2019-06-08 | 101 | /blog/hack-the-box/ | keep |
| Half marathon in the books II | 2019-06-10 | 119 | /blog/half-marathon-in-the-books-ii/ | keep |
| Natural, Everyday Degradation | 2019-06-11 | 175 | /blog/natural-everyday-degradation/ | keep |
| Political Enemies | 2019-06-12 | 104 | /blog/political-enemies/ | keep |
| Commit Yourself Completely | 2019-06-13 | 90 | /blog/commit-yourself-completely/ | noindex |
| Oculus Revisited | 2019-06-14 | 115 | /blog/oculus-revisited/ | keep |
| Nerves II | 2019-06-15 | 119 | /blog/nerves-ii/ | keep |
| Half marathon in the books III | 2019-06-16 | 187 | /blog/half-marathon-in-the-books-iii/ | keep |
| Adam Ondra | 2019-06-17 | 56 | /blog/adam-ondra/ | noindex |
| The Joy Of Spinning Up New Machines | 2019-06-18 | 129 | /blog/the-joy-of-spinning-up-new-machines/ | keep |
| Todoist | 2019-06-19 | 163 | /blog/todoist/ | keep |
| Will Hurd the Black Hat | 2019-06-21 | 200 | /blog/will-hurd-the-black-hat/ | keep |
| Dark, The Swarm | 2019-06-22 | 248 | /blog/dark-the-swarm/ | keep |
| Schlagenheim | 2019-06-23 | 76 | /blog/schlagenheim/ | noindex |
| Summer League | 2019-06-25 | 92 | /blog/summer-league/ | noindex |
| So This is What It's Come To | 2019-06-26 | 107 | /blog/so-this-is-what-its-come-to/ | keep |
| The Sri Chinmoy Self Transcendence Race | 2019-06-27 | 179 | /blog/the-sri-chinmoy-self-transcendence-race/ | keep |
| The Hedonic Treadmill | 2019-06-28 | 80 | /blog/the-hedonic-treadmill/ | keep |
| Hay Fever | 2019-06-29 | 41 | /blog/hay-fever/ | noindex |
| Taking a Break | 2019-06-30 | 73 | /blog/taking-a-break/ | noindex |
| Book Reviews The Master and Margarita by Mikhail Bulgakov | 2019-07-28 | 255 | /blog/book-reviews-the-master-and-margarita-by-mikhail-bulgakov/ | keep |
| Climbing Progress | 2019-07-29 | 182 | /blog/climbing-progress/ | keep |
| The Hedonic Treadmill III | 2019-07-31 | 264 | /blog/the-hedonic-treadmill-iii/ | keep |
| What're You Feeling? | 2019-08-01 | 193 | /blog/whatre-you-feeling/ | keep |
| 50 Ways To Show Someone You Love Them Without Having Sex | 2019-08-02 | 208 | /blog/50-ways-to-show-someone-you-love-them-without-having-sex/ | keep |
| Radical Honesty II | 2019-08-03 | 114 | /blog/radical-honesty-ii/ | keep |
| Candid Photos | 2019-08-06 | 134 | /blog/candid-photos/ | keep |
| Build All The Things IV | 2019-08-07 | 201 | /blog/build-all-the-things-iv/ | keep |
| Social Media FOMO | 2019-08-09 | 248 | /blog/social-media-fomo/ | keep |
| Super Meat Boy | 2019-08-10 | 139 | /blog/super-meat-boy/ | keep |
| How Many Sheep Crossed The Bridge? | 2019-08-11 | 175 | /blog/how-many-sheep-crossed-the-bridge/ | keep |
| Beware of Dog IV | 2019-08-13 | 38 | /blog/beware-of-dog-iv/ | noindex |
| I love you iii | 2019-08-14 | 64 | /blog/i-love-you-iii/ | noindex |
| Alcohol IV | 2019-08-18 | 143 | /blog/alcohol-iv/ | keep |
| Infest The Rats' Nest Review | 2019-08-20 | 290 | /blog/infest-the-rats-nest-review/ | keep |
| rPi Plans | 2019-08-21 | 137 | /blog/rpi-plans/ | keep |
| GCSE Results | 2019-08-22 | 249 | /blog/gcse-results/ | keep |
| Pomegranates | 2019-08-24 | 52 | /blog/pomegranates/ | noindex |
| Self Control | 2019-08-25 | 247 | /blog/self-control/ | keep |
| The End of Summer | 2019-08-27 | 218 | /blog/the-end-of-summer/ | keep |
| RSS Has Landed | 2019-08-28 | 140 | /blog/rss-has-landed/ | keep |
| Positive Juice II | 2019-08-29 | 245 | /blog/positive-juice-ii/ | keep |
| Motivation | 2019-08-31 | 140 | /blog/motivation/ | keep |
| Photos II | 2019-09-01 | 228 | /blog/photos-ii/ | keep |
| Competition IV | 2019-09-02 | 265 | /blog/competition-iv/ | keep |
| It Isn't What It Is | 2019-09-03 | 96 | /blog/it-isnt-what-it-is/ | noindex |
| Happy Endings | 2019-09-04 | 172 | /blog/happy-endings/ | keep |
| Customer Support | 2019-09-05 | 162 | /blog/customer-support/ | keep |
| Being English When It's Convenient | 2019-09-07 | 112 | /blog/being-english-when-its-convenient/ | keep |
| Enjoying Writing | 2019-09-08 | 158 | /blog/enjoying-writing/ | keep |
| exercism.io | 2019-09-09 | 122 | /blog/exercism.io/ | keep |
| Perspective | 2019-09-11 | 71 | /blog/perspective/ | noindex |
| Walking The Cow | 2019-09-12 | 143 | /blog/walking-the-cow/ | keep |
| The Fall Of Hobo Johnson Review | 2019-09-14 | 205 | /blog/the-fall-of-hobo-johnson-review/ | keep |
| Fragility | 2019-09-15 | 119 | /blog/fragility/ | keep |
| Health | 2019-09-16 | 179 | /blog/health/ | keep |
| Giving It All Up And Becoming a Farmer | 2019-09-17 | 145 | /blog/giving-it-all-up-and-becoming-a-farmer/ | keep |
| What're You Feeling? II | 2019-09-18 | 49 | /blog/whatre-you-feeling-ii/ | keep |
| Should I Call Myself a Feminist III | 2019-09-19 | 250 | /blog/should-i-call-myself-a-feminist-iii/ | keep |
| Self Care and Self Pity | 2019-09-20 | 75 | /blog/self-care-and-self-pity/ | noindex |
| Conference Anxiety | 2019-09-21 | 206 | /blog/conference-anxiety/ | keep |
| Be My Eyes | 2019-09-22 | 176 | /blog/be-my-eyes/ | keep |
| Listening | 2019-09-23 | 141 | /blog/listening/ | keep |
| The Purpose Of The Blog | 2019-09-24 | 220 | /blog/the-purpose-of-the-blog/ | keep |
| A Slave to One's Emotions | 2019-09-26 | 69 | /blog/a-slave-to-ones-emotions/ | noindex |
| Size Medium | 2019-09-27 | 67 | /blog/size-medium/ | noindex |
| Book Reviews: Foundation by Isaac Asimov | 2019-10-21 | 293 | /blog/book-reviews-foundation-by-isaac-asimov/ | keep |
| I Disagree Review | 2020-01-16 | 280 | /blog/i-disagree-review/ | keep |
| Everything Else Has Gone Wrong | 2020-01-17 | 112 | /blog/everything-else-has-gone-wrong/ | keep |
| The Bet is Back | 2020-01-18 | 116 | /blog/the-bet-is-back/ | keep |
| Lunch && Code | 2020-01-22 | 164 | /blog/lunch-code/ | keep |
| Goryachkina v Ju | 2020-01-23 | 284 | /blog/goryachkina-v-ju/ | keep |
| Welcome Back to the Black Parade | 2020-01-24 | 156 | /blog/welcome-back-to-the-black-parade/ | keep |
| Home Games | 2020-01-25 | 92 | /blog/home-games/ | noindex |
| Can Jonny Actually Read Challenge 2.0 | 2020-01-26 | 124 | /blog/can-jonny-actually-read-challenge-2.0/ | keep |
| Correspondence Chess Tournaments | 2020-01-27 | 204 | /blog/correspondence-chess-tournaments/ | keep |
| Teamwork | 2020-01-28 | 104 | /blog/teamwork/ | keep |
| Almost Smart | 2020-01-30 | 218 | /blog/almost-smart/ | keep |
| To speak or to listen | 2020-01-31 | 174 | /blog/to-speak-or-to-listen/ | keep |
| Game Jam II | 2020-02-01 | 102 | /blog/game-jam-ii/ | keep |
| Polyphia | 2020-02-02 | 115 | /blog/polyphia/ | keep |
| Man Club | 2020-02-04 | 231 | /blog/man-club/ | keep |
| Lack of Time | 2020-02-05 | 109 | /blog/lack-of-time/ | keep |
| Publishing blogs is hard | 2020-02-06 | 137 | /blog/publishing-blogs-is-hard/ | keep |
| Pride | 2020-02-08 | 41 | /blog/pride/ | noindex |
| Poker Hand Stories | 2020-02-10 | 124 | /blog/poker-hand-stories/ | keep |
| I also won and I will also win again | 2020-02-11 | 89 | /blog/i-also-won-and-i-will-also-win-again/ | noindex |
| Compassion Fatigue | 2020-02-12 | 194 | /blog/compassion-fatigue/ | keep |
| Infinite Jest for the Wrong Reasons | 2020-02-13 | 297 | /blog/infinite-jest-for-the-wrong-reasons/ | keep |
| Things That Are More Therapeutic Than Therapy II: Live Music | 2020-02-14 | 200 | /blog/things-that-are-more-therapeutic-than-therapy-ii-live-music/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Trying to Teach an Idiot Poker | 2020-02-15 | 151 | /blog/trying-to-teach-an-idiot-poker/ | keep |
| Things That Are More Therapeutic Than Therapy III: Bumpy Flights | 2020-02-16 | 187 | /blog/things-that-are-more-therapeutic-than-therapy-iii-bumpy-flights/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Adjusting For Your Own Biases | 2020-02-17 | 154 | /blog/adjusting-for-your-own-biases/ | keep |
| Things That Are More Therapeutic Than Therapy IV: Swimming in the Sea | 2020-02-18 | 183 | /blog/things-that-are-more-therapeutic-than-therapy-iv-swimming-in-the-sea/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Violent Video Games | 2020-02-19 | 107 | /blog/violent-video-games/ | keep |
| Staff Car Parks | 2020-02-20 | 82 | /blog/staff-car-parks/ | noindex |
| Buho | 2020-02-21 | 93 | /blog/buho/ | noindex |
| A Peaceful Battle | 2020-02-22 | 118 | /blog/a-peaceful-battle/ | keep |
| The Great Game | 2020-02-23 | 46 | /blog/the-great-game/ | noindex |
| Infinite Jest: I've Written a Novel | 2020-02-24 | 210 | /blog/infinite-jest-ive-written-a-novel/ | keep |
| Miss Anthropocene Review | 2020-02-25 | 267 | /blog/miss-anthropocene-review/ | keep |
| Ego in Chess II | 2020-02-26 | 107 | /blog/ego-in-chess-ii/ | keep |
| The Barkley Marathons II | 2020-02-27 | 261 | /blog/the-barkley-marathons-ii/ | keep |
| Satire's Golden Age | 2020-02-28 | 115 | /blog/satires-golden-age/ | keep |
| Diabotical | 2020-02-29 | 214 | /blog/diabotical/ | keep |
| Life Without Wifi | 2020-03-01 | 156 | /blog/life-without-wifi/ | keep |
| Victimhood Identity | 2020-03-02 | 138 | /blog/victimhood-identity/ | keep |
| Disco Elysium | 2020-03-03 | 204 | /blog/disco-elysium/ | keep |
| Travis CI | 2020-03-04 | 86 | /blog/travis-ci/ | noindex |
| Sometimes Laziness Pays Off | 2020-03-05 | 87 | /blog/sometimes-laziness-pays-off/ | noindex |
| Puppeteer | 2020-03-06 | 71 | /blog/puppeteer/ | noindex |
| Food is Food for the Soul | 2020-03-07 | 158 | /blog/food-is-food-for-the-soul/ | keep |
| Itachi Uchiha | 2020-03-08 | 130 | /blog/itachi-uchiha/ | keep |
| Open-Jaw Flights | 2020-03-09 | 149 | /blog/open-jaw-flights/ | keep |
| You're Welcome, Ted | 2020-03-10 | 58 | /blog/youre-welcome-ted/ | noindex |
| An Hour of Nothing | 2020-03-11 | 101 | /blog/an-hour-of-nothing/ | keep |
| Nietzsche Quotes | 2020-03-12 | 83 | /blog/nietzsche-quotes/ | noindex |
| Folding at Home | 2020-03-14 | 207 | /blog/folding-at-home/ | keep |
| Underneath Review | 2020-03-15 | 184 | /blog/underneath-review/ | keep |
| Intermittent Fasting | 2020-03-16 | 185 | /blog/intermittent-fasting/ | keep |
| Guns Akimbo Review | 2020-03-18 | 143 | /blog/guns-akimbo-review/ | keep |
| A Calm Soul | 2020-03-19 | 88 | /blog/a-calm-soul/ | noindex |
| Pretending | 2020-03-20 | 213 | /blog/pretending/ | keep |
| Stubborness | 2020-03-21 | 43 | /blog/stubborness/ | noindex |
| WFH Day 1 | 2020-03-23 | 149 | /blog/wfh-day-1/ | keep |
| Lockdown | 2020-03-24 | 77 | /blog/lockdown/ | noindex |
| Governmental Exercise Rationing | 2020-03-25 | 271 | /blog/governmental-exercise-rationing/ | keep |
| Lockdown II | 2020-03-27 | 136 | /blog/lockdown-ii/ | keep |
| The recipe for success II | 2020-03-28 | 158 | /blog/the-recipe-for-success-ii/ | keep |
| Know the Risk | 2020-03-30 | 94 | /blog/know-the-risk/ | noindex |
| Sea Mine Spotted | 2020-03-31 | 149 | /blog/sea-mine-spotted/ | keep |
| Three Things to be Grateful For | 2020-04-01 | 119 | /blog/three-things-to-be-grateful-for/ | keep |
| New Students | 2020-04-02 | 145 | /blog/new-students/ | keep |
| Three More Things To Be Grateful For | 2020-04-03 | 130 | /blog/three-more-things-to-be-grateful-for/ | keep |
| Fight Club | 2020-04-07 | 113 | /blog/fight-club/ | keep |
| Psychosomaticity | 2020-04-08 | 132 | /blog/psychosomaticity/ | keep |
| Virtual Pub Quizzes | 2020-04-09 | 81 | /blog/virtual-pub-quizzes/ | noindex |
| Another Love Letter to the GSL | 2020-04-11 | 174 | /blog/another-love-letter-to-the-gsl/ | keep |
| Playing at Being an Adult III | 2020-04-12 | 158 | /blog/playing-at-being-an-adult-iii/ | keep |
| Escapism | 2020-04-13 | 256 | /blog/escapism/ | keep |
| Flight Refunds | 2020-04-14 | 183 | /blog/flight-refunds/ | keep |
| I Miss Climbing | 2020-04-15 | 126 | /blog/i-miss-climbing/ | keep |
| Self-Reflection | 2020-04-16 | 200 | /blog/self-reflection/ | keep |
| Hackathon Day 1 | 2020-04-17 | 269 | /blog/hackathon-day-1/ | keep |
| Self-Reflection II | 2020-04-18 | 79 | /blog/self-reflection-ii/ | noindex |
| Computer Burnout | 2020-04-19 | 73 | /blog/computer-burnout/ | noindex |
| TWINT | 2020-04-20 | 158 | /blog/twint/ | keep |
| TWINT II | 2020-04-21 | 208 | /blog/twint-ii/ | keep |
| Middleditch and Schwartz | 2020-04-22 | 135 | /blog/middleditch-and-schwartz/ | keep |
| What it Means to be a Man III: Honesty | 2020-04-25 | 206 | /blog/what-it-means-to-be-a-man-iii-honesty/ | merge into "What it Means to be a Man" |
| What it Means to be a Man VII: Non-Complicity | 2020-04-29 | 236 | /blog/what-it-means-to-be-a-man-vii-non-complicity/ | merge into "What it Means to be a Man" |
| What it Means to be a Man VIII: Patience | 2020-04-30 | 227 | /blog/what-it-means-to-be-a-man-viii-patience/ | merge into "What it Means to be a Man" |
| What it Means to be a Man IX: Acceptance | 2020-05-01 | 237 | /blog/what-it-means-to-be-a-man-ix-acceptance/ | merge into "What it Means to be a Man" |
| What it Means to be a Man XI: Empathy | 2020-05-03 | 216 | /blog/what-it-means-to-be-a-man-xi-empathy/ | merge into "What it Means to be a Man" |
| What it Means to be a Man XII: In Conclusion | 2020-05-04 | 175 | /blog/what-it-means-to-be-a-man-xii-in-conclusion/ | merge into "What it Means to be a Man" |
| Bad Post | 2020-05-06 | 257 | /blog/bad-post/ | keep |
| Maniac Review | 2020-05-07 | 250 | /blog/maniac-review/ | keep |
| Saying Yes To The Wrong Things | 2020-05-08 | 220 | /blog/saying-yes-to-the-wrong-things/ | keep |
| Return of the Snark | 2020-05-11 | 273 | /blog/return-of-the-snark/ | keep |
| Feed Me | 2020-05-14 | 240 | /blog/feed-me/ | keep |
| Things That Are More Therapeutic Than Therapy V: ASMR | 2020-05-15 | 205 | /blog/things-that-are-more-therapeutic-than-therapy-v-asmr/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| The Beauty on One's Doorstep | 2020-05-16 | 79 | /blog/the-beauty-on-ones-doorstep/ | noindex |
| An Island of Memories | 2020-05-17 | 164 | /blog/an-island-of-memories/ | keep |
| Fencing | 2020-05-18 | 141 | /blog/fencing/ | keep |
| It's Always Sunny In Philadelphia | 2020-05-19 | 206 | /blog/its-always-sunny-in-philadelphia/ | keep |
| NO DREAM Review | 2020-05-20 | 212 | /blog/no-dream-review/ | keep |
| Weight Loss Communities | 2020-05-22 | 119 | /blog/weight-loss-communities/ | keep |
| Just Like Riding a Bike | 2020-05-23 | 270 | /blog/just-like-riding-a-bike/ | keep |
| Things That Are More Therapeutic Than Therapy VI: Climbing Outdoors | 2020-05-24 | 244 | /blog/things-that-are-more-therapeutic-than-therapy-vi-climbing-outdoors/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Intermittent Fasting II | 2020-05-26 | 208 | /blog/intermittent-fasting-ii/ | keep |
| Ten Days of Meditation | 2020-05-27 | 272 | /blog/ten-days-of-meditation/ | keep |
| Ben and Jerry's | 2020-05-28 | 90 | /blog/ben-and-jerrys/ | noindex |
| Some Days | 2020-05-29 | 104 | /blog/some-days/ | keep |
| Just Like Riding a Bike II | 2020-05-30 | 94 | /blog/just-like-riding-a-bike-ii/ | noindex |
| Back to the Office | 2020-05-31 | 117 | /blog/back-to-the-office/ | keep |
| Some Days II | 2020-06-02 | 50 | /blog/some-days-ii/ | noindex |
| Cache Invalidation | 2020-06-03 | 90 | /blog/cache-invalidation/ | noindex |
| Some Days III | 2020-06-04 | 39 | /blog/some-days-iii/ | noindex |
| Takeaway | 2020-06-05 | 61 | /blog/takeaway/ | noindex |
| Positive Feedback | 2020-06-06 | 133 | /blog/positive-feedback/ | keep |
| No Regrets | 2020-06-07 | 294 | /blog/no-regrets/ | keep |
| Body Image Advice | 2020-06-08 | 156 | /blog/body-image-advice/ | keep |
| Another Three Things To Be Grateful For | 2020-06-09 | 178 | /blog/another-three-things-to-be-grateful-for/ | keep |
| Another Three Things To Be Grateful For II | 2020-06-10 | 191 | /blog/another-three-things-to-be-grateful-for-ii/ | keep |
| Another Three Things To Be Grateful For III | 2020-06-11 | 214 | /blog/another-three-things-to-be-grateful-for-iii/ | keep |
| Another Three Things To Be Grateful For IV | 2020-06-12 | 123 | /blog/another-three-things-to-be-grateful-for-iv/ | keep |
| Another Three Things To Be Grateful For V | 2020-06-13 | 83 | /blog/another-three-things-to-be-grateful-for-v/ | noindex |
| The Evil Dead | 2020-06-15 | 268 | /blog/the-evil-dead/ | keep |
| Mercy | 2020-06-17 | 58 | /blog/mercy/ | noindex |
| Fragility II | 2020-06-18 | 98 | /blog/fragility-ii/ | noindex |
| Social Responsibility II | 2020-06-19 | 152 | /blog/social-responsibility-ii/ | keep |
| Punisher Review | 2020-06-20 | 88 | /blog/punisher-review/ | noindex |
| Marathons | 2020-06-21 | 220 | /blog/marathons/ | keep |
| Normality | 2020-06-22 | 247 | /blog/normality/ | keep |
| Another Three Things To Be Grateful For VI | 2020-06-25 | 220 | /blog/another-three-things-to-be-grateful-for-vi/ | keep |
| I Hate It When People Are Nice To Me | 2020-06-26 | 96 | /blog/i-hate-it-when-people-are-nice-to-me/ | noindex |
| Art Club | 2020-06-27 | 77 | /blog/art-club/ | noindex |
| Sober Narcissism | 2020-06-28 | 218 | /blog/sober-narcissism/ | keep |
| The Feeling After Food | 2020-06-29 | 106 | /blog/the-feeling-after-food/ | keep |
| Reddit and Hate Speech | 2020-06-30 | 296 | /blog/reddit-and-hate-speech/ | keep |
| Busy-ness | 2020-07-01 | 115 | /blog/busy-ness/ | keep |
| Bao | 2020-07-02 | 119 | /blog/bao/ | keep |
| Sadnesses | 2020-07-04 | 165 | /blog/sadnesses/ | keep |
| New Site II | 2020-07-05 | 160 | /blog/new-site-ii/ | keep |
| Other Perspectives | 2020-07-07 | 228 | /blog/other-perspectives/ | keep |
| Chess and Attention | 2020-07-08 | 205 | /blog/chess-and-attention/ | keep |
| Mean Reviews | 2020-07-10 | 108 | /blog/mean-reviews/ | keep |
| Just Like Riding a Bike III | 2020-07-11 | 51 | /blog/just-like-riding-a-bike-iii/ | noindex |
| No Internet | 2020-07-12 | 79 | /blog/no-internet/ | noindex |
| Chess Programming | 2020-07-15 | 290 | /blog/chess-programming/ | keep |
| Things I Hate: Yachts | 2020-07-17 | 133 | /blog/things-i-hate-yachts/ | keep |
| Just Like Riding a Bike IV | 2020-07-20 | 121 | /blog/just-like-riding-a-bike-iv/ | keep |
| Things That Are More Therapeutic Than Therapy VII: Kayaking | 2020-07-21 | 80 | /blog/things-that-are-more-therapeutic-than-therapy-vii-kayaking/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Dubai Chess & Culture Club | 2020-07-23 | 113 | /blog/dubai-chess-culture-club/ | keep |
| Another Three Things To Be Grateful For VII | 2020-07-24 | 84 | /blog/another-three-things-to-be-grateful-for-vii/ | noindex |
| Boundaries | 2020-07-25 | 208 | /blog/boundaries/ | keep |
| Despair Is Not Useful | 2020-07-26 | 106 | /blog/despair-is-not-useful/ | keep |
| Happy Playlists | 2020-07-27 | 100 | /blog/happy-playlists/ | keep |
| Defining Characteristics | 2020-07-28 | 132 | /blog/defining-characteristics/ | keep |
| Stubborn Cats | 2020-07-29 | 109 | /blog/stubborn-cats/ | keep |
| Blogs Actually Worth Writing | 2020-07-30 | 185 | /blog/blogs-actually-worth-writing/ | keep |
| Choosing What To Think II | 2020-08-01 | 121 | /blog/choosing-what-to-think-ii/ | merge into "Choosing What To Think" |
| Music vs Podcasts | 2020-08-03 | 202 | /blog/music-vs-podcasts/ | keep |
| Things I'm Grateful For: Light Edition | 2020-08-04 | 98 | /blog/things-im-grateful-for-light-edition/ | noindex |
| The Struggles of Others | 2020-08-05 | 257 | /blog/the-struggles-of-others/ | keep |
| Weight Over Time | 2020-08-06 | 239 | /blog/weight-over-time/ | keep |
| Radical Listening | 2020-08-07 | 214 | /blog/radical-listening/ | keep |
| Things I Hate: Country Music | 2020-08-08 | 105 | /blog/things-i-hate-country-music/ | keep |
| Empathy | 2020-08-10 | 175 | /blog/empathy/ | keep |
| Vulfpeck Track 10 | 2020-08-11 | 183 | /blog/vulfpeck-track-10/ | keep |
| Protect Your Energy | 2020-08-12 | 185 | /blog/protect-your-energy/ | keep |
| Pandemic Expectations | 2020-08-13 | 149 | /blog/pandemic-expectations/ | keep |
| No Such Thing as Should | 2020-08-16 | 157 | /blog/no-such-thing-as-should/ | keep |
| Choosing What To Think III | 2020-08-18 | 140 | /blog/choosing-what-to-think-iii/ | merge into "Choosing What To Think" |
| Friends | 2020-08-19 | 169 | /blog/friends/ | keep |
| Therapy Deja Vu II | 2020-08-20 | 195 | /blog/therapy-deja-vu-ii/ | keep |
| It's Only Fun When It Hurts | 2020-08-21 | 115 | /blog/its-only-fun-when-it-hurts/ | keep |
| Singalongs | 2020-08-22 | 113 | /blog/singalongs/ | keep |
| Choosing What To Think IV: Suppression vs Regulation | 2020-08-23 | 251 | /blog/choosing-what-to-think-iv-suppression-vs-regulation/ | merge into "Choosing What To Think" |
| I Love You IV | 2020-08-24 | 157 | /blog/i-love-you-iv/ | keep |
| Therapeutic Work is Draining | 2020-08-25 | 127 | /blog/therapeutic-work-is-draining/ | keep |
| Unwanted Feelings | 2020-08-26 | 115 | /blog/unwanted-feelings/ | keep |
| Things That Are More Therapeutic Than Therapy VIII: Going To The Pub | 2020-08-28 | 118 | /blog/things-that-are-more-therapeutic-than-therapy-viii-going-to-the-pub/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Post Punk | 2020-08-29 | 174 | /blog/post-punk/ | keep |
| Fall Guys | 2020-08-30 | 99 | /blog/fall-guys/ | noindex |
| Vale Earth Fair | 2020-08-31 | 128 | /blog/vale-earth-fair/ | keep |
| Feeling Overwhelmed II | 2020-09-01 | 182 | /blog/feeling-overwhelmed-ii/ | keep |
| Ice Cream Victories | 2020-09-02 | 210 | /blog/ice-cream-victories/ | keep |
| Proctrasinating Homework | 2020-09-03 | 90 | /blog/proctrasinating-homework/ | noindex |
| Small Hands | 2020-09-04 | 161 | /blog/small-hands/ | keep |
| Killing Eve | 2020-09-05 | 68 | /blog/killing-eve/ | noindex |
| Half marathon in the books IV | 2020-09-06 | 118 | /blog/half-marathon-in-the-books-iv/ | keep |
| Media Bingeing | 2020-09-07 | 153 | /blog/media-bingeing/ | keep |
| Return of the Candidates | 2020-09-08 | 202 | /blog/return-of-the-candidates/ | keep |
| Destressing | 2020-09-09 | 80 | /blog/destressing/ | noindex |
| Last Night of the Proms | 2020-09-12 | 184 | /blog/last-night-of-the-proms/ | keep |
| Presence | 2020-09-13 | 96 | /blog/presence/ | noindex |
| Ambiguous Jokes | 2020-09-15 | 88 | /blog/ambiguous-jokes/ | noindex |
| Zero Notifications | 2020-09-16 | 196 | /blog/zero-notifications/ | keep |
| Thinking Before Speaking | 2020-09-17 | 174 | /blog/thinking-before-speaking/ | keep |
| Mugs | 2020-09-18 | 149 | /blog/mugs/ | keep |
| Long Overdue Tasks | 2020-09-19 | 127 | /blog/long-overdue-tasks/ | keep |
| Moving Out | 2020-09-20 | 110 | /blog/moving-out/ | keep |
| Last Day of Summer | 2020-09-21 | 147 | /blog/last-day-of-summer/ | keep |
| Last Day Of Summer II | 2020-09-22 | 111 | /blog/last-day-of-summer-ii/ | keep |
| Voice Notes | 2020-09-23 | 176 | /blog/voice-notes/ | keep |
| When Was The Last Time You Just Listened? | 2020-09-25 | 158 | /blog/when-was-the-last-time-you-just-listened/ | keep |
| Moving Out II | 2020-09-26 | 121 | /blog/moving-out-ii/ | keep |
| Slow Internet | 2020-09-27 | 63 | /blog/slow-internet/ | noindex |
| Directionlessness | 2020-09-28 | 140 | /blog/directionlessness/ | keep |
| Moving Out III | 2020-09-29 | 106 | /blog/moving-out-iii/ | keep |
| Endless Disco | 2020-09-30 | 175 | /blog/endless-disco/ | keep |
| Hacktoberfest | 2020-10-02 | 109 | /blog/hacktoberfest/ | keep |
| Media Fatigue | 2020-10-03 | 204 | /blog/media-fatigue/ | keep |
| My Soul Toupee | 2020-10-04 | 246 | /blog/my-soul-toupee/ | keep |
| Manifestos II | 2020-10-05 | 215 | /blog/manifestos-ii/ | keep |
| Naps | 2020-10-06 | 79 | /blog/naps/ | noindex |
| Inside Out | 2020-10-07 | 148 | /blog/inside-out/ | keep |
| Quantitative Analysis | 2020-10-08 | 142 | /blog/quantitative-analysis/ | keep |
| Manifestos III | 2020-10-09 | 234 | /blog/manifestos-iii/ | keep |
| Hangovers | 2020-10-10 | 87 | /blog/hangovers/ | noindex |
| Strangers' Validation | 2020-10-12 | 50 | /blog/strangers-validation/ | noindex |
| Strangers' Validation II: Niche Memes | 2020-10-13 | 108 | /blog/strangers-validation-ii-niche-memes/ | keep |
| Drunk Buys | 2020-10-14 | 105 | /blog/drunk-buys/ | keep |
| Getting Your Hopes Up | 2020-10-16 | 92 | /blog/getting-your-hopes-up/ | noindex |
| Outdoor Bouldering | 2020-10-17 | 176 | /blog/outdoor-bouldering/ | keep |
| Doing Nothing | 2020-10-18 | 131 | /blog/doing-nothing/ | keep |
| New Job | 2020-10-19 | 128 | /blog/new-job/ | keep |
| How Should You Write? | 2020-10-20 | 231 | /blog/how-should-you-write/ | keep |
| Lost For Things To Do | 2020-10-21 | 45 | /blog/lost-for-things-to-do/ | noindex |
| The First Honk | 2020-10-23 | 68 | /blog/the-first-honk/ | noindex |
| Sweating The Odds | 2020-10-24 | 95 | /blog/sweating-the-odds/ | noindex |
| The Basics | 2020-10-25 | 245 | /blog/the-basics/ | keep |
| It's Dark | 2020-10-26 | 88 | /blog/its-dark/ | noindex |
| How Far To Go | 2020-10-27 | 140 | /blog/how-far-to-go/ | keep |
| Taikyoku Shogi | 2020-10-28 | 160 | /blog/taikyoku-shogi/ | keep |
| Last Days | 2020-10-29 | 203 | /blog/last-days/ | keep |
| I Can't Wait To Be Old | 2020-10-30 | 128 | /blog/i-cant-wait-to-be-old/ | keep |
| Exploring | 2020-10-31 | 165 | /blog/exploring/ | keep |
| Think Less | 2020-11-01 | 143 | /blog/think-less/ | keep |
| Ten Things I'm Looking Forward To Moving For | 2020-11-03 | 248 | /blog/ten-things-im-looking-forward-to-moving-for/ | keep |
| Some More Thoughts About Weight Loss II | 2020-11-05 | 172 | /blog/some-more-thoughts-about-weight-loss-ii/ | merge into "Some More Thoughts About Weight Loss" |
| Choosing What To Think V: Banishment | 2020-11-06 | 142 | /blog/choosing-what-to-think-v-banishment/ | merge into "Choosing What To Think" |
| Election Day II | 2020-11-07 | 138 | /blog/election-day-ii/ | keep |
| 26 | 2020-11-08 | 180 | /blog/26/ | keep |
| One Tab | 2020-11-09 | 137 | /blog/one-tab/ | keep |
| I'm Bad at Guitar | 2020-11-10 | 198 | /blog/im-bad-at-guitar/ | keep |
| Too Close To Home | 2020-11-11 | 218 | /blog/too-close-to-home/ | keep |
| Curiosity | 2020-11-12 | 129 | /blog/curiosity/ | keep |
| Manifold Garden | 2020-11-13 | 98 | /blog/manifold-garden/ | noindex |
| Just Like Riding a Bike V | 2020-11-15 | 142 | /blog/just-like-riding-a-bike-v/ | keep |
| One Tab II | 2020-11-16 | 136 | /blog/one-tab-ii/ | keep |
| Things That Are More Therapeutic Than Therapy IX: Podcasts | 2020-11-17 | 127 | /blog/things-that-are-more-therapeutic-than-therapy-ix-podcasts/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Krill Waves Radio | 2020-11-18 | 49 | /blog/krill-waves-radio/ | noindex |
| Groundhog Day | 2020-11-19 | 277 | /blog/groundhog-day/ | keep |
| Things I'm Looking Forward To After The Pandemic I: Live Music | 2020-11-20 | 201 | /blog/things-im-looking-forward-to-after-the-pandemic-i-live-music/ | keep |
| KG Review | 2020-11-21 | 273 | /blog/kg-review/ | keep |
| Things I'm Looking Forward To After The Pandemic II: Seeing Friends | 2020-11-22 | 119 | /blog/things-im-looking-forward-to-after-the-pandemic-ii-seeing-friends/ | keep |
| The Queen's Gambit | 2020-11-23 | 189 | /blog/the-queens-gambit/ | keep |
| Things To Write About | 2020-11-24 | 257 | /blog/things-to-write-about/ | keep |
| Things That Are More Therapeutic Than Therapy X: Journaling | 2020-11-25 | 125 | /blog/things-that-are-more-therapeutic-than-therapy-x-journaling/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Prisencolinensinainciusol | 2020-11-27 | 115 | /blog/prisencolinensinainciusol/ | keep |
| Things That Are More Therapeutic Than Therapy XI: Sleep | 2020-11-28 | 163 | /blog/things-that-are-more-therapeutic-than-therapy-xi-sleep/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Productive Overthinking | 2020-11-29 | 204 | /blog/productive-overthinking/ | keep |
| Sarkese Digital Nomads | 2020-11-30 | 258 | /blog/sarkese-digital-nomads/ | keep |
| Christmas Season | 2020-12-01 | 131 | /blog/christmas-season/ | keep |
| Things I'm Looking Forward To After The Pandemic III: Floating | 2020-12-02 | 93 | /blog/things-im-looking-forward-to-after-the-pandemic-iii-floating/ | noindex |
| Forgetting | 2020-12-03 | 162 | /blog/forgetting/ | keep |
| Sober Socialising | 2020-12-05 | 152 | /blog/sober-socialising/ | keep |
| Shingeki no Kyojin Season 4 | 2020-12-06 | 147 | /blog/shingeki-no-kyojin-season-4/ | keep |
| Some More Thoughts About Weight Loss IV | 2020-12-07 | 147 | /blog/some-more-thoughts-about-weight-loss-iv/ | merge into "Some More Thoughts About Weight Loss" |
| Ice Skating | 2020-12-08 | 139 | /blog/ice-skating/ | keep |
| The Night Before Christmas | 2020-12-09 | 164 | /blog/the-night-before-christmas/ | keep |
| A Retraction | 2020-12-10 | 109 | /blog/a-retraction/ | keep |
| Things I'm Looking Forward To After The Pandemic IV: Climbing Gyms | 2020-12-11 | 95 | /blog/things-im-looking-forward-to-after-the-pandemic-iv-climbing-gyms/ | noindex |
| Clean Environment Clean Mind | 2020-12-12 | 50 | /blog/clean-environment-clean-mind/ | noindex |
| Cooking For Other People | 2020-12-13 | 126 | /blog/cooking-for-other-people/ | keep |
| Album Of The Year 2020 | 2020-12-14 | 252 | /blog/album-of-the-year-2020/ | keep |
| Tired All The Time | 2020-12-15 | 80 | /blog/tired-all-the-time/ | noindex |
| Crossfit | 2020-12-16 | 129 | /blog/crossfit/ | keep |
| Imposter Syndrome | 2020-12-17 | 88 | /blog/imposter-syndrome/ | noindex |
| Wasted Days | 2020-12-18 | 128 | /blog/wasted-days/ | keep |
| Christmas Nights Out | 2020-12-19 | 164 | /blog/christmas-nights-out/ | keep |
| Video Games | 2020-12-20 | 160 | /blog/video-games/ | keep |
| Crossfit II | 2020-12-21 | 123 | /blog/crossfit-ii/ | keep |
| Christmanxiety | 2020-12-22 | 120 | /blog/christmanxiety/ | keep |
| Dry January | 2020-12-23 | 172 | /blog/dry-january/ | keep |
| Missed Hits | 2020-12-24 | 75 | /blog/missed-hits/ | noindex |
| Christmas II | 2020-12-25 | 147 | /blog/christmas-ii/ | keep |
| Go First Impressions | 2020-12-26 | 198 | /blog/go-first-impressions/ | keep |
| Aeroplane Mode | 2020-12-27 | 87 | /blog/aeroplane-mode/ | noindex |
| Lightbulb Moments | 2020-12-28 | 129 | /blog/lightbulb-moments/ | keep |
| December Blues | 2020-12-29 | 115 | /blog/december-blues/ | keep |
| Trumpet | 2020-12-30 | 87 | /blog/trumpet/ | noindex |
| New Year's Resolutions II | 2020-12-31 | 145 | /blog/new-years-resolutions-ii/ | keep |
| A Good Start | 2021-01-01 | 67 | /blog/a-good-start/ | noindex |
| Go Karting | 2021-01-02 | 121 | /blog/go-karting/ | keep |
| Journaling I | 2021-01-03 | 166 | /blog/journaling-i/ | keep |
| Waking Up | 2021-01-05 | 140 | /blog/waking-up/ | keep |
| America | 2021-01-06 | 119 | /blog/america/ | keep |
| The Digital Greenhouse | 2021-01-07 | 142 | /blog/the-digital-greenhouse/ | keep |
| Alexi Laiho | 2021-01-08 | 229 | /blog/alexi-laiho/ | keep |
| Weightlifting | 2021-01-09 | 91 | /blog/weightlifting/ | noindex |
| High Stakes Blogging | 2021-01-10 | 111 | /blog/high-stakes-blogging/ | keep |
| 2021 Goals | 2021-01-11 | 100 | /blog/2021-goals/ | keep |
| Running in the Dark | 2021-01-12 | 136 | /blog/running-in-the-dark/ | keep |
| Noughts and Crosses | 2021-01-13 | 112 | /blog/noughts-and-crosses/ | keep |
| Emotional Riches | 2021-01-14 | 134 | /blog/emotional-riches/ | keep |
| 2021 Goals II | 2021-01-15 | 184 | /blog/2021-goals-ii/ | keep |
| New Job Nerves | 2021-01-16 | 194 | /blog/new-job-nerves/ | keep |
| Joy Division | 2021-01-17 | 126 | /blog/joy-division/ | keep |
| Blue Monday II | 2021-01-18 | 147 | /blog/blue-monday-ii/ | keep |
| Some More Thoughts About Weight Loss V | 2021-01-19 | 289 | /blog/some-more-thoughts-about-weight-loss-v/ | merge into "Some More Thoughts About Weight Loss" |
| Prententious Blogs | 2021-01-20 | 118 | /blog/prententious-blogs/ | keep |
| Some More Thoughts About Weight Loss VI | 2021-01-21 | 112 | /blog/some-more-thoughts-about-weight-loss-vi/ | merge into "Some More Thoughts About Weight Loss" |
| Lockdown Take Two | 2021-01-23 | 181 | /blog/lockdown-take-two/ | keep |
| Some More Thoughts About Weight Loss VII | 2021-01-24 | 120 | /blog/some-more-thoughts-about-weight-loss-vii/ | merge into "Some More Thoughts About Weight Loss" |
| Lockdown Goals I | 2021-01-25 | 90 | /blog/lockdown-goals-i/ | noindex |
| Being a Mid Level Dev | 2021-01-26 | 220 | /blog/being-a-mid-level-dev/ | keep |
| Lockdown Take Two II | 2021-01-27 | 96 | /blog/lockdown-take-two-ii/ | noindex |
| Running in the Dark II | 2021-01-28 | 103 | /blog/running-in-the-dark-ii/ | keep |
| Finishing What I Start | 2021-01-29 | 148 | /blog/finishing-what-i-start/ | keep |
| Lockdown Goals II: Yoga | 2021-01-31 | 146 | /blog/lockdown-goals-ii-yoga/ | keep |
| Lockdown Take Two III | 2021-02-02 | 147 | /blog/lockdown-take-two-iii/ | keep |
| Window Shopping for Flats | 2021-02-03 | 152 | /blog/window-shopping-for-flats/ | keep |
| Time To Talk | 2021-02-04 | 161 | /blog/time-to-talk/ | keep |
| For the first time Review | 2021-02-05 | 236 | /blog/for-the-first-time-review/ | keep |
| Feeling On | 2021-02-06 | 241 | /blog/feeling-on/ | keep |
| There's Snow Hope | 2021-02-08 | 124 | /blog/theres-snow-hope/ | keep |
| Frustration | 2021-02-09 | 277 | /blog/frustration/ | keep |
| Being a Mid Level Dev II | 2021-02-10 | 252 | /blog/being-a-mid-level-dev-ii/ | keep |
| Fiction and Escapism | 2021-02-12 | 185 | /blog/fiction-and-escapism/ | keep |
| Power Cuts | 2021-02-13 | 113 | /blog/power-cuts/ | keep |
| Valentine's Day II | 2021-02-14 | 283 | /blog/valentines-day-ii/ | keep |
| The Vanishing at the Cecil Hotel | 2021-02-15 | 237 | /blog/the-vanishing-at-the-cecil-hotel/ | keep |
| A Year Without Flying | 2021-02-16 | 279 | /blog/a-year-without-flying/ | keep |
| Lent | 2021-02-17 | 156 | /blog/lent/ | keep |
| Emotional Fragility | 2021-02-18 | 175 | /blog/emotional-fragility/ | keep |
| Moving | 2021-02-20 | 158 | /blog/moving/ | keep |
| Blitz | 2021-02-22 | 161 | /blog/blitz/ | keep |
| Emotional Riches II | 2021-02-23 | 142 | /blog/emotional-riches-ii/ | keep |
| Online Chess Tournaments II | 2021-02-24 | 168 | /blog/online-chess-tournaments-ii/ | keep |
| A Keen Idiot | 2021-02-25 | 85 | /blog/a-keen-idiot/ | noindex |
| The Laughing Sea | 2021-02-27 | 219 | /blog/the-laughing-sea/ | keep |
| Lockdown Goals III: Yoga Complete | 2021-02-28 | 208 | /blog/lockdown-goals-iii-yoga-complete/ | keep |
| Blitz II | 2021-03-01 | 212 | /blog/blitz-ii/ | keep |
| Cold Bones | 2021-03-02 | 168 | /blog/cold-bones/ | keep |
| Big Company Opportunities | 2021-03-03 | 221 | /blog/big-company-opportunities/ | keep |
| Post Pandemic Plans | 2021-03-05 | 267 | /blog/post-pandemic-plans/ | keep |
| Not Jinxing It II | 2021-03-06 | 268 | /blog/not-jinxing-it-ii/ | keep |
| Making The Most Of It | 2021-03-07 | 126 | /blog/making-the-most-of-it/ | keep |
| Things That Are More Therapeutic Than Therapy XII: Yoga | 2021-03-08 | 138 | /blog/things-that-are-more-therapeutic-than-therapy-xii-yoga/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| A Good Thing A Day | 2021-03-10 | 185 | /blog/a-good-thing-a-day/ | keep |
| Old Code | 2021-03-12 | 178 | /blog/old-code/ | keep |
| 1000 Posts | 2021-03-19 | 231 | /blog/1000-posts/ | keep |
| Writing Up Old Ideas XII: Round 1 Conclusion | 2021-04-06 | 280 | /blog/writing-up-old-ideas-xii-round-1-conclusion/ | keep |
| Flat Hunting | 2021-04-12 | 88 | /blog/flat-hunting/ | noindex |
| No News | 2021-04-15 | 241 | /blog/no-news/ | keep |
| Bloomfield | 2021-04-17 | 255 | /blog/bloomfield/ | keep |
| It's Really Happening | 2021-04-19 | 92 | /blog/its-really-happening/ | noindex |
| It's Really Happening II | 2021-04-20 | 170 | /blog/its-really-happening-ii/ | keep |
| Misbeliefs | 2021-04-21 | 298 | /blog/misbeliefs/ | keep |
| The Imminent Office | 2021-04-23 | 164 | /blog/the-imminent-office/ | keep |
| Self Analysis is Exhausting | 2021-04-24 | 276 | /blog/self-analysis-is-exhausting/ | keep |
| I Miss Lockdown | 2021-04-28 | 197 | /blog/i-miss-lockdown/ | keep |
| Stressed | 2021-04-29 | 268 | /blog/stressed/ | keep |
| The Laughing Sea II | 2021-05-01 | 195 | /blog/the-laughing-sea-ii/ | keep |
| Packing | 2021-05-04 | 195 | /blog/packing/ | keep |
| New Routines | 2021-05-06 | 158 | /blog/new-routines/ | keep |
| Liberation Day | 2021-05-09 | 128 | /blog/liberation-day/ | keep |
| Procrastinanxiety | 2021-05-11 | 235 | /blog/procrastinanxiety/ | keep |
| Argos | 2021-05-12 | 122 | /blog/argos/ | keep |
| No Scale | 2021-05-13 | 212 | /blog/no-scale/ | keep |
| A Week In London | 2021-05-14 | 266 | /blog/a-week-in-london/ | keep |
| Back Floating | 2021-05-15 | 114 | /blog/back-floating/ | keep |
| Tower Bridge Lunch Reviews | 2021-05-16 | 138 | /blog/tower-bridge-lunch-reviews/ | keep as merge target |
| Tower Bridge Lunch Reviews V: Omoide | 2021-05-20 | 264 | /blog/tower-bridge-lunch-reviews-v-omoide/ | merge into "Tower Bridge Lunch Reviews" |
| Tower Bridge Lunch Reviews VI: Chilango | 2021-05-21 | 245 | /blog/tower-bridge-lunch-reviews-vi-chilango/ | merge into "Tower Bridge Lunch Reviews" |
| New Routines II | 2021-05-24 | 194 | /blog/new-routines-ii/ | keep |
| Dry June | 2021-05-25 | 202 | /blog/dry-june/ | keep |
| Meet The Team | 2021-05-26 | 155 | /blog/meet-the-team/ | keep |
| Shorts Weather | 2021-05-27 | 92 | /blog/shorts-weather/ | noindex |
| Overstimulated | 2021-05-28 | 126 | /blog/overstimulated/ | keep |
| Overstimulated II | 2021-05-29 | 178 | /blog/overstimulated-ii/ | keep |
| Resources | 2021-05-30 | 250 | /blog/resources/ | keep |
| Things That Are More Therapeutic Than Therapy XIV: Sunbathing | 2021-06-01 | 208 | /blog/things-that-are-more-therapeutic-than-therapy-xiv-sunbathing/ | merge into "Things That Are More Therapeutic Than Therapy: Running" |
| Heat | 2021-06-03 | 209 | /blog/heat/ | keep |
| Spellchecking | 2021-06-06 | 75 | /blog/spellchecking/ | noindex |
| Cheap Sleep Upgrades | 2021-06-08 | 183 | /blog/cheap-sleep-upgrades/ | keep |
| Track Debut | 2021-06-09 | 220 | /blog/track-debut/ | keep |
| Vaccinations Booked | 2021-06-10 | 95 | /blog/vaccinations-booked/ | noindex |
| Vegas Envy | 2021-06-11 | 174 | /blog/vegas-envy/ | keep |
| Record Stores | 2021-06-12 | 194 | /blog/record-stores/ | keep |
| Vintage Shops | 2021-06-13 | 129 | /blog/vintage-shops/ | keep |
| Brighton | 2021-06-14 | 168 | /blog/brighton/ | keep |
| Free Solo II | 2021-06-16 | 247 | /blog/free-solo-ii/ | keep |
| Back To Work | 2021-06-17 | 188 | /blog/back-to-work/ | keep |
| Full of Surprises | 2021-06-18 | 98 | /blog/full-of-surprises/ | noindex |
| Self Pity is Useless | 2021-06-20 | 173 | /blog/self-pity-is-useless/ | keep |
| Overgamification | 2021-06-21 | 264 | /blog/overgamification/ | keep |
| Exercise Inertia | 2021-06-22 | 220 | /blog/exercise-inertia/ | keep |
| Ultra Cancelled | 2021-06-24 | 186 | /blog/ultra-cancelled/ | keep |
| Mental Restlessness | 2021-06-25 | 145 | /blog/mental-restlessness/ | keep |
| Getting Ahead of Myself | 2021-06-26 | 141 | /blog/getting-ahead-of-myself/ | keep |
| Not Saying Much | 2021-06-27 | 223 | /blog/not-saying-much/ | keep |
| A New Ultra | 2021-06-29 | 250 | /blog/a-new-ultra/ | keep |
| Out Of Your Head | 2021-07-02 | 195 | /blog/out-of-your-head/ | keep |
| Doing Nothing II | 2021-07-03 | 150 | /blog/doing-nothing-ii/ | keep |
| Pork and Beans | 2021-07-05 | 210 | /blog/pork-and-beans/ | keep |
| The Right Team | 2021-07-06 | 95 | /blog/the-right-team/ | noindex |
| Locked Out | 2021-07-07 | 122 | /blog/locked-out/ | keep |
| Necessary Resources | 2021-07-08 | 123 | /blog/necessary-resources/ | keep |
| Football Chat | 2021-07-09 | 178 | /blog/football-chat/ | keep |
| Procrastinanxiety II | 2021-07-12 | 156 | /blog/procrastinanxiety-ii/ | keep |
| Reunited With My Baby | 2021-07-13 | 173 | /blog/reunited-with-my-baby/ | keep |
| Database Terror | 2021-07-14 | 108 | /blog/database-terror/ | keep |
| Ryoji Ikeda at 180 The Strand | 2021-07-15 | 287 | /blog/ryoji-ikeda-at-180-the-strand/ | keep |
| Freedom Day Looms | 2021-07-16 | 119 | /blog/freedom-day-looms/ | keep |
| Superpowers | 2021-07-17 | 225 | /blog/superpowers/ | keep |
| Driven or Obsessive? | 2021-07-19 | 246 | /blog/driven-or-obsessive/ | keep |
| Highlights and Lowlights | 2021-07-20 | 227 | /blog/highlights-and-lowlights/ | keep |
| I Miss Lockdown II | 2021-07-21 | 196 | /blog/i-miss-lockdown-ii/ | keep |
| Immortal Airlines | 2021-07-22 | 163 | /blog/immortal-airlines/ | keep |
| Tokyo 2020 | 2021-07-23 | 183 | /blog/tokyo-2020/ | keep |
| Video Games II | 2021-07-25 | 166 | /blog/video-games-ii/ | keep |
| I Don't Like Running | 2021-07-26 | 186 | /blog/i-dont-like-running/ | keep |
| Leicester Square | 2021-07-28 | 149 | /blog/leicester-square/ | keep |
| Locked Out II | 2021-07-29 | 64 | /blog/locked-out-ii/ | noindex |
| Leicester Square II: The M&M Shop | 2021-07-30 | 143 | /blog/leicester-square-ii-the-mm-shop/ | keep |
| Priorities II | 2021-08-01 | 121 | /blog/priorities-ii/ | keep |
| Caffeine Detox | 2021-08-02 | 66 | /blog/caffeine-detox/ | noindex |
| Tokyo 2020 II: Climbing | 2021-08-03 | 278 | /blog/tokyo-2020-ii-climbing/ | keep |
| A Healthy Role Model | 2021-08-04 | 211 | /blog/a-healthy-role-model/ | keep |
| I Hate It When People Are Nice To Me II | 2021-08-05 | 53 | /blog/i-hate-it-when-people-are-nice-to-me-ii/ | noindex |
| Vaccinated | 2021-08-06 | 135 | /blog/vaccinated/ | keep |
| SINNER GET READY Review | 2021-08-07 | 204 | /blog/sinner-get-ready-review/ | keep |
| Anger Management | 2021-08-08 | 240 | /blog/anger-management/ | keep |
| Caffeine Detox II | 2021-08-09 | 173 | /blog/caffeine-detox-ii/ | keep |
| I Don't Like Running II | 2021-08-10 | 144 | /blog/i-dont-like-running-ii/ | keep |
| Weekend Breaks | 2021-08-12 | 200 | /blog/weekend-breaks/ | keep |
| Overpacking | 2021-08-13 | 87 | /blog/overpacking/ | noindex |
| Leeds I | 2021-08-14 | 184 | /blog/leeds-i/ | keep |
| Locked Out III | 2021-08-15 | 194 | /blog/locked-out-iii/ | keep |
| Kentucky Route Zero | 2021-08-17 | 290 | /blog/kentucky-route-zero/ | keep |
| Polyglotism | 2021-08-18 | 290 | /blog/polyglotism/ | keep |
| Too Much Holiday | 2021-08-19 | 173 | /blog/too-much-holiday/ | keep |
| Ross From Friends | 2021-08-20 | 174 | /blog/ross-from-friends/ | keep |
| Revision | 2021-08-21 | 187 | /blog/revision/ | keep |
| AWS Certified | 2021-08-23 | 215 | /blog/aws-certified/ | keep |
| 2021 Goals III | 2021-08-24 | 180 | /blog/2021-goals-iii/ | keep |
| The Pub | 2021-08-26 | 130 | /blog/the-pub/ | keep |
| Out of Office | 2021-08-27 | 95 | /blog/out-of-office/ | noindex |
| Holiday Plans | 2021-08-28 | 158 | /blog/holiday-plans/ | keep |
| Margate | 2021-08-29 | 183 | /blog/margate/ | keep |
| Fear of Falling II | 2021-08-30 | 235 | /blog/fear-of-falling-ii/ | keep |
| Tapering | 2021-08-31 | 164 | /blog/tapering/ | keep |
| Brick Lane Beigels | 2021-09-01 | 190 | /blog/brick-lane-beigels/ | keep |
| I'm Bad At Running | 2021-09-02 | 190 | /blog/im-bad-at-running/ | keep |
| Flight Club | 2021-09-03 | 124 | /blog/flight-club/ | keep |
| Self Pity is Useless II | 2021-09-05 | 196 | /blog/self-pity-is-useless-ii/ | keep |
| Receiptify | 2021-09-06 | 184 | /blog/receiptify/ | keep |
| Flat Hunting II | 2021-09-08 | 262 | /blog/flat-hunting-ii/ | keep |
| The Matrix Resurrections | 2021-09-09 | 197 | /blog/the-matrix-resurrections/ | keep |
| Blog Embarrassment | 2021-09-12 | 209 | /blog/blog-embarrassment/ | keep |
| OFC Poker: The Gateway Drug | 2021-09-13 | 118 | /blog/ofc-poker-the-gateway-drug/ | keep |
| Uncomfortable Challenge | 2021-09-14 | 81 | /blog/uncomfortable-challenge/ | noindex |
| Playing at Being an Adult IV | 2021-09-15 | 224 | /blog/playing-at-being-an-adult-iv/ | keep |
| Recovery Running | 2021-09-16 | 159 | /blog/recovery-running/ | keep |
| RE: An Honest Living II | 2021-09-17 | 256 | /blog/re-an-honest-living-ii/ | keep |
| Trips Out of the City | 2021-09-18 | 127 | /blog/trips-out-of-the-city/ | keep |
| Fancy Dessert Places | 2021-09-19 | 97 | /blog/fancy-dessert-places/ | noindex |
| Always Wanting to be Liked | 2021-09-20 | 171 | /blog/always-wanting-to-be-liked/ | keep |
| OFC Poker II: The Game Is On | 2021-09-21 | 69 | /blog/ofc-poker-ii-the-game-is-on/ | noindex |
| I Really Want a Record Player | 2021-09-22 | 205 | /blog/i-really-want-a-record-player/ | keep |
| Shorter Days | 2021-09-23 | 95 | /blog/shorter-days/ | noindex |
| Perfectionism | 2021-09-26 | 125 | /blog/perfectionism/ | keep |
| I Want To Spend A Lot More Time Playing Video Games | 2021-09-27 | 293 | /blog/i-want-to-spend-a-lot-more-time-playing-video-games/ | keep |
| Mental Health Goals | 2021-09-28 | 247 | /blog/mental-health-goals/ | keep |
| How To Take A Holiday From Blogging | 2021-09-29 | 284 | /blog/how-to-take-a-holiday-from-blogging/ | keep |
| Strava | 2021-10-03 | 282 | /blog/strava/ | keep |
| 2021 Book Reviews VIII: Anna Karenina | 2021-10-05 | 274 | /blog/2021-book-reviews-viii-anna-karenina/ | keep |
| Mental Health Goals II | 2021-10-06 | 179 | /blog/mental-health-goals-ii/ | keep |
| Flat Hunting III | 2021-10-07 | 177 | /blog/flat-hunting-iii/ | keep |
| Tennis | 2021-10-08 | 143 | /blog/tennis/ | keep |
| Flat Hunting IV | 2021-10-09 | 173 | /blog/flat-hunting-iv/ | keep |
| A Quiet Mind | 2021-10-10 | 247 | /blog/a-quiet-mind/ | keep |
| Sable | 2021-10-11 | 98 | /blog/sable/ | noindex |
| Tennis II | 2021-10-12 | 124 | /blog/tennis-ii/ | keep |
| Mexico Day 26 | 2021-10-13 | 291 | /blog/mexico-day-26/ | keep |
| Retros | 2021-10-15 | 166 | /blog/retros/ | keep |
| Happy Blogoversary | 2021-10-16 | 156 | /blog/happy-blogoversary/ | keep |
| The Room II | 2021-10-17 | 199 | /blog/the-room-ii/ | keep |
| The French Dispatch | 2021-10-18 | 222 | /blog/the-french-dispatch/ | keep |
| London City Runners | 2021-10-19 | 265 | /blog/london-city-runners/ | keep |
| Blood | 2021-10-20 | 183 | /blog/blood/ | keep |
| Musical Regulation | 2021-10-21 | 274 | /blog/musical-regulation/ | keep |
| Winter Weather Running | 2021-10-22 | 125 | /blog/winter-weather-running/ | keep |
| Tennis III | 2021-10-24 | 119 | /blog/tennis-iii/ | keep |
| Dune | 2021-10-25 | 256 | /blog/dune/ | keep |
| Skincare | 2021-10-26 | 129 | /blog/skincare/ | keep |
| The Worst Kind of Firsts | 2021-10-27 | 211 | /blog/the-worst-kind-of-firsts/ | keep |
| Emotional Investment | 2021-10-28 | 156 | /blog/emotional-investment/ | keep |
| Emotional Investment II | 2021-10-29 | 106 | /blog/emotional-investment-ii/ | keep |
| The Cookie Disaster | 2021-10-30 | 169 | /blog/the-cookie-disaster/ | keep |
| Retreat Envy | 2021-10-31 | 281 | /blog/retreat-envy/ | keep |
| Birthday Stress | 2021-11-01 | 153 | /blog/birthday-stress/ | keep |
| Movember | 2021-11-02 | 199 | /blog/movember/ | keep |
| A Week Off Running | 2021-11-03 | 243 | /blog/a-week-off-running/ | keep |
| 2000 Kilometres | 2021-11-04 | 160 | /blog/2000-kilometres/ | keep |
| Critical Feedback | 2021-11-05 | 177 | /blog/critical-feedback/ | keep |
| Watchhouse | 2021-11-06 | 170 | /blog/watchhouse/ | keep |
| Birthday Gratitude | 2021-11-10 | 159 | /blog/birthday-gratitude/ | keep |
| Solo Gigs | 2021-11-11 | 221 | /blog/solo-gigs/ | keep |
| Metronomy | 2021-11-12 | 272 | /blog/metronomy/ | keep |
| Two Weeks Of Nothing | 2021-11-13 | 178 | /blog/two-weeks-of-nothing/ | keep |
| Moving Day II | 2021-11-14 | 144 | /blog/moving-day-ii/ | keep |
| New Flat | 2021-11-15 | 166 | /blog/new-flat/ | keep |
| Big Races & Bad Ideas | 2021-11-16 | 141 | /blog/big-races-bad-ideas/ | keep |
| The Louis Cole Big Band | 2021-11-17 | 259 | /blog/the-louis-cole-big-band/ | keep |
| Cooking | 2021-11-19 | 123 | /blog/cooking/ | keep |
| Daebak | 2021-11-20 | 284 | /blog/daebak/ | keep |
| A Week Of Running | 2021-11-21 | 169 | /blog/a-week-of-running/ | keep |
| International Films | 2021-11-22 | 197 | /blog/international-films/ | keep |
| The Commute | 2021-11-23 | 160 | /blog/the-commute/ | keep |
| Extreme Pair Programming | 2021-11-24 | 282 | /blog/extreme-pair-programming/ | keep |
| World Chess Championship 2021 | 2021-11-25 | 203 | /blog/world-chess-championship-2021/ | keep |
| Extreme Pair Programming II | 2021-11-26 | 200 | /blog/extreme-pair-programming-ii/ | keep |
| No Time To Say Anything | 2021-11-27 | 221 | /blog/no-time-to-say-anything/ | keep |
| Better Than Nothing | 2021-11-28 | 272 | /blog/better-than-nothing/ | keep |
| Back To Yoga | 2021-11-29 | 199 | /blog/back-to-yoga/ | keep |
| Advent of Code | 2021-11-30 | 155 | /blog/advent-of-code/ | keep |
| Christmas Gifts | 2021-12-02 | 107 | /blog/christmas-gifts/ | keep |
| Parkrun II | 2021-12-04 | 151 | /blog/parkrun-ii/ | keep |
| Early Starts | 2021-12-07 | 138 | /blog/early-starts/ | keep |
| 2022 Races | 2021-12-12 | 263 | /blog/2022-races/ | keep |
| Boosted | 2021-12-14 | 223 | /blog/boosted/ | keep |
| Christmas Gifts II | 2021-12-16 | 119 | /blog/christmas-gifts-ii/ | keep |
| A Proper Break | 2021-12-18 | 149 | /blog/a-proper-break/ | keep |
| Finally Moved In | 2021-12-19 | 129 | /blog/finally-moved-in/ | keep |
| Sick | 2021-12-21 | 173 | /blog/sick/ | keep |
| Algorithms | 2021-12-22 | 176 | /blog/algorithms/ | keep |
| Covid for Christmas | 2021-12-23 | 121 | /blog/covid-for-christmas/ | keep |
| Superstore | 2021-12-24 | 85 | /blog/superstore/ | noindex |
| Christmas III | 2021-12-25 | 79 | /blog/christmas-iii/ | noindex |
| Quarantine Day 4 | 2021-12-26 | 166 | /blog/quarantine-day-4/ | keep |
| Chess Commentators | 2021-12-27 | 245 | /blog/chess-commentators/ | keep |
| Enhanced Passive Followup | 2021-12-29 | 164 | /blog/enhanced-passive-followup/ | keep |
| 100 Hours | 2022-01-02 | 62 | /blog/100-hours/ | keep |
| Back in London | 2022-01-03 | 221 | /blog/back-in-london/ | keep |
| Feedback II | 2022-01-04 | 269 | /blog/feedback-ii/ | keep |
| OCC Lottery | 2022-01-06 | 142 | /blog/occ-lottery/ | keep |
| Another Week of Yoga | 2022-01-07 | 247 | /blog/another-week-of-yoga/ | keep |
| Back To The North Downs Way | 2022-01-09 | 273 | /blog/back-to-the-north-downs-way/ | keep |
| One Thing At A Time | 2022-01-10 | 98 | /blog/one-thing-at-a-time/ | noindex |
| The Book of Mormon | 2022-01-11 | 217 | /blog/the-book-of-mormon/ | keep |
| Quiztory | 2022-01-12 | 216 | /blog/quiztory/ | keep |
| Shobu | 2022-01-13 | 222 | /blog/shobu/ | keep |
| Mentoring III | 2022-01-14 | 212 | /blog/mentoring-iii/ | keep |
| A New Way To Run II | 2022-01-15 | 283 | /blog/a-new-way-to-run-ii/ | keep |
| Cooking II | 2022-01-16 | 158 | /blog/cooking-ii/ | keep |
| Leeds III | 2022-01-17 | 245 | /blog/leeds-iii/ | keep |
| Hot Sauce | 2022-01-19 | 297 | /blog/hot-sauce/ | keep |
| Overdoing It | 2022-01-20 | 285 | /blog/overdoing-it/ | keep |
| Baking | 2022-01-21 | 133 | /blog/baking/ | keep |
| RunThrough Olympic Park | 2022-01-22 | 295 | /blog/runthrough-olympic-park/ | keep |
| Tata Steel Masters 2022 | 2022-01-23 | 247 | /blog/tata-steel-masters-2022/ | keep |
| Better Than Medication | 2022-01-24 | 245 | /blog/better-than-medication/ | keep |
| Performance Review | 2022-01-25 | 229 | /blog/performance-review/ | keep |
| OCC Lottery II: Not This Year | 2022-01-26 | 165 | /blog/occ-lottery-ii-not-this-year/ | keep |
| Back to the Office II | 2022-01-27 | 105 | /blog/back-to-the-office-ii/ | keep |
| Rest Day | 2022-01-28 | 140 | /blog/rest-day/ | keep |
| Arc Envy | 2022-01-29 | 244 | /blog/arc-envy/ | keep |
| A Gift To Your Future Self | 2022-01-30 | 194 | /blog/a-gift-to-your-future-self/ | keep |
| I Know What To Do To Be Happy | 2022-02-03 | 200 | /blog/i-know-what-to-do-to-be-happy/ | keep |
| Wordle | 2022-02-04 | 97 | /blog/wordle/ | noindex |
| A Normal Sized Leg | 2022-02-08 | 146 | /blog/a-normal-sized-leg/ | keep |
| Priorities III | 2022-02-09 | 135 | /blog/priorities-iii/ | keep |
| Nationally Insured | 2022-02-10 | 43 | /blog/nationally-insured/ | noindex |
| Good Enough At Go | 2022-02-11 | 259 | /blog/good-enough-at-go/ | keep |
| Life Goals | 2022-02-13 | 271 | /blog/life-goals/ | keep |
| Valentine's Day III | 2022-02-14 | 98 | /blog/valentines-day-iii/ | noindex |
| Software | 2025-04-05 | 215 | /software/ | keep |
| A Good Life | 2025-04-06 | 93 | /a-good-life/ | noindex |
| Fuzzy Heuristics and Blurry Lenses | 2025-04-06 | 0 | /blog/fuzzy-heuristics-and-blurry-lenses/ | noindex (empty body; finish or unpublish) |

</details>

## 7. Verification

Production build (`hugo --environment production`, Hugo 0.128.1): no errors. The 7 WARN lines are the same as on `main` (duplicate menu entries and the navbar JS layout). Every commit on the branch also builds on its own.

| Check | Homepage `/` | Recent: `/blog/chestertons-fence-as-a-core-concept-in-psychology/` | Old (2017): `/blog/looking-in-the-mirror/` |
|---|---|---|---|
| `<title>` | Jonny Spicer | Chesterton's Fence as a core concept in psychology \| Jonny Spicer | Looking in the mirror \| Jonny Spicer |
| description | Front matter ✓ | Excerpt ✓ (starts with the Chesterton quote, so worth writing one) | Excerpt ✓ |
| canonical | `https://jonnyspicer.com/` ✓ | Self, absolute ✓ | Self, absolute ✓ |
| OG tags | title, description, url, image, type=website ✓ | + type=article, published/modified ✓ | + type=article ✓ |
| Twitter card | summary_large_image ✓ | ✓ | ✓ |
| JSON-LD | Person + WebSite, valid ✓ | Person + BlogPosting, valid ✓ | Person + BlogPosting, valid ✓ |
| `lang` | en-GB ✓ | en-GB ✓ | en-GB ✓ |

- `public/robots.txt` ✓, with the `Sitemap:` line.
- `public/sitemap.xml` ✓: well-formed XML with 1,399 URLs and 0 taxonomy, `/draft/` or `/page/` URLs.

## Other findings (not changed)

- **A URL with a slash in it:** `/blog/reflections-following-eag-london-conference-strategy-and-in/outgroup-dynamics/`. The "/" in the title "In/Outgroup" became a path segment. The page works, but to tidy it, set `slug:` in its front matter and add the old URL as an alias.
- **Posts that share a title with a taxonomy page**, such as the post *Running* and the category *Running*, or *Caffeine Detox* and its series. That gives two pages titled "Running | Jonny Spicer". It's minor, and category titles could be prefixed in `seo/title.html` if you care.
- **Case-duplicate categories:** "Diet And Fitness" vs "Diet and Fitness", and "Film And TV" vs "Film and TV". Hugo merges them into one URL, but the display label varies.
- **`<base href>`** is still in `<head>`. I kept it because old imported posts may rely on it for relative links. Removing it would be cleaner, but test before you do.
- **111 series pages for 393 posts.** Many series have one or two posts. They're now out of the sitemap but still indexable. Consider `noindex` on series terms with fewer than 3 posts.
- **Cross-posts:** *What I Learned In My First Year of Community Building* was originally published on the EA Forum. That's fine, but if you'd rather your site be the canonical copy, ask for a canonical link back from the Forum version, or add a `canonical:` front-matter override (not implemented yet).
- **`new.py`** could add `description: ""` and `lastmod:` stubs to the front matter it generates, which would make the habit automatic.

## Checklist: things that can't be done from the repo

- [ ] **Cloudflare dashboard:** check Security → Bots → AI crawler blocking, and any Cloudflare-managed robots.txt, which can override the repo's robots.txt. **Note: jonnyspicer.com currently resolves to CloudFront (Amplify) with Route53 DNS, not Cloudflare.** The only Cloudflare piece on the site is the Web Analytics beacon script, which doesn't affect crawling. If you put the domain behind Cloudflare later, check those settings then. Today, the robots.txt served is the one in this repo. Also check the **Amplify console** for redirect or rewrite rules or custom headers (for example `X-Robots-Tag`) that would override the repo.
- [ ] **Google Search Console:** add the site (a Domain property via a Route53 TXT record is simplest) and submit `https://jonnyspicer.com/sitemap.xml`. After the deploy, use URL Inspection on a couple of posts to confirm the new canonical and structured data are picked up.
- [ ] **Bing Webmaster Tools:** add the site (you can import from GSC) and submit the sitemap. Bing's index also feeds ChatGPT search and DuckDuckGo.
- [ ] **Umami:** check referrers from `chatgpt.com`, `perplexity.ai`, `claude.ai` and `gemini.google.com`, plus `copilot.microsoft.com`, as a baseline now and again in 4–8 weeks.
- [ ] Fill in the `sameAs` placeholders above.
- [ ] Write `description:` front matter for your 20–30 most important posts, starting with the hub posts and Bestof.
- [ ] Decide on the thin-content actions (section 5) and the hub pages (section 4).

## Agent-friendliness (2026-10-15)

- **`/posts.json`**: compact index of the ~611 indexed posts and essays (title, URL, date, word count, categories, plus `updated` where it differs from the date), with the category list. It's about 20k tokens, so an agent can see the whole catalogue in one fetch, whereas `/archive/` is ~580 KB. It's linked from every page's `<head>` and matches the sitemap exactly.
- **RSS**: the site feed (`/index.xml`) now carries the latest 50 *posts* with full content. Root-relative links and images are made absolute. Previously the feed led with /about/ and /contact/ (because they have a menu weight), mixed in garden pages, and carried only ~200-character summaries.
- **`<article>`**: wraps blog, essay and garden page bodies, for reader-mode style extraction.
- **`/chat/`**: noindexed. It's a JavaScript-only app with nothing to read without JS.
