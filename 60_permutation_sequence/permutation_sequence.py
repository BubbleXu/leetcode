# coding: utf-8
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.


class Solution(object):
    def get_permutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        res = []
        k -= 1
        for i in range(n):
            index, k = divmod(k, factorial[n - 1 - i])
            res.append(nums[index])
            nums.remove(nums[index])
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    n = 3
    k = 4
    print solution.get_permutation(n, k)

