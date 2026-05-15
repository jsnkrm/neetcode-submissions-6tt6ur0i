class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = 0
        index = 0
        check = False
        while index < len(strs[0]):
            curr = strs[0][index]
            for s in strs:
                if len(s) - 1 < index or s[index] != curr:
                    check = True
                    break
            if check: 
                break
            index += 1
            res += 1
        
        return strs[0][:res]