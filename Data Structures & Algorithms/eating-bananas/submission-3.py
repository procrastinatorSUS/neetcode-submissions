from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        rez = right = max(piles)
        while left <= right:
            i = (left + right) // 2
            target = sum(ceil(n/i) for n in piles)
            if target > h:
                left = i + 1
            elif target <= h:
                rez = i
                right = i - 1
        return rez