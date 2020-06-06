# CHRIS FELLI, 2019
# Given a Binary Tree, is it a Binary Search Tree?


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self, root):
        self.root = root

    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, None, None)
