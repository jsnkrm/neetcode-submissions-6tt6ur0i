class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        dp = [[0 for i in range(N1 + 1)] for i in range(N2 + 1)]

        for r in range(N2 - 1, -1, -1):
            for c in range(N1 - 1, -1, -1):
                if text2[r] == text1[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]