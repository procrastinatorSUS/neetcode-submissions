from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ln = len(cost)

        @lru_cache(None)
        def calc_cost(i, sm):
            if i == ln-1: 
                return sm+cost[i]
            if i == ln:
                return sm
            sm += cost[i]
            return min(calc_cost(i+1, sm), calc_cost(i+2, sm))
        
        return min(calc_cost(0, 0), calc_cost(1, 0))