class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def visit(node):
            visited.add(node)
            for nxt in adj[node]:
                if nxt not in visited:
                    visit(nxt)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visit(i)
        return res