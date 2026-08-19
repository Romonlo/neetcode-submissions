class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 0:
            return False
        current = nums[0]
        for num in nums[1:]:
            if num == current:
                return True
            current = num
        return False

        