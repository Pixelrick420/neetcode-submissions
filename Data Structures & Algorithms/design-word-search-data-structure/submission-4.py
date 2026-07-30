class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isTerminal = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            index = (ord(char) - ord('a'))
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.isTerminal = True

    def find(self, word, index, node):
        if not node:
            return False
        
        elif index >= len(word):
            return node.isTerminal

        elif word[index] == '.':
            for char in range(26):
                if self.find(word, index + 1, node.children[char]):
                    return True
            return False

        else:
            char = (ord(word[index]) - ord('a'))
            return self.find(word, index + 1, node.children[char]) 


class WordDictionary:
    def __init__(self):
        self.trie = PrefixTree()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        index = ord(word[0]) - ord('a')
        return self.trie.find(word, 0, self.trie.root)
