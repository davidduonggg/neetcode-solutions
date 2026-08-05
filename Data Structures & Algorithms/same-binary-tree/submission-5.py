# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        # check if the trees have same structure and nodes
        # we have to check every node, the best we can do is O(n) time
        # an easy way is to just traverse one first, then write, then traverse second
        # i think we can do both at the same time


        def traverse(p, q):
            if not q and not p: return True

            if (not q and p) or (q and not p) or (q.val != p.val):
                return False

            if not traverse(p.left, q.left) or not traverse(p.right, q.right): return False

            return True

        return traverse(a, b)