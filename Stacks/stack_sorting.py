"""
Stack Sorting Algorithm - Data Structure Problem Solution

This module implements a solution to sort a stack using only one additional stack.
The algorithm sorts the input stack in ascending order (smallest elements at the bottom,
largest at the top) without using any other data structures.

The solution uses a two-stack approach where elements are moved between the original
stack and a temporary stack to achieve the sorted order. The algorithm ensures that
the temporary stack maintains sorted order at all times by moving elements back to
the original stack when necessary.

Sorting strategy:
1. Use a temporary stack to maintain sorted order (largest at top)
2. Pop elements from original stack one by one
3. Find correct position in temp stack by moving larger elements back
4. Insert current element at correct position in temp stack

Example:
    For stack [43, 2, 31, 98, 23, 92] -> returns [2, 23, 31, 43, 92, 98]
    For stack [5, 3, 8, 1] -> returns [1, 3, 5, 8]
    For stack [10] -> returns [10]
    For stack [] -> returns []

Time Complexity: O(n²) where n is the number of elements in the stack
Space Complexity: O(n) for the additional temporary stack
"""

from typing import List


def stack_sort(stack: List[int]) -> List[int]:
    """
    Sort a stack using only one additional stack.
    
    Uses a two-stack algorithm to sort the input stack in ascending order.
    The function maintains a temporary stack that is always sorted (largest at top).
    For each element popped from the original stack, it finds the correct position
    in the temporary stack by moving larger elements back to the original stack.
    
    Args:
        stack (List[int]): Input stack represented as a list where the last element
                          is the top of the stack. The original stack is modified
                          during the sorting process.
    
    Returns:
        List[int]: A new sorted stack in ascending order where the first element
                  is the smallest and the last element is the largest.
                  Returns empty list if input stack is empty.
    
    Examples:
        >>> # Stack: [43, 2, 31, 98, 23, 92]
        >>> # Returns [2, 23, 31, 43, 92, 98]
        
        >>> # Stack: [5, 3, 8, 1]  
        >>> # Returns [1, 3, 5, 8]
        
        >>> # Stack: [10]
        >>> # Returns [10]
    
    Algorithm:
        1. Create an empty temporary stack
        2. While original stack is not empty:
           - Pop an element from original stack
           - While temp stack is not empty and top element is smaller:
             * Move elements from temp stack back to original stack
           - Push current element onto temp stack
        3. Return the sorted temporary stack
    
    Note:
        The input stack is modified during the sorting process. If you need
        to preserve the original stack, pass a copy of it.
    
    Time Complexity: O(n²) where n is the number of elements in the stack
                    In worst case (reverse sorted), each element may be moved n times
    Space Complexity: O(n) for the additional temporary stack
    """
    # Temporary stack to maintain sorted order (largest at top)
    temp_stack: List[int] = []
    
    # Process all elements from the original stack
    while stack:
        # Pop the top element from original stack
        current_element = stack.pop()
        
        # Move elements from temp stack back to original stack
        # until we find the correct position for current element
        while temp_stack and temp_stack[-1] > current_element:
            # Move larger elements back to original stack
            stack.append(temp_stack.pop())
        
        # Insert current element at its correct position in temp stack
        temp_stack.append(current_element)
    
    # Return the sorted temporary stack
    return temp_stack


def main():
    """
    Demonstrate the stack_sort function with comprehensive test cases.
    
    This function tests various stack configurations to showcase the
    sorting algorithm's capabilities. It includes different stack sizes,
    edge cases, and various sorting scenarios to provide thorough examples.
    
    Creates test cases covering normal cases, edge cases, already sorted stacks,
    reverse sorted stacks, and stacks with duplicate elements. For each test,
    it shows the input stack and the sorted result.
    """
    # Test cases with different stack configurations
    test_stacks = [
        ([43, 2, 31, 98, 23, 92], [2, 23, 31, 43, 92, 98], "Random order stack"),
        ([5, 3, 8, 1], [1, 3, 5, 8], "Small random stack"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Already sorted stack"),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "Reverse sorted stack"),
        ([10], [10], "Single element stack"),
        ([], [], "Empty stack"),
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3], "Stack with duplicates"),
        ([100, 50, 75, 25], [25, 50, 75, 100], "Powers and multiples"),
        ([7, 7, 7, 7], [7, 7, 7, 7], "All identical elements")
    ]
    
    print("Stack Sorting Algorithm Demonstration:")
    print("=" * 42)
    
    for original, expected, description in test_stacks:
        # Use copy to preserve original for display
        stack_copy = original.copy()
        print(f"\nInput Stack: {original}")
        print(f"Description: {description}")
        result = stack_sort(stack_copy)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | Sorted: {result} | Expected: {expected}")
        print("-" * 50)
    
    print(f"\nTest Summary: Sorting stacks using auxiliary stack")
    print(f"Algorithm: Two-stack sorting with element repositioning")


if __name__ == "__main__":
    main()