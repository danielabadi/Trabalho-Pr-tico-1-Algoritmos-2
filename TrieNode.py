class TrieNode:
    def __init__(self, char, pai):
        self.pref = char
        self.array = []
        self.children = {}
        self.pai = pai