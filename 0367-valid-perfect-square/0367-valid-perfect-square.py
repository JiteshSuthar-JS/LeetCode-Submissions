class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1 
        right = num
    
        while left <= right:
            mid = (left + right) // 2
            midsqr = mid * mid
            if midsqr == num:
                return True
            elif num < midsqr:
                right = mid - 1
            else:
                left = mid + 1
        return False
        

