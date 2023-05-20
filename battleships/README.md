# Battleships Project

Design and test-drive a terminal-based Battleships game.

## Getting Started

How to get started:

```shell
; pipenv install # To install dependencies

; pipenv run pytest # All tests should pass
; pipenv run pytest --cov lib # To see test coverage too

; pipenv run python play.py
# This will give you a few prompts and show you a board.
```

## User Stories

Here is the full set of user stories for this game. Some are already implemented:

```
As a player
So that I can prepare for the game
I would like to place a ship in a board location

As a player
So that I can play a more interesting game
I would like to have a range of ship sizes to choose from

As a player
So the game is more fun to play
I would like a nice command line interface that lets me enter ship positions and
shots using commands.

As a player
So that I can create a layout of ships to outwit my opponent
I would like to be able to choose the directions my ships face in

As a player
So that I can have a coherent game
I would like ships to be constrained to be on the board

As a player
So that I can have a coherent game
I would like ships to be constrained not to overlap

As a player
So that I can win the game
I would like to be able to fire at my opponent's board

As a player
So that I can refine my strategy
I would like to know when I have sunk an opponent's ship

As a player
So that I know when to finish playing
I would like to know when I have won or lost

As a player
So that I can consider my next shot
I would like to be able to see my hits and misses so far

As a player
So that I can play against a human opponent
I would like to play a two-player game
```

### UML Class Diagram

<img width="906" alt="Screenshot 2023-05-05 at 11 53 48" src="https://user-images.githubusercontent.com/93719632/236439807-d5871974-c68b-4c43-911e-d24124f92b79.png">

💡 Notes

- **Association**: shows that one class uses another class or has some kind of relationship with it. This relationship can be one-way or two-way.
- **Direct Association**: where one class uses another class directly but the objects can exist independently, for example, a car and a passenger.
- **Aggregation**: where one class contains another class as a part of it. In other words, it's a "has-a" relationship. For example, a library has a book. The book is part of the library, but it can also exist on its own. Here the associated objects are a crucial part of the containing object.
- **Composition**: the contained object cannot exist without the container. The container "owns" the contained object. For example, a board is composed of tiles. If the board is destroyed, the tiles are destroyed as well.
- **Inheritance**: a mechanism that allows one class to inherit properties and behaviour from another class. The class that is being inherited from is called the superclass or parent class, and the class that inherits from it is called the subclass or child class.
