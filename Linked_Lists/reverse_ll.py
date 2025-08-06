from typing import Optional

class ListNode:
    def __init__(self, val=0, tail=None, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
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


    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(-1)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    # Test for cycle detection
    reverse = reverseLinkedList(head)

if __name__ == "__main__":
    main()

