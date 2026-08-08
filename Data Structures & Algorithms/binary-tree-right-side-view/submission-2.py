# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return only the values of nodes that are visible from right side of the tree
        # 0 <= nodes <= 100
        
        if not root: return []

        res = []
        q = deque([root])

        while q:
            last = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                last = node

            res.append(last.val)

        return res