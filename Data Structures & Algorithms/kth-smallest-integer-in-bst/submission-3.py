# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # given the root of a binary search tree
        # return the kth smallest value in the tree
        
        # in a BST: in order traversal
        # we can use dfs, and pass the k in
        # or we can just add it to an array too, it doesnt matter
        i = 0

        def dfs(node):
            nonlocal i

            if not node: return -1

            left = dfs(node.left)
            if left != -1: return left

            i = i + 1
            if i == k:
                return node.val

            right = dfs(node.right)
            if right != -1: return right

            return -1


        return dfs(root)





            