class Solution:
    def isHappy(self, n: int) -> bool: 
        ans = 0
        if n ==1 or n == 7:
            return True
        elif n < 10:
            return False
        while n > 0:
            temp = n %10
            ans += temp*temp
            n = n//10
        return self.isHappy(ans)
