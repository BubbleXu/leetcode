# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
# (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.


class Solution(object):
    def can_complete_circuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = len(gas)
        for i in range(total):
            cur_gas = 0
            for j in range(total):
                next_station = (i + j) % total
                cur_gas += gas[next_station] - cost[next_station]
                if cur_gas < 0:
                    break
            if cur_gas >= 0:
                return i

        return -1

    def can_complete_circuit2(self, gas, cost):
        start_position, gap, cur_gas = 0, 0, 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            gap += gas[i] - cost[i]
            if cur_gas < 0:
                start_position = i + 1
                cur_gas = 0
        return -1 if gap < 0 else start_position


if __name__ == '__main__':
    solution = Solution()
    gas = [6, 1, 4, 3, 5]
    cost = [3, 8, 2, 4, 2]
    print solution.can_complete_circuit2(gas, cost)
