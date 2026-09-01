class TrieNode: 
    def __init__(self) : 
        self.children = {} 
        self.isWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 


    def addWord(self, word: str) -> None:
        curr = self.root 

        for c in word : 
            if c not in curr.children : 
                curr.children[c] = TrieNode() 
            curr = curr.children[c]
        curr.isWord = True 


    def search(self, word: str) -> bool:
        def dfs(node, index) : 
            curr = node 

            for i in range(index, len(word)) : 
                c = word[i]
                if c != '.' : 
                    if c not in curr.children : 
                        return False 
                    curr = curr.children[c]
                else : 
                    # if c == '.'
                    for child in curr.children.values() : 
                        if dfs(child, i+1) : 
                            return True 
                    return False 
            return curr.isWord 
        return dfs(self.root, 0)
