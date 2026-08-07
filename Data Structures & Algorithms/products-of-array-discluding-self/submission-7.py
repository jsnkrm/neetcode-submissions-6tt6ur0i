class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        hasZeroes = 0

        for n in nums:
            if n == 0:
                hasZeroes += 1
                continue
            prod *= n
        
        if hasZeroes > 1:
            return [0]*(len(nums))

        res = []
        
        if hasZeroes:
            for n in nums:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for n in nums:
                res.append(prod // n)
        return res
                
