class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        arr = [[] for i in range(len(nums)+ 1)]

        for num in nums: 
            if num in hashmap: 
                hashmap[num]+=1 
            else: 
                hashmap[num] = 1
        # Now we have a hashmap with key = num, and value = frequency 

        for num, freq in hashmap.items(): 
            arr[freq].append(num)

        # Now we have a list of lists, where the index is the freq, and the lists contain nums with said freq

        res = []
        for i in range(len(nums), 0, -1): 
            for j in arr[i]: 
                res.append(j)
                if len(res) == k: 
                    return res 