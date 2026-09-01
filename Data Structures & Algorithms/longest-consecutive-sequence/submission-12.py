class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0

        for num in nums: 
            # This is the trick to solving this leetcode problem 
            if num-1 not in seen: # If num is at the start of its sequence 
                seq = 1 
                while num + seq in seen: 
                    seq += 1 
                longest = max(longest, seq)
        return longest 
