from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    def list_to_LL(self, arr):
        if len(arr) < 1:
            return None

        if len(arr) == 1:
            return ListNode(arr[0])

        return ListNode(arr[0], next=self.list_to_LL(arr[1:]))


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None             # ListNone always end with None
    while head:
        next = head.next    # Store next node
        head.next = prev    # set pointer of current node to prev instead of next node
        prev = head         # Move one step forward of prev
        head = next         # Move one step forward of head
    return prev


head = ListNode().list_to_LL([1,2,3,4,5])
print(reverseList(head))