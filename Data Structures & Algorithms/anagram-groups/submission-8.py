class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Key = tuple representing the anagram code, Value = the words with that anagram code 

        for s in strs : 
            anagram_code = [0] * 26
            for c in s : 
                anagram_code[ ( ord(c) - ord('a') ) ] += 1 
            res[tuple(anagram_code)].append(s)
        
        return list(res.values() )