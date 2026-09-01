class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower() 

        res = ''
        new_s = ''

        for i in s: 
            if i.isalnum() : 
                new_s += i

        for i in range(len(s)-1, -1, -1): 
            if s[i].isalnum(): 
                res+=s[i]

        return res == new_s