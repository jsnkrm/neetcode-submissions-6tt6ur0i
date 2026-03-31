class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        offset = 0
        res = []
        while offset < len(nums) - k + 1:
            res.append(max(nums[offset:(offset + k)]))
            offset += 1
        return res

        