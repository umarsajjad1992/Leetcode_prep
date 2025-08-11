"""
Linked List Cycle Detection

This module implements a solution to detect if a singly linked list contains a cycle
using Floyd's Cycle Detection Algorithm (also known as the Tortoise and Hare algorithm).

A cycle exists in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. The algorithm uses two pointers 
moving at different speeds to detect if they ever meet, which indicates a cycle.

Example:
    For list: 3 -> 2 -> -1 -> 4 -> (back to 2) -> creates a cycle
    Returns: True
    
    For list: 1 -> 2 -> 3 -> None (no cycle)
    Returns: False

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - only uses two pointers
"""

from typing import Optional

class ListNode:
    """
    A node in a singly linked list with cycle detection support.
    
    This class represents a single node in a linked list data structure,
    containing a value, position information, and a reference to the next node.
    The pos attribute is used for creating test cases with cycles.
    
    Attributes:
        val (int): The value stored in this node
        pos (int): Position indicator used for creating cycles in test cases
        next (Optional[ListNode]): Reference to the next node in the list, 
                                  or None if this is the last node
    
    Args:
        val (int, optional): The value to store in this node. Defaults to 0.
        pos (int, optional): Position indicator for cycle creation. Defaults to 0.
        next (Optional[ListNode], optional): The next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def cycleLinkedList(head: Optional[ListNode]) -> bool:
    """
    Detect if a linked list contains a cycle using Floyd's Cycle Detection Algorithm.
    
    This function uses the two-pointer technique where:
    - slow_ptr (tortoise) moves one step at a time
    - fast_ptr (hare) moves two steps at a time
    
    If there's a cycle, the fast pointer will eventually meet the slow pointer.
    If there's no cycle, the fast pointer will reach the end (None).
    
    Args:
        head (Optional[ListNode]): The head node of the linked list.
                                  Can be None for an empty list.
    
    Returns:
        bool: True if the linked list contains a cycle, False otherwise.
              Returns False for empty lists or single-node lists without self-loops.
    
    Examples:
        >>> # List with cycle: 1 -> 2 -> 3 -> (back to 2)
        >>> # Returns True
        
        >>> # List without cycle: 1 -> 2 -> 3 -> None
        >>> # Returns False
        
        >>> # Empty list: None
        >>> # Returns False
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses two pointer variables
    
    Note:
        This algorithm is also known as Floyd's Tortoise and Hare algorithm.
        It's guaranteed to detect a cycle if one exists, as the fast pointer
        will eventually "lap" the slow pointer within the cycle.
    """
    if not head or not head.next:
        return False
        
    slow_ptr = fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next  # type: ignore
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False



def main():
    """
    Demonstrate the cycleLinkedList function with a sample linked list containing a cycle.
    
    Creates a linked list with the structure:
    3 -> 2 -> -1 -> 4 -> (back to node with value 2)
    
    This creates a cycle where the last node (4) points back to the second node (2).
    The function should return True indicating that a cycle is detected.
    
    Test case visualization:
        Node 0: val=3,  next -> Node 1
        Node 1: val=2,  next -> Node 2  
        Node 2: val=-1, next -> Node 3
        Node 3: val=4,  next -> Node 1 (creates cycle)
    """
    # Create the linked list: 3 -> 2 -> -1 -> 4
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(-1)
    head.next.next.next = ListNode(4)
    
    # Create cycle: make the last node point back to the second node
    head.next.next.next.next = head.next
    
    # Test for cycle detection
    has_cycle = cycleLinkedList(head)
    print(f"Does the linked list have a cycle? {has_cycle}")

if __name__ == "__main__":
    main()