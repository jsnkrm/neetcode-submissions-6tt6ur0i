class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
      

        def dfs(t, i):

            if t == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            
            res = dfs(t + nums[i], i + 1) + dfs(t - nums[i], i + 1)
            return res

        return dfs(0, 0)