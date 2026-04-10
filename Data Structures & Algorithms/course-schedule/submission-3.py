class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for f, t in prerequisites:
            adj[f].append(t)
        visited = set()

        def dfs(crs):
            if adj[crs] == []:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            adj[crs] = []
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
        