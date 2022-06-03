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


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    temp = {}
    counter = 1

    while head:
        temp[counter] = head
        counter += 1
        head = head.next

    index = ((counter - 1) // 2) + 1
    return temp.get(index)


head = ListNode().list_to_LL([1,2,3,4,5,6])
print(middleNode(head))