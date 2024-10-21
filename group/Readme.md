# Pre-Build Setup

## Game Selection

- Snake
- Tic-Tac-Toe
- Pong
- Flappy Bird Clone
- Breakout (Brick Breaker)
- Memory Game (Matching Pairs)

## Languages or Frameworks to Use

- Pygame (Python): A popular library for building 2D games with Python.

## Game Design Architecture

- a menu system that lets the player select which game to play. (A simple text-based menu of graphical selection.)
- an implementation of individual games

## General structure:

- Main Menu: Displays the game options.
- Game Loop:
  - Each game will have its own loop with event handling (keyboard/mouse input),
  - game updates (movement, collision detection, etc.),
  - and rendering (drawing graphics to the screen).

## MileStone Sequence:

1. Create a main arcade loop: This will serve as the base, handling the menu and navigation between games.
2. Game 1: Simple implementation (e.g., Snake).
3. Game 2-6: Implement each game one by one. Use the structure from the first game and adapt it to the mechanics of the others.
4. Polish & Integration: Ensure that all games return to the main menu upon completion and handle transitions smoothly.

# Build Milestone 1: Create a main arcade loop
