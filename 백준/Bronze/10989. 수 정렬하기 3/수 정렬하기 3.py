import sys
input = sys.stdin.readline

N = int(input())

lst = [0] * 10001
 
for i in range(N):
    lst[int(input())] += 1

# print(lst) 
for i in range(1,10001):
    for _ in range(lst[i]):
        print(i)