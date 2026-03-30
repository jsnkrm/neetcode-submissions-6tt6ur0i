class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visitedP = set()
        visitedA = set()
        pQ = deque()
        aQ = deque()

        def checkP(row, col, currHeight):
            if(row >= 0 and col >=0 
                and row < ROWS and col <COLS
                and (row, col) not in visitedP
                and currHeight <= heights[row][col]):
                    pacific.add((row,col))
                    visitedP.add((row,col))
                    pQ.append([row, col])

        def checkA(row, col, currHeight):
            if(row >= 0 and col >=0 
                and row < ROWS and col <COLS
                and (row, col) not in visitedA
                and currHeight <= heights[row][col]):
                    atlantic.add((row,col))
                    visitedA.add((row,col))
                    aQ.append([row, col])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                    pQ.append([r, c])
                    visitedP.add((r,c))
                if r == ROWS -1 or c == COLS - 1:
                    atlantic.add((r,c))
                    aQ.append([r, c])
                    visitedA.add((r,c))

        
        while pQ:
            for i in range(len(pQ)):
                r, c = pQ.popleft()
                currHeight = heights[r][c]
                for x, y in directions:
                    row, col = r + x, c + y
                    checkP(row, col, currHeight)
        while aQ:
            for i in range(len(aQ)):
                r, c = aQ.popleft()
                currHeight = heights[r][c]
                for x, y in directions:
                    row, col = r + x, c + y
                    checkA(row, col, currHeight)
        res = []
        for cell in pacific:
            if cell in atlantic:
                res.append(cell)
        
        return res
