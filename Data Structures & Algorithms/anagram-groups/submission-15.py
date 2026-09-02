class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs : 
            count = {key: 0 for key in range(26)}

            for c in s : 
                count[ord(c) - ord('a')] += 1 
            res[tuple(count.values())].append(s)
        return list(res.values())