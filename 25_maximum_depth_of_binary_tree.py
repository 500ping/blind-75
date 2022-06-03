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


def maxDepth(root: Optional[TreeNode]) -> int:

    def dfs(root):
        if not root:
            return 0
            
        left, right = dfs(root.left), dfs(root.right)

        return 1 + max(left, right)

    return dfs(root) 


root = TreeNode().list_to_tree_node([3,9,20,None,None,15,7])
print(maxDepth(root))