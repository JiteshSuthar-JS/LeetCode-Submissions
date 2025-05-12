class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev = 2 
        nex = 3
        cur = 0
        
        for _ in range(3,n):
            cur = prev + nex
            prev = nex
            nex = cur
        return cur