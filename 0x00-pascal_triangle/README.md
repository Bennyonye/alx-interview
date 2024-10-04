# 0x00. Pascal's Triangle

## Description
This project involves implementing **Pascal’s Triangle** using Python. Pascal’s Triangle is a triangular array of numbers where the values are the coefficients of a binomial expansion. Each number is obtained as the sum of the two numbers directly above it. This project will enhance your understanding of algorithms, list manipulation, and mathematical properties through the implementation of Pascal’s Triangle.

The goal is to generate a list of lists where each sub-list represents a row in Pascal’s Triangle. The project will require applying various Python concepts such as loops, list comprehensions, functions, and more.

## Learning Objectives
By the end of this project, you should be able to:

- Understand what Pascal’s Triangle is and how it is generated.
- Implement algorithms using Python lists and list comprehensions.
- Create a function to generate Pascal’s Triangle up to a specified number of rows.
- Use nested loops or list comprehensions for constructing each row.
- Return a list of lists representing Pascal’s Triangle.
- Handle edge cases such as invalid input types or values.
- Understand the time and space complexity of your solution.

## Project Requirements
To complete and run the project successfully, the following requirements must be met:

- All files will be executed on **Ubuntu 18.04 LTS** using Python 3.7.
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
- All files should end with a new line.
- A `README.md` file is mandatory at the root of the project folder.
- The function should be named `pascal_triangle` and saved in a file named `0-pascal_triangle.py`.
- Your code will be verified against a coding style checker (PEP 8).
- You should be able to test your function by running:

  ```bash
  python3 0-main.py
  ```

## Project Setup
### 1. Install Python 3.7
Ensure that Python 3.7 is installed on your machine:

```bash
sudo apt update
sudo apt install python3.7
```

Verify the installation:

```bash
python3 --version  # Should output Python 3.7 or a similar version
```

### 2. Create the Function File
Create a file named `0-pascal_triangle.py` in the project directory. This file should contain your `pascal_triangle` function.

### 3. Create a Test File
Create a `0-main.py` file to test your function. This file should contain test cases to verify that your implementation works as expected.

### 4. Run Tests
Run the test file to ensure your function generates Pascal’s Triangle correctly:

```bash
python3 0-main.py
```

### 5. Code Style
Ensure that your code adheres to the PEP 8 coding style:

```bash
pep8 0-pascal_triangle.py
```

## Implementation Details
### Concepts to Revise
To successfully complete this project, ensure you have a good understanding of the following Python concepts:

1. **Lists and List Comprehensions**: 
   - Use list comprehensions to generate rows of Pascal’s Triangle.
   - Create, access, modify, and iterate over lists effectively.

2. **Functions**:
   - Define and call functions that pass parameters and return values.
   - The `pascal_triangle` function should return a list of lists representing Pascal’s Triangle.

3. **Loops**:
   - Use `for` and `while` loops to iterate through sequences.
   - Nested loops may be necessary for generating each row and calculating the values of Pascal’s Triangle.

4. **Conditional Statements**:
   - Apply `if`, `elif`, and `else` conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).

5. **Arithmetic Operations**:
   - Perform addition, which is fundamental for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.

6. **Indexing and Slicing**:
   - Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.

### Additional Considerations
- **Memory Management**:
  - Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.

- **Efficiency and Optimization**:
  - Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
  - Evaluate and apply optimizations to improve the performance of the solution.

## Example Output
The `pascal_triangle` function should generate the following output when `n` is set to 5:

```python
pascal_triangle(5)
```

Output:

```
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```

## Additional Resources
For more information on Pascal’s Triangle and algorithms, refer to the following resources:

- [What is Pascal’s Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Pascal’s Triangle - Numberphile](https://www.youtube.com/watch?v=XMriWTvPXHI)
- [Python Algorithms](https://realpython.com/learning-paths/python-algorithms/)

## Author
This project is developed and maintained by **BennyOnye**.
