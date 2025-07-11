"""
Three Sum Problem Solution

Find all unique triplets in an array that sum to zero using two-pointer technique.
Two approaches: basic set-based and optimized duplicate-handling implementations.

Example: [-1, 0, 1, 2, -1, -4] → [[-1, -1, 2], [-1, 0, 1]]
"""

def threeSum(num_list: list[int]) -> list[list[int]]:
    """
    Find all unique triplets that sum to zero using set-based approach.
    
    Args:
        num_list (list[int]): Array of integers
        
    Returns:
        list[list[int]]: List of unique triplets that sum to zero
        
    Algorithm:
        1. Sort the array to enable two-pointer technique
        2. For each element, use two pointers to find complementary pair
        3. Use set to automatically handle duplicates
        4. Convert set of tuples back to list of lists
        
    Time: O(n²), Space: O(n)
    
    Example:
        >>> threeSum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    num_list.sort()

    ret = set()
    for ind, val in enumerate(num_list):

        i = val
        l, r = ind + 1, len(num_list) - 1

        while l < r:

            j, k = num_list[l], num_list[r]
            current_sum = i + j + k
            
            if  current_sum == 0:
                ret.add((i, j, k))
                break
            elif current_sum > 0:
                r -= 1
            else:
                l += 1
    return [list(item) for item in ret]

def threeSum_v2(num_list: list[int]) -> list[list[int]]:
    """
    Find all unique triplets that sum to zero with optimized duplicate handling (preferred).
    
    Args:
        num_list (list[int]): Array of integers
        
    Returns:
        list[list[int]]: List of unique triplets that sum to zero
        
    Algorithm:
        1. Sort the array to enable two-pointer technique
        2. Skip duplicate values for the first element
        3. For each element, use two pointers to find complementary pair
        4. When triplet found, skip duplicates for both pointers
        5. Move pointers appropriately based on sum comparison
        
    Time: O(n²), Space: O(1)
    
    Example:
        >>> threeSum_v2([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        
    Note: Preferred solution - more efficient with explicit duplicate handling.
    """
    num_list.sort()
    ret = []
    n = len(num_list)
    for ind, val in enumerate(num_list):
        if ind > 0 and val == num_list[ind - 1]:
            continue
        i = val
        l, r = ind + 1, n - 1
        while l < r:
            j, k = num_list[l], num_list[r]
            currentSum = i + j + k
            if currentSum == 0:
                ret.append([i, j, k])
                while l < r and j == num_list[l + 1]:
                    l += 1
                l += 1
            elif currentSum < 0:
                l += 1
            else:
                r -= 1
    return ret

print(threeSum_v2([-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3, 5, -6, 2, 3]))
# [-4, -1, -1, -1, 0, 0, 1, 1, 2, 2, 3]