class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out  = []
        left = intervals[0][0]
        right = intervals[0][1]

        for  start, end in intervals:
            if start > right:
                out.append([left, right])
                left = start
            
            right = max(right, end)
        

        out.append([left, right])
            
        return out