class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Have a big dict, where the key is the map value of each word. For example
        # Key : 00000010001010100012000202...0 would be the length 26 key for a value.
        # The value will be a list of all words with this exact number of letters per word. thus a list of anagrams. 
        # At the end, we will just print the dict's values as a list 

        # Init the big dict 
        res = defaultdict(list)

        # First, go through the list of words
        for word in strs : 
            # Init the dict that will be used by each word 
            count = {key: 0 for key in range(26)}

            # Then, through the list of chars per word 
            for char in word :
                count[ord(char) - ord('a')] += 1 
            
            res[str(count.values())].append(word)
        
        return list(res.values())