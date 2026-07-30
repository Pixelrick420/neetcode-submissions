class Node:
    def __init__(self):
        self.isTerminal = False
        self.word = None
        self.children = [None] * 26

class PrefixTree:
    def __init__(self):
        self.root = Node()
    
    def add(self, word: str) -> None:
        node = self.root

        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = Node()
            
            node = node.children[index]
        
        node.isTerminal = True
        node.word = word
    
    def find(self, word: str) -> bool:
        node = self.root

        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        
        return node.isTerminal


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.add(word)
        
        self.out = set()
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def explore(row, col, node, used):
            char = board[row][col]
            index = ord(char) - ord('a')
            
            if node.children[index]:
                if node.children[index].isTerminal:
                    self.out.add(node.children[index].word)

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in used:
                        used.add((nr, nc))
                        explore(nr, nc, node.children[index], used)
                        used.remove((nr, nc))
        
        for i in range(m):
            for j in range(n):
                explore(i, j, trie.root, {(i, j)})
        
        return list(self.out)