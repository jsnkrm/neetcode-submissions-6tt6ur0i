class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = {}

        def dfs(i, l, r):
            if i == N:
                if l == r:
                    dp[(l,r)] = True
                else: 
                    dp[(l,r)] = False
                return dp[(l,r)]
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = (dfs(i + 1, l + nums[i], r) 
                    or dfs(i + 1, l, r + nums[i]))
            
            return dp[(l,r)]
        
        ans = dfs(0, 0, 0)
        print(dp)
        return ans
