"""
Permutations Generation Problem Solution

This module provides a backtracking approach to solve the permutations generation problem.
The problem: Given a list of distinct integers, return all possible permutations.
Every permutation is a unique arrangement of the original elements.

Example:
    Input: [1, 2, 3]
    Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Time Complexity: O(n! * n) where n is the number of elements
Space Complexity: O(n! * n) for storing all permutations
"""

def permutations(num_list: list[int]) -> list[list[int]]:
    """
    Generate all possible permutations using recursive backtracking approach.
    
    This function uses depth-first search with backtracking to explore all possible
    arrangements of elements. It works by swapping elements in-place and recursively
    permuting the remaining elements, then backtracking to try different swaps.
    
    Algorithm:
        1. Base case: if current position equals list length, add permutation to results
        2. For each position from current to end:
           - Swap current element with element at position i
           - Recursively generate permutations for next position
           - Backtrack by swapping elements back (restore original order)
        3. This generates all possible arrangements exactly once
    
    Args:
        num_list (list[int]): List of distinct integers to generate permutations from.
                            Can be empty list.
                            Order of elements affects initial state only.
    
    Returns:
        list[list[int]]: List of all possible permutations.
                        Each permutation is a new list copy.
                        Total count is n! where n is length of input.
                        If input is empty, returns [[]].
    
    Examples:
        >>> permutations([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
        
        >>> permutations([1])
        [[1]]
        
        >>> permutations([])
        [[]]
    
    Note:
        - Uses in-place swapping to generate permutations efficiently
        - Takes num_list[:] to create a copy of current permutation
        - Recursive approach with O(n) recursion depth
    
    Time Complexity: O(n! * n) where n is the number of elements
                    - n! permutations to generate
                    - O(n) to copy each permutation
    Space Complexity: O(n! * n) for storing all permutations + O(n) for recursion stack
    """
    res = []
    def backtracking(start, end = len(num_list)):
        if start == end:
            res.append(num_list[:])
        for i in range(start, end):
            num_list[start], num_list[i] = num_list[i], num_list[start]
            backtracking(start+1)
            num_list[start], num_list[i] = num_list[i], num_list[start]
    
    backtracking(0)
    return res


print(permutations([1, 2, 3]))
