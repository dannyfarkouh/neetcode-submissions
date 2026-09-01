class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_profit = 0 

        l, r = 0, 1 

        while r < len(prices) : 
            profit = prices[r] - prices[l]

            if profit > best_profit : 
                best_profit = profit 
            
            if prices[r] < prices[l] : 
                l = r 
            r+=1 
        
        return best_profit 