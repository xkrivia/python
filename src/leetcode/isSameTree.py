# CHRIS FELLI, 2019
# Given a Binary Tree, are they the same?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Helper function
        def traverse(node: TreeNode, result):
            # If a node exists, recurse through children.
            if node:
                result.append(node.val)
                traverse(node.left, result)
                traverse(node.right, result)
            else:
                result.append(0)
            return result
        # Return True if tree traversal is equivalent.
        return traverse(p, []) == traverse(q, [])