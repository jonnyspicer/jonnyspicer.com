# About Page Timeline Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a vertical life timeline (1994-2026) below the existing About page content, with good events on the left and bad events on the right.

**Architecture:** Pure HTML + SCSS. Timeline HTML goes directly into `content/about.md` as raw HTML. Styles live in a new `_timeline.scss` partial imported by `style.scss`. No JavaScript needed.

**Tech Stack:** Hugo 0.128, SCSS, HTML

---

### Task 1: Create worktree

**Step 1: Create a worktree and branch for this feature**

Run: `wt switch --create feature/about-timeline`

**Step 2: Verify you're in the new worktree**

Run: `git branch --show-current`
Expected: `feature/about-timeline`

**Step 3: Commit the design doc**

```bash
git add docs/plans/2026-02-17-about-timeline-design.md
git commit -m "docs: add about timeline design doc"
```

---

### Task 2: Create the SCSS partial

**Files:**
- Create: `assets/scss/_timeline.scss`
- Modify: `assets/scss/style.scss` (add import)

**Step 1: Create `assets/scss/_timeline.scss`**

```scss
// Timeline component for About page
.timeline {
  position: relative;
  max-width: 680px;
  margin: 3em auto 0;
  padding: 2em 0;

  // Central vertical line
  &::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: $color_grey_very_light;
    transform: translateX(-50%);
  }
}

// Year markers on the line
.timeline-year {
  position: relative;
  text-align: center;
  margin: 2em 0 1em;
  z-index: 1;

  span {
    font-family: $font-stack-header;
    font-size: 1.3em;
    background: $color_white;
    padding: 0.2em 0.8em;
    color: $color_dark_blue;
  }
}

// Individual event
.timeline-event {
  position: relative;
  width: 45%;
  padding: 0.5em 0;
  margin-bottom: 1em;

  p {
    font-family: $font-stack-copy;
    font-size: 0.95em;
    line-height: 1.5;
    margin: 0;
  }

  // Dot on the line
  &::before {
    content: "";
    position: absolute;
    top: 0.7em;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    z-index: 1;
  }

  // Connector line from dot to card
  &::after {
    content: "";
    position: absolute;
    top: calc(0.7em + 4px);
    height: 2px;
    z-index: 0;
  }

  // Left side (good)
  &--good {
    margin-left: 0;
    margin-right: auto;
    text-align: right;
    padding-right: 2em;

    &::before {
      right: -6px;
      background: $color_green;
    }

    &::after {
      right: 0;
      width: 2em;
      background: $color_grey_very_light;
    }
  }

  // Right side (bad)
  &--bad {
    margin-left: auto;
    margin-right: 0;
    text-align: left;
    padding-left: 2em;

    &::before {
      left: -6px;
      background: $color_pink;
    }

    &::after {
      left: 0;
      width: 2em;
      background: $color_grey_very_light;
    }
  }
}

// Mobile: single column, line on left
@media (max-width: 540px) {
  .timeline {
    padding-left: 2em;

    &::before {
      left: 0;
      transform: none;
    }
  }

  .timeline-year {
    text-align: left;

    span {
      padding-left: 0;
    }
  }

  .timeline-event {
    width: 100%;
    text-align: left;
    padding-left: 1.5em;
    padding-right: 0;

    &::after {
      display: none;
    }

    &--good {
      margin-left: 0;
      text-align: left;
      padding-right: 0;
      padding-left: 1.5em;
      border-left: 3px solid $color_green;

      &::before {
        left: -8px;
        right: auto;
      }
    }

    &--bad {
      margin-left: 0;
      text-align: left;
      padding-left: 1.5em;
      border-left: 3px solid $color_pink;

      &::before {
        left: -8px;
      }
    }
  }
}

// Dark mode
@media (prefers-color-scheme: dark) {
  .timeline::before {
    background: rgba(255, 255, 255, 0.15);
  }

  .timeline-year span {
    background: $color_darkmode_background;
    color: $color_darkmode_text;
  }

  .timeline-event::after {
    background: rgba(255, 255, 255, 0.15);
  }
}
```

**Step 2: Add the import to `assets/scss/style.scss`**

Add `@import "timeline";` after the `"garden"` import on line 10.

**Step 3: Commit**

```bash
git add assets/scss/_timeline.scss assets/scss/style.scss
git commit -m "feat: add timeline SCSS partial"
```

---

### Task 3: Add timeline HTML to About page

**Files:**
- Modify: `content/about.md`

**Step 1: Append the timeline HTML below the existing content in `content/about.md`**

Add a horizontal rule, then an H2, then the timeline markup with placeholder events spanning 1994-2026. Events should use `<div class="timeline-event timeline-event--good">` and `timeline-event--bad` classes. Year markers use `<div class="timeline-year"><span>YYYY</span></div>`.

Placeholder events:
- 1994: Born in Guernsey (good)
- 1998: Placeholder bad event (bad)
- 2002: Got first computer (good)
- 2005: Placeholder bad event (bad)
- 2010: Placeholder good event (good)
- 2011: A-level stress (bad)
- 2012: Started university (good)
- 2017: Played poker full time (good)
- 2019: Placeholder bad event (bad)
- 2020: Pandemic (bad)
- 2021: Moved to London (good)
- 2023: Founded All In Labs (good)
- 2024: Placeholder bad event (bad)
- 2026: Present day (good)

**Step 2: Commit**

```bash
git add content/about.md
git commit -m "feat: add life timeline to About page"
```

---

### Task 4: Visual verification

**Step 1: Start Hugo dev server**

Run: `hugo server -D`

**Step 2: Open the About page in Chrome and verify:**

- Timeline renders below existing prose
- Green dots on good events, pink dots on bad events
- Year markers are centred on the line
- Responsive: resize to check mobile layout
- Dark mode: check if system is in dark mode or toggle

**Step 3: Fix any visual issues found during verification**

**Step 4: Final commit if any fixes were made**

```bash
git add -A
git commit -m "fix: timeline visual adjustments"
```
