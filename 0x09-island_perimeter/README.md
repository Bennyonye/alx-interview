# 0x09. Island Perimeter

## Project Overview

In this project, you will implement a function called `island_perimeter(grid)` to calculate the perimeter of an island represented by a grid of integers. Each grid cell can either be water (`0`) or land (`1`). Your task is to find the perimeter of the island formed by land cells, considering the following constraints and conditions.

## Problem Requirements

- **Function Definition**:
    - `def island_perimeter(grid):`
    - This function returns the perimeter of the island described in the `grid`.

- **Input**:
    - `grid` is a list of lists (2D array) of integers, where:
      - `0` represents water,
      - `1` represents land.
    - Each cell in the grid is a square with side length of `1`.
    - Land cells are connected either horizontally or vertically, but not diagonally.

- **Grid Constraints**:
    - The grid is rectangular, and its width and height do not exceed `100`.
    - The grid is completely surrounded by water.
    - There is at most one island in the grid (or no island at all).
    - The island doesn’t contain "lakes," meaning there are no water cells inside the island that aren't connected to the surrounding water.

## Approach

The goal is to calculate the perimeter of the island by summing the lengths of exposed edges of the land cells. Each land cell (`1`) can contribute up to four edges to the perimeter. For each land cell, check if its adjacent cells (up, down, left, and right) are water (`0`) or out of bounds (which means they are surrounded by water). If an adjacent cell is water or the boundary of the grid, the edge is exposed and contributes to the perimeter.

## Example

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

The perimeter of the island is calculated to be `12`.

## Expected Output

For the above grid, calling the function `island_perimeter(grid)` will return `12`.

## Constraints

- The grid is surrounded by water on all sides.
- The grid may have no land (if it is entirely water), in which case the perimeter is `0`.
- The grid contains only one island, and there are no isolated water cells inside the island.
