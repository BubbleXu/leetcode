# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.


class TireNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if not cur.children.get(c):
                cur.children[c] = TireNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)

    def dfs(self, word, cur_node):
        if not word:
            return cur_node.is_word

        c = word[0]
        if c == '.':
            for child in cur_node.children.values():
                if self.dfs(word[1:], child):
                    return True
            return False
        else:
            if cur_node.children.get(c):
                return self.dfs(word[1:], cur_node.children[c])
            else:
                return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)