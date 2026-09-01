class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_n = {}

        for i in range(len(nums)) : 
            diff = target - nums[i]
            if diff in map_n : 
                return [map_n[diff], i]
            else : 
                map_n[nums[i]] = i 
