def longest_mount(num_list: list[int]) -> int:
    """
    Find the length of the longest mountain in an array.
    
    A mountain is defined as a sequence of consecutive elements where:
    1. The sequence starts with strictly increasing elements
    2. Followed by strictly decreasing elements
    3. The mountain must have at least 3 elements
    
    Args:
        num_list (list[int]): List of integers to search for mountains
        
    Returns:
        int: Length of the longest mountain found, or 0 if no mountain exists
        
    Examples:
        >>> longest_mount([2, 1, 4, 7, 3, 2, 5])
        5  # Mountain: [1, 4, 7, 3, 2]
        
        >>> longest_mount([2, 2, 2])
        0  # No mountain (no strictly increasing/decreasing parts)
        
        >>> longest_mount([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])
        11  # Entire array forms one mountain
    """
    
    n = len(num_list)
    if n < 3:
        return 0


    count = 0
    for i in range(1, n - 1):
        if num_list[i - 1] < num_list[i] > num_list[i + 1]:
            l = r = i
            while l > 0 and num_list[l] > num_list[l-1]:
                l -= 1
            while r < n - 1 and num_list[r] > num_list[r+1]:
                r += 1
            count = max(count, r - l + 1)
    
    
    return count

print(longest_mount([2, 1, 4, 7, 3, 2, 1, 4, 6, 3, 2, 1, 0]))