class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp: int = 0
        nums: List[int] = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k):
            temp = heapq.heappop(nums)

        return -temp