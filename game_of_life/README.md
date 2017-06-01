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
You can run the tests by simply calling `python3 test_game_of_life.py` from the command line. You can replace `python3` with `python` if you want to use python2 instead.

## How to write tests
The test file [test_game_of_life.py](test_game_of_life.py) contains an example test case with an example (failing) test that you can easily adjust. Just add more methods, starting with `test_`, to this class to add additional tests.

## Nice to know
Python knows some not so common list operations that might come in handy for this task.

### List slicing
List subscription for more than one element, with `[start:end:step]`, with all parameters and the second colon being optional (defaulting to `0` and the length of the list and `1` respectively).
```python
>>> example_list = [1, 2, 3, 4]
>>> example_list[:2]
[1, 2]
>>> example_list[2:3]
[3]
>>> example_list[:-2]
[1, 2]
>>> example_list[-2:]
[3, 4]
>>> example_list[1:-1:2]
[2]
>>> example_list[::2]
[1, 3]
```

### List comprehension
Creating a list from a loop directly. Can also be used for filtering list with an optional `if` clause.
```python
>>> example_list = [1, 2, 3, 4]
>>> [x**2 for x in example_list if x != 2]
[1, 9, 16]
```

### List multiplication
Creating a list from another one by repeating the second's elements `n` times.
```python
>>> 4 * [2, 3]
[2, 3, 2, 3, 2, 3, 2, 3]
```
But beware that this creates copies:
```python
>>> example_list = [[1, 2]] * 2
>>> example_list
[[1, 2], [1, 2]]
>>> example_list[0].append(3)
>>> example_list
[[1, 2, 3], [1, 2, 3]]
```

## Bonus

1. Write a function that pretty prints the grid
2. Write a function that "animates" several successive iterations
