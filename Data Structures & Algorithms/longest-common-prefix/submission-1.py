class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        idx = 0

        while idx < len(strs[0]):
            curr = strs[0][idx]
            found = True
            for s in strs:
                if s == strs[0]: continue
                if len(s) <= idx: 
                    found = False
                    break
                if s[idx] == curr:
                    continue
                else:
                    found = False
                    break
            if found:
                res += curr
                print(res)
            else:
                break
            idx += 1
        
        return res