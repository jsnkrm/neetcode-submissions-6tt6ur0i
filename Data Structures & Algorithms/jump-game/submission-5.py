class Solution:
    def canJump(self, nums: List[int]) -> bool:
        least = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= least:
                least = i
        return least == 0