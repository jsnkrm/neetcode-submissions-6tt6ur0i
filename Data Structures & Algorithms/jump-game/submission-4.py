class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastTrueIdx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if lastTrueIdx <= i + nums[i]:
                lastTrueIdx = i
        return lastTrueIdx == 0