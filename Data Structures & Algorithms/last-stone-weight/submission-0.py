class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # f = -8
            # s = -7

            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])