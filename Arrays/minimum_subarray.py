"""
Minimum Subarray Sum Problem Solution

Find the minimum length of a contiguous subarray whose sum is greater than or equal to target.
Uses sliding window technique for efficient O(n) solution.

Example: [2, 3, 1, 2, 4, 3], target=7 → 2 (subarray [4, 3])
"""

def minimum_subarray_sum(num_list: list[int], target: int) -> int:
    """
    Find minimum length of subarray with sum >= target using sliding window.
    
    Args:
        num_list (list[int]): Array of positive integers
        target (int): Target sum to reach or exceed
        
    Returns:
        int: Minimum length of subarray with sum >= target, or 0 if impossible
        
    Algorithm:
        1. Use two pointers (left and right) to maintain sliding window
        2. Expand window by moving right pointer and adding to sum
        3. When sum >= target, try to shrink window from left
        4. Track minimum window size that satisfies condition
        5. Return minimum length found
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> minimum_subarray_sum([2, 3, 1, 2, 4, 3], 7)
        2  # Subarray [4, 3] has sum=7 and length=2
        
    Note: Uses sliding window technique for optimal linear time complexity.
    """
    res = float('inf')
    total = 0
    l = 0
    for r, num in enumerate(num_list):
        total += num
        while total >= target:
            res = min(res, r-l+1)
            total -= num_list[l]
            l += 1
    if res == float('inf'):
        return 0
    return res

print(minimum_subarray_sum(num_list=[1, 1, 1, 1, 1, 1], target=7))