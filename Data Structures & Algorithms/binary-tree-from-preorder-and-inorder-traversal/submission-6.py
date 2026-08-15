# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # given the preorder and inorder traversal
        # rebuild the binarry tree from the preorder and inorder traversals

        # preorder is root first, then left subtree, then right subtree
        # inorder is left subtree, root, right subtree

        # problem: how do we build the binary tree

        # invariant: root will always be first in preorder
        # and the left and right subtrees will always be partitioned by that root

        # we can recursively keep finding and building the root, and split 

        # we can also use a hashmap, to map the values to its index
        # that way we can find the index in O(1) time

        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx

        self.preIdx = 0
        def dfs(l, r):
            if l > r: return None

            root_val = preorder[self.preIdx]
            self.preIdx += 1

            root = TreeNode(root_val)
            split = hashmap[root_val]
            
            root.left = dfs(l, split - 1)
            root.right = dfs(split + 1, r)
        
            return root


        return dfs(0, len(preorder) - 1)