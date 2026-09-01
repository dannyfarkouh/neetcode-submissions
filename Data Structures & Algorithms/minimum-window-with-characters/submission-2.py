class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Edge case 
        if t == "" : 
            return ""
        
        count_t, window = {}, {} 

        # Init count_t, since it will remain constant 
        for c in t : 
            if c not in count_t : 
                count_t[c] = 1 
            else : 
                count_t[c] += 1
        
        # Init other values 
        l = 0 
        res, res_len = [-1, -1], float("infinity")
        have, need = 0, len(count_t) 

        for r in range(len(s)) : 

            # Add s[r] to our window 
            c = s[r]
            if c not in window : 
                window[c] = 1 
            else : 
                window[c] += 1 
            
            if c in count_t and count_t[c] == window[c] : 
                have += 1 
            
            while have == need : 

                if (r-l+1) < res_len : 
                    res = [l, r]
                    res_len = (r-l+1)
                
                window[s[l]] -= 1 

                if s[l] in count_t and count_t[s[l]] > window[s[l]]: 
                    have -= 1 
                l+=1 

        l, r = res 
        return s[l:r+1] if res != float("infinity") else ""
        
