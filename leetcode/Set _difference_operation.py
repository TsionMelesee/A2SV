# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
n = set(map(int, input().split()))
y = int(input())
m = set(map(int, input().split()))
s = n - m
print(len(s))
