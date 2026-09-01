class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case 
        if t == "" : return ""
        
        count_t, window = {}, {}

        # init count_t 
        for c in t : 
            count_t[c] = 1 + count_t.get(c, 0)
        
        l = 0 
        res, res_len = [-1, -1], float("infinity")
        have, need = 0, len(count_t)

        for r in range(len(s)) : 
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and count_t[c] == window[c] : 
                have += 1 
            
            while have == need : 

                if (r-l+1) < res_len : 
                    res = [l, r]
                    res_len = (r-l+1)
                
                window[s[l]] -= 1 

                if s[l] in count_t and count_t[s[l]] > window[s[l]] : 
                    have -= 1 
                l+=1 
        l, r = res 
        return s[l:r+1] if res != float("infinity") else ""