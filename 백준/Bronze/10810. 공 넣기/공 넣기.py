N, M = map(int, input().split())

lst = [0] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i,j+1):
        if lst[x] != 0:
            lst[x] = 0
        lst[x] += k
    # print(lst)
for i in lst[1:]:
    print(i, end = ' ')