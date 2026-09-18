class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # First we find where the rotation occurs 

        l, r = 0, len(nums)-1 

        while l < r : 
            mid = (l + r) // 2 

            # If nums[mid] > nums[r] then we know mid is not the minimum, so we eliminate it 
            if nums[mid] > nums[r] : 
                l = mid + 1 
            # Here, mid can still be the min, so we keep it 
            else : 
                r = mid 
        cut = l

        # Now let us check if the target is before or after the cut 

        # If on the right side 
        if nums[cut] <= target <= nums[-1] : 
            l, r = cut, len(nums)-1 
        else : 
            l, r = 0, cut-1

        # Now that we have the min and the min index, we just do a normal binary search 

        while l <= r : 
            mid = (l + r) // 2

            if target < nums[mid] : 
                r = mid - 1 
            elif target > nums[mid] : 
                l = mid + 1 
            elif target == nums[mid] : 
                return mid 
        return -1 