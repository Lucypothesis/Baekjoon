import sys
input = sys.stdin.readline

k = int(input())
lst =[]
for _ in range(k):
    n = int(input())
    if n > 0:
        lst.append(n)
    elif n == 0:
        lst.pop()
print(sum(lst))