# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for every node n:
        # case 1: it is a root, like node 2
        # case 2: it's in the path

        # for every node n, we compute the maximum between
        # being a root, or being in the path

        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node: return 0

            l, r = dfs(node.left), dfs(node.right)
            
            diameter = max(diameter, l + r)

            return 1 + max(l, r)

        dfs(root)
        return diameter 