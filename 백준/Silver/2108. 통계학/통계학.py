import sys
import math
input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

def realround(x):
    if x- math.floor(x) >= 0.5:
        return math.floor(x) + 1
    else:
        return math.floor(x)

# 산술평균
a = sum(num) / N
print(realround(a))
# # 중앙값
num.sort()
print(num[N // 2])
# 최빈값
lst = [0] * 8001
for i in num:
    lst[i + 4000] += 1
    # -4000 -> 0 / 0 -> 4000 / 1 -> 4001
a = max(lst)
# print(a)
if lst.count(a) == 1:
    print(lst.index(max(lst))-4000)
else:
    lst.remove(a)
    print(lst.index(a)-4000+1)
    
# 범위
print(max(num) - min(num))