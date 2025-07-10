"""
Nearby Duplicate Detection

Check if there are duplicate values exactly k positions apart in an array.
Algorithm: Compare elements at indices i and i+k for all valid i.
Time: O(n), Space: O(1)
"""

def contains_nearby_duplicate_v2(num_list: list[int], k: int) -> bool:
    """
    Check if there are duplicate values exactly k positions apart.
    
    Args:
        num_list (list[int]): List of integers to check
        k (int): Exact distance between duplicate elements to search for
        
    Returns:
        bool: True if duplicates found exactly k positions apart, False otherwise
              
    Algorithm:
        Iterate through array and compare each element at index i with element
        at index i+k. Return True on first match found.
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> contains_nearby_duplicate_v2([1, 2, 3, 1, 2, 3], 3)
        True  # num_list[0] == num_list[3] (both are 1)
    
    Note: Checks exactly distance k, not within distance k.
    """
    for i in range(len(num_list) - k):
        if num_list[i] == num_list[i + k]:
            return True
    return False



print(contains_nearby_duplicate_v2(num_list=[1, 2, 3, 1, 2, 3], k=3))