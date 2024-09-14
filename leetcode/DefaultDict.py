from collections import defaultdict

n, m = map(int, input().split())
x = defaultdict(list)

res = []
for i in range(1, n + m + 1):
    w = input().strip()
    if i <= n:
        x[w].append(i)
    else:
        if w in x:
            res.append(" ".join(map(str, x[w])))
        else:
            res.append('-1')

print("\n".join(res))
