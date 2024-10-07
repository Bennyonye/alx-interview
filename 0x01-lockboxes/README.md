# 0x01. Lockboxes

## Project Overview

This project focuses on developing an algorithm in Python to determine whether all locked boxes can be opened. Each box may contain keys to other boxes, and the goal is to check if all boxes can be accessed.

## Must Know Concepts

To successfully tackle this project, you should have a solid understanding of the following key concepts:

### Lists and List Manipulation
- Working with lists, including accessing elements, iterating over lists, and dynamically modifying lists.
- [Python Lists (Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Graph Theory Basics
- Knowledge of graph theory, particularly traversal algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS), can be helpful as boxes and keys can be modeled as nodes and edges in a graph.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/geometry-home/geometry-angles/geometry-intro-to-angles/v/what-is-a-graph)

### Algorithmic Complexity
- Understanding time and space complexity is important for writing efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-big-o-notation/)

### Recursion
- Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

### Queue and Stack
- Knowledge of queues and stacks is crucial for implementing BFS or DFS algorithms.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

### Set Operations
- Using sets to track visited boxes and available keys can optimize the search process.
- [Python Sets (Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

By reviewing these concepts and utilizing the resources, you will be well-equipped to develop an efficient solution for this project.

## Requirements

- Allowed editors: **vi**, **vim**, **emacs**.
- All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.4.3).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A **README.md** file, at the root of the folder of the project, is mandatory.
- Your code should be documented.
- Your code should adhere to **PEP 8** style (version 1.7.x).
- All your files must be executable.

## Task: Lockboxes

### Description
You have `n` number of locked boxes in front of you, each numbered from `0` to `n - 1`. Each box may contain keys to other boxes. Write a method that determines if all the boxes can be opened.

### Prototype
```python
def canUnlockAll(boxes):
```

### Parameters
- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.

### Return Value
- Return `True` if all boxes can be opened, else return `False`.

### Example Usage
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```