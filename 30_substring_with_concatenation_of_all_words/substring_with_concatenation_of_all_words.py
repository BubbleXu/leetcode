# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s
# that is a concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).


class Solution(object):
    def find_substring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if not words:
            return result

        single_l = len(words[0])
        total_l = single_l * len(words)
        dict = {}
        for w in words:
            dict[w] = dict[w] + 1 if w in dict else 1

        for i in range(single_l):
            left = i
            right = i
            cur_dict = {}
            while right + single_l <= len(s):
                cur_word = s[right: right + single_l]
                right += single_l
                if cur_word in dict:
                    cur_dict[cur_word] = cur_dict[cur_word] + 1 if cur_word in cur_dict else 1
                    while cur_dict[cur_word] > dict[cur_word]:
                        cur_dict[s[left: left + single_l]] -= 1
                        left += single_l
                    if right - left == total_l:
                        result.append(left)
                else:
                    cur_dict.clear()
                    left = right

        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'wordgoodgoodgoodbestword'
    words = ["word", "good", "best", "good"]
    print solution.find_substring(s, words)
