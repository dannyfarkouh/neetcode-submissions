class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        def dfs( index, total, curr ) :

            # base case 
            if total > target or index >= len(nums) or index < 0: 
                return 

            if total == target : 
                res.append(curr.copy())
                return 
            
            curr.append(nums[index])
            dfs(index, total + nums[index], curr)
            curr.pop() 
            dfs(index+1, total, curr)
        
        dfs(0, 0, [])
        return res 