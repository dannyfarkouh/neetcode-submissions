class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "" : return ""

        # left pointer init
        l = 0 

        # string t as a dict + the window itself as a dict 
        dict_t, window = {}, {}

        # Fill the dict_t with values from t 
        for c in t : 
            if c in dict_t : 
                dict_t[c] += 1 
            else : 
                dict_t[c] = 1 

        # how many letters from t we have vs we need for the window to be valid 
        need, have = len(dict_t), 0 

        # result + length of result 
        res, res_len = [-1, -1], float("inf")

        for r, c in enumerate(s) : 

            # First add the c to the window dict 
            if c in window : 
                window[c] += 1 
            else : 
                window[c] = 1 
        
            # If the char is in dict_t and it matches the amount we need for the window to be valid, iterate have. 
            if c in dict_t and window[c] == dict_t[c] : 
                have += 1 
            
            # Now if the window is valid : 
            while have == need : 

                # Renew the result if needed 
                if (r-l+1) < res_len : 
                    res = [l, r]
                    res_len = (r-l+1)
                
                # Now it is time to iterate to a new length window (maybe smaller than what we have now and still valid)
                window[s[l]] -= 1 

                # It is key to check whether the letter we just removed changed the have, to make sure if the window is valid or not 
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]] : 
                    have -= 1 

                # Now iterate the left pointer
                l+=1

        l, r = res 
        return s[l : r + 1] if res_len != float("inf") else ""