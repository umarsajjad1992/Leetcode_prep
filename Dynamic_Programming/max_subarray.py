"""
Maximum Subarray Problem Solution

Find the maximum sum of a contiguous subarray using dynamic programming (Kadane's Algorithm).
Given an array of integers, find the contiguous subarray with the largest sum.

Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 (subarray [4,-1,2,1])
"""

def max_subarray_sum(num_list: list[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray using dynamic programming.
    
    Args:
        num_list (list[int]): List of integers (can contain negative numbers)
        
    Returns:
        int: Maximum sum of any contiguous subarray, or 0 if list is empty
        
    Algorithm:
        1. Handle edge case: return 0 for empty list
        2. Create DP array where dp[i] = maximum sum ending at index i
        3. For each element, choose between:
           - Starting a new subarray (current element only)
           - Extending previous subarray (previous sum + current element)
        4. dp[i] = max(num, dp[i-1] + num)
        5. Return the maximum value from the DP array
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
        6  # Subarray [4,-1,2,1] has sum 6
        >>> max_subarray_sum([])
        0  # Empty list returns 0
    """
    if not num_list:
        return 0
    dp = [0] * len(num_list)
    for i, num in enumerate(num_list):
        dp[i] = max(num, dp[i - 1] + num)
    return max(dp)
    
print(max_subarray_sum([]))