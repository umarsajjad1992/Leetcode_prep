"""
Sorted Array Squares Problem Solutions

Three approaches to compute squares of a sorted array and return sorted result:
1. sorted_squares(): Simple sort approach - O(n log n) 
2. sorted_squares_v2(): Two-pointer merge approach - O(n)
3. sorted_squares_v3(): Two-pointer deque approach - O(n) [Preferred]

Example: [-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100]
"""
from collections import deque

# My first attempt
def sorted_squares(num_list: list[int]) -> list:
    """
    Square all elements and sort using built-in sort (simple approach).
    
    Args:
        num_list (list[int]): Sorted array of integers (can contain negatives)
        
    Returns:
        list[int]: Sorted array of squares
        
    Algorithm:
        1. Square each element using list comprehension
        2. Sort the squared values using built-in sort
        
    Time: O(n log n), Space: O(n)
    
    Example:
        >>> sorted_squares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
    """
    return sorted([num**2 for num in num_list])

# Non Trivial Version
def sorted_squares_v2(num_list: list[int]) -> list:
    """
    Square elements using two-pointer merge approach (split and merge).
    
    Args:
        num_list (list[int]): Sorted array of integers (can contain negatives)
        
    Returns:
        list[int]: Sorted array of squares
        
    Algorithm:
        1. Handle edge cases (empty array, all positive numbers)
        2. Split array into positive and negative parts
        3. Convert negatives to positive and reverse order
        4. Merge the two sorted arrays of absolute values
        5. Square the final merged result
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> sorted_squares_v2([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
    """
    if not num_list:
        return None
    
    # Return squared list if no -ve element
    if num_list[0] >= 0:
        return [num**2 for num in num_list]
    
    # Find first +ve element
    m = 0
    for i, num in enumerate(num_list):
        if num >= 0:
            m = i
            break
    
    # split positive and negative numbers
    A = num_list[m:]
    B = [num*-1 for num in num_list[:m]][::-1]

    # Compared and merge the two list A and B
    def merge(A, B):
        """
        Merge two sorted arrays into one sorted array.
        
        Args:
            A (list[int]): First sorted array (positive numbers)
            B (list[int]): Second sorted array (absolute values of negatives)
            
        Returns:
            list[int]: Merged array with squares applied
            
        Algorithm:
            1. Use two pointers to compare elements from both arrays
            2. Always pick the smaller element and add to result
            3. Extend result with remaining elements from non-empty array
            4. Square all elements in the final result
        """
        a = b = 0
        ret = []
        while A and B:
            if A[a] < B[b]:
                ret.append(A.pop(0))
            else:
                ret.append(B.pop(0))

        if len(A) == 0:
            ret.extend(B[:])
            print(ret)
        else:
            ret.extend(A[:])
        
        return [num**2 for num in ret]
    
    return merge(A, B)


# two pointer method
def sorted_squares_v3(num_list: list[int]) -> list:
    """
    Square elements using two-pointer deque approach (optimal solution).
    
    Args:
        num_list (list[int]): Sorted array of integers (can contain negatives)
        
    Returns:
        list[int]: Sorted array of squares
        
    Algorithm:
        1. Use two pointers: left at start, right at end
        2. Compare absolute values of elements at both pointers
        3. Square the larger absolute value and add to front of deque
        4. Move the pointer that had the larger absolute value
        5. Continue until pointers meet
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> sorted_squares_v3([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        
    Note: Preferred solution - most efficient and clean implementation.
    """
    answers = deque()
    l, r = 0, len(num_list) - 1
    while l <= r:
        left, right = abs(num_list[l]), abs(num_list[r])
        if left > right:
            answers.appendleft(left**2)
            l += 1
        else:
            answers.appendleft(right**2)
            r -= 1

    return list(answers)


# print(sorted_squares_v2([-7, -3, -1, 0, 2, 3, 11]))
print(sorted_squares_v3([-7, -3, -1, 0, 2, 3, 11]))