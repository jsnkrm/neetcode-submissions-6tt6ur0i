class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        lMap = {}
        for l, r in intervals:
            curr = r - l + 1
            for i in range(l, r + 1):
                lMap[i] = min(lMap.get(i, 30000), curr)
        res = []
        print(lMap)
        for q in queries:
            if q not in lMap:
                res.append(-1)
            else:
                res.append(lMap[q])
        return res