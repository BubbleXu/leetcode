# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


class Solution(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if 1 & total_len:
            return self.find_k(nums1, nums2, total_len / 2 + 1)
        else:
            return (self.find_k(nums1, nums2, total_len / 2) + self.find_k(nums1, nums2, total_len / 2 + 1)) / 2.0

    def find_k(self, A, B, k):
        la = len(A)
        lb = len(B)
        pa = min(k / 2, la)
        pb = k - pa

        if la > lb:
            return self.find_k(B, A, k)

        if la == 0:
            return B[k - 1]

        if k == 1:
            return min(A[0], B[0])

        if A[pa - 1] < B[pb - 1]:
            return self.find_k(A[pa:], B, k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.find_k(A, B[pb:], k - pb)
        else:
            return A[pa - 1]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print solution.find_median_sorted_arrays(nums1, nums2)
