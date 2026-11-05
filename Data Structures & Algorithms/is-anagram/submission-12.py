class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram1 = [0 for _ in range(26)]
        anagram2 = [0 for _ in range(26)]

        for c in s: 
            anagram1[ord(c) - ord('a')] += 1 
        
        for c in t: 
            anagram2[ord(c) - ord('a')] += 1 
        
        return anagram1 == anagram2