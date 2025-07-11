"""
Spiral Matrix Problem Solution

Traverse a 2D matrix in spiral order (clockwise) starting from top-left corner.
Two approaches: basic and optimized implementations.

Example: [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]
"""

# First approach
def spiral(matrix: list[list[int]]) -> list:
    """
    Traverse matrix in spiral order using explicit bounds checking.
    
    Args:
        matrix (list[list[int]]): 2D matrix to traverse
        
    Returns:
        list[int]: Elements in spiral order
        
    Algorithm:
        1. Add top row (left to right)
        2. Add right column (top to bottom)
        3. Add bottom row (right to left)
        4. Add left column (bottom to top)
        5. Repeat until matrix is empty
        
    Time: O(m * n), Space: O(1)
    
    Example:
        >>> spiral([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    res = []

    # Check if matrix empty
    def check_fin():
        """Check if matrix is empty to terminate spiral traversal."""
        if len(matrix) == 0:
            return True
    
    while True:
        # Add first row of matrix to res
        res.extend(matrix[0])
        matrix.pop(0)
        print(matrix)

        if check_fin(): return res

        # Adding last items of remaining rows
        for item in matrix:
            res.append(item[-1])
            item.pop(-1)
        
        if check_fin(): return res
        
        # Adding last row in reverse order
        res.extend(matrix[-1][::-1])
        matrix.pop(-1)

        if check_fin(): return res

        # Adding first items of remaing rows
        for item in matrix[::-1]:
            res.append(item[0])
            item.pop(0)
        
        if check_fin(): return res

# Cleaner approach
def spiral_clean(matrix: list[list[int]]) -> list:
    """
    Traverse matrix in spiral order using optimized approach (preferred).
    
    Args:
        matrix (list[list[int]]): 2D matrix to traverse
        
    Returns:
        list[int]: Elements in spiral order
        
    Algorithm:
        1. While matrix is not empty:
           - Add and remove top row
           - Add last element of each remaining row
           - Add and remove bottom row (reversed)
           - Add first element of each remaining row (bottom to top)
        2. Use conditional checks to avoid empty matrix operations
        
    Time: O(m * n), Space: O(1)
    
    Example:
        >>> spiral_clean([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        
    Note: Preferred solution - cleaner and more efficient implementation.
    """
    res = []
    
    # Checking if matrix is non empty
    while matrix:
        # Add first row of matrix to res
        res.extend(matrix.pop(0))

        if matrix:
        # Adding last items of remaining rows
            for item in matrix:
                res.append(item.pop())

        if matrix:
        # Adding last row in reverse order
            res.extend(matrix.pop()[::-1])

        # Adding first items of remaing rows
        if matrix:
            for item in matrix[::-1]:
                res.append(item.pop(0))
                
    return res

print(spiral_clean([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]))