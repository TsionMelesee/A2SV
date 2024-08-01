class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = Counter()
        
        for word in words:
            unique = ''.join(sorted(set(word)))
            ans += cnt[unique]
            cnt[unique] += 1
            
        return ans
