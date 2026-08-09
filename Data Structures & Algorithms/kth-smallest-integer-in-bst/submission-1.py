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

        def dfs(node, arr):
            if not node: return

            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)

        res = []
        dfs(root, res)
        return res[k - 1]





            