n = int(input())


d = [0] * 1001
d[1], d[2] = 1, 3
for n in range(3,n+1):
    d[n] = d[n-1] + 2 * d[n-2]

print(d[n] % 10007)