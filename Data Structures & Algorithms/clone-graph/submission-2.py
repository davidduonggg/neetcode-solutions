"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given a node in a node, return a deep copy of the graph

        # node values are 1 - n
        # the input node will always be the first node

        # the problem is: how can we create a deep copy successfully without duplicating any nodes
        
        # my first thought is just to dfs from the starting node, we will visit every node once and it models the connected structure of a graph well
        # and we can use a hashmap to fetch and store our ndoes, so we don't recreate any nodes twice

        nodes = {}

        def dfs(root):
            if not root:
                return None

            if root.val in nodes:
                return nodes[root.val]

            if root.val not in nodes:
                nodes[root.val] = Node(root.val)

            for nbr in root.neighbors:
                clonedNbr = dfs(nbr)
                if clonedNbr:
                    nodes[root.val].neighbors.append(clonedNbr)


            return nodes[root.val]

        return dfs(node)