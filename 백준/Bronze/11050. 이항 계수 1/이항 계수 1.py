n ,k = map(int, input().split())
n_fact = 1
k_fact = 1
nk_fact = 1
for i in range(1, n+1):
    n_fact *= i
for i in range(1, k+1):
    k_fact *= i
for i in range(1, n-k+1):
    nk_fact *= i
print(n_fact // (k_fact * nk_fact))