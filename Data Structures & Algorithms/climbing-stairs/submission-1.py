class Solution:
    def climbStairs(self, n: int) -> int:
        step = [0] * (n + 1)
        step[0] = 1
        step[1] = 1

        def climb(n):
            if n <= 1:
                return step[n]
            if not step[n-1]:
                step[n-1] = climb(n-1)
            if not step[n-2]:
                step[n-2] = climb(n-2)
            return step[n-1] + step[n-2]

        return climb(n)

