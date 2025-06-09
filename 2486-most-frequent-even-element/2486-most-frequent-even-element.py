class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        sortednum = [num for num in nums if num % 2 == 0]

        if not sortednum:
            return -1
            
        c = Counter(sortednum)
        max_freq = max(c.values())
        candidates = [num for num in c if c[num] == max_freq]
        return min(candidates)

            