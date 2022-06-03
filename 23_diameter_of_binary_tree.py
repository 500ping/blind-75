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


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = [0]

    def dfs(root):
        if not root:
            return -1
            
        left, right = dfs(root.left), dfs(root.right)

        res[0] = max(res[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return res[0]

root = TreeNode().list_to_tree_node([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
print(diameterOfBinaryTree(root))