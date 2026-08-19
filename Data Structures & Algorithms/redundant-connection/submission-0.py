class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}
        self.size = {i: 1 for i in range(1, n + 1)}

    def find(self, x):
        # path compression
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x

    def union(self, x, y):
        u, v = self.find(x), self.find(y)
        if u == v:
            return True

        # union sets
        if self.size[u] > self.size[v]:
            self.par[v] = u
            self.size[u] += self.size[v]
        else:
            self.par[u] = v
            self.size[v] += self.size[u]

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # connected == orphans
        # undirected 
        # nodes : 1 - n
        # edge added not a self loop edge, not a duplicate
        # return the last edge that makes the graph cyclic
        # ordering 

        # constraints
        # at least 3 nodes
        # at least one edge

        uf = UnionFind(len(edges))

        for a, b in edges:
            if uf.union(a, b):
                return [a, b]