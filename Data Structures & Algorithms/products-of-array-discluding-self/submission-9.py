class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # List that will add the products from left to right O(N)
        left = [1 for i in range(len(nums))] 
        # Fill the list with the products 
        for i in range(1, len(nums)) : 
            left[i] = nums[i-1] * left[i-1]

        # List that will ad the products from right to left O(N)
        right = [1 for i in range(len(nums))] 
        # Fill the list with the products 
        for i in range(len(nums)-2, -1, -1) : 
            right[i] = nums[i+1] * right[i+1]

        res = [1 for i in range(len(nums))] 

        for i in range(len(nums)) : 
            res[i] = left[i] * right[i]
        
        return res 

