# sys 쓰니까 훠얼씬 빠르다. 웬만해서는 sys 쓰자.
import sys
input = sys.stdin.readline
N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x :(x[1], x[0]))

# print(lst)
for i in lst:
    print(i[0], i[1])
