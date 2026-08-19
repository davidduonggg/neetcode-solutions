class UnionFind:
    def __init__(self, n: int):
        # every node is its own parent at first
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
        

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        u, v = self.find(x), self.find(y)
        if u == v: return False

        self.par[v] = u
        self.components -= 1

        return True



    def getNumComponents(self) -> int:
        return self.components
