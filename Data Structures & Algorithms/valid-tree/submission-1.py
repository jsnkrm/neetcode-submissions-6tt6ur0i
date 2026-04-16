class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            res = True
            for nxt in adj[curr]:
                if nxt != prev:
                    res = res & dfs(nxt, curr)
                    if not res:
                        break
            return res
        
        return len(visited) == n if dfs(0, -1) else False
