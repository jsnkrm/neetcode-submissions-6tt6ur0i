class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lMap = { 
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]}
        res = []

        def dfs(i, curr):
            if i == len(digits):
                res.append(curr[::])
                return
            for c in lMap[digits[i]]:
                curr += c
                dfs(i+1, curr)
                curr = curr[:-1]
        
        dfs(0,"")
        return res if len(digits) else []