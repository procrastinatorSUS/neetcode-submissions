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
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if target <= array[-1]:
                return self.search(array, target)
        return False