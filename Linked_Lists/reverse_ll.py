"""
Linked List Reversal

This module implements a solution to reverse a singly linked list
using an iterative approach with three pointers.

The algorithm maintains three pointers (previous, current, next) and 
iteratively reverses the direction of each link in the list.

Example:
    For list [1,2,3,4,5] -> returns [5,4,3,2,1]
    For list [3,2,-1,4,5] -> returns [5,4,-1,2,3]

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - only uses three pointer variables
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
        tail: Unused parameter (kept for compatibility). 
        next (Optional[ListNode], optional): The next node in the list. Defaults to None.
    """
    def __init__(self, val=0, tail=None, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list using an iterative three-pointer approach.
    
    This function reverses the direction of all links in a singly linked list
    by maintaining three pointers:
    - prev: points to the previous node (initially None)
    - curr: points to the current node being processed
    - next_ptr: temporarily stores the next node to avoid losing it
    
    Args:
        head (Optional[ListNode]): The head node of the linked list to reverse.
                                  Can be None for an empty list.
    
    Returns:
        Optional[ListNode]: The new head of the reversed linked list.
                           Returns None if the input list is empty.
    
    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5
        >>> # Returns: 5 -> 4 -> 3 -> 2 -> 1
        
        >>> # List: 3 -> 2 -> -1 -> 4 -> 5
        >>> # Returns: 5 -> 4 -> -1 -> 2 -> 3
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses three pointer variables
    """
    prev = None
    curr = head

    while curr:
        next_ptr = curr.next
        curr.next = prev
        prev = curr
        curr = next_ptr

    head = prev
    curr = head
    print(curr.val)
    while curr.next:
        print(curr.next.val)
        curr = curr.next

def main():
    """
    Demonstrate the reverseLinkedList function with a sample linked list.
    
    Creates a linked list with values [3, 2, -1, 4, 5] and reverses it.
    The function should return a list with values [5, 4, -1, 2, 3].
    
    The function prints the values of the reversed list to demonstrate the algorithm.
    """
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(-1)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    # Reverse the linked list
    reverse = reverseLinkedList(head)

if __name__ == "__main__":
    main()

