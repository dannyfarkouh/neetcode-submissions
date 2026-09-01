class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs: 
            res += str(len(s)) + "#" + s 
        return res 

    def decode(self, s: str) -> List[str]:
        
        res = [] # result list 
        i = 0 # index to iterate through string 

        while i < len(s): 
            j = i # j will iterate through the strings in s 

            while s[j] != "#": 
                j+= 1; 
            length = int(s[i : j])

            res.append(s[j + 1 : (j + 1) + length])
            i = j + 1 + length
        
        return res 