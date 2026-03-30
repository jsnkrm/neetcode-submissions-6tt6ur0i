class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            area = 0
            q = deque()
            q.append((r,c))

            while q:
                (r, c) = q.popleft()

                if (r < 0 or r >= ROWS or 
                    c < 0 or c >= COLS or
                    grid[r][c] == 0):
                    continue
                
                grid[r][c] = 0
                area += 1
                q.append((r, c + 1))
                q.append((r, c - 1))
                q.append((r - 1, c))
                q.append((r + 1, c))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res

