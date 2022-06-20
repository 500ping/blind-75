from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
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


def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(node, left, right):
        if not node:
            return True

        if not (node.val < right and node.val > left):
            return False

        return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
    return valid(root, float('-inf'), float('inf'))


root = TreeNode().list_to_tree_node([5,4,6,None,None,3,7])
print(isValidBST(root))