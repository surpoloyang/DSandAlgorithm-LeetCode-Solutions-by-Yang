class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        self.n = len(grid)
        self.m = len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    self.count += 1
        return self.count
