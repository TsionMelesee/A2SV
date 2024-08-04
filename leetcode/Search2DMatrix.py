class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix), len(matrix[0])
        left, right = 0, x * y - 1
        
        while left < right:
            mid = (left + right) // 2
            row = mid // y
            col = mid % y
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1
        
        return matrix[left // y][left % y] == target
        