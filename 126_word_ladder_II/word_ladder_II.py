# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
#  from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
import collections


class Solution(object):
    def find_ladders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        queue = {beginWord}
        parents = collections.defaultdict(set)
        while queue and endWord not in parents:
            next_queue = collections.defaultdict(set)
            for word in queue:
                for i in range(len(beginWord)):
                    p1, p2 = word[:i], word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            child_word = p1 + j + p2
                            if child_word in word_set and child_word not in parents:
                                next_queue[child_word].add(word)
            queue = next_queue
            parents.update(next_queue)

        result = [[endWord]]
        while result and result[0][0] != beginWord:
            result = [[p] + r for r in result for p in parents[r[0]]]

        return result

        # dict = {x: [] for x in wordList}
        # for i in xrange(len(wordList) - 1):
        #     for j in xrange(i + 1, len(wordList)):
        #         if self.check(wordList[i], wordList[j]):
        #             dict[wordList[i]].append(wordList[j])
        #             dict[wordList[j]].append(wordList[i])
        #
        # result = []
        # queue = []
        # for x in wordList:
        #     if self.check(beginWord, x):
        #         if x == endWord:
        #             result.append([beginWord, endWord])
        #             return result
        #
        #         queue.append([beginWord, x])
        #
        # done = False
        # while queue:
        #     next_queue = []
        #     pop_set = set()
        #     while queue:
        #         cur_list = queue.pop(0)
        #         cur_word = cur_list[-1]
        #         next_candidates = dict.get(cur_word)
        #         if next_candidates:
        #             pop_set.add(cur_word)
        #             for next_word in next_candidates:
        #                 if next_word not in cur_list:
        #                     if next_word == endWord:
        #                         result.append(cur_list + [next_word])
        #                         done = True
        #                     else:
        #                         next_queue.append(cur_list + [next_word])
        #
        #     if done:
        #         break
        #     for word in pop_set:
        #         dict.pop(word)
        #     queue = next_queue
        #
        # return result

    # def check(self, w1, w2):
    #     count = 0
    #     for i in range(len(w1)):
    #         if w1[i] != w2[i]:
    #             count += 1
    #     return count == 1


if __name__ == '__main__':
    solution = Solution()
    print solution.find_ladders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])

