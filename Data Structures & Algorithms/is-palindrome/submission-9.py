class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1

        while i < j: 
            
            if not self.isValidChar(s[i]):
                i+=1 
            
            elif not self.isValidChar(s[j]): 
                j-=1 

            elif s[i].lower() != s[j].lower():
                return False 
            
            else: 
                i+=1 
                j-=1
        
        return True 


    def isValidChar(self, char):
        return (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'))