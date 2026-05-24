class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        rez = []
        for first in range(len(nums) - 2):
            left = first + 1
            right = len(nums) - 1
            target = nums[first] * -1
            
            while left < right:

                if nums[left] + nums[right] == target:
                    three = [nums[first], nums[left], nums[right]]
                    if three not in rez:
                        rez.append(three)
                    left += 1
                    right -= 1
                else:
                    if nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return rez
