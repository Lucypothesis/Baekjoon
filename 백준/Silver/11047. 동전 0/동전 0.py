N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort(reverse=True)

answer = 0
for i in A:
    if i <= K:
        answer += K // i
        K %= i 
print(answer)