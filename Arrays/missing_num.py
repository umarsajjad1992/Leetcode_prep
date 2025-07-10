"""
Missing Number Problem Solutions

Two approaches to find the missing number from range [0, 1, 2, ..., n]:
1. miss_num(): Sorting approach - O(n log n)
2. fast_miss_num(): Sum approach - O(n) [Preferred]

Example: [3, 0, 1] → missing 2
"""

# Good Solution but Slow
def miss_num(num_list: list[int]) -> int:
    """
    Find missing number using sorting approach.
    
    Args:
        num_list (list[int]): Array with one missing number from range [0, n]
        
    Returns:
        int: The missing number
        
    Algorithm:
        1. Sort array to arrange numbers in order
        2. Compare each element with its index
        3. Return first index where arr[i] != i
        4. If no mismatch, missing number is n (last position)
        
    Time: O(n log n), Space: O(1)
    
    Example:
        >>> miss_num([3, 0, 1])  # After sort: [0, 1, 3]
        2  # arr[2] = 3 ≠ 2, so missing = 2
    
    Note: Modifies input array.
    """
    num_list.sort()
    for i, num in enumerate(num_list):
        if i != num:
            return i
        
        if i == len(num_list) - 1:
            return i + 1

def fast_miss_num(num_list: list[int]) -> int:
    """
    Find missing number using mathematical sum approach (optimal).
    
    Args:
        num_list (list[int]): Array with one missing number from range [0, n]
        
    Returns:
        int: The missing number
        
    Algorithm:
        Uses arithmetic series sum formula: sum([0, 1, ..., n]) = n*(n+1)/2
        Missing number = Expected sum - Actual sum
        
        1. Calculate expected sum: sum(range(len(num_list) + 1))
        2. Calculate actual sum: sum(num_list)  
        3. Return the difference
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> fast_miss_num([3, 0, 1])
        2  # Expected: 0+1+2+3=6, Actual: 3+0+1=4, Missing: 6-4=2
    
    Note: Preferred solution. Does not modify input.
    """
    return (sum(range(len(num_list) + 1)) - sum(num_list))

print(fast_miss_num([0, 4, 5, 3, 1]))