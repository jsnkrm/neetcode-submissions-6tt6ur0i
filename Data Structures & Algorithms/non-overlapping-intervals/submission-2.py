class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        lastEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < lastEnd:
                res += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end
        return res
        
        