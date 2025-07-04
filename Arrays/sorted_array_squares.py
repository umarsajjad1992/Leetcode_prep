"""
FILE: sorted_array_squares.py

DESCRIPTION:
This script contains functions to compute the squares of elements in a sorted array 
and return the result as a sorted array. The input array can contain both negative 
and positive integers, and the goal is to efficiently produce a sorted array of their squares.

FUNCTIONS:
1. sorted_squares: A simple implementation using list comprehension and sorting.
2. sorted_squares_v2: A more efficient implementation that merges two sorted subarrays 
   (negative and positive parts) to produce the result.

EXAMPLE USAGE:
Input: [-4, -1, 0, 3, 10]
Output:
- sorted_squares: [0, 1, 9, 16, 100]
- sorted_squares_v2: [0, 1, 9, 16, 100]

TIME COMPLEXITY:
- sorted_squares: O(n log n), due to the sorting step.
- sorted_squares_v2: O(n), as it uses a two-pointer approach to merge sorted subarrays.
- sorted_squares_v3: O(n), as it uses a two-pointer approach to merge sorted subarrays.

SPACE COMPLEXITY:
- sorted_squares: O(n), due to the storage of squared values.
- sorted_squares_v2: O(n), due to the storage of squared values and merged results.
- sorted_squares_v3: O(1), due to only.
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

    while num_list:
        l_val, r_val = num_list[0], num_list[-1]
        if (abs(l_val) > abs(r_val)):
            answers.appendleft(l_val**2)
            num_list.pop(0)
        else:
            answers.appendleft(r_val**2)
            num_list.pop()

    return list(answers)
print(sorted_squares_v2([-7, -3, -1, 0, 2, 3, 11]))
print(sorted_squares_v3([-7, -3, -1, 0, 2, 3, 11]))