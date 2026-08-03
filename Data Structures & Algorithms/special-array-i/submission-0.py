class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        i, j = 0, 1

        while j < len(nums):
            if (nums[i] + nums[j]) % 2 == 0: 
                return False
            i += 1
            j += 1
        return True