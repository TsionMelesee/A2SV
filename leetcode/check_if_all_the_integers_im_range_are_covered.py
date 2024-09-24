class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = [0] * 52
        for l, r in ranges:
            x[l] += 1
            if r + 1 <= 51:
                x[r + 1] -= 1
        
        s = 0
        for i in range(1, 51):
            s += x[i]
            if left <= i <= right and s <= 0:
                return False
        return True
