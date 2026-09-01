class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)): 
            diff = target - nums[i] 
            if diff not in seen: 
                seen[nums[i]] = i
            else: 
                if i > seen[diff]: 
                    return [seen[diff], i]
                else: 
                    return [i, seen[diff]]