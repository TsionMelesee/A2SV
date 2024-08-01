class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i, n = 0, len(s)
        res = []
        
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                res.append(alphabet[int(s[i : i + 2]) - 1])
                i += 3
            else:
                res.append(alphabet[int(s[i]) - 1])
                i += 1
        
        return ''.join(res)
