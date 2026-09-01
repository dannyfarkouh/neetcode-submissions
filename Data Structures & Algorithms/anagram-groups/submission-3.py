class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = defaultdict(list)

        for string in strs: 
            array = [0] * 26
            for char in string: 
                array[ord(char) - ord('a')] += 1 
            count[tuple(array)].append(string)
        return list(count.values())