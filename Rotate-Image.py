class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ncols = len(matrix[0])
        mat = []
        for i in range(ncols):
            mat.append([])
            
        for col in range(ncols):
            for row in range(ncols):
                mat[col].insert(0,matrix[row][col])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = mat[i][j]
        
