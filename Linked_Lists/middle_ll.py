"""
Linked List Middle Node Finder

This module implements a solution to find the middle node of a singly linked list
using the two-pointer technique (Floyd's Tortoise and Hare algorithm).

For odd-length lists, returns the exact middle node.
For even-length lists, returns the second of the two middle nodes.

Example:
    For list [1,2,3,4,5] -> returns node with value 3
    For list [1,2,3,4,5,6] -> returns node with value 4

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - only uses two pointers
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


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node of a singly linked list using the two-pointer technique.
    
    This function uses Floyd's Tortoise and Hare algorithm where two pointers
    traverse the list at different speeds:
    - slow pointer moves one step at a time
    - fast pointer moves two steps at a time
    
    When the fast pointer reaches the end, the slow pointer will be at the middle.
    
    Args:
        head (Optional[ListNode]): The head node of the linked list.
                                  Can be None for an empty list.
    
    Returns:
        Optional[ListNode]: The middle node of the list. For lists with even length,
                           returns the second of the two middle nodes.
                           Returns None if the input list is empty.
    
    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5
        >>> # Returns node with value 3
        
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6  
        >>> # Returns node with value 4
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses two pointer variables
    """
    if not head:
        return None
        
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next  # type: ignore
        fast = fast.next.next
    return slow


def main():
    """
    Demonstrate the middleNode function with a sample linked list.
    
    Creates a linked list with values [1, 2, 3, 4, 5, 6] and finds the middle node.
    For this even-length list, the function should return the node with value 4.
    
    The function prints the value of the middle node to demonstrate the algorithm.
    """
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    
    middle = middleNode(head)
    if middle:
        print(f"Middle node value: {middle.val}")
    else:
        print("List is empty")

if __name__ == "__main__":
    main()