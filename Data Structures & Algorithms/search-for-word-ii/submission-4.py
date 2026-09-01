class TrieNode : 
    def __init__(self) : 
        self.children = {} 
        self.isWord = False 
    
    def addWord(self, word) : 
        curr = self 

        for c in word : 
            if c not in curr.children : 
                curr.children[c] = TrieNode() 
            curr = curr.children[c]
        curr.isWord = True 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # init vars 
        root = TrieNode() 
        res, visited = set(), set() 
        ROWS, COLS = len(board), len(board[0])

        for word in words : 
            root.addWord(word)

        def dfs( r, c, node, word ) : 

            # base case 
            if (r < 0 or c < 0  or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited or 
                board[r][c] not in node.children) : 
                return False 
            
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.isWord : 
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r, c))
        
        for r in range(ROWS) : 
            for c in range(COLS) : 
                dfs(r, c, root, "")
        return list(res) 





