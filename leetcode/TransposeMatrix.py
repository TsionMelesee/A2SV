class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        soln =  [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(rows):
            for j in range(cols):
                soln[j][i] = matrix[i][j]
        return soln

        