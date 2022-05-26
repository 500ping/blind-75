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


def mergeTwoLists(list1, list2):
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

list1 = ListNode().list_to_LL([1,2,4]) 
list2 = ListNode().list_to_LL([1,3,4]) 
print(mergeTwoLists(list1, list2))
