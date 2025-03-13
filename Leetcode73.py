class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row={}
        col={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for k,v in row.items():
            matrix[k]=[0]*len(matrix[0])

        for rows in matrix:
            for k,v in col.items():
                rows[k]=0
