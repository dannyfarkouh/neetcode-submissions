class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "" : return ""
        
        dict_t, window = {} , {} 

        # fill in the dict_t 
        for c in t : 
            dict_t[c] = 1 + dict_t.get(c, 0)
        
        need, have = len(dict_t), 0 

        res, res_len = [-1,-1], float("inf")

        l, r = 0, 0

        for r in range(len(s)) : 
            
            c = s[r] 
            window[c] = 1 + window.get(c, 0)

            if c in dict_t and window[c] == dict_t[c] : 
                have += 1 
            
            while have == need : 

                if (r-l+1) < res_len : 
                    res_len = (r-l+1)
                    res = [l, r]
                 
                window[s[l]] -= 1 
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]] : 
                    have-=1 
                l+=1 
        l, r = res 
        return s[l : r + 1] if res_len != float("inf") else ""    