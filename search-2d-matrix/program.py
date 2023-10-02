class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=matrix[0]
        m=len(matrix)
        n=len(row)
        flag=False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                    flag=True
                    break
        return flag