class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        res= []
        for i in range(len(nums)):
            if target - nums[i] in s:
                if i < s.get(target - nums[i]):
                    res = [ i,s.get(target - nums[i])]
                else:
                    res = [s.get(target - nums[i]),i]
            s[nums[i]] = i

        return res