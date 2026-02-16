---
type: "garden"
title: "Boudica"
date: "2025-02-11T00:00:00Z"
author: Jonny Spicer
summary: "An experimental chess engine that plays at 2100 strength, built to explore the intersection of algorithm design and tactical pattern recognition."
project_url: "https://chess.jonnyspicer.com"
github: "https://github.com/jonnyspicer/boudica"
tier: "growing"
tech_stack: "Python · Flask"
planted: "November 2024"
last_tended: "January 2025"
---

## The Hook

I wanted to understand how chess engines actually work by building one from scratch, without copying existing architectures.

## The Context

I've been playing chess on and off for years, but I never really understood what was happening under the hood of engines like Stockfish. I knew about minimax and alpha-beta pruning from algorithms classes, but I wanted to see if I could build something that actually played decent chess rather than just a toy that blunders pieces.

## The Journey

The naive minimax approach plays terrible chess because the branching factor is insane. Adding alpha-beta pruning helps but isn't enough. The breakthrough was implementing a proper evaluation function that considers piece positioning, king safety, pawn structure, and tactical patterns — not just material count. I also added move ordering (checking captures and checks first) which dramatically improves pruning efficiency. The engine now plays at around 2100 Elo, which is solidly intermediate club strength.

## The Current State

Boudica is a chess engine you can play against at chess.jonnyspicer.com. It's experimental in the sense that I'm still tweaking the evaluation weights and sometimes it makes moves that look brilliant but are actually unsound. The web interface works reliably, but the engine itself is still learning (well, I'm still learning how to make it learn).
