from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perm = set()
        for p in permutations(digits, 3):
            if p[0] == 0:
                continue
            num = p[0]*100 + p[1]*10 + p[2]
            if num % 2 == 0:
                perm.add(num)
        return sorted(list(perm))
