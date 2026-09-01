class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        Build one helper list that will contain the products of all values from left to right other than the one in index
        Build another helper list that will contain the products of all values from right to left other than the one in index 
        At the end, iterate through and multiply products of two numbers in index of both helper lists. 
        '''

        left_to_right = [1] * len(nums) 
        right_to_left = [1] * len(nums)
        res = [1] * len(nums)

        # helper list left to right 
        for i in range(1, len(nums)) : 
            left_to_right[i] = nums[i-1] * left_to_right[i-1]
        
        # helper list right to left 
        for i in range(len(nums)-2, -1, -1) : 
            right_to_left[i] = nums[i+1] * right_to_left[i+1]

        # final res list 
        for i in range(len(nums)) : 
            res[i] = left_to_right[i] * right_to_left[i]
        
        return res 