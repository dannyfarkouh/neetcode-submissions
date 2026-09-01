class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        array = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)): 
            if nums[i] in count: 
                count[nums[i]] += 1 
            else: 
                count[nums[i]] = 1 
        
        for num, freq in count.items(): 
            array[freq].append(num)
        
        res = [] 
        for i in range(len(array)-1, 0, -1): 
            for j in array[i]: 
                res.append(j)
                if len(res) == k: 
                    return res 