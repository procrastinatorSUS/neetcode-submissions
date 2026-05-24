class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums:
                try:
                    return [i, nums.index(target - nums[i],i+1)]
                except ValueError:
                    pass