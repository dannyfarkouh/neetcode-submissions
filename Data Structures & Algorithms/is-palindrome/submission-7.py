class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1

        while i < j : 
            if not self.isValidChar(s[i]): 
                i+=1
            elif not self.isValidChar(s[j]): 
                j-=1
            else: 
                if s[i].lower() != s[j].lower(): 
                    return False 
                i+=1
                j-=1
        
        return True 


    def isValidChar(self, char): 
        if (ord('a') <= ord(char) <= ord('z') or 
            ord('A') <= ord(char) <= ord('Z') or 
            ord ('0') <= ord(char) <= ord('9')):
            return True 
        else: 
            return False 