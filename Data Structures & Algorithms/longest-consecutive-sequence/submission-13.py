class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0 

        for num in seen : 
            if num-1 not in seen : 
                count = 0 

                curr = num 
                while curr in seen : 
                    count += 1 
                    curr += 1 
                
                if count > longest : 
                    longest = count 
        return longest 