class UnionFind:
    def __init__(self, n) -> None:
        self.fa = [i for i in range(n)]
        
    def find(self, x) -> int:
        while self.fa[x] != x:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x
    
    def union(self, x, y) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.fa[root_x] = root_y
        return True
    
    def is_connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        union_find = UnionFind(size)
        for i in range(size):
            for j in range(i+1, size):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        ans = set()
        for i in range(size):
            ans.add(union_find.find(i))
        return len(ans)