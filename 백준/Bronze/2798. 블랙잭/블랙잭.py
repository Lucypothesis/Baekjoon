N, M = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            # 헐 여기서 i, j, k 다 다르도록 해야됨
            if i < j < k:
                sum = lst[i] + lst[j] + lst[k]
                sum_lst.append(sum)
sum_lst = list(set(sum_lst))

last_lst = []
for i in range(len(sum_lst)):
    if sum_lst[i] <= M:
        last_lst.append(sum_lst[i])
print(max(last_lst))