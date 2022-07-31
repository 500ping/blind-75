from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", left={" + str(self.left) + "}, right={" + str(self.right) + "})"

    def list_to_tree_node(self, arr, index=0):
        tree = None
        if index < len(arr):
            if arr[index] == None:
                return
            tree = TreeNode(arr[index])
            tree.left = self.list_to_tree_node(
                arr, 2 * index + 1)  # [1, 3, 7, 15, ...]
            tree.right = self.list_to_tree_node(
                arr, 2 * index + 2)  # [2, 5, 12, 25, ...]
        return tree


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    n = 0
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1
        if n == k: return curr.val

        curr = curr.right



root = TreeNode().list_to_tree_node([5,3,6,2,4,None,None,1])
k = 3
print(kthSmallest(root, k))