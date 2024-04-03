from collections import deque
N, k = map(int, input().split())

lst = []
queue = deque(range(1,N+1))

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    lst.append(queue.popleft())

print('<' + ', '.join(map(str, lst)) + '>')