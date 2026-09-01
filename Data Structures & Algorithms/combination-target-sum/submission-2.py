class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def back( index, curr, total ) : 
            # index is the index of the number that we are currently adding 
            # curr is the current sublist that adds up to total 
            # total is the total of adding up the numbers in curr (list)

            if total == target : 
                res.append(curr.copy())
                return 

            if index >= len(nums) or total > target : 
                return 
            
            curr.append(nums[index])
            back(index, curr, total + nums[index])
            curr.pop() 
            back(index+1, curr, total)
        
        back(0, [], 0)
        return res 
