from collections import deque
from typing import List, Optional


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


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    q = deque([root])

    while q:
        right_side = None
        q_len = len(q)

        for _ in range(q_len):
            node = q.popleft()
            if node:
                right_side = node
                q.append(node.left)
                q.append(node.right)
        
        if right_side:
            res.append(right_side.val)

    return res


root = TreeNode().list_to_tree_node([1,2,3,4])
print(rightSideView(root))