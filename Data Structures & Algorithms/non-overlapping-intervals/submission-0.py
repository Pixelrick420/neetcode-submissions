class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        last = intervals[0][0] 
        count = 0

        for start, end in intervals:
            if start < last:
                count += 1
                last = min(end, last)
            
            else:
                last = end

        return count