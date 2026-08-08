# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node x is good if 
        # path from the root of the tree to node x contains no nodes with a value greater than x
        # return the number of good nodes within the tree

        # constraints
        # 1 <= n <= 100,000
        # values don't matter
        # if n can get so large, we definitely want a solution in O(n) time, anything above that would most likely hit a TLE

        # contains no nodes with a value greater than X
        # we can figure this out by taking a running max, and if the node x is smaller or equal to that max its valid

        def dfs(node, maximum):
            if not node: 
                return 0

            res = 0

            if node.val >= maximum:
                res += 1
                maximum = node.val

            res += dfs(node.left, maximum)
            res += dfs(node.right, maximum)

            return res


        return dfs(root, root.val)