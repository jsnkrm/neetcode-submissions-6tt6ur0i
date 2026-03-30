class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        
        def markVisited(r, c):
            if (r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or board[r][c] == "X"
                or (r, c) in visited):
                return
            
            visited.add((r,c))
            for x, y in directions:
                markVisited(r + x, c + y)

        def dfs(r, c):
            if (r <= 0 or r >= ROWS - 1
                or c <= 0 or c >= COLS - 1
                or board[r][c] == "X"
                or (r, c) in visited):
                 return
            
            board[r][c] = "X"
            for x, y in directions:
                dfs(r + x, c + y)
        
        for c in range(0, COLS):
            if board[0][c] == "O":
                markVisited(0, c)
            if board[ROWS - 1][c] == "O":
                markVisited(ROWS - 1, c)
        
        for r in range(0, ROWS):
            if board[r][0] == "O":
                markVisited(r, 0)
            if board[r][COLS - 1] == "O":
                markVisited(r, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r, c)

        