class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Basically, we have to go from left to right, and find the biggest difference between two numbers in the array. This difference has to be where left is lowest, and right is highest. 
        # So we can have two pointers, starting on the right side. 
        # l, r. We start with l = 0, r = 0. When r is smaller, we make l = r, and continue from there. 
        # We have a value tracking the biggest diff. When we find a diff that is bigger, replace it. 

        l, r = 0, 1
        res = 0  

        while r < len(prices) : 
            diff = prices[r] - prices[l]
            res = max(res, diff)

            if prices[r] < prices[l] : 
                l = r 
                r += 1 
            else : 
                r += 1  
        
        return res 
