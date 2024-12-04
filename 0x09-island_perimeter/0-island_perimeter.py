#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid
"""

def island_perimeter(grid):
    # Initialize perimeter counter
    perimeter = 0
    
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Only consider land cells (value of 1)
            if grid[i][j] == 1:
                # Check the four directions (up, down, left, right)
                
                # Up direction
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                
                # Down direction
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                
                # Left direction
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                
                # Right direction
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    
    return perimeter
