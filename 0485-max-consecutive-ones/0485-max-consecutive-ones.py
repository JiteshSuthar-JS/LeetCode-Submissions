class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        temp_Res = 0
        for i in nums:
            if i == 1:
                temp_Res += 1
                ans = max(ans,temp_Res)
            else:
                temp_Res = 0
        return ans 