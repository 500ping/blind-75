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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                res.append('#')

        helper(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split())
        return helper()


root = TreeNode().list_to_tree_node([1,2,3,None,None,4,5])
# print(root)
codec = Codec()
print(codec.serialize(root))
print(codec.deserialize(codec.serialize(root)))