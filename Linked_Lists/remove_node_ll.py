from typing import Optional

class ListNode:
    def __init__(self, val=0, tail=None, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: Optional[ListNode], val) -> Optional[ListNode]:
    curr = head

    dummy_head = ListNode(-1)
    dummy_head.next = head

    curr = dummy_head
    while curr and curr.next:

        if curr.next.val == val: 
            curr.next = curr.next.next

        curr = curr.next

    curr = dummy_head.next
    while curr:
        print(curr.val)
        curr = curr.next
        

def main():


    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(6)
    # Test for cycle detection
    deleteNodes(head, 6)

if __name__ == "__main__":
    main()