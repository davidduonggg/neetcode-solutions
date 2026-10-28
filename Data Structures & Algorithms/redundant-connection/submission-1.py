class UnionFind:
    def __init__(self, n):
        self.rank = [1] * (n)
        self.par = [i for i in range(n)]

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])

        return self.par[x]

    def union(self, x, y):
        u, v = self.find(x), self.find(y)

        if u == v: return False # same tree

        if self.rank[u] < self.rank[v]:
            self.par[u] = v
            self.rank[v] += 1
        else:
            self.par[v] = u
            self.rank[u] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # undirected graph
        # extra edge, and we return the edge that can be removed so that the resulting graph is a tree of n nodes
        # len edges = n + 1

        uf = UnionFind(len(edges) + 1)

        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]