from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        indices = {}

        for i, num in enumerate(nums): 
            complement = target - num 
            if complement in indices:
                return [indices[complement], i] 
            indices[num] = i
 
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print("Output:", result)
