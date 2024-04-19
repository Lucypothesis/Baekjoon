import sys
input = sys.stdin.readline

N = int(input())

num = list(set(map(int, input().split())))

num.sort()

for i in num:
    print(i, end=' ')