class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1 - find the cut (find the min)

        l, r = 0, len(nums)-1 

        while l < r : 
            mid = (r-l )// 2 + l 
            if nums[mid] <= nums[r] : 
                r = mid 
            else : 
                l = mid + 1 
        
        cut = l 

        l, r = 0, len(nums)-1

        if nums[cut] <= target <= nums[r] : 
            l = cut 
        else : 
            r = cut - 1 
        
        while l <= r : 
            mid = (r - l) // 2 + l 
            if target < nums[mid] : 
                r = mid - 1 
            elif target > nums[mid] : 
                l = mid + 1 
            else : 
                return mid 
        return -1 