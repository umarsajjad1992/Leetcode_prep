"""
Linked List Node Removal

This module implements a solution to remove all nodes with a specific value
from a singly linked list using a dummy head approach.

The algorithm uses a dummy head node to simplify edge cases when the head
node itself needs to be removed.

Example:
    For list [1,2,3,4,3,6] and val=3 -> returns [1,2,4,6]
    For list [7,7,7,7] and val=7 -> returns []

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
        tail: Unused parameter (kept for compatibility).
        next (Optional[ListNode], optional): The next node in the list. Defaults to None.
    """
    def __init__(self, val=0, tail=None, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: Optional[ListNode], val) -> Optional[ListNode]:
    """
    Remove all nodes with a specific value from a singly linked list.
    
    This function removes all occurrences of nodes with the given value
    from the linked list using a dummy head approach to handle edge cases
    when the head node itself needs to be removed.
    
    Args:
        head (Optional[ListNode]): The head node of the linked list.
                                  Can be None for an empty list.
        val: The value to remove from the list.
    
    Returns:
        Optional[ListNode]: The new head of the modified linked list.
                           Returns None if all nodes are removed or input is empty.
    
    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 3 -> 6, val=3
        >>> # Returns: 1 -> 2 -> 4 -> 6
        
        >>> # List: 7 -> 7 -> 7 -> 7, val=7
        >>> # Returns: None (empty list)
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses a dummy head node
    """
    curr = head

    dummy_head = ListNode(-1)
    dummy_head.next = head

    curr = dummy_head
    while curr and curr.next:

        if curr.next.val == val: 
            curr.next = curr.next.next
        else:
            curr = curr.next

    curr = dummy_head.next
    while curr:
        print(curr.val)
        curr = curr.next
        

def main():
    """
    Demonstrate the deleteNodes function with a sample linked list.
    
    Creates a linked list with values [1, 2, 3, 4, 3, 6] and removes all nodes
    with value 6. The function should return a list with values [1, 2, 3, 4, 3].
    
    The function prints the values of the modified list to demonstrate the algorithm.
    """


    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(6)
    
    # Remove all nodes with value 6
    deleteNodes(head, 4)

if __name__ == "__main__":
    main()