class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        array = [[] for i in range(len(nums) + 1)] 
        count = defaultdict(int)

        # count will contain a value of num and key of count of this num
        for num in nums: 
            count[num] += 1

        # now place these into the count array 
        for num, freq in count.items(): 
            array[freq].append(num)

        result = []
        for i in range(len(array) -1, 0, -1):
            for j in array[i]: 
                result.append(j)
                if len(result) == k: 
                    return result