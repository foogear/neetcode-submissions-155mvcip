class UnionFind:
    
    def __init__(self, n: int):
        # UnionFind(10) -> 0~10
        self.par = {}
        self.hei = {}
        self.numComponents = n
        for i in range(n):
            self.par[i] = i
            self.hei[i] = 0

    def findRoot(self, x: int) -> int:
        curr = x
        p = self.par[curr]
        while p != curr:
            curr = p
            p = self.par[curr]
            self.par[x], self.hei[x] = p, self.hei[x] - 1
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        px = self.findRoot(x)
        py = self.findRoot(y)
        if px == py:
            return True
        return False

    def union(self, x: int, y: int) -> bool:
        px = self.findRoot(x)
        py = self.findRoot(y)
        if px == py:
            return False

        self.numComponents -= 1

        if self.hei[px] < self.hei[py]:
            px, py = py, px
        self.par[py] = px

        if self.hei[px] == self.hei[py]:
            self.hei[px] += 1

        return True
        
    def getNumComponents(self) -> int:
        return self.numComponents


