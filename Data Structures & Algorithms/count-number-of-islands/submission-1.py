class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def sink(i, j):
            if (i < 0 or i >= r or j < 0 or j >= c):
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for x, y in dirs:
                sink(x + i, y + j)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    res += 1
                    sink(i, j)
        return res