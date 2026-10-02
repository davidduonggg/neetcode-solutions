# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can just do an inorder traversal for the binary search tree
        # an easy way to do this is with recursion
        i = 0
        res = 0

        def inorder(node):
            nonlocal i
            nonlocal res
            if not node: return

            inorder(node.left)
            i += 1
            if i == k:
                res = node.val
            inorder(node.right)

        inorder(root)
        return res

        
            
