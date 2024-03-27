import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int,input().split())) for i in range(N)]
# print(lst)

lst.sort(key = lambda x : (x[0], x[1]))

for i in lst:
    print(i[0], i[1])