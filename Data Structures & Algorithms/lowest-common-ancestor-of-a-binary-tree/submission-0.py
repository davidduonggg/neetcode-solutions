# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the lowest common ancestor of two given nodes in the tree

        # return the node itself
        # a node can be a descendant of itself
        # p and q are guaranteed to exist, all node values are unique
        
        # my initial thought is just to perform a dfs in the tree, and basically return true if 
        # we find the node. the first instance where its both True we can store the node and we return that.

        # case 1: if we find p or q, the LCA is guaranteed to be above it
        # case 2: p and q are in different subtrees, we return left == right
        # case 3: if p and q are in the same subtree, the first instance of p or q is the LCA

        def dfs(node):
            if not node: return None

            if node == p or node == q: # a node can be a descendant of itself
                return node

            left, right = dfs(node.left), dfs(node.right)

            if left and not right: return left
            if right and not left: return right
            if left and right: return node


        return dfs(root)