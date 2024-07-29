class Solution(object):
    def commonChars(self, words):
        cnt = Counter(words[0])
        for w in words:
            ccnt = Counter(w)
            for c in cnt.keys():
                cnt[c] = min(cnt[c], ccnt[c])
        ans = []
        for c, v in cnt.items():
            ans.extend([c] * v)
        return ans
        