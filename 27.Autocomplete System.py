import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []   # store words passing through this node

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()
        self.freq = {}

    def insert(self, word, frequency):
        self.freq[word] = frequency
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.words.append(word)

    def search(self, prefix, k):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        # Use heap to get top k frequent words
        return heapq.nlargest(k, node.words, key=lambda w: self.freq[w])


# Example
auto = AutocompleteSystem()
auto.insert("apple", 10)
auto.insert("app", 25)
auto.insert("april", 5)
auto.insert("ape", 15)

print(auto.search("ap", 3))
