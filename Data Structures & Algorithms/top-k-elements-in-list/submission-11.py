class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dict, key = number, value = frequency of that number 
        count = {}

        # List, index = frequency, value = list of numbers of that frequency 
        freq = [ [] for i in range(len(nums) + 1) ]

        for num in nums : 
            if num in count : 
                count[num] += 1 
            else : 
                count[num] = 1 
        
        for num, f in count.items() : 
            freq[f].append(num)

        res = [] 
        for i in range(len(freq)-1, 0, -1) : 
            for j in range(len(freq[i])): 
                if k != 0 : 
                    res.append(freq[i][j])
                    k-=1
        return res 