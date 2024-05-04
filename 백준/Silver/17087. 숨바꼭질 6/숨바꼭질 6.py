import math, sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

num = []
for i in lst:
    a = abs(i-S)
    num.append(a)

answer = math.gcd(*num)
print(answer)