T = int(input())

for _ in range(T):
    lst = list(input().split())
    for i in lst:
        print(''.join(list(i)[::-1]), end = ' ')