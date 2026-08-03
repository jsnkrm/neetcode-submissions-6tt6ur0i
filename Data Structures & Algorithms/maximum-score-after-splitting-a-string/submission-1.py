class Solution:
    def maxScore(self, s: str) -> int:
        maxOnes = [0 for i in range(len(s))]
        maxZeroes = [0 for i in range(len(s))]

        maxZeroes[0] = 1 if s[0] == "0" else 0
        maxOnes[len(s) - 1] = 1 if s[-1] == "1" else 0

        for i in range(1, len(s)):
            if s[i] == "0":
                maxZeroes[i] = 1 + maxZeroes[i - 1]
            else:
                maxZeroes[i] = maxZeroes[i - 1]

        for i in range(len(s) - 2, -1, -1):
            if s[i] == "1":
                maxOnes[i] = 1 + maxOnes[i + 1]
            else:
                maxOnes[i] = maxOnes[i + 1]
        

        res = 0

        for i in range(len(s) - 1):
            res = max(res, maxZeroes[i] + maxOnes[i+1])
        
        return res