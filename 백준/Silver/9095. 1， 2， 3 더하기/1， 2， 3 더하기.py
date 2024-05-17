n = int(input())

d = [0] * 11
d[1], d[2], d[3] = 1, 2, 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(n):
    t = int(input())
    print(d[t])

# 아 문제 제대로 안 읽고 왜 세 개만 세는지 계속 머리싸맸다
# 빡친다 문제 좀 잘 읽자!!!