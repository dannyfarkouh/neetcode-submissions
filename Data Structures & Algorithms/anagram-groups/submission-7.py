class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs: 
            key = 26 * [0]

            for char in s: 
                key[ord(char) - ord('a')]+= 1 

            hashmap[tuple(key)].append(s)

        return list(hashmap.values())