import sys
input = sys.stdin.readline

N = int(input())

num = list(set(map(int, input().split())))

num.sort()

print(' '.join(map(str, num)))