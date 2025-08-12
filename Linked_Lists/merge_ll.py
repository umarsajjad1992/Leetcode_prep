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
    dummy_node = ListNode()
    curr1 = head1
    curr2 = head2
    curr = dummy_node
    

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            print("list 1")
            print(f"list 1: curr1: {curr1.val}")
            print(f"list 1: curr2: {curr2.val}")
            curr.next = curr1
            curr1 = curr1.next
            curr = curr1
        elif curr1.val > curr2.val:
            print("list 2")
            print(f"list 2: curr1: {curr1.val}")
            print(f"list 2: curr2: {curr2.val}")
            curr.next = curr2
            curr2 = curr2.next
            curr = curr2
    if curr1 or curr2:
        curr.next = curr1 if curr1 else curr2
    
    curr = dummy_node.next
    while curr:
        print(curr.val)
        curr = curr.next




def main():
    """
    Demonstrate the reverseLinkedList function with a sample linked list.
    
    Creates a linked list with values [3, 2, -1, 4, 5] and reverses it.
    The function should return a list with values [5, 4, -1, 2, 3].
    
    The function prints the values of the reversed list to demonstrate the algorithm.
    """
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)

    head1 = ListNode(0)
    head1.next = ListNode(6)
    head1.next.next = ListNode(7)
    head1.next.next.next = ListNode(8)
    head1.next.next.next.next = ListNode(9)
    
    # Reverse the linked list
    merge_sorted_list(head1, head2)

if __name__ == "__main__":
    main()