---
type: "garden"
title: "Mango"
date: "2025-02-16T00:00:00Z"
author: Jonny Spicer
summary: "A Go library providing complete API coverage for Manifold Markets, the prediction market platform. Features type-safe wrappers for all documented endpoints and custom structs for every data structure."
github: "https://github.com/jonnyspicer/mango"
tier: "shipped"
tech_stack: "Go"
planted: "March 2024"
last_tended: "February 2026"
---

## The Hook

I was building trading bots for Manifold Markets and kept writing the same HTTP request boilerplate over and over. I wanted a proper client library that felt natural in Go.

## The Context

Manifold Markets has a comprehensive REST API, but no official Go client. Every time I started a new project, I'd spend a day setting up the API calls, type definitions, and error handling. The repetition was making me want to write fewer bots, not more.

## The Journey

Mango started as a weekend project to extract the common code from my first trading bot. I realized that if I was going to maintain it anyway, I might as well do it properly — full API coverage, comprehensive documentation, and type safety throughout. The trickiest part was handling Manifold's polymorphic market types (binary, multiple-choice, free-response) in Go's type system without making the API awkward to use.

## The Current State

Mango is a Go library that provides wrapper functions for every documented Manifold Markets API endpoint and custom data types representing each structure returned by the API. It's stable, documented on pkg.go.dev, and powers both my personal trading bots and other projects in the Manifold ecosystem.

## Features

- **Complete API Coverage** — Wrapper functions for all documented Manifold Markets API endpoints
- **Type Safety** — Custom structs for every data structure (markets, bets, users, comments, etc.)
- **Simple Authentication** — Environment variable-based API key management
- **Well Documented** — Full documentation available on [pkg.go.dev](https://pkg.go.dev/github.com/jonnyspicer/mango)

## Use Cases

- Creating automated trading bots
- Building analytics dashboards
- Developing market creation tools
- Integrating prediction markets into other applications

## Example

```go
mc := mango.DefaultClientInstance()

// Create a new market
pmr := mango.PostMarketRequest{
    OutcomeType: mango.Binary,
    Question:    "Will X happen by end of year?",
    Description: "Resolves YES if...",
    InitialProb: 50,
    CloseTime:   1704067199000,
}

marketId, err := mc.CreateMarket(pmr)
```

Mango powers [Hyperkaehler](/garden/hyperkaehler), a multi-strategy trading bot that uses fractional Kelly criterion for position sizing.
