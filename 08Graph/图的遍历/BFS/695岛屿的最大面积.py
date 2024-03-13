import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue.append((i, j))
                    tem_area = 1
                    while queue:
                        i, j = queue.popleft()
                        for dir in directs:
                            _i = i + dir[0]
                            _j = j + dir[1]
                            if _i >= 0 and _i < m and _j >= 0 and _j < n and grid[_i][_j] == 1:
                                tem_area += 1
                                grid[_i][_j] = 0
                                queue.append((_i, _j))
                    ans = max(ans, tem_area)
        return ans
                        
