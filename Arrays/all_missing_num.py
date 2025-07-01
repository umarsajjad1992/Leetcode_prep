"""
DESCRIPTION:
This script solves the problem of finding missing numbers in a given list of integers.
The function `all_miss` takes a list of integers as input, where the integers are expected
to range from 1 to n (n being the length of the list). The function identifies and returns
a list of numbers that are missing from the input list.

PROBLEM STATEMENT:
Given an array of size n containing integers ranging from 1 to n, some numbers may be
missing or duplicated. The task is to find all the missing numbers in the range [1, n].

EXAMPLE:
Input: [1, 2, 3, 4, 6, 5, 2, 7]
Output: [8]
"""

def all_miss(num_list: list[int]) -> list[int]:
    # Convert the input list to a set to remove duplicates
    num_set = set(num_list)
    
    # Empty list to store missing numbers
    miss_list = []

    for i in range(1, len(num_list) + 1):
        # Check if the current number is not in the set
        if i not in num_set:
            miss_list.append(i)
    
    return miss_list

# Example usage: Given an array, find the missing numbers
print(all_miss([1, 2, 3, 4, 6, 5, 2, 7]))