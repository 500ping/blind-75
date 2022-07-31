from functools import lru_cache
import heapq
from typing import List, Optional


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


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    all_vals = []
    # res = ListNode()

    for list_node in lists:
        while list_node:
            heapq.heappush(all_vals, list_node.val)
            list_node = list_node.next
    
    def helper(arr):
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            return ListNode(heapq.heappop(arr))
        return ListNode(heapq.heappop(arr), next=helper(arr))

    return helper(all_vals)


ll_1 = ListNode().list_to_LL([1,4,5])
ll_2 = ListNode().list_to_LL([1,3,4])
ll_3 = ListNode().list_to_LL([2,6])
data = [ll_1, ll_2, ll_3]
print(print(mergeKLists(data)))