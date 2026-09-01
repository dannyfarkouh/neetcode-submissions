class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1- Create hashmap with key = num, value = freq 
        num_freq = defaultdict(int)

        for num in nums : 
            num_freq[num] += 1 
        
        # 2- Create array with index = freq, value = list of nums 
        array_num_freq = [ [] for _ in range(len(nums)+1) ]
        print(array_num_freq)

        for num, freq in num_freq.items() : 
            array_num_freq[freq].append(num)

        # 3- Iterate through array_num_freq from end to beginning, k times, 

        count = k 
        res = [] 

        for i in range(len(array_num_freq)-1, -1, -1) : 
            for j in range(len(array_num_freq[i])-1, -1, -1) : 
                if count == 0 : 
                    break 
                res.append(array_num_freq[i][j])
                count -= 1 
        return res 