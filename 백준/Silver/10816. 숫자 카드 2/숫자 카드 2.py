import sys
input = sys.stdin.readline

N = int(input())
a_lst = list(map(int, input().split()))
M = int(input())
b_lst = list(map(int, input().split()))
lst = [0] * (20000001)
for i in a_lst:
    lst[i] += 1
# print(lst)
for i in b_lst:
    print(lst[i], end = ' ')

# 우와 나 좀 발전한듯