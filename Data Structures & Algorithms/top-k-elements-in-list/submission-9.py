class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Basically, return the k most frequent numbers within an array of numbers.
        So if the list num = [1,2,2,3,3,3], k = 1, we return [3]. 
        If k = 2, we return [3,2] or [2,3] (order does not matter)

        Note that the nums is not always ordered, if we sort, time complexity will be
        O(nlog(n)), but we think we can do in O(n), so we can do better. 

        Solution in mind : 
        Create a hash map, where the key is the frequency at which a number is 
        present. So search time in the hashmap becomes O(1). Space becomes O(n). We 
        will go through the whole initial array, so time complexity is O(n). The hash 
        map can be initialized with key = 0 of size len(num), which is O(1) time in 
        python.

        Before we get the final frequency hash map, we need an intermediate hash map 
        that will have the numbers as key, and their respective frequencies as 
        values. 
        """

        # Initialize the intermediate hash map with length len(nums)
        # Key = number, Values = Frequency 
        count = {}

        # Initialize the hash map with length len(nums)
        # Key = frequency, Values = list of numbers 
        res = {key: [] for key in range(len(nums)+1)}

        for num in nums :
            if num in count : 
                count[num] += 1 
            else : 
                count[num] = 1

        for num, freq in count.items() : 
            res[freq].append(num)
        
        result = []
        for i in range(len(res)-1, -1, -1): 
            if k != 0 : 
                for num in res[i] : 
                    result.append(num)
                    k-=1
        return result
