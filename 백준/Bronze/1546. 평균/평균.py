N = int(input())
lst = list(map(int, input().split()))

n_lst = []
for i in range(N):
    n_score = lst[i] / max(lst) * 100
    n_lst.append(n_score)
print(sum(n_lst) / N)