# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
import collections


class Solution(object):
    def ladder_length(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        queue = {beginWord}
        parents = collections.defaultdict(set)
        while queue and endWord not in parents:
            next_queue = collections.defaultdict(set)
            for word in queue:
                for i in range(len(beginWord)):
                    p1, p2 = word[:i], word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            child_word = p1 + j + p2
                            if child_word in word_set and child_word not in parents:
                                next_queue[child_word].add(word)
            queue = next_queue
            parents.update(next_queue)

        result = 0
        cur_word = endWord
        while cur_word != beginWord and parents[cur_word]:
            result += 1
            cur_word = parents[cur_word].pop()

        return result if result == 0 else result + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.ladder_length('hit', 'cog', ["hot","dot","dog","lot","log","cog"])