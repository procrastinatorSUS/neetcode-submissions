from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ln = len(cost)

        ans = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            ans.append(min(ans[i-1], ans[i-2]) + cost[i])

        return min(ans[-1], ans[-2])