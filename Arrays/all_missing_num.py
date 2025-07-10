"""
Find All Missing Numbers

Find all missing numbers from range [1, n] in an array of size n.
Algorithm: Use set for O(1) lookup, iterate through expected range.
Time: O(n), Space: O(n)
"""

def all_miss(num_list: list[int]) -> list[int]:
    """
    Find all missing numbers from range [1, n] in array of size n.
    
    Args:
        num_list (list[int]): Array of integers (may contain duplicates)
        
    Returns:
        list[int]: List of missing numbers from range [1, len(num_list)]
        
    Algorithm:
        1. Convert input to set for O(1) lookup
        2. Iterate through range [1, n] and check presence in set
        3. Collect missing numbers
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> all_miss([1, 2, 3, 4, 6, 5, 2, 7])
        [8]  # Missing 8 from range [1, 8]
    """
    num_set = set(num_list)
    miss_list = []

    for i in range(1, len(num_list) + 1):
        if i not in num_set:
            miss_list.append(i)
    
    return miss_list

# Example usage: Given an array, find the missing numbers
print(all_miss([1, 2, 3, 4, 6, 5, 2, 7]))