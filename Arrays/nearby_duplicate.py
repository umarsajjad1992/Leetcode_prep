def contains_nearby_duplicate_v2(num_list: list[int], k: int) -> bool:
    """
    Check if there are duplicate values exactly k positions apart in the array.
    
    This function looks for pairs of identical elements where the second element
    is exactly k positions after the first element (i.e., at indices i and i+k).
    
    Args:
        num_list (list[int]): List of integers to check for nearby duplicates
        k (int): The exact distance between duplicate elements to search for
        
    Returns:
        bool: True if there exists a pair of identical elements exactly k positions apart,
              False otherwise
              
    Examples:
        >>> contains_nearby_duplicate_v2([1, 2, 3, 1, 2, 3], 3)
        True  # num_list[0] == num_list[3] (both are 1)
        
        >>> contains_nearby_duplicate_v2([1, 0, 1, 1], 1)
        True  # num_list[2] == num_list[3] (both are 1)
        
        >>> contains_nearby_duplicate_v2([1, 2, 3, 1, 2, 3], 2)
        False  # No elements are identical exactly 2 positions apart
        
    Note:
        This function checks for duplicates at exactly distance k, not within distance k.
        Time complexity: O(n) where n is the length of num_list
        Space complexity: O(1)
    """
    for i in range(len(num_list) - k):
        if num_list[i] == num_list[i + k]:
            return True
    return False



print(contains_nearby_duplicate_v2(num_list=[1, 2, 3, 1, 2, 3], k=3))