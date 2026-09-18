from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def path_find(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            return path_find(n-1) + path_find(n-2)

        for i in range(1, n):
            path_find(i)
        return path_find(n)