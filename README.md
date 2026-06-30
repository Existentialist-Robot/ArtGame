# ArtGame

Interactive art installation built in Unity for a BFA student's final exhibit — a virtual pet deployed on a Raspberry Pi with custom external sensor input.

## Concept

A Tamagotchi-style companion that decays in real time across food, happiness, and energy axes. The pet's state persists between sessions — if you neglect it, it remembers. Physical sensor inputs (mapped via GPIO) replace the standard keyboard, making interaction tactile and installation-appropriate.

The sprite set — idle, hungry, tired, angsty, eating, happy — was commissioned for the exhibit and reflects the emotional vocabulary of contemporary life.

## Architecture

- **NeedsController** — real-time need decay using wall-clock deltas, not game ticks; state recalculates on load based on elapsed real-world time
- **PetController** — animator state machine driving pet behaviour and movement
- **DatabaseManager** — persistent SQLite save/load so the pet survives across power cycles
- **TimingManager** — configurable game-hour length for controlling decay speed per installation context
- **KeyMap / mapkeytoclick** — maps physical sensor inputs (RPi GPIO via keyboard emulation) to in-game events
- **Minigame system** — extensible `BaseMinigameController` for interactive pet engagement loops
- **SoundMusicManager** — audio layer tied to pet state transitions

## Stack

- Unity (C#) — game engine and scripting
- Raspberry Pi — deployment hardware
- External sensors — GPIO-mapped physical inputs

## Context

Delivered as contract work in 2020. Exhibited as part of a BFA final project.