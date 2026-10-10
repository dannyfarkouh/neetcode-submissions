class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "" : return ""

        l = 0 

        dict_t, window = {}, {}

        for c in t : 
            if c in dict_t : 
                dict_t[c] += 1 
            else : 
                dict_t[c] = 1 

        have, need = 0, len(dict_t)

        res, res_len = [-1, -1], float("inf")

        for r, c in enumerate(s) : 

            # add c in window 
            if c in window : 
                window[c] += 1 
            else : 
                window[c] = 1 

            if c in dict_t and dict_t[c] == window[c] : 
                have += 1 

            while have == need : 

                if (r-l+1) < res_len : 
                    res = [l, r]
                    res_len = (r-l+1)
                
                window[s[l]] -= 1 
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]] : 
                    have -= 1 
                l+=1
        l, r = res 
        return s[l:r+1] if res_len != float("inf") else ""