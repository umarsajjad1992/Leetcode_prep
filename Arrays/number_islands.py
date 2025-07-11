"""
Number of Islands Problem Solution

Find the number of islands in a 2D grid using BFS traversal.
An island is a group of connected 1s (land) surrounded by 0s (water).

Example: [[1,1,0],[0,1,0],[0,0,1]] → 2 islands
"""

def num_islands(grid: list[list[int]]) -> int:
    """
    Count the number of islands in a 2D grid using BFS.
    
    Args:
        grid (list[list[int]]): 2D grid where 1 represents land and 0 represents water
        
    Returns:
        int: Number of distinct islands
        
    Algorithm:
        1. Iterate through each cell in the grid
        2. When finding unvisited land (1), start BFS to mark entire island
        3. Use BFS to visit all connected land cells (4-directional)
        4. Count each complete island traversal
        
    Time: O(m * n), Space: O(m * n)
    
    Example:
        >>> grid = [[1,1,0],[0,1,0],[0,0,1]]
        >>> num_islands(grid)
        2  # Two separate islands
    """
    if not grid:
        return 0
    
    def bfs(row, col):
        """
        Mark all connected land cells as visited using BFS.
        
        Args:
            row (int): Starting row position
            col (int): Starting column position
            
        Algorithm:
            1. Add starting position to queue and mark as visited
            2. Process queue: for each cell, check 4 directions
            3. Add unvisited land neighbors to queue
            4. Continue until all connected land is visited
        """
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