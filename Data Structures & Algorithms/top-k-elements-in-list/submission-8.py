class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1 - add numbers to a dict with the number and its frequency 
        freq_dict = {} # key = num, value = freq 

        for num in nums : 
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        # 2 - translate to a datastructure that holds the freq, and nums at that freq on the right 
        freq_arr = [ [] for i in range(len(nums) + 1) ] 

        for num, freq in freq_dict.items() : 
            freq_arr[freq].append(num)
        
        # 3 - get k frequent nums from that array of arrays, sorted by frequency 
        res = []

        for i in range(len(freq_arr)-1, -1, -1) : 
            for j in range(len(freq_arr[i])) : 
                res.append(freq_arr[i][j])
                k-=1 

                if k <= 0 : 
                    return res 
        return [] 