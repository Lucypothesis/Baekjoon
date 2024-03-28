import sys
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    a = list(input().split())
    # push X
    if a[0] == 'push':
        queue.append(a[1])
    # pop
    if a[0] == 'pop':
        print(queue.pop(0) if queue else -1)
    # size
    if a[0] == 'size':
        print(len(queue))
    # empty
    if a[0] == 'empty':
        print(0 if queue else 1)
    # front
    if a[0] == 'front':
        print(queue[0] if queue else -1)
    # back
    if a[0] == 'back':
        print(queue[-1] if queue else -1)