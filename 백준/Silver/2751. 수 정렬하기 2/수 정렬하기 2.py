import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()
# print(lst)
for i in lst:
    print(i)