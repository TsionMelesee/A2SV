class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = len(mat)
        b = len(mat[0])
        if a * b != r * c:
            return mat
        ans = [[0] * c for _ in range(r)]
        for i in range(a * b):
            ans[i // c][i % c] = mat[i // b][i % b]
        return ans       
