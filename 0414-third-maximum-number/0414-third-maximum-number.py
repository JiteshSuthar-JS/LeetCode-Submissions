class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        for _ in range(2):
            max_num = max(nums)
            nums.remove(max_num)
        return max(nums)