# TDD Kata

Some small katas for a TDD workshop. Check each subdirectory's README for more information on the particular kata.
Keep in mind the "_three laws_":

1. You may not write production code until you have written a failing unit test
2. You may not write more of a unit test than is sufficient to fail, and not compiling is failing
3. You may not write more production code than is sufficient to pass the currently failing test

And the "_five steps_":

1. Add a test
2. Run all tests, check if new test fails
3. Write the code
4. Run all tests, check if all pass
5. Refactor code

## Python "nice to know"s
Python knows some not so common list operations that might come in handy for these katas.

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

### List creation
Python2 know range to create a list of successive numbers and xrange for an iterator of the same. Python3 only knows range which gives you an iterator. The interface is the same as for slices: `start`, `end`, `step`

Python2:
```python
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(1,3)
[1, 2]
>>> range(-2,4,3)
[-2, 1]
>>> range(-2,4,2)
[-2, 0, 2]
```

Python3 (or Python2 when replaced by `xrange`):
```python
>>> r = range(5)
>>> r
range(0, 5)
>>> for x in r:
...     print(x)
...
0
1
2
3
4
>>> list(r)
[0, 1, 2, 3, 4]
```
