class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        if nums[len(nums) - 2] > 0:
            dp[len(nums) - 2] = 1
        dp[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                if(j <= i + nums[i]):
                    dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]
        