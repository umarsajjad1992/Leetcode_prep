"""
Linked List Palindrome Checker

This module implements a solution to check if a singly linked list forms a palindrome
using the two-pointer technique combined with in-place reversal.

The algorithm uses Floyd's Tortoise and Hare to find the middle, then reverses
the second half and compares it with the first half.

Example:
    For list [1,2,2,1] -> returns True (palindrome)
    For list [1,2,3,4,5] -> returns False (not palindrome)

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - only uses a constant amount of extra space
"""

from typing import Optional

class ListNode:
    """
    A node in a singly linked list.
    
    This class represents a single node in a linked list data structure,
    containing a value and a reference to the next node.
    
    Attributes:
        val (int): The value stored in this node
        next (Optional[ListNode]): Reference to the next node in the list, 
                                  or None if this is the last node
    
    Args:
        val (int, optional): The value to store in this node. Defaults to 0.
        next (Optional[ListNode], optional): The next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Check if a singly linked list forms a palindrome.
    
    This function determines if the linked list reads the same forwards and backwards
    using a two-phase approach:
    1. Find the middle using Floyd's Tortoise and Hare algorithm
    2. Reverse the second half of the list and compare with the first half
    
    Args:
        head (Optional[ListNode]): The head node of the linked list to check.
                                  Can be None for an empty list.
    
    Returns:
        None: Prints "It is a Palindrome" or "Not a Palindrome" to console.
    
    Examples:
        >>> # List: 1 -> 2 -> 2 -> 1
        >>> # Prints: "It is a Palindrome"
        
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5
        >>> # Prints: "Not a Palindrome"
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses a few pointer variables
    """

    fast = slow = head
    prev = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse List
    while slow:
        next_ptr = slow.next
        slow.next = prev
        prev = slow
        slow = next_ptr
    
    left = head
    right = prev
    while right:
        if left.val != right.val:
            print("Not a Palindrome")
            return False
        left = left.next
        right = right.next
    print("It is a Palindrome")
    return True

def main():
    """
    Demonstrate the is_palindrome function with a sample linked list.
    
    Creates a linked list with values [2, 2, 2, 2, 2, 2] and checks if it forms
    a palindrome. Since all values are the same, this should be a palindrome.
    
    The function prints whether the list is a palindrome to demonstrate the algorithm.
    """
    head = ListNode(2)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(2)
    
    # Check if the linked list is a palindrome
    is_palindrome(head)

if __name__ == "__main__":
    main()

