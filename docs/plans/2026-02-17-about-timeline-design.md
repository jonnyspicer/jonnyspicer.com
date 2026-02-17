# About Page Timeline Design

## Overview

Add a vertical life timeline (1994-2026) below the existing About page prose. Good events on one side, bad events on the other, using an alternating-card centered-line layout.

## Visual Design

- **Vertical line**: thin (2px), light grey (`#eaeaea`), centered on desktop
- **Year markers**: Playfair Display, sitting on the line, with a subtle background pill
- **Event cards**: Jost body text, minimal — short description only, no borders, just text with a small coloured dot connecting to the line
- **Good side** (left on desktop): green dot (`#06d6a0`)
- **Bad side** (right on desktop): pink dot (`#ef476f`)
- **Section header**: H2 "Timeline" above the component, styled consistently with the rest of the site

## Responsive Behaviour

- **Desktop (>540px)**: centered line, events alternate left/right
- **Mobile (<=540px)**: line on left edge, all events stacked in single column, coloured left-border indicates good/bad

## Dark Mode

- Line colour adjusts to `rgba(255,255,255,0.15)`
- Dot colours remain the same (already vibrant enough)
- Year marker background adjusts

## Implementation

- Pure HTML + CSS (no JS needed for the timeline itself)
- SCSS in a new partial `_timeline.scss`, imported into the main stylesheet
- Timeline content added directly to `content/about.md` as raw HTML below the existing markdown
- Placeholder events spanning 1994-2026

## Placeholder Events (to be replaced with real content)

Good side: Born (1994), Started school (1999), First computer (2002), University (2012), Moved to London (2021), Founded All In Labs (2023)
Bad side: Broke arm (1998), A-level stress (2011), Burnout (2019), Pandemic isolation (2020), Injury (2024)
