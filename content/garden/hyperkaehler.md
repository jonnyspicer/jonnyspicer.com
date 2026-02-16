---
type: "garden"
title: "Hyperkaehler"
date: "2025-02-16T00:00:00Z"
author: Jonny Spicer
summary: "A quantitative trading bot for Manifold Markets implementing arbitrage, time decay, and mispricing strategies with Kelly-based position sizing and comprehensive risk management."
github: "https://github.com/jonnyspicer/hyperkaehler"
tier: "growing"
tech_stack: "Go · SQLite"
planted: "December 2024"
last_tended: "February 2026"
---

## The Hook

I was spending hours manually tracking prediction markets looking for arbitrage opportunities. I wanted a bot that could scan thousands of markets and execute trades faster than I could blink.

## The Context

Manifold Markets has fascinating inefficiencies — multiple-choice markets where the probabilities don't add to 100%, time-decay opportunities in "will X happen by DATE?" markets, and mean reversion plays after poorly-calibrated users make large trades. The opportunities exist, but they're fleeting. By the time I'd manually calculate position sizes and place orders, someone else had already taken the edge.

## The Journey

The first version just did simple arbitrage scanning. Then I added time decay detection. Then mean reversion signals. The hardest part was the risk management — Kelly criterion is mathematically beautiful but if you implement it naively you'll blow up your bankroll on a bad run. I ended up using fractional Kelly (1/4 by default) with multiple safety rails: per-position limits, per-market exposure caps, drawdown circuit breakers, and a minimum edge threshold. The bot now runs continuously with auto-restart and stores every bet in SQLite for post-trade analysis.

## The Current State

Hyperkaehler is a multi-strategy trading bot for Manifold Markets that implements arbitrage, time decay, and mispricing strategies. It works about 80% of the time, and I fix the other 20% when I notice something broke. Built in Go using [Mango](/garden/mango) as the Manifold Markets API client, with SQLite for persistence and comprehensive backtesting data.

## Trading Strategies

### Arbitrage
Exploits probability mispricing in multiple-choice markets where answer probabilities don't sum to 1. Places limit orders against overpriced answers (or for underpriced ones), filtering out resolved answers and markets closing more than 90 days out.

### Time Decay
Targets "Will X happen by DATE?" markets where the event hasn't occurred and time is running out. As the deadline approaches with no news, probability should decay toward NO.

### Mispricing Detection
- Identifies extreme probability markets (>95% or <5%) that are likely correct but not extreme enough
- Detects mean reversion opportunities after sudden moves by poorly-calibrated users

### Market Making
Places limit orders on both sides of active binary markets to capture the spread. Low priority at small bankroll sizes.

## Risk Management

- **Fractional Kelly sizing** — Default 1/4 Kelly to reduce variance
- **Position limits** — Max 5% of bankroll per position
- **Market exposure caps** — Max 10% exposure per market
- **Total capital deployed** — Max 50% total capital at risk
- **Drawdown circuit breaker** — 20% drawdown halts all trading
- **Edge threshold** — Minimum 3% edge required
- **Blacklisting** — Permanent blocking of bets on resolved/closed answers

## Technical Architecture

Uses SQLite with WAL mode for persistence, storing:
- Market snapshots for backtesting
- Every bet placed with strategy attribution
- Bankroll snapshots for drawdown calculation
- Outstanding limit orders

The bot runs continuously with auto-restart and daily log rotation, scanning markets on a configurable interval.
