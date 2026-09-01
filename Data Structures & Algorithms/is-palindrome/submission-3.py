class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1

        while l<r: 
            if not self.isValid(s[l]): 
                l+=1 
            elif not self.isValid(s[r]): 
                r-=1 
            else: 
                if s[l].lower() != s[r].lower() : 
                    return False 
                else: 
                    l+=1 
                    r-=1 
        return True 


    def isValid(self, c): 
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') 