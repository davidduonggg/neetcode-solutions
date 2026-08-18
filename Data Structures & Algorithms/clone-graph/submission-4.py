"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        if not node: return None

        def dfs(node):
            if node in mapping:
                return mapping[node]

            mapping[node] = Node(node.val)

            for nbr in node.neighbors:
                mapping[node].neighbors.append(dfs(nbr))

            return mapping[node]

        return dfs(node)