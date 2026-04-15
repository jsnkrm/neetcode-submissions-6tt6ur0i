class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numset:
                curr = 1
                while curr + n in numset:
                    curr += 1
                longest = max(longest, curr)
        return longest