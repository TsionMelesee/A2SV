class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = Counter()
        for i in words:
            x = 0
            for j in i:
                x |= 1 << (ord(j) - ord("A"))
            ans += cnt[x]
            cnt[x] += 1
        return ans
        