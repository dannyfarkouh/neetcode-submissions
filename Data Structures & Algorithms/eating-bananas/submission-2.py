class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_num = max(piles)
        optimal = max_num

        l, r = 1, max_num
        while l <= r : 
            mid = (l+r) // 2 
            if mid == 0 : 
                mid = 1 

            hours = 0 

            for pile in piles : 
                hours += math.ceil(pile/mid)

            if hours > h : 
                l = mid + 1 
            elif hours <= h : 
                r = mid - 1 
                optimal = min(optimal, mid)

        return optimal 