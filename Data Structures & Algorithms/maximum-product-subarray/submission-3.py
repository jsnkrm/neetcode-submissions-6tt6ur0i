class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal = [float("inf")] * len(nums)
        maxVal = [-float("inf")] * len(nums)

        minVal[0] = maxVal[0] = nums[0]
        for i in range(1, len(nums)):
            minVal[i] = min(nums[i], minVal[i - 1] * nums[i], maxVal[i - 1] * nums[i])
            maxVal[i] = max(nums[i], minVal[i - 1] * nums[i], maxVal[i - 1] * nums[i])
        return max(maxVal)