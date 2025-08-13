"""
Linked List Merge Sorted Lists

This module implements a solution to merge two sorted singly linked lists
into one sorted linked list using a dummy head approach.

The algorithm compares values from both lists and builds a new sorted list
by selecting the smaller value at each step.

Example:
    For lists [0,6,7,8,9] and [1,2,3,4,5] -> returns [0,1,2,3,4,5,6,7,8,9]
    For lists [1,3,5] and [2,4,6] -> returns [1,2,3,4,5,6]

Time Complexity: O(m + n) where m and n are the lengths of the two lists
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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_list(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted linked list.
    
    This function merges two sorted linked lists by comparing values from both lists
    and building a new sorted list using a dummy head approach. The algorithm
    selects the smaller value at each step and advances the corresponding pointer.
    
    Args:
        head1 (Optional[ListNode]): The head of the first sorted linked list.
                                   Can be None for an empty list.
        head2 (Optional[ListNode]): The head of the second sorted linked list.
                                   Can be None for an empty list.
    
    Returns:
        Optional[ListNode]: The head of the merged sorted linked list.
                           Returns None if both input lists are empty.
    
    Examples:
        >>> # List1: 0 -> 6 -> 7 -> 8 -> 9
        >>> # List2: 1 -> 2 -> 3 -> 4 -> 5
        >>> # Returns: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
        
        >>> # List1: 1 -> 3 -> 5
        >>> # List2: 2 -> 4 -> 6
        >>> # Returns: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    
    Time Complexity: O(m + n) where m and n are the lengths of the input lists
    Space Complexity: O(1) - only uses a dummy head and few pointer variables
    """
    dummy_node = ListNode()
    curr1 = head1
    curr2 = head2
    curr = dummy_node
    

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr, curr1 = curr1, curr1.next
        else:
            curr.next = curr2
            curr, curr2 = curr2, curr2.next
    if curr1 or curr2:
        curr.next = curr1 if curr1 else curr2
    
    curr = dummy_node.next
    while curr:
        print(curr.val)
        curr = curr.next

    return dummy_node.next




def main():
    """
    Demonstrate the merge_sorted_list function with two sample linked lists.
    
    Creates two sorted linked lists:
    - List1: [0, 6, 7, 8, 9]
    - List2: [1, 2, 3, 4, 5]
    
    Merges them into a single sorted list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    The function prints the values of the merged list to demonstrate the algorithm.
    """
    head1 = ListNode(0)
    head1.next = ListNode(6)
    head1.next.next = ListNode(7)
    head1.next.next.next = ListNode(8)
    head1.next.next.next.next = ListNode(9)
    
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    
    # Merge the two sorted linked lists
    head = merge_sorted_list(head1, head2)

if __name__ == "__main__":
    main()