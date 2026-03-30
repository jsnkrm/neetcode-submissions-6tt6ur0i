class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = [0]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def makeRotten(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r,c) in visited):
                return
            
            if(grid[r][c] == 0):
                return
            
            visited.add((r,c))
            grid[r][c] = 2
            fresh[0] -= 1
            q.append([r, c])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                if grid[r][c] == 1:
                    fresh[0] += 1
        
        time = 0
        while q and fresh[0]:
            for i in range(len(q)):
                r, c = q.popleft()
                makeRotten(r + 1, c)
                makeRotten(r - 1, c)
                makeRotten(r, c + 1)
                makeRotten(r, c - 1)
            time += 1
        
        return time if fresh[0] == 0 else -1                  
        