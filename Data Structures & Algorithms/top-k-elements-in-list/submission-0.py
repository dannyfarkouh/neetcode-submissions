class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #initialize
        count = {}
        arrayFreq = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            if num in count: 
                count[num] += 1
            else: 
                count[num] = 1

        for num, freq in count.items(): 
            arrayFreq[freq].append(num)

        result = []
        for i in range(len(arrayFreq) - 1, 0, -1): 
            for j in arrayFreq[i]: 
                result.append(j)
                if len(result) == k: 
                    return result
                