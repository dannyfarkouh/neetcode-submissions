class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for char in s:
            if char in mapS: 
                mapS[char] += 1 
            else: 
                mapS[char] = 1 
        
        for char in t: 
            if char in mapT: 
                mapT[char] += 1 
            else: 
                mapT[char] = 1 
        
        return mapS == mapT