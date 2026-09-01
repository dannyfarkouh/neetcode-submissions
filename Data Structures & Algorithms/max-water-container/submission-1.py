class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1

        largest_surface = 0 

        while l < r : 
            curr_surface = (r - l) * min(heights[l], heights[r])
            largest_surface = max(largest_surface, curr_surface)

            if heights[l] > heights[r] : 
                r-=1 
            elif heights[l] < heights[r] : 
                l+=1 
            else: 
                l+=1 
            
        return largest_surface