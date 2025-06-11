class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        ans = []
        i = 0
        j = 0
         
        while i < len(pos) and j < len(neg):
            ans.append(pos[i])
            ans.append(neg[j])
            i += 1
            j += 1
         
        while i < len(pos):
            ans.append(pos[i])
            i += 1
 
        while j < len(neg):
            ans.append(neg[j])
            j += 1
        
        return ans
