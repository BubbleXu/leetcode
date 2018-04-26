# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?

class Solution:
    # @param n, an integer
    # @return an integer
    def reverse_bits(self, n):
        b = str(bin(n))
        b = b[2:]
        b = '0' * (32 - len(b)) + b
        b = b[::-1]
        return int(b, 2)


if __name__ == '__main__':
    solution = Solution()
    n = 43261596
    print solution.reverse_bits(n)
