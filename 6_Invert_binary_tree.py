# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", left={" + str(self.left) + "}, right={" + str(self.right) + "})"

    def list_to_tree_node(self, arr, index):
        tree = None
        if index < len(arr):
            if arr[index] == None:
                return
            tree = TreeNode(arr[index])
            tree.left = self.list_to_tree_node(arr, 2 * index + 1) # [1, 3, 7, 15, ...]
            tree.right = self.list_to_tree_node(arr, 2 * index + 2) # [2, 5, 12, 25, ...]
        return tree 


def invertTree(root):
    # res = TreeNode()
    def inverse(root):
        if root:
            if root.left or root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
                inverse(root.left)
                inverse(root.right)
        else:
            return
    inverse(root)
    return root


root = TreeNode().list_to_tree_node([], 0)
print(invertTree(root))