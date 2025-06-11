class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        lst = []
        for i,j in zip(pos,neg):
            lst.append(i)
            lst.append(j)
        
        return lst
