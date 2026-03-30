class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dir = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        visited = set()
        minH = [[grid[0][0], 0, 0]]
        visited.add((0, 0))
        while len(minH) > 0:
            h, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return h

            for dx, dy in dir:
                row, col = r + dx, c + dy
                if(row < 0 or col < 0 or row == N or col == N
                    or (row, col) in visited):
                    continue
                visited.add((row, col))
                heapq.heappush(minH, [max(h, grid[row][col]), row, col])
