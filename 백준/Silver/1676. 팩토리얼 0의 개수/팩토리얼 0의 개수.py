N = int(input())

N_fact = 1
for i in range(1, N+1):
    N_fact *= i
# print(N_fact)

S = list(map(int, str(N_fact)))
# print(S)
final_S = S[::-1]
# print(final_S)
for i in range(len(final_S)):
    if final_S[i] != 0:
        break
print(i)