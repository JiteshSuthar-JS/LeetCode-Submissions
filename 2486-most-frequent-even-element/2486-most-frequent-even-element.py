class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        sortednum = [num for num in nums if num % 2 == 0]

        if not sortednum:
            return -1
            
        c = Counter(sortednum)
        freq = min(c.items(), key=lambda x: (-x[1], x[0]))[0]
        return freq

            