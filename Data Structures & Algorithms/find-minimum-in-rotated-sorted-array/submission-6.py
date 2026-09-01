class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1 

        while l < r : 

            mid = (r-l) // 2 + l 

            if nums[mid] <= nums[r] : # so they are in order, so minimum not here 
                r = mid 
            else : 
                l = mid + 1 
            
        return nums[r]