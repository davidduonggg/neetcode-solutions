class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x

    def union(self, x, y):
        u, v = self.find(x), self.find(y)

        if u == v:
            return True

        if self.size[u] >= self.size[v]:
            self.par[v] = u
            self.size[u] += self.size[v]
        else:
            self.par[u] = v
            self.size[v] += self.size[u]

        self.components -= 1
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        numEdges = 0
        res = 0
        uf = UnionFind(n)
        edges.sort(key=lambda x: x[2])

        i = 0
        while i < len(edges) and numEdges < n - 1:
            src, dst, wt = edges[i]

            if uf.union(src, dst):
                i += 1
                continue

            res += wt
            i += 1
            numEdges += 1

        return res if uf.components == 1 else -1

            
