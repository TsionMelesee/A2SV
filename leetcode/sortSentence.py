class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        map = {}
        
        for word in words:
            num = int(word[-1])
            map[num] = word[:-1]

        result = [""] * len(words)
        for key in map:
            result[key - 1] = map[key]

        return " ".join(result)
