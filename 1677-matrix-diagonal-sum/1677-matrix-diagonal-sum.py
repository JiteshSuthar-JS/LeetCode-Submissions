class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        ans = 0
        
        for i in range(row):
            ans += mat[i][i]  
            ans += mat[i][row - 1 - i]  
         
        if row % 2 != 0:
            mid = row // 2
            ans -= mat[mid][mid]
        
        return ans
