class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, curr):
            if o == n and c == n:
                res.append(curr[::])
                return
            
            if o < n:
                curr += "("
                dfs(o + 1, c, curr)
                curr = curr[:-1]

            if c < o:
                curr += ")"
                dfs(o, c + 1, curr)
                curr = curr[:-1]

        dfs(0 , 0, "")
        return res