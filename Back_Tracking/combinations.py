"""
Combinations Generation Problem Solution

This module provides a backtracking approach to solve the combinations generation problem.
The problem: Given two integers n and k, generate all possible combinations of k numbers
chosen from the range [1, n].

Example:
    Input: n=4, k=2
    Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

Time Complexity: O(C(n,k) * k) where C(n,k) is binomial coefficient
Space Complexity: O(C(n,k) * k) for storing all combinations
"""

def combinations(n: int, k: int) -> list[list[int]]:
    """
    Generate all possible combinations of k numbers from range [1, n] using backtracking.
    
    This function uses depth-first search with backtracking to explore all possible
    combinations of k elements from the range [1, n]. It builds combinations
    incrementally by making decisions at each step to include numbers, ensuring
    all valid combinations are generated exactly once without duplicates.
    
    Algorithm:
        1. Base case: if current path length equals k, add combination to results
        2. For each number from start to n:
           - Include current number in combination
           - Recursively generate combinations with remaining positions
           - Backtrack by removing current number
        3. Start index ensures no duplicate combinations and maintains order
    
    Args:
        n (int): Upper bound of the range [1, n] (inclusive).
                Must be positive integer.
        k (int): Number of elements to choose for each combination.
                Must be non-negative and <= n.
    
    Returns:
        list[list[int]]: List of all possible combinations of k numbers from [1, n].
                        Each combination is sorted in ascending order.
                        Total count is C(n,k) = n! / (k! * (n-k)!)
                        If k > n or k < 0, returns empty list.
    
    Examples:
        >>> combinations(4, 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        
        >>> combinations(3, 1)
        [[1], [2], [3]]
        
        >>> combinations(3, 3)
        [[1, 2, 3]]
        
        >>> combinations(3, 0)
        [[]]
        
        >>> combinations(2, 3)
        []
    
    Note:
        - Uses path[:] to create a copy of current combination
        - Start index prevents duplicate combinations (e.g., [1,2] and [2,1])
        - Maintains lexicographic order in output
        - Handles edge cases like k=0 (returns empty combination) and k>n
    
    Time Complexity: O(C(n,k) * k) where C(n,k) is binomial coefficient
                    - C(n,k) combinations to generate
                    - O(k) to copy each combination
    Space Complexity: O(C(n,k) * k) for storing all combinations + O(k) for recursion stack
    """
    
    res = []
    def backTracking(start, path = []):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backTracking(i + 1, path)
            path.pop()
            
                
    backTracking(1, [])
    return res

print(combinations(4, 3))