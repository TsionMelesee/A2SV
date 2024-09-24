if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        x = input().split()
        
        if x[0] == "insert":
            index = int(x[1])
            value = int(x[2])
            arr.insert(index, value)
        elif x[0] == "print":
            print(arr)
        elif x[0] == "remove":
            value = int(x[1])
            arr.remove(value)
        elif x[0] == "append":
            value = int(x[1])
            arr.append(value)
        elif x[0] == "sort":
            arr.sort()
        elif x[0] == "pop":
            arr.pop()
        elif x[0] == "reverse":
            arr.reverse()
