class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 
        a = int(str(abs(x))[::-1]) * sign
        return a if -2**31 <= a <=  2**31 - 1 else 0