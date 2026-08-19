class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reduced = list(set(nums))
        if len(nums) == 0:
            return False
        elif len(reduced) == len(nums):
            return False
        else:
            return True


        