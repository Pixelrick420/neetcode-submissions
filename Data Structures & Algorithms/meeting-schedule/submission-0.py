class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval: (interval.start, interval.end))
        n = len(intervals)

        for index in range(1, n):
            if intervals[index].start < intervals[index - 1].end:
                return False
        
        return True