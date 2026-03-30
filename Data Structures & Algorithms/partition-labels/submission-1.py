class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = i
        
        curr = s[0]
        i = 0 
        res = []
        count = 0
        while i < len(s):
            
            if s[i] == curr and i == freq[curr]:
                res.append(count + 1)
                count = 0
                if i < len(s) - 1:
                    curr = s[i + 1]
                i += 1
            
            elif s[i] == curr or freq[s[i]] == -1:
                count += 1
                i += 1
            
            elif s[i] != curr:
                if freq[curr] < freq[s[i]]:
                    freq[curr] = -1
                    curr = s[i]
                else:
                    freq[s[i]] = -1
                count += 1
                i += 1
        return res
