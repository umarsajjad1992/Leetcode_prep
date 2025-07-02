"""
FILE: spiral_matrix.py

DESCRIPTION:
This script contains a function `spiral` that takes a 2D matrix as input and returns 
a list of its elements in spiral order. The spiral traversal starts from the top-left 
corner and proceeds clockwise, layer by layer, until all elements are visited.

EXAMPLE USAGE:
Input: 
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]
Output: [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]

TIME COMPLEXITY:
The function iteratively removes rows and columns from the matrix while traversing 
its elements. For a matrix with m rows and n columns, the time complexity is O(m * n), 
as each element is visited exactly once.

"""

# My Code
def spiral(matrix: list[list[int]]) -> list:
    res = []

    # Check if matrix empty
    def check_fin():
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
def spiral_2(matrix: list[list[int]]) -> list:
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

print(spiral_2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]))