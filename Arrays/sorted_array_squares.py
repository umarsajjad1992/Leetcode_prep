"""
FILE: sorted_array_squares.py

DESCRIPTION:
This script contains functions to compute the squares of elements in a sorted array 
and return the result as a sorted array. The input array can contain both negative 
and positive integers, and the goal is to efficiently produce a sorted array of their squares.

FUNCTIONS:
1. sorted_squares: A simple implementation using list comprehension and sorting.
2. sorted_squares_v2: A more efficient implementation that uses a two-pointer approach 
   to merge the squares of negative and positive numbers into a sorted array.
3. sorted_squares_v3: An optimized implementation using a two-pointer approach to 
   directly construct the sorted array of squares in reverse order.

EXAMPLE USAGE:
Input: [-4, -1, 0, 3, 10]
Output:
- sorted_squares: [0, 1, 9, 16, 100]
- sorted_squares_v2: [0, 1, 9, 16, 100]
- sorted_squares_v3: [0, 1, 9, 16, 100]

TIME COMPLEXITY:
- sorted_squares: O(n log n), due to the sorting step.
- sorted_squares_v2: O(n), as it uses a two-pointer approach to merge sorted squares.
- sorted_squares_v3: O(n), as it uses a two-pointer approach to construct the result array.

SPACE COMPLEXITY:
- sorted_squares: O(n), due to the storage of squared values.
- sorted_squares_v2: O(n), due to the storage of squared values and merged results.
- sorted_squares_v3: O(n), due to the storage of the result array.
"""
from collections import deque

# My first attempt
def sorted_squares(num_list: list[int]) -> list:
    return sorted([num**2 for num in num_list])

# Non Trivial Version
def sorted_squares_v2(num_list: list[int]) -> list:
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