"""
Linked List Partial Reversal

This module implements solutions to reverse a portion of a singly linked list
between two given positions using different approaches.

The algorithms reverse only the nodes between positions 'left' and 'right' (inclusive),
while keeping the rest of the list intact.

Example:
    For list [1,2,3,4,5] with left=2, right=4 -> returns [1,4,3,2,5]
    For list [1,2,3,4,5] with left=1, right=3 -> returns [3,2,1,4,5]

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

def reverseLinkedList2(head: Optional[ListNode], left=2, right=4) -> Optional[ListNode]:
    """
    Reverse nodes of a linked list between positions left and right (inclusive).
    
    This function reverses only the portion of the linked list between the given
    positions using a two-pass approach:
    1. First pass: Navigate to the starting position
    2. Second pass: Reverse the specified range of nodes
    
    Args:
        head (Optional[ListNode]): The head node of the linked list.
                                  Can be None for an empty list.
        left (int, optional): The starting position (1-indexed) of reversal. Defaults to 2.
        right (int, optional): The ending position (1-indexed) of reversal. Defaults to 4.
    
    Returns:
        Optional[ListNode]: The head of the modified linked list.
                           Returns None if the input list is empty.
    
    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5, left=2, right=4
        >>> # Returns: 1 -> 4 -> 3 -> 2 -> 5
        
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5, left=1, right=3
        >>> # Returns: 3 -> 2 -> 1 -> 4 -> 5
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses a dummy head and few pointer variables
    """

    dummmy_head = ListNode(-1, head)

    left_node, curr_node = dummmy_head, head
    for i in range(left-1):
        left_node, curr_node = curr_node, curr_node.next
    
    prev = None
    for i in range(right-left+1):
        next_ptr = curr_node.next
        curr_node.next = prev
        prev = curr_node
        curr_node = next_ptr
    
    left_node.next.next = curr_node
    left_node.next = prev
    

    curr = dummmy_head.next
    while curr:
        print(curr.val)
        curr = curr.next

    return dummmy_head.next

def reverseLinkedList2_v2(head: Optional[ListNode], left=2, right=4) -> Optional[ListNode]:
    """
    Reverse nodes of a linked list between positions left and right (alternative approach).
    
    This function reverses only the portion of the linked list between the given
    positions using a single-pass approach with position tracking:
    - Uses a position counter to identify the reversal range
    - Reverses nodes only when within the specified range
    
    Args:
        head (Optional[ListNode]): The head node of the linked list.
                                  Can be None for an empty list.
        left (int, optional): The starting position (1-indexed) of reversal. Defaults to 2.
        right (int, optional): The ending position (1-indexed) of reversal. Defaults to 4.
    
    Returns:
        Optional[ListNode]: The head of the modified linked list.
                           Returns None if the input list is empty.
    
    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5, left=2, right=4
        >>> # Returns: 1 -> 4 -> 3 -> 2 -> 5
        
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5, left=1, right=3
        >>> # Returns: 3 -> 2 -> 1 -> 4 -> 5
    
    Time Complexity: O(n) where n is the number of nodes in the list
    Space Complexity: O(1) - only uses a dummy head and few pointer variables
    """

    dummmy_head = ListNode(-1, head)

    left_node, curr_node = dummmy_head, head
    pos = 1
    prev = None
    while curr_node:
        if pos < left:
            left_node, curr_node = curr_node, curr_node.next

        elif pos >= left and pos <= right:
            next_ptr = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_ptr

        else:
            break
        pos += 1

    left_node.next.next = curr_node
    left_node.next = prev
        

    curr = dummmy_head.next
    while curr:
        print(curr.val)
        curr = curr.next

    return dummmy_head.next



def main():
    """
    Demonstrate the reverseLinkedList2_v2 function with a sample linked list.
    
    Creates a linked list with values [1, 2, 3, 4, 5] and reverses nodes
    between positions 1 and 3 (inclusive). The function should return a list
    with values [3, 2, 1, 4, 5].
    
    The function prints the values of the modified list to demonstrate the algorithm.
    """

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    # Reverse nodes between positions 1 and 3
    reverse = reverseLinkedList2_v2(head, 1, 3)

if __name__ == "__main__":
    main()