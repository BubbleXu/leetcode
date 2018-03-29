# Given an array of words and a length L,
# format the text such that each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach;
# that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]


class Solution(object):
    def full_justify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        cur_line_words = []
        cur_line_len = 0
        i = 0
        while i < len(words):
            if cur_line_len + len(words[i]) + len(cur_line_words) > maxWidth:
                # add this line
                if len(cur_line_words) == 1:
                    result.append(cur_line_words[0] + ' ' * (maxWidth - cur_line_len))
                else:
                    avg_num, add_num = divmod(maxWidth - cur_line_len, len(cur_line_words) - 1)
                    line = cur_line_words[0]
                    for j in range(1, len(cur_line_words)):
                        if add_num > 0:
                            line += ' ' * (avg_num + 1)
                            add_num -= 1
                        else:
                            line += ' ' * avg_num
                        line += cur_line_words[j]
                    result.append(line)

                cur_line_words = []
                cur_line_len = 0
            else:
                cur_line_len += len(words[i])
                cur_line_words.append(words[i])
                i += 1

        # last line
        line = ' '.join(cur_line_words)
        line += ' ' * (maxWidth - len(line))
        result.append(line)

        return result


if __name__ == '__main__':
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16

    words = ["What","must","be","shall","be."]
    L = 12

    print solution.full_justify(words, L)
