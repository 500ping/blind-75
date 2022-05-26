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
            tree.left = self.list_to_tree_node(arr, 2 * index + 1) # [1, 3, 7, 15, ...]
            tree.right = self.list_to_tree_node(arr, 2 * index + 2) # [2, 5, 12, 25, ...]
        return tree 


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    '''
    Algorithm:

    Three possible cases:

    Case_#1:
    Both p and q are smaller than current node, then search left-subtree by recursive

    Case_#2:
    Both p and q are larger than current node, then search right-subtree by recursive

    Case_#3:
    Both p and q are not on the same side of current node, then current node must be the Lowest common ancestor of ( p, q )
    '''
    cur_value = root.val
        
    if p.val > cur_value and q.val > cur_value:
        return lowestCommonAncestor( root.right, p, q)
    
    elif p.val < cur_value and q.val < cur_value:
        return lowestCommonAncestor( root.left, p, q)
    
    else:
        return root



root = TreeNode().list_to_tree_node([2,1])
p = TreeNode(2)
q = TreeNode(1)
print(lowestCommonAncestor(root, p, q))

