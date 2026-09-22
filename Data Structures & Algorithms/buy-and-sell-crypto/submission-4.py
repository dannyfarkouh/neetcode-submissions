class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        res = 0 

        while r < len(prices) : 
            diff = prices[r] - prices[l]
            res = max(diff, res)
            if prices[r] < prices[l] : 
                l = r 
                r = l + 1 
            else : 
                r += 1 
        return res 