# Enter your code here. Read input from STDIN. Print output to STDOUT
res = []
a = int(input())
eng = list(map(int, input().rstrip().split()))
x = int(input())
french = list(map(int, input().rstrip().split()))

for i in eng:
    res.append(i)

for i in french:
    res.append(i)

S = set(res)
print(len(S))
