# Definition for singly-linked list.
from typing import Optional


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


def hasCycle(head: Optional[ListNode]) -> bool:
    # Floyd's Tortoise and Hare 
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if fast == slow: return True
    return False


head = ListNode(3)
dummy = ListNode().list_to_LL([2,0,-4])
head.next = dummy
dummy.next=dummy
print(hasCycle(head))