class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(2*n)]

        for i in range(2*n):
            index = i if i < n else i - n
            ans[i] = nums[index]
        return ans
