class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # first of all, sort the intervals depending on start time 
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals : 

            # if this interval is fully bigger than the biggest in res as of now 
            if start > res[-1][1] : 
                res.append([start, end])
            
            # if this interval is within the last interval 
            else : 
                res[-1][1] = max(res[-1][1], end)
        return res 