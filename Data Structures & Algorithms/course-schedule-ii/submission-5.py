class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = { i : [] for i in range(numCourses) }
        visited = set()
        added = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                if crs not in added:
                    added.add(crs)
                    res.append(crs)
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            added.add(crs)
            res.append(crs)
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res