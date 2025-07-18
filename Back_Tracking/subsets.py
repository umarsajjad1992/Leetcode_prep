"""
Subsets Generation Problem Solution

This module provides a backtracking approach to solve the subsets generation problem.
The problem: Given a list of unique integers, generate all possible subsets (the power set).

Example:
    Input: [1, 2, 3]
    Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Time Complexity: O(2^n * n) where n is the number of elements
Space Complexity: O(2^n * n) for storing all subsets
"""

def subsets(num_list: list[int]) -> list[list[int]]:
    """
    Generate all possible subsets using recursive backtracking approach.
    
    This function uses depth-first search with backtracking to explore all possible
    combinations of elements. It builds subsets incrementally by making decisions
    at each step to either include or exclude elements, ensuring all combinations
    are generated exactly once.
    
    Algorithm:
        1. Start with empty subset and add it to results
        2. For each position from start index to end:
           - Include current element in subset
           - Recursively generate subsets with remaining elements
           - Backtrack by removing current element
        3. The path represents current subset being built
    
    Args:
        num_list (list[int]): List of unique integers to generate subsets from.
                             Can be empty list.
                             Order of elements affects output order but not content.
    
    Returns:
        list[list[int]]: List of all possible subsets (power set).
                        Always includes empty subset [].
                        Total count is 2^n where n is length of input.
                        Each subset is a new list copy.
    
    Examples:
        >>> subsets([1, 2, 3])
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        
        >>> subsets([4, 5])
        [[], [4], [4, 5], [5]]
        
        >>> subsets([])
        [[]]
        
        >>> subsets([1])
        [[], [1]]
    
    Note:
        - Uses path[:] to create a copy of current subset
        - Start index prevents duplicate subsets
        - Backtracking ensures all combinations are explored
    
    Time Complexity: O(2^n * n) where n is number of elements
                    - 2^n subsets to generate
                    - O(n) to copy each subset
    Space Complexity: O(2^n * n) for storing all subsets + O(n) for recursion stack
    """
    

    def backtrack(start, path):

        res.append(path[:])
        for i in range(start, len(num_list)):
            path.append(num_list[i])
            backtrack(i + 1, path)
            path.pop()
    
    res = []
    backtrack(0, [])
    return res


print(subsets([1, 2, 3]))