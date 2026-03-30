class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        N = len(s)
        res = s[0]
        for l in range(N):
            for r in range(l+1, N):
                if isPali(s[l:r+1]):
                    res = s[l:r+1] if r - l + 1 > len(res) else res
        
        return res
        