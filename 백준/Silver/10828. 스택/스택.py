import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    stack = input().split()
    if stack[0] == 'push':
        lst.append(stack[1])
    elif stack[0] == 'pop':
        print(lst.pop() if lst else -1)
    elif stack[0] == 'size':
        print(len(lst))
    elif stack[0] == 'empty':
        print(0 if lst else 1)
    else:
        print(lst[-1] if lst else -1)
