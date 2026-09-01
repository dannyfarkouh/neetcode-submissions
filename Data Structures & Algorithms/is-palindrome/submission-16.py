class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        while l < r : 

            while l < r and not self.isValidChar(s[l]) : 
                l+=1
            
            while r > l and not self.isValidChar(s[r]) : 
                r-=1 
            
            if s[l].lower() != s[r].lower() : 
                return False 
            else : 
                l+=1 
                r-=1 
        return True 


    def isValidChar(self, c) : 
        return ( ('a' <= c <= 'z') or 
                ('A' <= c <= 'Z') or 
                ('0' <= c <= '9') )