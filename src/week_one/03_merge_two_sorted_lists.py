from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    @classmethod
    def list_to_LL(cls, arr):
        if len(arr) < 1:
            return None

        if len(arr) == 1:
            return ListNode(arr[0])

        return ListNode(arr[0], next=cls.list_to_LL(arr[1:]))


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return dummy.next


if __name__ == "__main__":
    list1 = ListNode().list_to_LL([1, 2, 4])
    list2 = ListNode().list_to_LL([1, 3, 4])
    print(mergeTwoLists(list1, list2))
