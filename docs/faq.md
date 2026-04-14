# FAQ

## Is this open source?

No. This repository is public, but it is not currently published under an open-source redistribution license. The current posture is evaluation-first and commercialization-ready. See [licensing-and-packaging.md](licensing-and-packaging.md).

## Can I use the downstream `gameplay-*` skills by themselves?

Normally, no. The intended operating model is orchestrator-first:

- start from `gameplay-design-orchestrator`
- let it control the downstream stages in order
- only do isolated stage revision when a package already exists and that exact stage is being revised

Using the stage skills like unrelated free-entry prompts weakens the design chain.

## What problem does this suite actually solve?

It solves the gap between loose ideation and structured execution. Many game-design prompts can generate exciting language. Far fewer can generate a package that another AI system can continue from with low ambiguity.

## Does this build the game automatically?

No. It is a game-design and spec-generation workflow, not a one-click game factory.

What it does well:

- direction lock
- loop design
- pacing structure
- scope control
- coding-oriented handoff
- full Chinese spec expansion

What it does not replace:

- implementation
- balancing through real playtests
- production judgment
- art direction execution

## Is it only for web games?

No, but the current included example is a web game. The workflow is most obviously useful for web games, lightweight prototypes, and small-to-mid scope game concepts where fast design compression matters.

## Why is the final spec written in Chinese?

Because the current downstream design spec target is a Chinese production format. That makes it easy to use in Chinese-speaking AI execution workflows and local team collaboration. The upstream logic is still broadly applicable.

## Why include validation scripts?

Because credibility matters. Without validators and a real example, a public skill repo is too easy to dismiss as a prompt museum. The validators turn this into a more defensible capability artifact.

## How should a studio or consultant commercialize this?

The realistic path is usually:

1. public showcase repo
2. paid private license or customization package
3. onboarding or workshop layer
4. optional bespoke pipeline adaptation for the client's genre, team, or production stack

See [pricing-and-commercial-offers.md](pricing-and-commercial-offers.md).

## Can this be sold as a SaaS today?

Not yet in its current form. Right now it is better positioned as:

- a commercial workflow asset
- a private licensed capability pack
- a consulting accelerator
- an internal studio toolkit

Turning it into self-serve SaaS would require:

- hosted workflow execution
- account boundaries
- usage tracking
- better packaging and onboarding
- stronger legal framing

## What is the strongest selling point?

The topology itself:

orchestrator first, downstream stages ordered, scope controlled, real example included, validators included.

That is much more defensible than "I have some good prompts."

