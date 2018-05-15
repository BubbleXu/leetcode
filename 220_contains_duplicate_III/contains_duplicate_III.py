# Given an array of integers,
# find out whether there are two distinct indices i and j in the array
# such that the absolute difference between nums[i] and nums[j] is at most t
# and the absolute difference between i and j is at most k.
#
# Example 1:
#
# Input: [1,2,3,1], k = 4, t = 0
# Output: true
# Example 2:
#
# Input: [1,0,1,1], k = 1, t = 0
# Output: true
# Example 3:
#
# Input: [4,2], k = 2, t = 1
# Output: false


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        pairs = []
        for i in range(len(nums)):
            pairs.append((nums[i], i))
        pairs.sort()
        for i in range(len(pairs) - 1):
            for j in range(i + 1, len(pairs)):
                if pairs[j][0] - pairs[i][0] <= t:
                    if abs(pairs[j][1] - pairs[i][1]) <= k:
                        return True
                else:
                    continue
        return False

    def contains_nearby_almost_duplicate(self, nums, k, t):
        if t < 0:
            return False

        # bucket_id -> num
        buckets = {}
        for i in range(len(nums)):
            bucket_id = nums[i] / (t + 1)
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(buckets[bucket_id - 1] - nums[i]) <= t:
                return True
            if bucket_id + 1 in buckets and abs(buckets[bucket_id + 1] - nums[i]) <= t:
                return True

            buckets[bucket_id] = nums[i]
            if i >= k:
                buckets.pop(nums[i - k] / (t + 1))
        return False
