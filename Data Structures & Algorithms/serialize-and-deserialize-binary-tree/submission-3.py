# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # i think bfs would be a generally straightforward way to serialize a tree
    # to serialize the string, we just do a bfs and then encode, have X be none
    # how can we construct the tree with bfs?
    # we could read it like a heap too, 2n + 1 and 2n + 2
    # that doesn't sound like a bad idea actually


    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""

        res = []

        def dfs(node):
            if not node:
                res.append("")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(res)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None

        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if i >= len(data) or data[i] == '': 
                i += 1
                return None

            root_val = int(data[i])
            root = TreeNode(root_val)
            i += 1
            root.left = dfs()
            root.right = dfs()

            return root


        return dfs()

            