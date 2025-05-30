class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i==nums2[-1]:
                l.append(-1)
            else:
                for j in range(nums2.index(i)+1,len(nums2)):
                    if nums2[j]>i:
                        l.append(nums2[j])
                        break
                else:
                    l.append(-1)
        return l
        