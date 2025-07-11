"""
Two Sum Problem Solution

Find two numbers in an array that add up to a target sum using hash map.
Two approaches: basic and optimized single-pass implementations.

Example: [2, 7, 11, 15], target=9 → [0, 1] (indices of 2 and 7)
"""

def two_sum(num_list: list[int], target) -> list[int]:
    """
    Find two numbers that add up to target using hash map approach.
    
    Args:
        num_list (list[int]): Array of integers
        target (int): Target sum to find
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
        
    Algorithm:
        1. Create hash map to store numbers and their indices
        2. For each number, calculate complement (target - num)
        3. If complement not in hash map, store current number
        4. If complement found, return indices of both numbers
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]  # indices of 2 and 7
    """
    hash_map = {}

    for i, num in enumerate(num_list):
        temp = target - num
        if temp not in hash_map.keys():
            hash_map[num] = i
        else:
            return [hash_map[temp], i]
        
def two_sum_v2(num_list: list[int], target) -> list[int]:
    """
    Find two numbers that add up to target using optimized single-pass approach (preferred).
    
    Args:
        num_list (list[int]): Array of integers
        target (int): Target sum to find
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
        
    Algorithm:
        1. Create hash map to store numbers and their indices
        2. For each number, calculate complement (target - num)
        3. If complement exists in hash map, return indices immediately
        4. Otherwise, store current number and continue
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> two_sum_v2([2, 7, 11, 15], 9)
        [0, 1]  # indices of 2 and 7
        
    Note: Preferred solution - more efficient with early termination.
    """
    hash_map = {}

    for ind, num in enumerate(num_list):
        diff = target - num
        if diff in hash_map.keys():
            return [hash_map[diff], ind]
        hash_map[num] = ind
            


print(two_sum_v2([2, 7, 11, 15], 2))