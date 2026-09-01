class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0 
        profit = 0 

        l, r = 0, 1 

        while r < len(prices) : 

            profit = prices[r] - prices[l]

            best = max(profit, best)

            if prices[r] < prices[l] : 
                l = r 
            r+=1 
        return best 