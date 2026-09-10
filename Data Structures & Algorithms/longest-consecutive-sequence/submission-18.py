class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 # Value of the longest sequence
        count = set(nums) # Searching through a hash set is O(1)

        for num in count : 
            longest = 1 # Value of the longest sequency up to now 
            if num-1 in count : 
                continue 
            while num+1 in count : 
                longest += 1 
                num += 1 
            res = max(res, longest)
        return res 