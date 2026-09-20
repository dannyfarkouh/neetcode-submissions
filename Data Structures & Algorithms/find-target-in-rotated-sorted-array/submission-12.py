class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Find min in a rotated sorted array 

        l, r = 0, len(nums)-1 

        while l < r : 
            mid = (l + r) // 2 

            if nums[mid] > nums[r] : 
                l = mid + 1 
            else : 
                r = mid 
        cut = l 

        # Check if target is on the left side of cut or on the right side of cut 
        if nums[cut] <= target <= nums[-1] : 
            l, r = cut, len(nums)-1  
        else : 
            l, r = 0, cut-1
        
        # Normal binary search 
        while l <= r : 
            mid = (l + r) // 2 
            
            if nums[mid] < target : 
                l = mid + 1 
            elif target < nums[mid] : 
                r = mid - 1 
            elif target == nums[mid] : 
                return mid 
        return -1 