class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge case 
        if t == "" : return ""

        # Init 
        window, count_t = {}, {} 
        l = 0 
        res, res_len = [-1, -1], float("infinity")

        # Init count_t 
        for c in t : 
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)

        for r in range(len(s)) : 
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c] : 
                have += 1 
            
            while have == need : 

                if res_len > (r-l+1) : 
                    res_len = (r-l+1)
                    res = [l, r]
                
                window[s[l]] -= 1 

                if s[l] in count_t and window[s[l]] < count_t[s[l]] : 
                    have -= 1 
                
                l+=1 
        l, r = res 
        return s[l:r+1] if res != float("infinity") else ""