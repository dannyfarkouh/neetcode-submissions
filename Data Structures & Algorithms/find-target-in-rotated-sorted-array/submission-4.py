class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        cut = 0 

        while l < r : 
            mid = (l+r) // 2 

            if nums[mid] <= nums[r] : 
                r = mid 
            else : 
                l = mid + 1 

        cut = l # Position of minimum value (so cut is here)
        
        l, r = 0, len(nums)-1

        if cut != 0 : 
            if target >= nums[cut] and target <= nums[-1] : 
                l = cut
            elif target > nums[cut] and target > nums[-1] : 
                r = cut - 1 
        
        while l <= r : 
            mid = (l+r) // 2 
            if target > nums[mid] : 
                l = mid + 1 
            elif target < nums[mid] : 
                r = mid - 1 
            elif target == nums[mid] : 
                return mid 
        return -1 
