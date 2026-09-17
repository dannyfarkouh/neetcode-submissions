class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 6, 1, 2, 3, 4, 5
        # l = 6, r = 5, mid = 2 
        # So when the nums[l] > nums[mid] or nums[r] < nums[mid], then the rotation is on that side 

        l, r = 0, len(nums)-1 

        while l < r : 
            mid = (l + r) // 2 
            if nums[mid] > nums[r] : 
                l = mid + 1
            else : 
                r = mid
        return nums[l]

