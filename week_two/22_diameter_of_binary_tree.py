from turtle import right
from typing import Optional


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


if __name__ == "__main__":
    root = TreeNode().list_to_tree_node([1, 2, 3, 4, 5])
    print(diameterOfBinaryTree(root))
