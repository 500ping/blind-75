from copy import deepcopy


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


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr_value = root.val
    if p.val < curr_value and q.val < curr_value:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > curr_value and q.val > curr_value:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


if __name__ == "__main__":
    root = TreeNode().list_to_tree_node(
        [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = deepcopy(root.left)
    q = deepcopy(root.left.right)
    print(lowestCommonAncestor(root, p, q))
