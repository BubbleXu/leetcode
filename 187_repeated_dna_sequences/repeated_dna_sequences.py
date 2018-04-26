# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
import collections


class Solution(object):
    def find_repeated_dna_sequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        dict = collections.defaultdict(lambda: 0)
        for i in range(len(s) - 9):
            dict[s[i:i+10]] += 1

        result = []
        for x in dict:
            if dict[x] > 1:
                result.append(x)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print solution.find_repeated_dna_sequences(s)
