class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # First, find the minimum in the array, then find the target 

        l, r = 0, len(nums)-1
        minimum = 0 

        while l < r : 

            mid = (r-l) // 2 + l 

            if nums[mid] <= nums[r] : 
                r = mid 
            else : 
                l = mid + 1 
        minimum = l 

        l, r = 0, len(nums)-1
        
        if nums[minimum] <= target <= nums[r] : 
            l = minimum
        else : 
            r = minimum - 1 

        while l <= r : 

            mid = (r-l) // 2 + l 

            if target > nums[mid] : 
                l = mid + 1 
            elif target < nums[mid] : 
                r = mid - 1 
            else : 
                return mid 
        return -1  