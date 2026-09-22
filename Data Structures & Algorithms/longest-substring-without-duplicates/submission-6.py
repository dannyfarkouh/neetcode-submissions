class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0 
        seen = set() 

        for r, c in enumerate(s) : 
            while c in seen : 
                seen.remove(s[l])
                l += 1 
            seen.add(c)
            res = max(res, r-l+1)
        return res 