# 0x07. Rotate 2D Matrix

## Task: Rotate 2D Matrix
Given an `n x n` 2D matrix, implement an algorithm to rotate the matrix 90 degrees clockwise.

### Function Prototype:
```python
def rotate_2d_matrix(matrix):
```
- The function should modify the matrix in-place and should not return any value.
- You can assume the matrix will be non-empty and will always have two dimensions.

## Example Usage
**main_0.py**
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Expected Output:**
```
$ ./main_0.py
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
$
```
