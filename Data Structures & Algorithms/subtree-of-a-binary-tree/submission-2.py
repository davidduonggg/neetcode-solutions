# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self, n1, n2):
        if not n1 and not n2:
            return True

        if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
            return False

        return self.check(n1.left, n2.left) and self.check(n1.right, n2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # a tree is also a subroot of itself

        # traverse root until we find the root same value as subroot
        # and then there we do a dfs and if they're the same return True
        if not root: return False

        res = False

        if root.val == subRoot.val: res = self.check(root, subRoot)

        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)