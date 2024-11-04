# N Queens

## Overview
The N Queens puzzle involves placing N non-attacking queens on an N×N chessboard. This repository contains a program that solves the N Queens problem.

## Usage
To run the program, use the following command:

```bash
nqueens N
```

### Requirements:
- The argument `N` must be an integer greater than or equal to 4.
  
### Error Handling:
- If the program is called with an incorrect number of arguments, it will output:
  ```
  Usage: nqueens N
  ```
  and exit with status 1.
  
- If `N` is not an integer, it will display:
  ```
  N must be a number
  ```
  and exit with status 1.
  
- If `N` is less than 4, it will show:
  ```
  N must be at least 4
  ```
  and exit with status 1.

### Output
The program prints all possible solutions to the N Queens problem, with each solution represented as a list of coordinate pairs (row, column). Each solution will be printed on a new line, and the format will look like this:

```python
[[row1, col1], [row2, col2], ...]
```

You do not need to print the solutions in any specific order.

### Example
To see the program in action, you can run:

```bash
./nqueens.py 4
```

The output might be:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

For a larger board:

```bash
./nqueens.py 6
```

You might get:

```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Dependencies
You are only allowed to import the `sys` module.
