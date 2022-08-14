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
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    head = ListNode().list_to_LL([2, 0, -4])
    head.next.next.next = head
    print(hasCycle(head))
