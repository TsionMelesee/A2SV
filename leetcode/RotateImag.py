class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = [[0]* len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            z = 0
            for j in range(len(matrix)-1,-1,-1):
                x[i][z]= matrix[j][i]
                z = z+1
        for i in range(len(matrix)):
            matrix[i]= x[i]
        return matrix


        
