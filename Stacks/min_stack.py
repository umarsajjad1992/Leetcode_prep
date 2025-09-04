"""
MinStack Implementation - LeetCode Problem Solution

This module implements a stack data structure that supports push, pop, top,
and retrieving the minimum element in constant time O(1).

The solution uses a stack of tuples where each element stores both the value
and the minimum value seen so far from the bottom of the stack up to that element.
This approach ensures that all operations (push, pop, top, getMin) run in O(1) time
without requiring additional space for a separate minimum-tracking structure.

Example:
    >>> stack = MinStack()
    >>> stack.push(-2)
    >>> stack.push(0)
    >>> stack.push(-3)
    >>> stack.getMin()  # Returns -3
    >>> stack.pop()
    >>> stack.top()     # Returns 0
    >>> stack.getMin()  # Returns -2

Time Complexity: O(1) for all operations
Space Complexity: O(n) where n is the number of elements, with O(1) overhead per element
"""

from typing import Optional, Tuple, List


class MinStack:
    """
    A stack implementation that supports retrieving the minimum element in O(1) time.
    
    This class maintains a stack where each element is stored as a tuple containing
    the actual value and the minimum value from the bottom of the stack up to that position.
    This allows constant-time access to the minimum element without additional space overhead
    for a separate min-tracking structure.
    
    The stack follows LIFO (Last In, First Out) principle while maintaining minimum element
    information at each level. When an element is pushed, the current minimum is calculated
    and stored with the element. When elements are popped, the minimum information is
    automatically maintained.
    
    Attributes:
        stack (List[Tuple[int, int]]): Internal list storing tuples of (value, min_so_far)
                                      where the first element is the actual value and
                                      the second is the minimum value up to that point
    
    Examples:
        >>> min_stack = MinStack()
        >>> min_stack.push(-2)
        >>> min_stack.push(0)
        >>> min_stack.push(-3)
        >>> min_stack.getMin()  # Returns -3
        >>> min_stack.pop()
        >>> min_stack.top()     # Returns 0
        >>> min_stack.getMin()  # Returns -2
    """

    def __init__(self) -> None:
        """
        Initialize an empty MinStack.
        
        Creates an empty stack that will store tuples of (element, current_minimum).
        The stack starts empty and will grow dynamically as elements are added.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.stack: List[Tuple[int, int]] = []

    def push(self, element: int) -> None:
        """
        Push an element onto the stack.
        
        Adds the given element to the top of the stack along with the current minimum value.
        The minimum is calculated as the smaller of the new element and the previous minimum.
        If the stack is empty, the new element becomes both the value and the minimum.
        
        Args:
            element (int): The integer value to push onto the stack
            
        Returns:
            None: This method doesn't return anything
            
        Time Complexity: O(1)
        Space Complexity: O(1) per element
        """
        if not self.stack:
            current_min = element
        else:
            current_min = min(element, self.stack[-1][1])
        self.stack.append((element, current_min))
    
    def pop(self) -> None:
        """
        Remove the top element from the stack.
        
        Removes the most recently added element from the stack along with its
        associated minimum value. This operation doesn't return the popped value,
        following the LeetCode problem specification.
        
        Returns:
            None: This method doesn't return the popped element
            
        Raises:
            IndexError: If the stack is empty when pop() is called
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack without removing it.
        
        Returns the most recently added element from the stack without modifying 
        the stack structure. This is a peek operation that allows you to see
        what's on top of the stack.
        
        Returns:
            int: The value of the top element in the stack
            
        Raises:
            IndexError: If the stack is empty when top() is called
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack in constant time.
        
        Returns the smallest element currently in the stack without removing it.
        This operation runs in constant time due to the stack's internal structure
        where each element stores the minimum value seen up to that point.
        
        Returns:
            int: The minimum value currently stored in the stack
            
        Raises:
            IndexError: If the stack is empty when getMin() is called
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("getMin from empty stack")
        return self.stack[-1][1]
    
def main() -> None:
    """
    Demonstrate the MinStack functionality with comprehensive examples.
    
    This function creates a MinStack instance and performs various operations
    to showcase the stack's capabilities, including push, pop, top, and getMin
    operations. It demonstrates how the minimum element tracking works correctly
    even as elements are added and removed.
    
    The example shows:
    1. Pushing multiple elements including negative numbers
    2. Retrieving the minimum element
    3. Getting the top element  
    4. Popping elements and observing how minimum changes
    
    Time Complexity: O(1) for each operation
    Space Complexity: O(n) where n is the number of elements pushed
    """
    print("MinStack Demonstration:")
    print("=" * 25)
    
    # Create a new MinStack instance
    mystack = MinStack()
    
    # Push elements and show the operations
    operations = [1, 4, 7, -3]
    for val in operations:
        mystack.push(val)
        print(f"Pushed {val} | Min: {mystack.getMin()} | Top: {mystack.top()}")
    
    print(f"\nFinal minimum element: {mystack.getMin()}")  # Should print -3
    print(f"Top element: {mystack.top()}")                 # Should print -3
    
    # Demonstrate popping and how minimum changes
    mystack.pop()
    print(f"After popping | Min: {mystack.getMin()} | Top: {mystack.top()}")


if __name__ == "__main__":
    main()
