"""
Longest Mountain Problem Solution

Find the length of the longest mountain in an array using peak detection.
A mountain is a sequence with strictly increasing then decreasing elements.

Example: [2, 1, 4, 7, 3, 2, 5] → 5 (mountain: [1, 4, 7, 3, 2])
"""

def longest_mount(num_list: list[int]) -> int:
    """
    Find the length of the longest mountain in an array.
    
    Args:
        num_list (list[int]): Array of integers to search for mountains
        
    Returns:
        int: Length of the longest mountain, or 0 if no mountain exists
        
    Algorithm:
        1. Iterate through array to find potential peaks (local maxima)
        2. For each peak, expand left while strictly increasing
        3. Expand right while strictly decreasing
        4. Calculate mountain length and track maximum
        5. Return the longest mountain found
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> longest_mount([2, 1, 4, 7, 3, 2, 5])
        5  # Mountain: [1, 4, 7, 3, 2]
        
    Note: A mountain must have at least 3 elements with strict increase then decrease.
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