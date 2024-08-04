class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        x,y = len(strs[0]), len(strs)
        a = 0
        for j in range(x):
            for i in range(1, y):
                if strs[i][j] < strs[i - 1][j]:
                    a += 1
                    break
        return a