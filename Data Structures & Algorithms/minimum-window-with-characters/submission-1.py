class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge case 
        if t == "" : 
            return ""

        # Init 
        l = 0 
        countT, window = {}, {} 
        res, res_len = [-1, -1], float("infinity")

        # Init countT
        for c in t : 
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        
        # Main 
        for r in range(len(s)) : 
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]] : 
                have += 1 
            
            while have == need : 

                if (r-l+1) < res_len : 
                    res = [l, r]
                    res_len = (r-l+1)
                
                window[s[l]] -= 1 

                if s[l] in countT and countT[s[l]] > window[s[l]] : 
                    have -= 1 
                l+=1 
        l, r = res 
        return s[l:r+1] if res_len != float('infinity') else ''

