class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        l = 0
        r = l + 1
        while r < len(intervals):
            if intervals[l][1] < intervals[r][0]:
                res.append(intervals[l])
                l = r
                r = r + 1
            else:
                updated = [min(intervals[l][0], intervals[r][0]), max(intervals[l][1], intervals[r][1])]
                intervals[l] = updated
                intervals.pop(r)
        if l < len(intervals):
            res.append(intervals[l])
        return res