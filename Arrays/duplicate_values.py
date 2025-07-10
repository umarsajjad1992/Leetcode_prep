"""
Duplicate Detection

Check if an array contains duplicate values.
Algorithm: Compare length of original list with set (unique elements).
Time: O(n), Space: O(n)
"""

def duplicates(num_list: list[int]) -> bool:
    """
    Check if array contains duplicate values.
    
    Args:
        num_list (list[int]): List of integers to check
        
    Returns:
        bool: True if duplicates exist, False otherwise
        
    Algorithm:
        Convert list to set (removes duplicates) and compare lengths.
        If lengths differ, duplicates exist.
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> duplicates([1, 2, 3, 1])
        True  # 1 appears twice
        
        >>> duplicates([1, 2, 3])
        False  # No duplicates
    """

    if len(set(num_list)) == len(num_list):
        return False
    return True

print(duplicates([1,2,3]))

