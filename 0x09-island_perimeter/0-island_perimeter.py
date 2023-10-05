#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to the perimeter

                # Check adjacent cells to subtract the shared sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 sides for top neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 sides for left neighbor

    return perimeter

