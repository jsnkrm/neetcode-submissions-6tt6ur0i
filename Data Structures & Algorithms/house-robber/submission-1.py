class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        n = len(nums)    
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        dp[n - 2] = max(nums[n - 1], nums[n - 2])

        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]