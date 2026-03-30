class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf') 

        while l <= r:
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            
            if nums[l] >= nums[r]:
                l += 1
            else:
                r = mid - 1
        
        return res