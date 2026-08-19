class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        indexes = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in indexes:
                return [indexes[diff], idx]
            else:
                indexes[num] = idx
            