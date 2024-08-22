class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)
        if num >= 0:
            x = ''.join(sorted(s))
            if x[0] == '0':
                for i in range(len(x)):
                    if x[i] != '0':
                        x = x[i] + x[:i] + x[i+1:]
                        break
            return int(x)
        
        else:
            x = '-' + ''.join(sorted(s[1:], reverse=True))
            return int(x)
