# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # given the root of a non-empty binary tree
        # return the maximum path sum

        # a path is a sequence of nodes where each pair of adjacent nodes has an edge connecting them
        # from looking at example two, there can also be negative numbers
        # there can also be negative numbers as well
        # we can't do a naive stop at negative number as well, because after -5 there could be +50 for example

        # brute force: at every node, we can compute the maximum path containing that node
        # thats O(n^2), we should aim for an O(n) solution
        # we should use dfs, and propagate up the sums
        # a node cannot appear in the sequence more than once

        # at every given node, a path is some combination of a traversal of the left and right subtrees
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right)

            res = node.val
            if left > 0:
                res += left
            if right > 0:
                res += right

            maxSum = max(maxSum, res)

            return node.val + max(left, right, 0)
            
        dfs(root)

        return maxSum