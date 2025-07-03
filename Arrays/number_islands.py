"""
FILE: number_islands.py

DESCRIPTION:
This script contains a function that calculates the number of islands in a given 2D grid. 
An island is defined as a group of connected 1s (representing land) surrounded by 0s 
(representing water). The function uses Breadth-First Search (BFS) to traverse the grid 
and count the number of distinct islands.

EXAMPLE USAGE:
Input:
grid = [
    [1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
]
Output: 3

TIME COMPLEXITY:
The function visits each cell in the grid exactly once. For a grid with m rows and n columns, 
the time complexity is O(m * n).

SPACE COMPLEXITY:
The space complexity is O(m * n) in the worst case, due to the storage of visited cells 
and the BFS queue.
"""

def num_islands(grid: list[list[int]]) -> int:

    if not grid:
        return 0
    
    def bfs(row, col):
    
        search_queue = []
        
        visited.add((row, col))
        search_queue.append((row, col))

        directions = [[1, 0], [0, 1]]
        while search_queue:
            r, c = search_queue.pop()
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if (row in range(rows) and col in range(columns) and 
                    grid[row][col] == 1 and (row,col) not in visited):
                    visited.add((row, col))
                    search_queue.append((row, col))

    count_islands = 0
    visited = set()
    rows = len(grid)
    columns = len(grid[0])
    
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1 and (row, col) not in visited:
                bfs(row, col)
                count_islands += 1

    return count_islands


grid = [[1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1]]

print(num_islands(grid))