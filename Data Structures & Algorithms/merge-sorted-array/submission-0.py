class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if num1[m - 1] > num2[n - 1]:
                num1[last] = num1[m - 1]
                m = m - 1
            else:
                num1[last] = num2[n - 1]
                n = n - 1
            last -= 1
        
        while n > 0:
            num1[last] = num2[n - 1]
            last -= 1
            n-= 1

