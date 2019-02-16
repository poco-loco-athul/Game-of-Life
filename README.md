
Introduction
=============
 Conway's Game of Life is my second project while learning python. It's a simple implementation. I recommend you to try this eventually if you are also a beginner to python.

Conway's Game of Life: How It Works
====================================
[Conway's Game of Life](http://www.conwaylife.com/wiki/Conway%27s_Game_of_Life) is more of a mathematical simulation than a game. The "game" is actually a zero-player game, meaning that its evolution is determined by its initial state, needing no input from human players. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

Usage
======
Requires python3 or python3.6+. Does not requires `numpy` or other packages to run the simulation.

To run [blinker](http://www.conwaylife.com/wiki/Blinker) configuration:
```bash
$ python blinker.py
```

To run your own configurations change the intial state in `try_ur_configuration.py`

End program using a keyboard interrupt (ctrl-c).

Background
===========
Initial configuration of the game of life is given through a matrix. Each element in this matrix is defined as a cell. At first, the program finds the number of neighboring alive cells for each cell. Then applies Conway's rules and produces the next generation. Each generation is displayed as a string. This process continues in a loop.
Read `spec.txt` to see the notes on the project.

Requirements
=============
Check `requirements.txt` for other dependencies
  - install them with `pip install -r requirements.txt`
  - to add more dependencies, use pip and: `pip freeze > requirements.txt`

Tests
======
This project is developed through Test Driven Development.

* `test_gameoflife.py` contains tests for `gameoflife`. You can run the tests after installing requirements. To test:
```bash
pytest test_gameoflife
```
`gameoflife` have 100% coverage by tests in `test_gameoflife`. To check coverage:
```bash
pytest --cov=gameoflfe


