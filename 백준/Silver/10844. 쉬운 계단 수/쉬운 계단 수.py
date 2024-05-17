n = int(input())

d = [[0] * 12 for _ in range(101)]
d[1] = [0,0,1,1,1,1,1,1,1,1,1,0]

for i in range(2,n+1):
    for j in range(1,11):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1] 

print(sum(d[n]) % 1000000000)