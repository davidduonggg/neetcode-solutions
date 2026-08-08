# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return true if it is a valid binary search tree, false if it isnt

        # LESS THAN OR GREATER THAN
        # both left and right subtrees are also binary search trees

        # guaranteed to have at least one node
        # values don't have to be unique, we can pass in a valid range

        def dfs(node, lower, upper):
            if not node: return True

            if node.val <= lower or node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, float('-inf'), float('inf'))