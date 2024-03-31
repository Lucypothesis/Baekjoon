import sys
import math
input = sys.stdin.readline

def realround(x):
    if x - math.floor(x) >= 0.5:
        return math.floor(x) + 1
    else:
        return math.floor(x)

n = int(input())
lst = [int(input()) for _ in range(n)]

if n > 0:
    lst.sort()
    n_lst = lst[realround(n * 0.15):(n - realround(n * 0.15))]
    print(realround(sum(n_lst) / len(n_lst)))
else:
    print('0')