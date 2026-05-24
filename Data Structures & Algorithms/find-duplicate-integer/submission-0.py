class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ln_r = len(nums)
        sm_r = sum(nums)
        nums = set(nums)
        ln_q = len(nums)
        sm_q = sum(nums)
        return (sm_r - sm_q) // (ln_r - ln_q)