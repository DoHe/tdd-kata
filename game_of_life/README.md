# Game of Life

## Task
Implement Conway's game of life. The function should take an arbitrarily sized grid (a list of same length lists) of cells like this:
```python
[
    ['.', '.', '.', '.'],
    ['.', '.', '*', '.'],
    ['.', '.', '*', '.'],
    ['.', '.', '*', '.'],
    ['.', '.', '.', '.'],
]
```
where `.` stands for _dead_ and `*` stands for _alive_. It should then apply the rules of Conway's game of life to it:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

All rules are applied at the same discrete tick (i.e. each cell can check all four rules independent of what will happen to the other cells). Neighbors that are outside the grid should be assumed dead (the original version stipulates an infinite grid, which is out of scope for this kata).

For the above example, the function should return:
```python
[
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '*', '*', '*'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
]
```

## How to run the code
You can run the tests by simply calling `python3 test_game_of_life.py` from within this directory. You can replace `python3` with `python` if you want to use python2 instead.

## How to write tests
The test file [test_game_of_life.py](test_game_of_life.py) contains an example test case with an example (failing) test that you can easily adjust. Just add more methods, starting with `test_`, to this class to add additional tests.

## Bonus

1. Write a function that pretty prints the grid
2. Write a function that "animates" several successive iterations
