z = set(map(int, input().split()))
x = int(input())
y = True

while x:
    a = set(map(int, input().split()))
    if len(z) <= len(a):
        y = False
        break
    
    for i in a:
        if i not in z:
            y = False
            break
    
    if not y:
        break
    
    x -= 1

print(y)
