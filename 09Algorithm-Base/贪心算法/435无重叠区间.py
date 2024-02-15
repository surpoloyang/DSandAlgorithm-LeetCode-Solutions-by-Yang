class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt = 1
        endpos = intervals[0][1]
        size = len(intervals)
        for i in range(1, size):
            if endpos <= intervals[i][0]:
                cnt += 1
                endpos = intervals[i][1]
        return size - cnt