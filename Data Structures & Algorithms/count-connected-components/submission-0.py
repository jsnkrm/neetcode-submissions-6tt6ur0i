class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i : [] for i in range(n)}
        count = 0
        visited = set()

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for j in adj[i]:
                dfs(j)

        while len(visited) != n:
            for i in range(n):
                if i not in visited:
                    dfs(i) 
                    count += 1
        return count