class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        curr = 1

        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                curr = 1
            increasing = max(increasing, curr)
        
        curr = 1

        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                curr += 1
            else:
                curr = 1
            decreasing = max(decreasing, curr)
        
        return max(increasing, decreasing)