if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    List = []
    for i in arr:
        if i not in List:
            List.append(i)
    List.remove(max(List))
    print(max(List))
