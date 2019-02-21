
Introduction
=============
 Conway's Game of Life is my second project while learning
 python. It's a simple implementation. I recommend you to try this
 eventually if you are also a beginner to python.

Conway's Game of Life: How It Works
====================================
[Conway's Game of
Life](http://www.conwaylife.com/wiki/Conway%27s_Game_of_Life) is more
of a mathematical simulation than a game. The "game" is actually a
zero-player game, meaning that its evolution is determined by its
initial state, needing no input from human players. One interacts with
the Game of Life by creating an initial configuration and observing
how it evolves.

Usage
======
Requires python3.x Does not requires `numpy` or other
packages to run the simulation.

To run [blinker](http://www.conwaylife.com/wiki/Blinker)
configuration:
```bash
$ python blinker.py
```
ConwayLife.com have a very good collection of
[patterns](http://www.conwaylife.com/wiki/Category:Patterns). The
[RLE](http://www.conwaylife.com/wiki/RLE)(Run Length Encoded) file
format is commonly used for storing large patterns. RLE can be decode
by functions in `RLEsupport.py`. Examples are given in
`other_configuration.py`. In the same file the patterns are then coded
to animated in terminal using `curses` module.

```bash
$ python other_configuration.py
```

End program using a keyboard interrupt (ctrl-c).

Background
===========
Initial configuration of the game of life is given through a
matrix. Each element in this matrix is defined as a cell. At first,
the program finds the number of neighboring alive cells for each
cell. Then applies Conway's rules and produces the next
generation. Each generation is displayed as a string. This process
continues in a loop.  Read `spec.txt` to see the notes on the project.

Requirements
=============
Check `requirements.txt` for other dependencies
  - install them with `pip install -r requirements.txt`
  - to add more dependencies, use pip and: `pip freeze > requirements.txt`

Tests
======
This project is developed through Test Driven Development.
Once required dependencies are there, tests can run. To test:
```bash
pytest test_gameoflife
```
To check coverage of these tests:
```bash
pytest --cov=gameoflfe
```

* `test_gameoflife.py` contains tests for `gameoflife`. It has 100% coverage.
* `test_RLEsupport.py` contains tests for `RLEsupport`. It has 100% coverage.


