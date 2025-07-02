# DESCRIPTION:
# This script contains a function `num_smaller` that calculates, for each number 
# in the input list, how many numbers are smaller than it when the list is sorted. 
# The function returns a list of these counts.

# TIME COMPLEXITY:
# 1. Sorting the input list: O(n log n), where n is the length of the input list.
# 2. Iterating through the sorted list to populate the dictionary: O(n).
# 3. Iterating through the original list to append counts: O(n).
# Overall time complexity: O(n log n), dominated by the sorting step.

# EXAMPLE USAGE:
# Input: [1, 2, 9, 15, 12, 5, 2, 7, 9]
# Output: [0, 1, 6, 8, 7, 4, 1, 5, 6]

def num_smaller(num_list: list[int]) -> list[int]:
    # Sort the input list in ascending order
    num_sorted = sorted(num_list)
    
    # Create a dictionary to store the index of each unique number in the sorted list
    temp_dict = {}
    
    # Initialize an empty list to store the result
    ret = []
    
    # Iterate through the sorted list and populate the dictionary
    # Since it's a sorted list,
    # The index will represent how many numbers are smaller than current number
    for i, num in enumerate(num_sorted):
        # This if condition is to ensure repeated numbers have the same value
        if num not in temp_dict.keys():
            temp_dict[num] = i
    
    # Iterate through the list again and append the index to the result list
    for num in num_list:
        ret.append(temp_dict[num])

    return(ret)

print(num_smaller([1, 2, 9, 15, 12, 5, 2, 7, 9]))