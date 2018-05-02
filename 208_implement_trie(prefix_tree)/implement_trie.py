# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


class TireNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return

        cur = self.root
        for c in word:
            if not cur.children.get(c):
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if cur.children.get(c):
                cur = cur.children[c]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if cur.children.get(c):
                cur = cur.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('a')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)