class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        largest_area = 0

        while l < r : 

            curr_area = (r - l) * (min(heights[l], heights[r]))

            largest_area = max(largest_area, curr_area)

            if heights[l] > heights[r] : 
                r-=1 
            elif heights[l] <= heights[r] : 
                l+=1 
        
        return largest_area