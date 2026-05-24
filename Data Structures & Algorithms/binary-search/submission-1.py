class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            i = left + ((right - left) // 2)
            if target > nums[i]:
                left = i + 1
            elif target < nums[i]:
                right = i - 1
            else:
                return i
        return -1
        