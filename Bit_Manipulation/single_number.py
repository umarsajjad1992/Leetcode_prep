"""
Single Number Problem Solutions

Find the single number in an array where every element appears twice except one.
Two different approaches: hashing and XOR bit manipulation.

Example: [4, 1, 2, 1, 2] → 4 (appears only once)
"""

# Hashing technique
def sing_num(num_list: list[int]):
    """
    Find the single number using hash table approach.
    
    Args:
        num_list (list[int]): List of integers where all elements appear twice except one
        
    Returns:
        int: The single number that appears only once
        
    Algorithm:
        1. Create a dictionary to count occurrences of each number
        2. Iterate through the list and count each number
        3. Find the key with the minimum count (which will be 1)
        4. Return that single number
        
    Time: O(n), Space: O(n)
    
    Example:
        >>> sing_num([4, 1, 2, 1, 2])
        4  # Only appears once
    """
    mydict = {}
    for num in num_list:
        if num not in mydict:
            mydict[num] = 1
            continue
        mydict[num] += 1
    for key, value in mydict.items():
        if value == 1:
            return key
        
# Bit Manipulation technique
def sing_num_bit(num_list: list[int]) -> int:
    """
    Find the single number using XOR bit manipulation.
    
    Args:
        num_list (list[int]): List of integers where all elements appear twice except one
        
    Returns:
        int: The single number that appears only once
        
    Algorithm:
        1. Initialize XOR result to 0
        2. XOR all numbers in the list
        3. Since a XOR a = 0 and a XOR 0 = a, duplicate numbers cancel out
        4. Only the single number remains
        
    Time: O(n), Space: O(1)
    
    Example:
        >>> sing_num_bit([4, 1, 2, 1, 2, 4, 5])
        5  # Only appears once
    """
    xor = 0
    for num in num_list:
        xor ^= num

    return xor

print(sing_num([4, 1, 2, 1, 2])) 
print(sing_num_bit([4, 1, 2, 1, 2, 4, 5]))