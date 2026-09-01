class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1

        while i < j: 
            if (not self.isValid(s[i])): 
                i+=1 
            elif (not self.isValid(s[j])): 
                j-=1 
            elif s[i].lower() != s[j].lower():
                return False
            else: 
                i+=1 
                j-=1 
        return True 
    
    def isValid(self, c): 
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9')