# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # all node vals are unique
        # lowest node in a tree that has both p and q as descendants
        # ancestor is a descendant of itself

        # p != q, p and q will exist

        # brute force: for every node n, we check if p and q are descendants
        # and then we check. thats O(n^2)
        # we want a solution that is O(n), we check every node once

        # my initial thoughts are just to dfs, and if we find the node
        # then return True, and then at the first instance of both returning true we set val to true?

        # all values are unique, we don't have to worry about repeating p and q

        # we also exploit that its a BST

        def dfs(node):
            if not node: return None

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node


        return dfs(root)





