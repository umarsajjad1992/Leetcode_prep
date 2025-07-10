"""
Numbers Smaller Than Current Number

For each element, count how many numbers in the array are smaller than it.
Algorithm: Sort array, map each unique number to its index (count of smaller numbers).
Time: O(n log n), Space: O(n)
"""

def num_smaller(num_list: list[int]) -> list[int]:
    """
    Count how many numbers are smaller than each element.
    
    Args:
        num_list (list[int]): List of integers to analyze
        
    Returns:
        list[int]: Count of smaller numbers for each element (maintains original order)
                   
    Algorithm:
        1. Sort array to get relative positions
        2. Map each unique number to its sorted index (= count of smaller numbers)
        3. For duplicates, use leftmost index (smallest count)
        4. Map original elements to their counts
        
    Time: O(n log n), Space: O(n)
    
    Example:
        >>> num_smaller([8, 1, 2, 2, 3])
        [4, 0, 1, 1, 3]  # 8 has 4 smaller, 1 has 0 smaller, etc.
    
    Note: Duplicates get same count.
    """
    num_sorted = sorted(num_list)
    temp_dict = {}
    ret = []
    
    for i, num in enumerate(num_sorted):
        if num not in temp_dict.keys():
            temp_dict[num] = i
    
    for num in num_list:
        ret.append(temp_dict[num])

    return(ret)

print(num_smaller([1, 2, 9, 15, 12, 5, 2, 7, 9]))