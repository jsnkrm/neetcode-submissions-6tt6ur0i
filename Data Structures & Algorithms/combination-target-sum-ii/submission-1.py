class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i > len(candidates) - 1 or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            skipped = candidates[i]
            while i < len(candidates) and candidates[i] == skipped:
                i +=1
            dfs(i, curr, total)
        
        dfs(0, [], 0)
        return res
     
