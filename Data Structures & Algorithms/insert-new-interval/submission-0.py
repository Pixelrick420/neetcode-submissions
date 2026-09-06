class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        index = 0
        n = len(intervals)

        while index < n and intervals[index][1] < newInterval[0]:
            out.append(intervals[index])
            index += 1
        
        while index < n and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        out.append(newInterval)

        while index < n:
            out.append(intervals[index])
            index += 1
            
        return out