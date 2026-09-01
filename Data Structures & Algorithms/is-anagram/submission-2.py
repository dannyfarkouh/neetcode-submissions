class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = {} 
        hashmapT = {}
        
        for char in s: 
            if char in hashmapS: 
                hashmapS[char] += 1 
            else : 
                hashmapS[char] = 1

        for char in t: 
            if char in hashmapT: 
                hashmapT[char] += 1
            else : 
                hashmapT[char] = 1 

        return hashmapT == hashmapS