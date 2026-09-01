class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initialize the hash map 
        map_s = {key: 0 for key in range(26)} 
        map_t = {key: 0 for key in range(26)} 

        # Go through string s and map to the hash map 
        for c in s : 
            map_s[ord(c) - ord('a')] += 1 
        
        for c in t : 
            map_t[ord(c) - ord('a')] += 1 

        
        return map_s == map_t