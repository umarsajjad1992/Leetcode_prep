"""
Minimum Pair Difference Problem Solution

Find all pairs of numbers with the minimum absolute difference in an array.
Uses sorting approach to efficiently find adjacent pairs with smallest difference.

Example: [4, 2, 1, 3] → [[1, 2], [2, 3], [3, 4]] (all pairs with diff=1)
"""

def minimum_difference(num_list: list[int]) -> list[list[int]]:
    """
    Find all pairs of numbers with the minimum absolute difference.
    
    Args:
        num_list (list[int]): Array of integers
        
    Returns:
        list[list[int]]: List of pairs with minimum absolute difference
        
    Algorithm:
        1. Sort the array to group numbers with smallest differences
        2. Find the minimum difference by comparing adjacent elements
        3. Collect all adjacent pairs that have this minimum difference
        4. Return list of all such pairs
        
    Time: O(n log n), Space: O(n)
    
    Example:
        >>> minimum_difference([4, 2, 1, 3])
        [[1, 2], [2, 3], [3, 4]]  # All pairs with difference = 1
        
    Note: Only adjacent pairs in sorted array can have minimum difference.
    """
    num_list.sort()
    min_diff = abs(num_list[1]-num_list[0])

    for i in range(1, len(num_list) - 1):
        min_diff = min(min_diff, abs(num_list[i+1]-num_list[i]))
    
    ret = []
    for i in range(len(num_list) - 1):
        if abs(num_list[i+1]-num_list[i]) == min_diff:
            ret.append([num_list[i], num_list[i+1]])

    return ret

print(minimum_difference([4, 2, 1, 3]))
print(minimum_difference([-14, -10, -4, 3, 8, 19, 23, 27]))