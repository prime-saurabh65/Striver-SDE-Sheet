class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        # sort the intervals:
        intervals.sort()
        ans = []

        for start, end in intervals:
            # if ans is empty or [start, end] is non overlapping:
            if not ans or ans[-1][-1] < start:
                ans.append([start, end])
            else:
                # change the end of last filled interval in ans:
                ans[-1][-1] = max(ans[-1][-1], end)
        
        return ans