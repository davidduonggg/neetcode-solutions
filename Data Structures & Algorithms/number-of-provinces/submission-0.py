class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.provinces = n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x


    def union(self, x, y):
        u, v = self.find(x), self.find(y)

        if u == v: return

        # union
        if self.size[u] > self.size[v]:
            self.par[v] = u
        else:
            self.par[u] = v

        self.provinces -= 1

        return


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # there are n cities
        # if a -> b, b -> c, then a -> c
        # a province is a group of directly or indirectly connected cities and no other cities

        # n x n matrix, isConnected[i][j] = 1  if the ith and jth city are connected, and 0 otherwise
        # return the total number of provinces

        # let's think about the core problem
        # the core difficulty is the indirect connections, if a is connected to b and b is connected to c, then a is connected to c
        # the disjoint set data structure fits this problem well because it basically models this: what nodes are connected to each other, 
        # and grouped by set

        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.provinces