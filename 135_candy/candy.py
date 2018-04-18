# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left_to_right = [1 for _ in range(len(ratings))]
        right_to_left = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                left_to_right[i] = left_to_right[i - 1] + 1

        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i]:
                right_to_left[i - 1] = right_to_left[i] + 1

        result = 0
        for i in range(len(ratings)):
            result += max(left_to_right[i], right_to_left[i])
        return result