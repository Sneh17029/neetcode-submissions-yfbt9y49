class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        end = 0
        curr = 0
        while start < len(gas):
            curr += gas[start] - cost[start]
            start += 1
            if curr < 0:
                end = start
                curr = 0
        return end