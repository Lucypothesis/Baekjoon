import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
# print(table)
K = int(input())
for _ in range(K):
    count = 0
    i, j, x, y = list(map(int, input().split()))
    for row in range(i-1, x):
        for column in range(j-1, y):
            count += table[row][column]
    print(count)
# 맞으면 ㄹㅇ 개뿌듯함 2 달성~ 아 제발