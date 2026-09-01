class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1

        while i < j: 
            #if letters are the exact same
            while i < j: 
                if (not self.isValidChar(s[i])): 
                    i += 1 
                else: 
                    break
            while j > i: 
                if (not self.isValidChar(s[j])): 
                    j -= 1
                else: 
                    break 
            if s[i].lower() != s[j].lower(): 
                return False 
            else: 
                i+=1
                j-=1 
        return True 
            
    def isValidChar(self, char):
        if ((ord('a') <= ord(char) <= ord('z')) or 
        (ord('A') <= ord(char) <= ord('Z')) or 
        (ord('0') <= ord(char) <= ord('9'))): 
            return True 
        else: 
            return False
            
