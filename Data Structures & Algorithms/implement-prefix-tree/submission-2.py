class Node:
    def __init__(self):
        self.isTerminal = False
        self.children = [None] * 26

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = (ord(char) - ord('a'))
            if not (node.children[index]):
                node.children[index] = Node()
            node = node.children[index]
        node.isTerminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = (ord(char) - ord('a'))
            if (node.children[index] == None):
                return False
            node = node.children[index]
        return node.isTerminal

    def startsWith(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = (ord(char) - ord('a'))
            if (node.children[index] == None):
                return False
            node = node.children[index]
        return True

        