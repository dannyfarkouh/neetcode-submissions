class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {} 
        dict_t = {} 

        # s 
        for c in s : 
            if c in dict_s : 
                dict_s[c] += 1 
            else : 
                dict_s[c] = 1
        
        # t 
        for c in t : 
            if c in dict_t : 
                dict_t[c] += 1 
            else : 
                dict_t[c] = 1
            
        return dict_s == dict_t 