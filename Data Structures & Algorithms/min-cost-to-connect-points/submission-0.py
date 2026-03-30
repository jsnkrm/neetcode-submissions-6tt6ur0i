class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = { i : [] for i in range(N) }

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])

        res = 0
        minHeap = [[0, 0]]
        visited = set()
        while len(visited) < N:
            c, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i) 
            res += c   
            for cost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [cost, nei])
        return res